# Copyright 2017 Cisco Systems, Inc.
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

import math
import logging

from imcsdk.imcexception import ImcOperationError, ImcException, ImcOperationErrorDetail
from imcsdk.apis.v2.storage.controller import _get_controller_dn
from imcsdk.apis.v2.storage.pd import pd_get
from imcsdk.mometa.storage.StorageVirtualDriveCreatorUsingUnusedPhysicalDrive \
    import StorageVirtualDriveCreatorUsingUnusedPhysicalDrive as vd_creator
from imcsdk.mometa.storage.StorageVirtualDriveCreatorUsingVirtualDriveGroup \
    import StorageVirtualDriveCreatorUsingVirtualDriveGroup as vd_carve

log = logging.getLogger('imc')


def _list_to_string(drive_list):
    # convert to format imc expects
    # list to string
    # [[1]] => '[1]'
    # [[1,2],[3,4]] => '[1,2][3,4]'
    # imc fails to parse '[1, 2]'
    # it needs to be '[1,2]'
    # and hence the replace(' ', '')
    dg_str = ""
    for each in drive_list:
        dg_str += str(each)
    return dg_str.replace(' ', '')


def _flatten_list(drive_list):
    # convert to format imc expects
    # [[1]] => [1]
    # [[1,2],[3,4]] => [1, 2, 3, 4]
    if not (isinstance(drive_list, list) and isinstance(drive_list[0], list)):
        raise "drive_list needs a list of list(s). i.e [[1,2],[3,4]]"
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


def vd_name_derive(raid_level, drive_list):
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


def _bytes_to_human(size, output_format=None):
    """
    converts bytes to human readable format.
        The return is in output_format.
    """
    convert = {'KB': 1, 'MB': 2, 'GB': 3, 'TB': 4,
               'PB': 5, 'EB': 6, 'ZB': 7, 'YB': 8}
    unit = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    if output_format is None:
        output_format = unit[int(math.floor(math.log(size, 2))/10)]
    if output_format not in convert:
        raise "unknown output format" + output_format
    return str(size >> (10 * convert[output_format])) + ' ' + output_format


def _pd_sizes_get(handle,
                  controller_type,
                  controller_slot,
                  drive_list,
                  server_id=1):
    sizes = []
    for each in drive_list:
        for drive in each:
            dmo = pd_get(handle=handle,
                         controller_type=controller_type,
                         controller_slot=controller_slot,
                         drive_slot=drive,
                         server_id=server_id)
            sizes.append(_human_to_bytes(dmo.coerced_size))
    return sizes


def _pd_min_size_get(sizes):
    return min(sizes)


def _pd_total_size_get(sizes):
    return sum(sizes)


def _pd_unused_get(handle):
    return handle.query_classid(class_id='StorageUnusedLocalDisk')


def _vd_span_depth_get(drive_list):
    return len(drive_list)


def _raid_max_size_get(raid_level, total_size, min_size, span_depth):
    size = {0: total_size,
            1: total_size/2,
            5: total_size - (span_depth * 1 * min_size),
            6: total_size - (span_depth * 2 * min_size),
            10: total_size/2,
            50: total_size - (span_depth * 1 * min_size),
            60: total_size - (span_depth * 2 * min_size)}

    if raid_level not in size:
        raise ImcOperationError("Create Virtual Drive",
                                "Unsupported Raid level <%s>" % raid_level)
    return size[raid_level]


def _vd_max_size_get(handle,
                     controller_type,
                     controller_slot,
                     drive_list,
                     raid_level,
                     server_id=1):
    """
    Returns the usable disk size for the specified virtual_drive
        drive_list:
            [[1]]
            [[1,2],[3,4]]

        min_size = smallest size of all the drives from this disk group
        available_size = accumulated size of all the drives together
        span_depth = number of sub groups [[1,2,3],[4,5,6]] span_depth = 2
    """
    sizes = _pd_sizes_get(handle=handle,
                          controller_type=controller_type,
                          controller_slot=controller_slot,
                          drive_list=drive_list,
                          server_id=server_id)
    min_size = _pd_min_size_get(sizes)
    total_size = _pd_total_size_get(sizes)
    span_depth = _vd_span_depth_get(drive_list)

    max_size = _raid_max_size_get(raid_level, total_size, min_size, span_depth)
    return _bytes_to_human(max_size, output_format="MB")


def _existing_vd_maxsize_get(handle, vd_carve, id):
    dn = vd_carve.dn + "/vd-" + str(id)

    mo = handle.query_dn(dn)
    if mo is None:
        raise ImcOperationError("Create Virtual drive using existing Virtual drives",
                                "Existing Drive: %s does not exist OR " \
                                "No space is available to create another Virtual " \
                                "drive." % id)
    return mo.max_available_space


