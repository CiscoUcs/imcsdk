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


def physical_drive_get(handle,
                       drive_slot,
                       controller_slot,
                       server_id=1):
    """
    Returns the drive Mo

    """
    server_dn = imccoreutils.get_server_dn(handle, server_id)
    drive_dn = server_dn + "/board/storage-SAS-SLOT-" + \
        str(controller_slot) + '/pd-' + str(drive_slot)
    return handle.query_dn(drive_dn)


def _list_to_string(drive_list):
    # convert to format imc expects
    # list to string
    # [[1]] => '[1]'
    # [[1,2],[3,4]] => '[1,2],[3,4]'
    # imc fails to parse '[1, 2]'
    # it needs to be '[1,2]'
    # and hence the replace(' ', '')
    dg_str = ""
    for each in drive_list:
        dg_str += str(each) + ','
    return dg_str[:-1].replace(' ', '')


def _flatten_list(drive_list):
    # convert to format imc expects
    # [[1]] => [1]
    # [[1,2],[3,4]] => [1, 2, 3, 4]
    dg_list = []
    for each in drive_list:
        for sub_each in each:
            dg_list.append(sub_each)
    return dg_list


def _flatten_to_string(drive_list):
    # convert to format imc expects
    # [[1]] => '1'
    # [[1,2],[3,4]] => '1234'
    return ''.join([''.join(str(x)) for x in _flatten_list(drive_list)])


def _vd_name_create(raid_level, drive_list):
    return "RAID" + str(raid_level) + "_" + _flatten_to_string(drive_list)


def _human_to_bytes(size_str):
    """
    returns the size in bytes
        supported formats KB, MB, GB, TB, PB, EB, ZB, YB

        KB to bytes = (* 1024) == << 10
        MB to bytes = (* 1024 * 1024) == << 20
        GB to bytes = (* 1024 * 1024 * 1024) == << 30
    """
    convert = {'KB': 1, 'MB': 2, 'GB': 3, 'TB': 4,
               'PB': 5, 'EB': 6, 'ZB': 7, 'YB': 8}
    s = size_str.split()
    if s[1] not in convert:
        raise "unknown size format" + size_str
    return int(s[0]) << (10 * convert[s[1]])


def _bytes_to_human(size, output_format='MB'):
    """
    converts bytes to human readable format.
        The return is in output_format.
    """
    convert = {'KB': 1, 'MB': 2, 'GB': 3, 'TB': 4,
               'PB': 5, 'EB': 6, 'ZB': 7, 'YB': 8}
    if output_format not in convert:
        raise "unknown output format" + output_format
    return str(size >> (10 * convert[output_format])) + output_format


def _drive_smallest_get(size_list):
    smallest = None
    for each in size_list:
        if smallest is None:
            smallest = each
        if each < smallest:
            smallest = each
    return smallest


def _vd_size_get(handle,
                 controller_slot,
                 drive_list,
                 raid_level,
                 server_id=1):
    """
    Returns the usable disk size for the specified virtual_drive
        drive_list:
            [[1]]
            [[1,2],[3,4]]
    """
    sizes = []
    for each in drive_list:
        sub_sizes = []
        for drive in each:
            dmo = physical_drive_get(handle=handle,
                                     drive_slot=drive,
                                     controller_slot=controller_slot,
                                     server_id=server_id)
            sub_sizes.append(_human_to_bytes(dmo.coerced_size))
        sizes.append(sub_sizes)

    if raid_level == 0:
        # RAID-0
        # only one disk allowed
        # smallest size disk * number of disks
        smallest = _drive_smallest_get(drive_list[0])
        return smallest * len(drive_list[0])
    elif raid_level == 1:
        # RAID-1
        #




    size = 0
    for drive in _flatten_list(drive_list):
        dmo = physical_drive_get(handle=handle,
                                 drive_slot=drive,
                                 controller_slot=controller_slot,
                                 server_id=server_id)
        size += _human_to_bytes(dmo.coerced_size)
    return _bytes_to_human(size)


def virtual_drive_create(handle,
                         drive_group,
                         controller_slot,
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
            drive_group (list of lists): list of drives
                            [[1]]
                            [[1,2]]
                            [[1,2],[3,4]]
            controller_slot(string): sas controller slot name/number
                                    "MEZZ","0"-"9"
            raid_level (int): raid level
                            0, 1, 5, 6, 10, 50, 60
                        Raid 0 — Simple striping.
                        Raid 1 — Simple mirroring.
                        Raid 5 — Striping with parity.
                        Raid 6 — Striping with two parity drives.
                        Raid 10 — Spanned mirroring.
                        Raid 50 — Spanned striping with parity.
                        Raid 60 — Spanned striping with two parity drives.

        Examples:
            virtual_drive_create(handle=imc,
                                 drive_group=[[2]],
                                 controller_slot='MEZZ')
    """
    server_dn = imccoreutils.get_server_dn(handle, server_id)
    slot_dn = server_dn + "/board/storage-SAS-SLOT-" + controller_slot

    dg_str = _list_to_string(drive_group)
    print(dg_str)
    vdn = virtual_drive_name

    params = {}
    params["parent_mo_or_dn"] = slot_dn
    params["drive_group"] = dg_str
    params["raid_level"] = str(raid_level)
    params["access_policy"] = access_policy
    params["read_policy"] = read_policy
    params["cache_policy"] = cache_policy
    params["disk_cache_policy"] = disk_cache_policy
    params["write_policy"] = write_policy
    params["strip_size"] = strip_size

    if (admin_action and
            handle.platform == imccoreutils.IMC_PLATFORM.TYPE_CLASSIC):
        params["admin_action"] = admin_action

    params["virtual_drive_name"] = \
        (_vd_name_create(raid_level, drive_group), vdn)[vdn is not None]

    params["size"] = (_vd_size_get(handle=handle,
                                   controller_slot=controller_slot,
                                   drive_list=drive_group,
                                   server_id=server_id),
                      size)[size is not None]

    mo = vd_creator(**params)
    mo.admin_state = "trigger"
    handle.add_mo(mo)
