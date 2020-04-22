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

import math
import logging
import imcsdk.imccoreutils as imccoreutils
from imcsdk.imcexception import ImcOperationError
from imcsdk.mometa.storage.StorageVirtualDriveCreatorUsingUnusedPhysicalDrive \
    import StorageVirtualDriveCreatorUsingUnusedPhysicalDrive as vd_creator
from imcsdk.mometa.self.SelfEncryptStorageController import \
    SelfEncryptStorageController, SelfEncryptStorageControllerConsts
from imcsdk.mometa.storage.StorageLocalDisk import StorageLocalDiskConsts
from imcsdk.mometa.storage.StorageController import StorageControllerConsts

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
            dmo = physical_drive_get(handle=handle,
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
        raise "Unsupported Raid level" + str(raid_level)
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


def _get_controller_dn(handle, controller_type, controller_slot, server_id=1):
    server_dn = imccoreutils.get_server_dn(handle, server_id)
    return (server_dn + "/board/storage-" + controller_type + "-" + controller_slot)


def _get_controller(handle, controller_type, controller_slot, server_id=1):
    mo = handle.query_dn(_get_controller_dn(handle,
                                            controller_type,
                                            controller_slot,
                                            server_id))
    if mo is None:
        raise ImcOperationError("Get Controller Type:%s Slot:%s" %
                                    (controller_type, controller_slot),
                                "Managed Object not found")
    return mo


def virtual_drive_create(handle,
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
        virtual_drive_name (str): Name of the virtual drive
        raid_level (int): raid level
                        0, 1, 5, 6, 10, 50, 60
                    Raid 0 Simple striping.
                    Raid 1 Simple mirroring.
                    Raid 5 Striping with parity.
                    Raid 6 Striping with two parity drives.
                    Raid 10 Spanned mirroring.
                    Raid 50 Spanned striping with parity.
                    Raid 60 Spanned striping with two parity drives.
        access_policy (str): Access-policy for the virtual drive
                ['read-write', 'read-only', 'hidden', 'default', 'blocked']
        self_encrypt (bool): Encrypt the virtual drive if the underlying
                             controller and physical drive support it

    Returns:
        StorageVirtualDrive object

    Examples:
        virtual_drive_create(handle=imc,
                             drive_group=[[2]],
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
    return mo


def vd_query_by_name(handle,
                     controller_type,
                     controller_slot,
                     name,
                     server_id=1):
    slot_dn = _get_controller_dn(handle, controller_type, controller_slot, server_id)

    mos = handle.query_children(in_dn=slot_dn, class_id="storageVirtualDrive")
    for mo in mos:
        if mo.name == name:
            return mo
    return None


def virtual_drive_exists(handle,
                         controller_type,
                         controller_slot,
                         virtual_drive_name,
                         server_id=1):
    """
    Checks if a virtual drive by the specified name exists.

    Args:
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        virtual_drive_name (str): Name of the virtual drive

    Returns:
        exists(bool), error(str)
    """
    mo = vd_query_by_name(handle, controller_type, controller_slot,
                          virtual_drive_name, server_id)
    return mo is not None, None


def virtual_drive_delete(handle,
                         controller_type,
                         controller_slot,
                         name,
                         server_id=1):
    """
    Deletes the specified virtual drive

    Args:
        handle (ImcHandle)
        controller_slot (str): controller slot name/number
                               "MEZZ","0"-"9"
        name (string): name of the virtual drive to delete
        server_id (int): server_id for UCS 3260 platform

    Examples:
        virtual_drive_delete(handle=imc,
                             controller_slot='MEZZ',
                             name="RAID0_1")
    """
    vd = vd_query_by_name(handle=handle,
                          controller_type=controller_type,
                          controller_slot=controller_slot,
                          name=name,
                          server_id=server_id)
    handle.remove_mo(vd)


def virtual_drive_encryption_enable(handle, controller_type,
                                    controller_slot, name, server_id=1):
    """
    Enables encryption on the virtual drive if it is supported by the controller
    and the underlying physical drive

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        name (string): name of the virtual drive
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageVirtualDrive object

    Examples:
        virtual_drive_encryption_enable(handle, 'SAS', 'HBA', 'test_vd')
    """
    from imcsdk.mometa.storage.StorageVirtualDrive import \
        StorageVirtualDriveConsts
    vd = vd_query_by_name(handle=handle,
                          controller_type=controller_type,
                          controller_slot=controller_slot,
                          name=name,
                          server_id=server_id)
    vd.admin_action = StorageVirtualDriveConsts.ADMIN_ACTION_ENABLE_SELF_ENCRYPT
    handle.set_mo(vd)
    return handle.query_dn(vd.dn)


def virtual_drive_set_boot_drive(handle, controller_type, controller_slot, name, server_id=1):
    """
    Set a virtual drive as boot drive.

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        name (string): name of the virtual drive
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageVirtualDrive object

    Examples:
        virtual_drive_set_boot_drive(handle, 'SAS', 'HBA', 'test_vd')
    """
    from imcsdk.mometa.storage.StorageVirtualDrive import \
        StorageVirtualDriveConsts
    vd = vd_query_by_name(handle=handle,
                          controller_type=controller_type,
                          controller_slot=controller_slot,
                          name=name,
                          server_id=server_id)
    vd.admin_action = StorageVirtualDriveConsts.ADMIN_ACTION_SET_BOOT_DRIVE
    handle.set_mo(vd)
    return handle.query_dn(vd.dn)

def _controller_action_set(handle, controller_type, controller_slot, action,
                           server_id=1):
    controller_mo = _get_controller(handle,
                                    controller_type,
                                    controller_slot,
                                    server_id)
    controller_mo.admin_action = action
    handle.set_mo(controller_mo)
    return handle.query_dn(controller_mo.dn)


def controller_jbod_mode_enable(handle, controller_type,
                                controller_slot, server_id=1):
    """
    Enables jbod mode on the controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        controller_jbod_mode_enable(handle, controller_type='SAS',
                                    controller_slot='HBA')

    """
    return _controller_action_set(handle, controller_type,
                                  controller_slot, 'enable-jbod',
                                  server_id=server_id)


def controller_jbod_mode_disable(handle, controller_type,
                                    controller_slot, server_id=1):
    """
    Disables jbod mode on the controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        controller_jbod_mode_disable(handle, controller_type='SAS',
                                     controller_slot='HBA')

    """
    return _controller_action_set(handle, controller_type,
                                  controller_slot, 'disable-jbod',
                                  server_id=server_id)


def is_controller_jbod_mode_enabled(handle, controller_type,
                                    controller_slot, server_id=1):
    """
    Checks if jbod mode is enabled on the controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        bool

    Examples:
        is_controller_jbod_mode_enabled(handle, controller_type='SAS',
                                        controller_slot='HBA')
    """
    dn = _get_controller_dn(handle, controller_type, controller_slot, server_id)
    settings = handle.query_children(in_dn=dn, class_id='StorageControllerSettings')
    return settings[0].enable_jbod.lower() in ['yes', 'true'] if settings else False


def controller_encryption_enable(handle, controller_type,
                                 controller_slot, key_id, security_key,
                                 key_management="local", server_id=1,
                                 **kwargs):
    """
    Enables encryption on the controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                               "MEZZ","0"-"9"
        key_id (str): Security Key Identifier.
                      Max Length is 256 characters.
        security_key (str): Security key used to enable controller security.
                            Max Length is 32 characters.
        key_management (str): "local" or "remote"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        controller_encryption_enable(handle,
                                 controller_type='SAS',
                                 controller_slot='HBA'',
                                 key_id='ABCD12345', security_key='12345')
    """
    from imcsdk.mometa.self.SelfEncryptStorageController import \
        SelfEncryptStorageController, SelfEncryptStorageControllerConsts

    enabled, mo = controller_encryption_exists(handle,
                                               controller_type,
                                               controller_slot,
                                               server_id)
    if enabled:
        return mo
    dn = mo.dn
    mo = SelfEncryptStorageController(parent_mo_or_dn=dn)
    params = {
        'key_id': key_id,
        'security_key': security_key,
        'key_management': key_management,
        'admin_action':
        SelfEncryptStorageControllerConsts.ADMIN_ACTION_ENABLE_SELF_ENCRYPT,
    }

    mo.set_prop_multiple(**params)
    handle.set_mo(mo)
    return handle.query_dn(dn)


def controller_encryption_disable(handle, controller_type,
                                  controller_slot, server_id=1):
    """
    Disables encryption on the controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        controller_encryption_disable(handle,
                                  controller_type='SAS',
                                  controller_slot='HBA'')
    """
    dn = _get_controller_dn(
                handle,
                controller_type,
                controller_slot,
                server_id)

    mo = SelfEncryptStorageController(parent_mo_or_dn=dn)
    mo.admin_action = \
        SelfEncryptStorageControllerConsts.ADMIN_ACTION_DISABLE_SELF_ENCRYPT
    handle.set_mo(mo)
    return handle.query_dn(dn)


def controller_encryption_exists(handle, controller_type, controller_slot,
                                 server_id=1):
    """
    Checks if encryption is enabled on the controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        bool

    Examples:
        is_controller_encryption_enabled(
                            handle,
                            controller_type='SAS',
                            controller_slot='HBA'')
    """

    mo = _get_controller(handle, controller_type, controller_slot, server_id)
    if mo.self_encrypt_enabled.lower() in ['yes', 'true']:
        return True, mo
    return False, mo


def controller_encryption_modify_security_key(handle,
                                              controller_type,
                                              controller_slot,
                                              existing_security_key,
                                              security_key,
                                              key_management="local",
                                              server_id=1):
    """
    Modifies the security key on the controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        existing_security_key (str): Existing Security Key
        security_key (str): New Security Key
        key_management (str): "local" or "remote"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        controller_encryption_modify_security_key(
                     handle,
                     controller_type='SAS',
                     controller_slot='HBA'',
                     existing_security_key='Nbv12345',
                     security_key='Nbv123456')
    """
    dn = _get_controller_dn(handle,
                            controller_type,
                            controller_slot,
                            server_id)
    mo = SelfEncryptStorageController(parent_mo_or_dn=dn)
    params = {
        'existing_security_key': existing_security_key,
        'security_key': security_key,
        'key_management': key_management,
    }
    mo.set_prop_multiple(**params)
    handle.set_mo(mo)
    return handle.query_dn(dn)


def controller_encryption_key_id_generate(handle, controller_type,
                                          controller_slot, server_id=1):
    """
    Generates a random key id for the given controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        Key-id string

    Examples:
        key_id = controller_encryption_key_id_generate(
                handle,
                controller_type='SAS',
                controller_slot='HBA'')
    """
    dn = _get_controller_dn(handle, controller_type, controller_slot, server_id)
    mos = handle.query_children(
                in_dn=dn,
                class_id='GeneratedStorageControllerKeyId')
    return mos[0].generated_key_id if mos else ""


def controller_encryption_key_generate(handle, controller_type,
                                       controller_slot, server_id=1):
    """
    Generates a random security key for the given controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        Security Key string

    Examples:
        key = controller_encryption_key_generate(
                handle,
                controller_type='SAS',
                controller_slot='HBA'')
    """
    dn = _get_controller_dn(handle, controller_type, controller_slot, server_id)
    mos = handle.query_children(
                in_dn=dn,
                class_id='SuggestedStorageControllerSecurityKey')
    return mos[0].suggested_security_key if mos else ""


def controller_unlock_foreign_drives(handle, controller_type,
                                     controller_slot, security_key,
                                     server_id=1):
    """
    Unlocks on the given controller, drives encrypted on another controller.

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        security_key (str): Security Key used to encrypt the foreign drive
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        key = controller_unlock_foreign_drives(
                handle,
                controller_type='SAS',
                controller_slot='HBA'',
                security_key='12345')
    """
    dn = _get_controller_dn(handle, controller_type, controller_slot, server_id)
    mo = SelfEncryptStorageController(parent_mo_or_dn=dn)
    params = {
        'security_key': security_key,
        'admin_action': SelfEncryptStorageControllerConsts.ADMIN_ACTION_UNLOCK_SECURED_DRIVES
    }
    mo.set_prop_multiple(**params)
    return handle.query_dn(dn)


def controller_import_foreign_config(handle, controller_type,
                                     controller_slot, server_id=1):
    """
    Imports foreign configuration on the given controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        controller_import_foreign_config(handle,
                controller_type='SAS',
                controller_slot='HBA'')
    """
    return _controller_action_set(
                handle,
                controller_type,
                controller_slot,
                action=StorageControllerConsts.ADMIN_ACTION_IMPORT_FOREIGN_CONFIG,
                server_id=server_id)


def physical_drive_get(handle,
                       controller_type,
                       controller_slot,
                       drive_slot,
                       server_id=1):
    """
    Gets the physical drive

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        drive_slot (int): Slot in which the drive resides
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageLocalDisk object

    Examples:
        mo = physical_drive_get(handle, controller_type='SAS',
                            controller_slot='HBA'',
                            drive_slot=4')
    """
    controller_dn = _get_controller_dn(handle, controller_type,
                                       controller_slot, server_id)
    drive_dn = controller_dn + '/pd-' + str(drive_slot)
    return handle.query_dn(drive_dn)


def _physical_drive_action_set(handle, controller_type,
                               controller_slot, drive_slot,
                               action, server_id=1):
    mo = physical_drive_get(handle, controller_type, controller_slot,
                       drive_slot, server_id)
    if mo is None:
        raise ImcOperationError("Get Physical Drive",
                                "Managed Object not found")
    mo.admin_action = action
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def is_physical_drive_encryption_capable(handle, controller_type,
                                         controller_slot, drive_slot,
                                         server_id=1):
    """
    Checks if encryption is supported on the physical drive

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        drive_slot (int): Slot in which the drive resides
        server_id (int): server_id for UCS 3260 platform

    Returns:
        bool

    Examples:
        capable = is_physical_drive_encryption_capable(
                    handle,
                    controller_type='SAS',
                    controller_slot='HBA'',
                    drive_slot=4')
    """
    drive = physical_drive_get(handle, controller_type,
                               controller_slot, drive_slot,
                               server_id)
    if drive is None:
        raise ImcOperationError("Get Physical Drive:%s" % drive_slot,
                                "Managed Object not found")
    return drive.fde_capable.lower() in ['yes', 'true']


def is_physical_drive_encryption_enabled(handle, controller_type,
                                             controller_slot, drive_slot,
                                             server_id=1):
    """
    Checks if encryption is enabled on the physical drive

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        drive_slot (int): Slot in which the drive resides
        server_id (int): server_id for UCS 3260 platform

    Returns:
        bool

    Examples:
        enabled = is_physical_drive_encryption_enabled(
                handle,
                controller_type='SAS',
                controller_slot='HBA'',
                drive_slot=4')
    """
    drive = physical_drive_get(handle, controller_type,
                               controller_slot, drive_slot,
                               server_id)
    if drive is None:
        raise ImcOperationError("Get Physical Drive:%s" % drive_slot,
                                "Managed Object not found")
    return drive.fde_enabled.lower() in ['yes', 'true']


def physical_drive_set_jbod_mode(handle, controller_type,
                                 controller_slot, drive_slot, server_id=1):
    """
    Sets the physical drive in jbod mode

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        drive_slot (int): Slot in which the drive resides
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageLocalDisk object

    Examples:
        physical_drive_set_jbod_mode(handle,
                                 controller_type='SAS',
                                 controller_slot='HBA'',
                                 drive_slot=4')
    """
    if not is_controller_jbod_mode_enabled(handle, controller_type,
                                           controller_slot, server_id):
        raise ImcOperationError("Physical Drive: %s JBOD Mode Enable",
                                "Controller JBOD mode is not enabled")
    return _physical_drive_action_set(
            handle,
            controller_type=controller_type,
            controller_slot=controller_slot,
            drive_slot=drive_slot,
            action=StorageLocalDiskConsts.ADMIN_ACTION_MAKE_JBOD,
            server_id=server_id
        )


def physical_drive_set_unconfigured_good(handle,
                                         controller_type,
                                         controller_slot,
                                         drive_slot,
                                         server_id=1):
    """
    Sets the physical drive in unconfigured good state

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        drive_slot (int): Slot in which the drive resides
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageLocalDisk object

    Examples:
        physical_drive_set_unconfigured_good(
                handle,
                controller_type='SAS',
                controller_slot='HBA'',
                drive_slot=4')
    """
    return _physical_drive_action_set(
            handle,
            controller_type=controller_type,
            controller_slot=controller_slot,
            drive_slot=drive_slot,
            action=StorageLocalDiskConsts.ADMIN_ACTION_MAKE_UNCONFIGURED_GOOD,
            server_id=server_id
        )


def physical_drive_encryption_enable(handle, controller_type,
                                     controller_slot, drive_slot, server_id=1):
    """
    Enables encryption on the physical drive

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        drive_slot (int): Slot in which the drive resides
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageLocalDisk object

    Examples:
        physical_drive_encryption_enable(
                handle,
                controller_type='SAS',
                controller_slot='HBA'',
                drive_slot=4')
    """
    return _physical_drive_action_set(
            handle,
            controller_type=controller_type,
            controller_slot=controller_slot,
            drive_slot=drive_slot,
            action=StorageLocalDiskConsts.ADMIN_ACTION_ENABLE_SELF_ENCRYPT,
            server_id=server_id
        )


def physical_drive_encryption_disable(handle, controller_type,
                                      controller_slot, drive_slot, server_id=1):
    """
    Disables encryption on the physical drive

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        drive_slot (int): Slot in which the drive resides
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageLocalDisk object

    Examples:
        physical_drive_encryption_disable(
                handle,
                controller_type='SAS',
                controller_slot='HBA'',
                drive_slot=4')
    """
    return _physical_drive_action_set(
            handle,
            controller_type=controller_type,
            controller_slot=controller_slot,
            drive_slot=drive_slot,
            action=StorageLocalDiskConsts.ADMIN_ACTION_DISABLE_SELF_ENCRYPT,
            server_id=server_id
        )


def physical_drive_secure_erase_foreign_drives(
                handle,
                controller_type,
                controller_slot,
                drive_slot,
                server_id=1):
    """
    Erases foreign configuration from the physical drive. Drive data is lost.

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        drive_slot (int): Slot in which the drive resides
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageLocalDisk object

    Examples:
        physical_drive_secure_erase_foreign_drives(
                handle,
                controller_type='SAS',
                controller_slot='HBA'',
                drive_slot=4')
    """
    return _physical_drive_action_set(
            handle,
            controller_type=controller_type,
            controller_slot=controller_slot,
            drive_slot=drive_slot,
            action=StorageLocalDiskConsts.ADMIN_ACTION_DISABLE_SED_FOREIGN_DRIVES,
            server_id=server_id
        )
