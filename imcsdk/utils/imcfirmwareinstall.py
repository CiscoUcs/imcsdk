# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import time
import datetime
import logging
import re

from imcsdk.imccoreutils import IMC_PLATFORM, get_server_dn
from imcsdk.imcexception import ImcOperationError
from imcsdk.mometa.huu.HuuFirmwareUpdater import HuuFirmwareUpdater, \
    HuuFirmwareUpdaterConsts
from imcsdk.mometa.huu.HuuFirmwareUpdateStatus import HuuFirmwareUpdateStatus
from imcsdk.mometa.top.TopSystem import TopSystem
from imcsdk.mometa.huu.HuuController import HuuController

log = logging.getLogger('imc')


def version_extract(remote_share):
    version = re.match(r"^.*-huu-(.*)\.iso$", remote_share).groups()[0]
    version = re.sub(r"(\..*?){1}\.", r"\1(", version).strip() + ")"
    log.debug("check for version <%s>" % str(version))
    return version


def firmware_exists(handle, version, server_id=1, force=False, backup_fw=False):
    if force:
        return False, None

    server_dn = get_server_dn(handle, server_id)
    dn = server_dn + "/mgmt/fw-system"
    if backup_fw:
        dn = server_dn + "/mgmt/fw-updatable"
    mo = handle.query_dn(dn)
    if mo is None:
        return False, None

    mo_ver = mo.version.strip().lower()
    ver = version.strip().lower()
    if mo.version.strip().lower() != version.strip().lower():
        log.debug("%s | %s " % (mo_ver, ver))
        return False, None
    return True, mo


def firmware_update(handle, remote_share, share_type, remote_ip,
                    username="", password="", update_component="all",
                    stop_on_error="yes", timeout=60,
                    verify_update="yes", cimc_secure_boot="no",
                    server_id=1, force=False, interval=60, backup_fw=False):

    version = version_extract(remote_share)
    if not force and firmware_exists(handle, version, force=force,
            backup_fw=backup_fw)[0]:
        return

    firmware_huu_update(handle, remote_share, share_type, remote_ip,
                        username, password, update_component, stop_on_error,
                        timeout, verify_update, cimc_secure_boot, server_id)

    firmware_huu_update_monitor(handle, timeout, interval, server_id)


def firmware_huu_update(handle, remote_share, share_type, remote_ip,
                        username="", password="", update_component="all",
                        stop_on_error="yes", timeout=240,
                        verify_update="yes", cimc_secure_boot="no",
                        server_id=1):
    """
    This method can be used to upgrade the cimc firmware

    Args:
        handle (ImcHandle)
        remote_share (string): Full path to the firmware file
        share_type (string): "nfs", "www", "cifs"
        remote_ip (string): IP address of the remote machine
        username (string): username
        password (string): password
        update_component (string): component to be updated.
            "all" for upgrading all components
            Refer release notes for individual component names
        stop_on_error (string): "yes", "no"
        timeout (int): Timeout value. Range is 30-240 mins.
        verify_update (string): "yes", "no"
        cimc_secure_boot (string): "yes", "no"
        server_id (int): Server id for which firmware is performed.
                         This is relevant to C3260 platforms.

    Returns:
        HuuFirmwareUpdater object

    Examples:
        firmware_huu_update(handle=handle,
                            remote_ip=ip,
                            remote_share='nfsshare2/ucs-c460m4-huu-2.0.9l.iso',
                            share_type='nfs',
                            username=username,
                            password=password,
                            update_component='all',
                            stop_on_error='yes',
                            verify_update='no',
                            cimc_secure_boot='no',
                            timeout=60)
    """

    top_system = TopSystem()
    if handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        parent_dn = top_system.dn
    elif handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        parent_dn = get_server_dn(handle, str(server_id))

    huu = HuuController(parent_mo_or_dn=parent_dn)

    huu_firmware_updater = HuuFirmwareUpdater(
        parent_mo_or_dn=huu,
        remote_share=remote_share,
        map_type=share_type,
        remote_ip=remote_ip,
        username=username,
        password=password,
        update_component=update_component,
        admin_state=HuuFirmwareUpdaterConsts.ADMIN_STATE_TRIGGER,
        stop_on_error=stop_on_error,
        time_out=str(timeout),
        verify_update=verify_update,
        cimc_secure_boot=cimc_secure_boot)
    handle.add_mo(huu_firmware_updater)
    return huu_firmware_updater


