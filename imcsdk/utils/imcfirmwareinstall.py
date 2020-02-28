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
from imcsdk.imcgenutils import *
from imcsdk.imccoreutils import IMC_PLATFORM, get_server_dn, \
    get_mo_property_meta
from imcsdk.mometa.adapter.AdapterSecureUpdate import AdapterSecureUpdate
from imcsdk.mometa.compute.ComputeRackUnit import ComputeRackUnit
from imcsdk.mometa.huu.HuuFirmwareUpdater import HuuFirmwareUpdater, \
    HuuFirmwareUpdaterConsts
from imcsdk.mometa.huu.HuuFirmwareUpdateStatus import HuuFirmwareUpdateStatus
from imcsdk.mometa.top.TopSystem import TopSystem
from imcsdk.mometa.huu.HuuController import HuuController

log = logging.getLogger('imc')

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
    return update.update_end_time != "NA"


def _print_component_upgrade_summary(handle):
    update_objs = handle.query_classid("HuuUpdateComponentStatus")
    log.info("Component Update Summary:-")
    for obj in update_objs:
        log.info("%20s: %s" % (obj.component, obj.update_status))


def _disable_secure_adapter_update(handle, parent_dn):
    """
    Disables secure adapter update so adapters can be downgraded.
    If the CIMC version doesn't support disabling secure adapter update,
    a warning is logged.
    """
    if handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        asu_prop_meta = get_mo_property_meta('ComputeRackUnit',
                                             key='adaptor_secure_update',
                                             platform=handle.platform)
        adapter_secure_mo = ComputeRackUnit(parent_mo_or_dn=parent_dn,
                                            server_id="1")
        adapter_secure_mo.adaptor_secure_update = 'disabled'
    elif handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        asu_prop_meta = get_mo_property_meta('AdapterSecureUpdate',
                                             key='secure_update',
                                             platform=handle.platform)
        adapter_secure_mo = AdapterSecureUpdate(parent_mo_or_dn=parent_dn)
        adapter_secure_mo.secure_update = 'disabled'
    if handle.version < asu_prop_meta.version:
        log.warning("CIMC version does not support disabling secure adapter "
                    "update.")
        return
    log.info("Disabling secure adapter update")
    handle.set_mo(adapter_secure_mo)


def firmware_huu_update_monitor(handle, secure_adapter_update=True,
                                timeout=60, interval=10, server_id=1):
    """
    This method monitors status of a firmware upgrade.

    Args:
        handle(ImcHandle)
        secure_adapter_update(bool): If set to False, secure adapater update
                                     will be disabled as part of the
                                     monitoring loop allowing for adapater
                                     downgrades.  This should be used with
                                     caution, adapter downgrades can
                                     reintroduce security issues that are
                                     fixed in newer adapter firmware versions.
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

    while True:
        try:
            update_obj = handle.query_dn(update_obj.dn)
            if _has_upgrade_started(update_obj):
                log_progress("Firmware upgrade is yet to start")

            if _has_upgrade_finished(update_obj):
                log_progress("Firmware upgrade has finished",
                             update_obj.overall_status)
                _print_component_upgrade_summary(handle)
                break
            elif update_obj.overall_status not in current_status:
                log_progress("Firmware Upgrade is still running",
                             update_obj.overall_status)
                current_status.append(update_obj.overall_status)
                if (not secure_adapter_update and
                    'HUU Discovery In Progress' in update_obj.overall_status):
                    # by design secure adapter update is enabled when
                    # the host reboots so if we want to allow adapter
                    # downgrade we need to set it to disabled in the monitor
                    # loop
                    _disable_secure_adapter_update(handle, parent_dn)

            time.sleep(interval)
            secs = (datetime.datetime.now() - start).total_seconds()
            if int(secs / 60) > timeout:
                log_progress("Monitor API timeout",
                             "rerun firmware_huu_update_monitor")
                break
        except:
            _validate_connection(handle)


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
