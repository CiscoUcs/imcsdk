# Copyright 2013 Cisco Systems, Inc.
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
This module contains the APIs used to create and download tech_support file.
"""

import time
from ..imcexception import ImcValidationException, ImcWarning
from ..imccoreutils import IMC_PLATFORM


def tech_support_get(handle, remote_host, remote_file, protocol, username,
                         password, timeout_in_sec=600,
                         component="all", **kwargs):
    """
    This operation creates and downloads the technical support file for
    the specified Ucs server.

    Args:
        handle (ImcHandle): Imc Connection handle
        remote_host (str): IP or Hostname for the remote host.
        remote_file (str): Absolute path and name for the tech support file
        protocol (str) : "ftp", "http", "none", "scp", "sftp", "tftp"
        username (str) : Remote Host user name
        password (str) : Remote Host user credentials/password
        timeout_in_sec (number) : time in seconds for which method waits
                              for the backUp file to generate before it exits.
        component (str) : For C3260 platforms
                          "all" for tech-support of all components
                          "cmc1" for tech-support of chassis related components on chassis controller-1
                          "cmc2" for tech-support of chassis related components on chassis controller-2
                          "cimc1" for tech-support of server related components on server-1
                          "cimc2" for tech-support of server related components on server-2
                          Combination of the above can also be given with space as separator
                          "cmc1 cmc2" or "cimc1 cimc2"
        kwargs : key=value paired arguments
                 Values for component should be given with space as delimiter

    Example:
        remote_file = "/root/tech_sup_backup.tar.gz"
        tech_support_get(h,remote_file=remote_file,
               protocol="scp",username="user",password="pass",
               remote_host="10.10.10.10")
        tech_support_get(h,remote_file=remote_file,
               protocol="scp",username="user",password="pass",
               remote_host="10.10.10.10", component="all")
    """

    from ..mometa.top.TopSystem import TopSystem
    from ..mometa.compute.ComputeRackUnit import ComputeRackUnit
    from ..mometa.equipment.EquipmentChassis import EquipmentChassis
    from ..mometa.sysdebug.SysdebugTechSupportExport import \
        SysdebugTechSupportExport
    if not remote_file.endswith('.tar.gz'):
        raise ImcValidationException('file_name should end with .tar.gz')

    if timeout_in_sec is None or timeout_in_sec == "" or timeout_in_sec < 1:
        timeout_in_sec = 600
        ImcWarning("Inappropriate <timeoutsec>. "
                   "Chosen default value is 600 Seconds")

    # create SysdebugTechSupport
    top_system = TopSystem()
    parent_mo = None

    if handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        parent_mo = ComputeRackUnit(parent_mo_or_dn=top_system, server_id="1")
    elif handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        parent_mo = EquipmentChassis(parent_mo_or_dn=top_system)

    sys_debug_tech_support = SysdebugTechSupportExport(
        parent_mo_or_dn=parent_mo,
        hostname=remote_host,
        protocol=protocol,
        pwd=password,
        user=username,
        remote_file=remote_file,
        admin_state="enabled")

    if handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        sys_debug_tech_support.component = component

    handle.add_mo(sys_debug_tech_support, modify_present=True)

    time.sleep(10)

    # poll for tech support to complete
    duration = timeout_in_sec
    poll_interval = 2
    status = False

    while True:
        tech_support = handle.query_dn(sys_debug_tech_support.dn)
        if tech_support.admin_state in ["Disabled", "disabled"]:
            if tech_support.fsm_status == "success":
                status = True
            else:
                raise ImcValidationException('Failed to create/transfer the '
                                             'TechSupport file.' +
                                             tech_support.fsm_status)
        if status:
            break
        time.sleep(min(duration, poll_interval))
        duration = max(0, (duration - poll_interval))
        if duration == 0:
            handle.remove_mo(tech_support)
            handle.commit()
            raise ImcValidationException('TechSupport file creation timed out')

    return tech_support