def vd_create_using_unused_pds(handle,
                               drive_group,
                               controller_type,
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
                               self_encrypt=False,
                               server_id=1):
    """
    Creates virtual drive from unused physical drives

    Args:
        handle (ImcHandle)
        drive_group (list of lists): list of drives
                        [[1]]
                        [[1,2]]
                        [[1,2],[3,4]]
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        raid_level (int): raid level
                        0, 1, 5, 6, 10, 50, 60
                    Raid 0 Simple striping.
                    Raid 1 Simple mirroring.
                    Raid 5 Striping with parity.
                    Raid 6 Striping with two parity drives.
                    Raid 10 Spanned mirroring.
                    Raid 50 Spanned striping with parity.
                    Raid 60 Spanned striping with two parity drives.
        virtual_drive_name (str): Name of the virtual drive
        access_policy (str): Access-policy for the virtual drive
                ['read-write', 'read-only', 'hidden', 'default', 'blocked']
        read_policy (str): Read Policy for the virtual drive.
                ["always-read-ahead", "no-read-ahead"]
        cache_policy (str): Cache policy used for buffering reads.
                ["cached-io", "direct-io"]
        disk_cache_policy: Disk cache policy.
                ["disabled", "enabled", "unchanged"]
        write_policy: Write policy
                ["always-write-back", "write-back-good-bbu", "write-through"]
        strip_size: Size of each strip
                ["1024k", "128k", "16k", "256k", "32k", "512k", "64k", "8k"]
        size: The size of the virtual drive you want to create.
                Enter a value and select one of the following units - MB,GB,TB
                e.g. '100 MB' or '20 GB' or '1 TB'
        self_encrypt (bool): Encrypt the virtual drive if the underlying
                             controller and physical drive support it
        server_id (int): Specify server id for UCS C3260 modular servers

    Returns:
        None

    Examples:
        vd_create_using_unused_pds(handle=imc, drive_group=[[2]],
                                   controller_type = 'SAS',
                                   controller_slot='MEZZ')
    """
    slot_dn = _get_controller_dn(handle, controller_type,
                                 controller_slot, server_id)

    dg_str = _list_to_string(drive_group)
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

    if self_encrypt:
        params["admin_action"] = "enable-self-encrypt"

    params["virtual_drive_name"] = \
        (vd_name_derive(raid_level, drive_group), vdn)[vdn is not None]

    params["size"] = (_vd_max_size_get(handle=handle,
                                       controller_type=controller_type,
                                       controller_slot=controller_slot,
                                       drive_list=drive_group,
                                       raid_level=raid_level,
                                       server_id=server_id),
                      size)[size is not None]

    mo = vd_creator(**params)
    mo.admin_state = "trigger"
    handle.add_mo(mo)


def vd_create_using_existing_vd(handle,
                                controller_type,
                                controller_slot,
                                shared_virtual_drive_id,
                                virtual_drive_name,
                                access_policy="read-write",
                                read_policy="no-read-ahead",
                                cache_policy="direct-io",
                                disk_cache_policy="unchanged",
                                write_policy="Write Through",
                                strip_size="64k",
                                size=None,
                                server_id=1):
    """
    Creates virtual drive from the existing virtua drives.

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        shared_virtual_drive_id (str): Id of the existing virtual drive
        virtual_drive_name (str): Name of the virtual drive
        access_policy (str): Access-policy for the virtual drive
                ['read-write', 'read-only', 'hidden', 'default', 'blocked']
        read_policy (str): Read Policy for the virtual drive.
                ["always-read-ahead", "no-read-ahead"]
        cache_policy (str): Cache policy used for buffering reads.
                ["cached-io", "direct-io"]
        disk_cache_policy: Disk cache policy.
                ["disabled", "enabled", "unchanged"]
        write_policy: Write policy
                ["always-write-back", "write-back-good-bbu", "write-through"]
        strip_size: Size of each strip
                ["1024k", "128k", "16k", "256k", "32k", "512k", "64k", "8k"]
        size: The size of the virtual drive you want to create.
                Enter a value and select one of the following units - MB,GB,TB
                e.g. '100 MB' or '20 GB' or '1 TB'
        server_id (int): Specify server id for UCS C3260 modular servers

    Returns:
        None

    Examples:
        vd_create_using_existing_vd(handle=imc,
                                    controller_type='SAS',
                                    controller_slot='MEZZ',
                                    shared_virtual_drive_id=1,
                                    virtual_drive_name='newvd')
    """
    slot_dn = _get_controller_dn(handle, controller_type,
                                 controller_slot, server_id)

    mo = vd_carve(parent_mo_or_dn=slot_dn)

    params = {}
    params["shared_virtual_drive_id"] = str(shared_virtual_drive_id)
    params["virtual_drive_name"] = virtual_drive_name
    params["access_policy"] = access_policy
    params["read_policy"] = read_policy
    params["cache_policy"] = cache_policy
    params["disk_cache_policy"] = disk_cache_policy
    params["write_policy"] = write_policy
    params["strip_size"] = strip_size

    if size and size.strip():
        params["size"] = size
    else:
        params["size"] = _existing_vd_maxsize_get(handle=handle,
            vd_carve=mo, id=shared_virtual_drive_id)

    mo.set_prop_multiple(**params)
    mo.admin_state = "trigger"
    handle.add_mo(mo)


