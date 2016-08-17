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
from imcsdk.imcgenutils import *


def update_imc_firmware_huu(handle, remote_share, share_type, remote_ip,
                            username, password, update_component="all",
                            stop_on_error="yes", timeout=240,
                            verify_update="yes", cimc_secure_boot="no"):
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
        stop_on_error (string): "yes", "no"
        timeout (int): Timeout value. Range is 30-240 secs.
        verify_update (string): "yes", "no"
        cimc_secure_boot (string): "yes", "no"

    Returns:
        HuuFirmwareUpdater object

    Examples:
        update_imc_firmware_huu(handle=handle,
                                remote_ip=ip,
                                remote_share='nfsshare2/ucs-c460m4-huu-2.0.9l.iso',
                                share_type='nfs',
                                username=username,
                                password=password,
                                update_component='all',
                                stop_on_error='yes',
                                verify_update='no',
                                cimc_secure_boot='no',
                                timeout='60')
    """

    from imcsdk.mometa.huu.HuuFirmwareUpdater import HuuFirmwareUpdater, \
        HuuFirmwareUpdaterConsts
    from imcsdk.mometa.top.TopSystem import TopSystem
    from imcsdk.mometa.huu.HuuController import HuuController

    top_system = TopSystem()
    huu = HuuController(top_system)

    huu_firmware_updater = HuuFirmwareUpdater(parent_mo_or_dn=huu,
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
    handle.add_mo(huu_firmware_updater, modify_present=True)
    return huu_firmware_updater


def monitor_huu_firmware_update(handle, time_out=1200):
    current_status = []
    firmware_upgrade_complete = False
    start = datetime.datetime.now()
    while not firmware_upgrade_complete:
        try:
            update_class = handle.query_classid("huuFirmwareUpdateStatus")
            if update_class[0].update_start_time == "" and update_class[
                    0].update_end_time == "":
                log.info("Firmware Upgrade not yet started!")
            if update_class[0].update_end_time != "NA":
                log.info("Firmware Upgrade Finished! Status: [%s] @ [%s]"
                         % (update_class[0].overall_status,
                            datetime.datetime.now()))
                firmware_upgrade_complete = True
            elif update_class[0].overall_status not in current_status:
                log.info("Firmware Upgrade still running. Current Status:"
                         "%s" % update_class[0].overall_status)
                current_status.append(update_class[0].overall_status)
            time.sleep(10)
            if (datetime.datetime.now() - start).total_seconds() > time_out:
                log.error("Timeout: Firmware Upgrade Timed Out")
                break
        except:
            validate_connection(handle)


def validate_connection(handle, timeout=15 * 60):
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
