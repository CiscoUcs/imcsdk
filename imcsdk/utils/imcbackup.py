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
This module contains APIs to facilitate Imc backup and import
"""

import time
import logging
from ..imcexception import ImcValidationException

log = logging.getLogger('imc')


def backup_imc(handle, remote_host, remote_file, protocol, username, password,
               passphrase, timeout_in_sec=600):
    """
    backup_imc helps create and download Imc backups.

    Args:
        handle (ImcHandle): Imc Connection handle
        remote_host (str): IP or Hostname for the remote host.
        remote_file (str): Absolute path and name for the backup file
        protocol (str) : "ftp", "http", "scp", "sftp", "tftp"
        username (str) : Remote Host user name
        password (str) : Remote Host user credentials/password
        passphrase (str) : Password for the backup file.
        timeout_in_sec (number) : time in seconds for which method waits
                              for the backUp file to generate before it exits.

    Example:
        remote_file = "/root/config_backup.xml"
        backup_imc(h,remote_file=remote_file,
               protocol="ftp",username="user",password="pass",
               remote_host="10.10.10.10",passphrase="xxxxxx")
    """

    from ..mometa.mgmt.MgmtBackup import MgmtBackup, MgmtBackupConsts
    from ..mometa.top.TopSystem import TopSystem

    if password == "" or passphrase == "":
        raise ImcValidationException("Invalid password or passphrase")

    top_system = TopSystem()
    mgmt_backup = MgmtBackup(parent_mo_or_dn=top_system,
                             hostname=remote_host,
                             admin_state=MgmtBackupConsts.ADMIN_STATE_ENABLED,
                             proto=protocol,
                             pwd=password,
                             user=username,
                             passphrase=passphrase,
                             remote_file=remote_file)

    handle.add_mo(mgmt_backup, modify_present=True)

    # Checking for the backup to compete.
    time.sleep(10)
    duration = timeout_in_sec
    poll_interval = 2
    download_status = False

    while not download_status:
        mgmt_backup = handle.query_dn(dn=mgmt_backup.dn)
        admin_state_temp = mgmt_backup.admin_state

        # Break condition:- if state id disabled then break
        if admin_state_temp == MgmtBackupConsts.ADMIN_STATE_DISABLED:
            if mgmt_backup.fsm_stage_descr == "Completed successfully":
                download_status = True
            if mgmt_backup.fsm_stage_descr == "Error":
                raise ImcValidationException("Failed to export the CIMC "
                                             "configuration file." +
                                             "Error Code: " +
                                             mgmt_backup.fsm_rmt_inv_err_code +
                                             " Error Description: " +
                                             mgmt_backup.fsm_rmt_inv_err_descr)
        if download_status:
            break

        time.sleep(min(duration, poll_interval))
        duration = max(0, (duration - poll_interval))
        if duration == 0:
            handle.remove_mo(mgmt_backup)
            raise ImcValidationException('backup_imc timed out')


def import_imc_backup(handle, remote_host, remote_file, protocol, username,
                      password, passphrase):
    """
    This operation uploads a Imc backup taken earlier via GUI
    or backup_imc operation for all configuration, system configuration,
    and logical configuration files. User can perform an import while the
    system is up and running.

    Args:
        handle (ImcHandle): connection handle
        remote_host (str): IP or Hostname for the remote host.
        remote_file (str): Absolute path and name for the backup file
        protocol (str) : "ftp", "http", "scp", "sftp", "tftp"
        username (str) : Remote Host user name
        password (str) : Remote Host user credentials/password
        passphrase (str) : Password for the backup file.

    Example:
        remote_file = "/root/config_backup.xml"
        import_imc_backup(h,remote_file=remote_file,
               protocol="ftp",username="user",password="pass",
               remote_host="10.10.10.10",passphrase="xxxxxx")
    """

    from ..mometa.top.TopSystem import TopSystem
    from ..mometa.mgmt.MgmtImporter import MgmtImporter, MgmtImporterConsts

    if password == "" or passphrase == "":
        raise ImcValidationException("Invalid password or passphrase")

    # create MgmtImporter
    top_system = TopSystem()
    mgmt_importer = MgmtImporter(parent_mo_or_dn=top_system,
                                 hostname=remote_host,
                                 remote_file=remote_file,
                                 proto=protocol,
                                 user=username,
                                 pwd=password,
                                 passphrase=passphrase,
                                 admin_state=MgmtImporterConsts.ADMIN_STATE_ENABLED)

    handle.add_mo(mgmt_importer, modify_present=True)

    time.sleep(10)
    download_status = False
    while not download_status:
        mgmt_importer = handle.query_dn(dn=mgmt_importer.dn)
        admin_state_temp = mgmt_importer.admin_state

        # Break condition:- if state id disabled then break
        if admin_state_temp == MgmtImporterConsts.ADMIN_STATE_DISABLED:
            if mgmt_importer.fsm_stage_descr == "Completed successfully":
                download_status = True
            if mgmt_importer.fsm_stage_descr == "Error":
                raise ImcValidationException("Failed to import the CIMC "
                                             "configuration file." +
                                             "Error Code: " +
                                             mgmt_importer.fsm_rmt_inv_err_code +
                                             " Error Description: " +
                                             mgmt_importer.fsm_rmt_inv_err_descr)
        if download_status:
            break

    return mgmt_importer