def vd_get(handle, controller_type, controller_slot, id, server_id=1):
    slot_dn = _get_controller_dn(handle, controller_type, controller_slot,
                                 server_id)
    dn = slot_dn + "/vd-" + str(id)
    mo = handle.query_dn(dn)
    if mo is None:
        raise ImcOperationError("Get Virtual drive: %s" % id,
                                "Not found")
    return mo

def vd_update(handle,
            controller_type,
            controller_slot,
            id,
            server_id=1,
            access_policy=None,
            read_policy=None,
            cache_policy=None,
            disk_cache_policy=None,
            write_policy=None):
    mo = vd_get(handle, controller_type, controller_slot, id, server_id)
    if mo is None:
        raise ImcOperationError("Get Virtual drive",
                                "Managed Object not found")

    if access_policy is not None:
        mo.access_policy = access_policy

    if read_policy is not None:
        mo.read_policy = read_policy

    if cache_policy is not None:
        mo.cache_policy = cache_policy

    if disk_cache_policy is not None:
        mo.disk_cache_policy = disk_cache_policy

    if write_policy is not None:
        mo.requested_write_cache_policy = write_policy

    handle.set_mo(mo)
    return mo


def _vd_set_action(handle, controller_type, controller_slot, id,
                   action,
                   server_id=1, **kwargs):
    mo = vd_get(handle, controller_type, controller_slot, id, server_id)
    if mo is None:
        raise ImcOperationError("Configure Virtual drive: %s" % id,
                                "Not found")
    mo.admin_action = action
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return mo


def vd_exists(handle, controller_type, controller_slot, id, server_id=1, **kwargs):
    """
    Checks if a virtual drive exists.

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        id (int): Id of the virtual drive

    Returns:
        exists(bool), error(str)

    Examples:
        vd_exists(handle=imc, controller_type='SAS', controller_slot='MEZZ',
                  id=1)
    """
    try:
        mo = vd_get(handle, controller_type, controller_slot, id, server_id)
    except:
        return False, None

    return True, mo


def vd_delete(handle, controller_type, controller_slot, id, server_id=1,
              delete_boot_drive=False):
    """
    Deletes the specified virtual drive

    Args:
        handle (ImcHandle)
        controller_slot (str): controller slot name/number
                               "MEZZ","0"-"9"
        id (int): id of the virtual drive
        server_id (int): server_id for UCS 3260 platform

    Examples:
        vd_delete(handle=imc, controller_type='SAS', controller_slot='MEZZ',
                  id=1)
    """
    from imcsdk.apis.v2.storage.controller import controller_clear_boot_drive

    mo = vd_get(handle=handle,
                controller_type=controller_type,
                controller_slot=controller_slot,
                id=id,
                server_id=server_id)

    if delete_boot_drive and mo.boot_drive.lower() in ('yes', 'true'):
        controller_clear_boot_drive(handle, controller_type,
                                    controller_slot, server_id)

    handle.remove_mo(mo)


def vd_delete_all(handle, controller_type, controller_slot, server_id=1,
                  delete_boot_drive=False):
    """
    Delete all the specified virtual drive

    Args:
        handle (ImcHandle)
        controller_slot (str): controller slot name/number
                               "MEZZ","0"-"9"
        id (int): id of the virtual drive
        server_id (int): server_id for UCS 3260 platform

    Examples:
        vd_delete_all(handle=imc, controller_type='SAS',
                      controller_slot='MEZZ', id=1)
    """
    from imcsdk.apis.v2.storage.controller import controller_clear_boot_drive

    controller_dn = _get_controller_dn(handle, controller_type,
                                       controller_slot, server_id)
    mos = handle.query_children(in_dn=controller_dn,
                                class_id="storageVirtualDrive")
    error_msg = ""
    for mo in mos:
        if delete_boot_drive and mo.boot_drive.lower() in ('yes', 'true'):
            controller_clear_boot_drive(handle, controller_type,
                                        controller_slot, server_id)
        try:
            handle.remove_mo(mo)
        except ImcException as e:
            error_msg += str(e)

    if error_msg:
        raise ImcOperationError("Delete all Virtual drives on controller: %s" % controller_slot,
                                error_msg)


