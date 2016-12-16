# Copyright 2016 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
This module provides APIs for storage configuration like virtual drives and
disk groups.
"""

import logging
import imcsdk.imccoreutils as imccoreutils
from imcsdk.mometa.storage.StorageVirtualDriveCreatorUsingUnusedPhysicalDrive \
    import StorageVirtualDriveCreatorUsingUnusedPhysicalDrive as vd_creator

log = logging.getLogger('imc')


def virtual_drive_create(handle,
                         drive_group,
                         sas_controller_slot,
                         raid_level=0,
                         virtual_drive_name=None,
                         access_policy="read-write",
                         read_policy="no-read-ahead",
                         cache_policy="direct-io",
                         disk_cache_policy="unchanged",
                         write_policy="Write Through",
                         strip_size="64k",
                         size=None,
                         admin_action=None,
                         server_id=1):
    """
        Creates virtul drive from unused physical drives

        Args:
            handle (ImcHandle)

        Examples:
            virtual_drive_create(handle=imc,
                                 drive_group='[2]',
                                 sas_controller_slot='MEZZ')
    """
    server_dn = imccoreutils.get_server_dn(handle, server_id)
    slot_dn = server_dn + "/board/storage-SAS-SLOT-" + sas_controller_slot

    params = {}
    params["parent_mo_or_dn"] = slot_dn
    params["drive_group"] = str(drive_group)
    params["raid_level"] = str(raid_level)
    params["access_policy"] = access_policy
    params["read_policy"] = read_policy
    params["cache_policy"] = cache_policy
    params["disk_cache_policy"] = disk_cache_policy
    params["write_policy"] = write_policy
    params["strip_size"] = strip_size

    if (admin_action and
            handle.platform == imccoreutils.IMC_PLATFORM.TYPE_MODULAR):
        params["admin_action"] = admin_action

    if virtual_drive_name:
        params["virtual_drive_name"] = virtual_drive_name
    else:
        # TODO: Calculate VD name
        params["virtual_drive_name"] = "RAID0_2"

    if size:
        params["size"] = size
    else:
        # TODO: Calculate the size
        params["size"] = "3814697 MB"

    mo = vd_creator(**params)
    mo.admin_state = "trigger"
    handle.add_mo(mo)
