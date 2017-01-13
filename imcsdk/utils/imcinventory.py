# Copyright 2016 Cisco Systems, Inc.
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

"""
This module contains APIs to download inventory to a remote location
"""

import time
import logging
from imcsdk.mometa.mgmt.MgmtInventory import MgmtInventory

log = logging.getLogger('imc')


def _get_parent_dn(handle):
    from imcsdk.imccoreutils import IMC_PLATFORM
    if handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        return 'sys'
    elif handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        return 'sys/chassis-1'


def inventory_remote(handle, hostname, remote_file, user=None, pwd=None,
                     proto='tftp', **kwargs):
    """
    Inventory the Cisco IMC server.

    Args:
        handle (ImcHandle): Imc Connection handle
        user (str) : Remote Host user name
        pwd (str) : Remote Host user credentials/password
        hostname (str): IP or Hostname for the remote host.
        remote_file (str): Absolute path and name for the backup file
        proto (str) : "ftp", "http", "scp", "sftp", "tftp"
        kwargs : key=value paired arguments

    Returns:
        MgmtInventory object

    Example:
        inventory_imc(handle, user="admin", pwd="password",
                      hostname="1.1.1.1", remote_file="/users/xyz/inventory",
                      proto="scp")
    """

    mo = MgmtInventory(parent_mo_or_dn=_get_parent_dn(handle))
    params = {
        'user': user,
        'pwd': pwd,
        'hostname': hostname,
        'remote_file': remote_file,
        'proto': proto,
        'admin_state': 'trigger'
        }

    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.add_mo(mo, modify_present=True)
    return handle.query_dn(mo.dn)


def monitor_inventory_collection(handle, timeout=300, interval=2):
    """
    Monitors the inventory collection feature supported natively by Cisco IMC

    Args:
        handle (ImcHandle)
        timeout (int): Timeout in secs for inventory collection to complete
        interval (int): Frequency of monitoring in seconds

    Returns:
        None

    Example:
        monitor_inventory_collection(handle)
    """
    mo = MgmtInventory(parent_mo_or_dn=_get_parent_dn(handle))
    log.info('Monitoring Inventory Collection for IMC[%s]' % handle.ip)
    time.sleep(interval)
    time_left = timeout

    # Check for the inventory collection to complete.
    while time_left > 0:
        mo = handle.query_dn(dn=mo.dn)
        log.info("Status:[%s] Progress:[%s]" % (mo.fsm_status, mo.progress))

        if mo.fsm_status == "COMPLETED" and mo.progress == "100%":
            log.info("Inventory Collection Complete")
            return

        time.sleep(interval)
        time_left -= interval

    log.info("Inventory Collection for IMC[%s] timed out after %s seconds!" %
             (handle.ip, timeout))