def vd_exists_any(handle, controller_type, controller_slot, server_id=1,
                  **kwargs):
    """
    Checks if any virtual drive exists

    Args:
        handle (ImcHandle)
        controller_slot (str): controller slot name/number
                               "MEZZ","0"-"9"
        id (int): id of the virtual drive
        server_id (int): server_id for UCS 3260 platform

    Returns:
        bool

    Examples:
        vd_exists_any(handle=imc, controller_type='SAS',
                      controller_slot='MEZZ', id=1)
    """
    controller_dn = _get_controller_dn(handle, controller_type,
                                       controller_slot, server_id)
    mos = handle.query_children(in_dn=controller_dn,
                                class_id="storageVirtualDrive")
    if mos and len(mos) > 0:
        return True
    return False


def vd_boot_drive_enable(handle, controller_type, controller_slot, id,
                         server_id=1, **kwargs):
    """
    Set a virtual drive as boot drive.

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        id (int): id of the virtual drive
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageVirtualDrive object

    Examples:
        vd_set_boot_drive(handle, 'SAS', 'HBA', 'test_vd')
    """
    from imcsdk.mometa.storage.StorageVirtualDrive import \
        StorageVirtualDriveConsts

    action = StorageVirtualDriveConsts.ADMIN_ACTION_SET_BOOT_DRIVE
    return _vd_set_action(
            handle,
            controller_type=controller_type,
            controller_slot=controller_slot,
            id=id,
            action=action,
            server_id=server_id
        )


def vd_boot_drive_exists(handle, controller_type, controller_slot, id,
                         server_id=1):
    """
    Checkes if virtual drive is set as boot drive.

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        id (int): id of the virtual drive
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageVirtualDrive object

    Examples:
        vd_boot_drive_exists(handle, 'SAS', 'HBA', 1)
    """
    try:
        mo = vd_get(handle=handle,
                    controller_type=controller_type,
                    controller_slot=controller_slot,
                    id=id,
                    server_id=server_id)
    except:
        False, None

    if mo.boot_drive.lower() not in ('yes', 'true'):
        return False, mo
    return True, mo


def vd_boot_drive_disable(handle, controller_type, controller_slot, id,
                          server_id=1):
    """
    Set a virtual drive as boot drive.

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        id (int): id of the virtual drive
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageVirtualDrive object

    Examples:
        vd_set_boot_drive(handle, 'SAS', 'HBA', 'test_vd')
    """
    from imcsdk.apis.v2.storage.controller import controller_clear_boot_drive

    vd = vd_get(handle, controller_type, controller_slot, id, server_id)
    if vd.boot_drive.lower() not in ('true', 'yes'):
        return vd

    controller_clear_boot_drive(handle, controller_type, controller_slot,
                                server_id)

    return handle.query_dn(vd.dn)


def vd_encryption_enable(handle, controller_type, controller_slot, id,
                         server_id=1):
    """
    Enables encryption on the virtual drive if it is supported by the
    controller and the underlying physical drive

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        id (int): id of the virtual drive
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageVirtualDrive object

    Examples:
        vd_encryption_enable(handle, 'SAS', 'HBA', 1)
    """
    from imcsdk.mometa.storage.StorageVirtualDrive import \
        StorageVirtualDriveConsts

    action = StorageVirtualDriveConsts.ADMIN_ACTION_ENABLE_SELF_ENCRYPT
    return _vd_set_action(
            handle,
            controller_type=controller_type,
            controller_slot=controller_slot,
            id=id,
            action=action,
            server_id=server_id
        )


def vd_encryption_exists(handle, controller_type, controller_slot, id,
                         server_id=1):
    """
    Checks if encryption is enabled on the virtual drive

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        id (int): id of the virtual drive
        server_id (int): server_id for UCS 3260 platform

    Returns:
        boot

    Examples:
        vd_encryption_exists(handle, 'SAS', 'HBA', 0)
    """
    mo = vd_get(handle, controller_type, controller_slot, id, server_id)
    if mo is None:
        return False, None

    if mo.fde_enabled.lower() not in ['yes', 'true']:
        return False, mo

    return True, mo


def vd_get_by_name(handle, controller_type, controller_slot, name,
                   server_id=1):
    """
    Gets a virtual drive by name

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        name (str): name of the virtual drive
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageVirtualDrive object

    Examples:
        vd_get_by_name(handle, 'SAS', 'HBA', 'test_vd')
    """
    slot_dn = _get_controller_dn(handle, controller_type, controller_slot,
                                 server_id)

    mos = handle.query_children(in_dn=slot_dn, class_id="storageVirtualDrive")
    for mo in mos:
        if mo.name == name:
            return mo
    return None