def log_progress(msg="", status=""):
    log.info("%s: %s. %s" % (datetime.datetime.now(), msg, status))


def _has_upgrade_started(update):
    return update.update_start_time == "" and update.update_end_time == ""


# Tracks if upgrade is over, not necessarily successful
def _has_upgrade_finished(update):
    return update.update_end_time != "NA" and update.update_end_time != ""


def _has_upgrade_successful(update):
    if re.search(r"error", update.overall_status.lower()) or \
       re.search(r"mapping has gone bad", update.overall_status.lower()):
        return False
    return True


def _print_component_upgrade_summary(handle):
    update_objs = handle.query_classid("HuuUpdateComponentStatus")
    log.info("Component Update Summary:-")
    for obj in update_objs:
        log.info("%20s: %s" % (obj.component, obj.update_status))


def firmware_huu_update_monitor(handle, timeout=60, interval=10, server_id=1):
    """
    This method monitors status of a firmware upgrade.

    Args:
        handle(ImcHandle)
        timeout(int): Timeout in minutes for monitor API.
        interval(int): frequency of monitoring in seconds
        server_id(int): Server id for monitoring firmware upgrade

    Returns:
        None

    Examples:
        firmware_huu_update_monitor(handle, 60, 10)
    """
    current_status = []
    start = datetime.datetime.now()

    top_system = TopSystem()
    if handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        parent_dn = top_system.dn
    elif handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        parent_dn = get_server_dn(handle, str(server_id))

    huu = HuuController(parent_mo_or_dn=parent_dn)
    huu_firmware_updater = HuuFirmwareUpdater(parent_mo_or_dn=huu.dn)
    update_obj = HuuFirmwareUpdateStatus(
            parent_mo_or_dn=huu_firmware_updater.dn)

    error_flag = False
    error_msg = None
    while True:
        try:
            update_obj = handle.query_dn(update_obj.dn)
            if _has_upgrade_started(update_obj):
                log_progress("Firmware upgrade is yet to start")

            if _has_upgrade_finished(update_obj):
                log_progress("Firmware upgrade has finished",
                             update_obj.overall_status)
                if not _has_upgrade_successful(update_obj):
                    error_flag = True
                    error_msg = "Error: %s" % update_obj.overall_status
                    break
                _print_component_upgrade_summary(handle)
                break
            elif update_obj.overall_status not in current_status:
                log_progress("Firmware Upgrade is still running",
                             update_obj.overall_status)
                current_status.append(update_obj.overall_status)

            time.sleep(interval)
            secs = (datetime.datetime.now() - start).total_seconds()
            if int(secs / 60) > timeout:
                log_progress("Monitor API timeout",
                             "rerun firmware_huu_update_monitor")
                error_flag = True
                error_msg = "Error: Monitor API timeout"
                break
        except:
            _validate_connection(handle)

    if error_flag:
        raise ImcOperationError("firmware_huu_update_monitor", error_msg)


def _validate_connection(handle, timeout=15 * 60):
    """
    Monitors IMC connection, if connection exists return True, else False
    Args:
        handle (ImcHandle)
        timeout (number): timeout in seconds
    Returns:
        True/False(bool)
    Raises:
        Exception if unable to connect to IMC
    """

    connected = False
    start = datetime.datetime.now()
    while not connected:
        try:
            # If the session is already established,
            # this will validate the session
            connected = handle.login()
        except Exception as e:
            # IMC may been in the middle of activation,
            # hence connection would fail
            log.debug("Login to IMC failed: %s", str(e))

        if not connected:
            try:
                log.debug("Login to IMC, elapsed time %ds",
                          (datetime.datetime.now() - start).total_seconds())
                handle.login(force=True)
                log.debug("Login successful")
                connected = True
            except:
                log.debug("Login failed. Sleeping for 60 seconds")
                time.sleep(60)
            if (datetime.datetime.now() - start).total_seconds() > timeout:
                raise Exception("TimeOut: Unable to login to IMC")
    return connected
