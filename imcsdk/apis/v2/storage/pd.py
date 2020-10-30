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
This module provides APIs for physical drive configuration.
"""

import logging

from imcsdk.imcexception import ImcOperationError, ImcException
from imcsdk.mometa.storage.StorageLocalDisk import StorageLocalDiskConsts
from imcsdk.apis.v2.storage.controller import _get_controller_dn, controller_m2_hwraid_exists

log = logging.getLogger('imc')


def pd_get(handle,
           controller_type, controller_slot, drive_slot,
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
        mo = pd_get(handle, controller_type='SAS', controller_slot='HBA',
                    drive_slot=4)
    """
    controller_dn = _get_controller_dn(handle,
                                       controller_type,
                                       controller_slot,
                                       server_id)
    dn = controller_dn + '/pd-' + str(drive_slot)
    return handle.query_dn(dn)


def _pd_set_action(handle, controller_type, controller_slot, drive_slot,
                   action,
                   server_id=1, **kwargs):
    mo = pd_get(handle, controller_type, controller_slot, drive_slot,
                server_id)
    if mo is None:
        raise ImcOperationError("Get Physical drive: %s" % drive_slot,
                                "Not found")
    mo.admin_action = action
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def pd_set_unconfigured_good(handle,
                             controller_type, controller_slot, drive_slot,
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
        pd_set_unconfigured_good(handle, controller_type='SAS',
                                 controller_slot='HBA', drive_slot=4)
    """
    action = StorageLocalDiskConsts.ADMIN_ACTION_MAKE_UNCONFIGURED_GOOD
    return _pd_set_action(
        handle,
        controller_type=controller_type,
        controller_slot=controller_slot,
        drive_slot=drive_slot,
        action=action,
        server_id=server_id
    )


def pd_set_jbod(handle,
                controller_type, controller_slot, drive_slot,
                server_id=1):
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
        pd_set_jbod(handle, controller_type='SAS', controller_slot='HBA',
                    drive_slot=4)
    """
    from imcsdk.apis.v2.storage.controller import controller_jbod_exists

    if not controller_jbod_exists(handle,
                                  controller_type,
                                  controller_slot,
                                  server_id):
        raise ImcOperationError("Enable JBOD mode on Physical drive: %s" % drive_slot,
                                "Controller JBOD mode is not enabled")

    action = StorageLocalDiskConsts.ADMIN_ACTION_MAKE_JBOD
    return _pd_set_action(
        handle,
        controller_type=controller_type,
        controller_slot=controller_slot,
        drive_slot=drive_slot,
        action=action,
        server_id=server_id
    )


def pd_set_global_hot_spare(handle,
                            controller_type, controller_slot, drive_slot,
                            server_id=1):
    """
    Sets the physical drive as a global hot spare

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
        pd_set_global_hot_spare(handle, controller_type='SAS',
                                controller_slot='HBA', drive_slot=4)
    """
    action = StorageLocalDiskConsts.ADMIN_ACTION_MAKE_GLOBAL_HOT_SPARE
    return _pd_set_action(
        handle,
        controller_type=controller_type,
        controller_slot=controller_slot,
        drive_slot=drive_slot,
        action=action,
        server_id=server_id
    )


def pd_set_dedicated_hot_spare(handle, controller_type, controller_slot,
                               drive_slot, vd_id, server_id=1):
    """
    Sets the physical drive as dedicated hot spare

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        drive_slot (int): Slot in which the drive resides
        vd_id (str): virtual drive id
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageLocalDisk object

    Examples:
        pd_set_dedicated_hot_spare(handle, controller_type='SAS',
                                   controller_slot='HBA', drive_slot=4)
    """
    action = StorageLocalDiskConsts.ADMIN_ACTION_MAKE_DEDICATED_HOT_SPARE
    return _pd_set_action(
        handle,
        controller_type=controller_type,
        controller_slot=controller_slot,
        drive_slot=drive_slot,
        action=action,
        server_id=server_id,
        dedicated_hot_spare_for_vd_id=vd_id
    )


def pd_remove_hot_spare(handle,
                        controller_type, controller_slot, drive_slot,
                        server_id=1):
    """
    Removes the physical drive from hot spare pool.

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
        pd_remove_hot_spare(handle, controller_type='SAS',
                                controller_slot='HBA', drive_slot=4)
    """
    action = StorageLocalDiskConsts.ADMIN_ACTION_REMOVE_HOT_SPARE
    return _pd_set_action(
        handle,
        controller_type=controller_type,
        controller_slot=controller_slot,
        drive_slot=drive_slot,
        action=action,
        server_id=server_id
    )


def pd_set_boot_drive(handle,
                      controller_type, controller_slot, drive_slot,
                      server_id=1):
    """
    Sets the physical drive as boot drive

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
        pd_set_boot_drive(handle, controller_type='SAS',
                          controller_slot='HBA', drive_slot=4)
    """
    action = StorageLocalDiskConsts.ADMIN_ACTION_SET_BOOT_DRIVE
    return _pd_set_action(
        handle,
        controller_type=controller_type,
        controller_slot=controller_slot,
        drive_slot=drive_slot,
        action=action,
        server_id=server_id
    )


def _pd_exists_boot_drive(handle, pd_dn):
    dn = pd_dn + '/general-props'
    mo = handle.query_dn(dn)
    if mo is None:
        return False
    if mo.boot_drive.lower() != 'true':
        return False
    return True


def pd_set_removal_prepare(handle,
                           controller_type, controller_slot, drive_slot,
                           server_id=1):
    """
    Sets the physical drive as boot drive

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
        pd_prepare_removal(handle, controller_type='SAS',
                           controller_slot='HBA', drive_slot=4)
    """
    action = StorageLocalDiskConsts.ADMIN_ACTION_PREPARE_FOR_REMOVAL
    return _pd_set_action(
        handle,
        controller_type=controller_type,
        controller_slot=controller_slot,
        drive_slot=drive_slot,
        action=action,
        server_id=server_id
    )


def pd_set_removal_undo(handle,
                        controller_type, controller_slot, drive_slot,
                        server_id=1):
    """
    Sets the physical drive as boot drive

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
        pd_undo_removal(handle, controller_type='SAS', controller_slot='HBA'',
                        drive_slot=4')
    """
    action = StorageLocalDiskConsts.ADMIN_ACTION_UNDO_PREPARE_FOR_REMOVAL
    return _pd_set_action(
        handle,
        controller_type=controller_type,
        controller_slot=controller_slot,
        drive_slot=drive_slot,
        action=action,
        server_id=server_id
    )


def pd_secure_erase_foreign_drives(handle, controller_type, controller_slot,
                                   drive_slot, server_id=1):
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
    action = StorageLocalDiskConsts.ADMIN_ACTION_DISABLE_SED_FOREIGN_DRIVES,
    return _pd_set_action(
        handle,
        controller_type=controller_type,
        controller_slot=controller_slot,
        drive_slot=drive_slot,
        action=action,
        server_id=server_id
    )


def sc_pd_state_set(handle, storage_controllers, drive_state, server_id=1, **kwargs):
    """
    Wrapper function for pd_state_set to handle multiple storage controllers.
    sc_pd_state_set sets the physical disk state of each of the storage controller in storage_controllers list.

    Args:
        handle (ImcHandle)
        storage_controllers (dictionary):
        Key: Storage controller pciSlot (string)
        Value: extravars of that storage controller.
                    {
          "storage_controllers": {
            "MRAID": {
              "controller_type": "SAS",
              "virtual_drives_on_pd": [
                {
                  "self_encrypt": false,
                  "read_policy": "no-read-ahead",
                  "cache_policy": "direct-io",
                  "disk_cache_policy": "unchanged",
                  "virtual_drive_name": "vd1",
                  "raid_level": 1,
                  "drive_group": "[[1,2]]",
                  "write_policy": "write-through",
                  "access_policy": "read-write",
                  "size": "1024 MB"
                }
              ],
              "dedicated_hot_spares": [
                {
                  "slot": 3,
                  "vd_id": "0"
                }
              ],
              "controller_slot": "MRAID",
              "virtual_drives_on_vd": [
                {
                  "read_policy": "no-read-ahead",
                  "cache_policy": "direct-io",
                  "disk_cache_policy": "unchanged",
                  "virtual_drive_name": "vd2",
                  "write_policy": "write-through",
                  "shared_virtual_drive_name": "vd1",
                  "access_policy": "read-write",
                  "size": "1024 MB"
                }
              ],
              "disks_state": [
                {
                  "slot": 4,
                  "state": "global_hot_spare"
                }
              ],
              "remove_all_vds": true
            }
          }
        }

    Example:
        sc_pd_state_set(handle, storage_controllers, drive_state="dedicated_hot_spare",
                     server_id=1)
    """
    if len(storage_controllers) == 0:
        raise ImcOperationError("Setting physical disk state failed. ",
                                "Storage controllers information is not specified.")
    for sc_obj in storage_controllers:
        sc = storage_controllers.get(sc_obj)

        # Check for storage controller and ignore if it is M.2 HWRAID Storage Controller as
        # setting physical disk state is invalid.
        is_m2_controller = controller_m2_hwraid_exists(handle, sc["controller_slot"], server_id)

        # Check for the physical disk state to configure its defined state.
        disks_state = sc.get("disks_state")
        if disks_state and not drive_state:
            for disk in disks_state:
                if disk.get("slot") is None or disk.get("state") is None:
                    raise ImcOperationError("Setting physical disk state failed. "
                                            "Drive slot/state is not found in controller: %s" % sc["controller_slot"])

                if not is_m2_controller:
                    try:
                        pd_state_set(handle,
                                 sc["controller_type"],
                            sc["controller_slot"],
                            disk["slot"],
                            disk["state"])
                    except ImcException as e:
                        # On deleting the VD, the pd state gets changed. If the end point state is same as configuration state,
                        # CIMC throws an ImcException.
                        # ignore errors because sometimes the previous operations will change the disk state to desired state
                        # eg: removing virtual drives move online disks to unconfigured good and dedicated hot spares to
                        # unconfigured good. Ignore this exception as our configuration state is same as end point state.
                        log.debug(e)
                        pass

        # Check if any dedicated_hot_spare disk configuration exists.
        dedicated_hot_spares = sc.get("dedicated_hot_spares")
        if dedicated_hot_spares and drive_state:
            for spare in dedicated_hot_spares:
                if spare.get("slot") is None or spare.get("vd_id") is None:
                    raise ImcOperationError("Setting physical disk as dedicated hot spare failed. "
                                            "Drive slot or vd_id not found in controller: %s" % sc["controller_slot"])
                if not is_m2_controller:
                    try:
                        pd_state_set(handle,
                                 sc["controller_type"],
                            sc["controller_slot"],
                            spare["slot"],
                            drive_state,
                            spare["vd_id"])
                    except ImcException as e:
                        # On deleting the VD, the pd state gets changed. If the end point state is same as configuration state,
                        # CIMC throws an ImcException.
                        # ignore errors because sometimes the previous operations will change the disk state to desired state
                        # eg: removing virtual drives move online disks to unconfigured good and dedicated hot spares to
                        # unconfigured good. Ignore this exception as our configuration state is same as end point state.
                        log.debug(e)
                        pass


def pd_state_set(handle,
                 controller_type, controller_slot, drive_slot, drive_state,
                 vd_id=None, server_id=1):
    """
    Sets the drive state of physical drive

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        drive_slot (int): Slot in which the drive resides
        drive_state (str): ["unconfigured_good", "jbod", "boot_drive",
                            "global_hot_spare", "dedicated_hot_spare",
                            "remove_hot_spare", "prepare_removal",
                            "undo_prepare_removal"]
        vd_id (int): virtual drive id.
                     Use only if drive_state == dedicated_hot_spare
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageLocalDisk object

    Examples:
        pd_state_set(handle, controller_type='SAS', controller_slot='HBA'',
                     drive_slot=4'i, drive_state="jbod")
    """
    ds_map = {
        "unconfigured_good": pd_set_unconfigured_good,
        "jbod": pd_set_jbod,
        "boot_drive": pd_set_boot_drive,
        "global_hot_spare": pd_set_global_hot_spare,
        "dedicated_hot_spare": pd_set_dedicated_hot_spare,
        "remove_hot_spare": pd_remove_hot_spare,
        "prepare_removal": pd_set_removal_prepare,
        "undo_prepare_removal": pd_set_removal_undo,
    }

    if drive_state not in ds_map:
        raise ImcOperationError("Get Physical drive: %s" % drive_slot,
                                "Invalid drive state. Valid values are  %s"
                                % str(", ".join(ds_map.keys())))

    params = {
        'handle': handle,
        'controller_type': controller_type,
        'controller_slot': controller_slot,
        'drive_slot': drive_slot,
        'vd_id': vd_id,
        'server_id': server_id
    }

    if not drive_state == "dedicated_hot_spare":
        params.pop('vd_id', None)

    execute_api = ds_map[drive_state]
    return execute_api(**params)


def sc_pd_state_exists(handle, storage_controllers, drive_state, server_id=1):
    """
    Wrapper function for pd_state_exists to handle multiple storage controllers.

    Args:
        handle (ImcHandle)
        storage_controllers (dictionary):
        Key: Storage controller pciSlot (string)
        Value: config information of that storage controller.
        drive_state (str)

    Example:
        sc_pd_state_exists(handle, storage_controllers, drive_state,
                     server_id=1)

    Return:
        exists (bool):  False / True
        mo : Physical Disks mos if it exists at end point.
    """
    error_msg = "Physical disk state check failed. "
    if len(storage_controllers) == 0:
        raise ImcOperationError(error_msg + "Storage controllers information is not specified.")

    if storage_controllers.get("remove_all_vds"):
        storage_controllers.pop("remove_all_vds")

    not_exists_pds_mo = []
    # If pd status at end point is same as the configuration state from policy, push the pd mo to a exists_pds list.
    for sc_obj in storage_controllers:
        sc = storage_controllers.get(sc_obj)

        if not sc.get("controller_slot"):
            raise ImcOperationError(error_msg + "controller_slot is not specified.")

        if not sc.get("controller_type"):
            raise ImcOperationError(error_msg + "controller_type is not specified for "
                                                "controller at pci slot: %s" % sc["controller_slot"])
        pds_to_set = []
        # Check for the physical disk disk state to configure its defined state.
        disks_state = sc.get("disks_state")
        if disks_state and not drive_state:
            for disk in disks_state:
                if disk.get("slot") is None or disk.get("state") is None:
                    raise ImcOperationError("Physical disk state check failed. drive slot/state not found.")

                exists, mo = pd_state_exists(handle, sc["controller_type"], sc["controller_slot"], disk["slot"], disk["state"])
                if not exists:
                    not_exists_pds_mo.append(mo)
                    pds_to_set.append(disk)
            sc["disks_state"] = pds_to_set
        hot_spares_pd = []
        # Check for dedicated hot spares
        dedicated_hot_spares = sc.get("dedicated_hot_spares")
        if dedicated_hot_spares and drive_state:
            for spare in dedicated_hot_spares:
                if spare.get("slot") is None or spare.get("vd_id") is None:
                    raise ImcOperationError("Physical disk state check failed. drive slot or vd id not found.")

                exists, mo = pd_state_exists(handle, sc["controller_type"], sc["controller_slot"], spare["slot"], drive_state, spare["vd_id"])
                if not exists:
                    not_exists_pds_mo.append(mo)
                    hot_spares_pd.append(spare)
            sc["dedicated_hot_spares"] = hot_spares_pd
    if len(not_exists_pds_mo) == 0:
        return True, not_exists_pds_mo
    return False, not_exists_pds_mo


def pd_state_exists(handle,
                    controller_type, controller_slot, drive_slot, drive_state,
                    vd_id=None, server_id=1):
    """
    Sets the drive state of physical drive

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        drive_slot (int): Slot in which the drive resides
        drive_state (str): ["unconfigured_good", "jbod", "boot_drive",
                            "global_hot_spare", "dedicated_hot_spare",
                            "remove_hot_spare", "prepare_removal",
                            "undo_prepare_removal"]
        vd_id (int): virtual drive id.
                     Use only if drive_state == dedicated_hot_spare
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageLocalDisk object

    Examples:
        pd_undo_removal(handle, controller_type='SAS', controller_slot='HBA'',
                        drive_slot=4')
    """
    ds_map = {
        "unconfigured_good": "Unconfigured Good",
        "jbod": "JBOD",
        "boot_drive": None,
        "global_hot_spare": "Global Hot Spare",
        "dedicated_hot_spare": "Dedicated Hot Spare",
        "remove_hot_spare": None,
        "prepare_removal": "Ready to Remove",
        "undo_prepare_removal": None,
    }

    if drive_state not in ds_map:
        raise ImcOperationError("Get Physical drive: %s" % drive_slot,
                                "Invalid drive state. Valid values are  %s"
                                % str(", ".join(ds_map.keys())))

    mo = pd_get(handle, controller_type, controller_slot, drive_slot,
                server_id)
    if mo is None:
        return False, None

    mo_drive_state = mo.pd_status
    expected_drive_state = ds_map[drive_state]

    if drive_state == "boot_drive":
        return _pd_exists_boot_drive(handle, mo.dn), mo

    if expected_drive_state is None:
        return False, mo
    return mo_drive_state == expected_drive_state, mo


def pd_encryption_capable(handle, controller_type, controller_slot, drive_slot,
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
    mo = pd_get(handle, controller_type, controller_slot, drive_slot,
                server_id)
    if mo is None:
        raise ImcOperationError("Get Physical drive:%s" % drive_slot,
                                "Not found")
    return mo.fde_capable.lower() in ['yes', 'true']


def pd_encryption_enable(handle,
                         controller_type, controller_slot, drive_slot,
                         server_id=1):
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
        pd_encryption_enable(handle, controller_type='SAS',
                             controller_slot='HBA'', drive_slot=4')
    """
    # pre-requisite
    # 1) disk should be encryption capable
    capable = pd_encryption_capable(handle, controller_type, controller_slot,
                                    drive_slot, server_id)
    if not capable:
        raise ImcOperationError("Enable encryption on the Physical drive: %s" % drive_slot,
                                "Drive is not FDE capable.")

    # 2) disk should be in JBOD mode.
    pd = pd_get(handle, controller_type, controller_slot, drive_slot,
                server_id)
    if pd.drive_state != "JBOD":
        raise ImcOperationError("Enable encryption on the Physical drive: %s" % drive_slot,
                                "Drive is not in JBOD mode")

    action = StorageLocalDiskConsts.ADMIN_ACTION_ENABLE_SELF_ENCRYPT
    return _pd_set_action(
        handle,
        controller_type=controller_type,
        controller_slot=controller_slot,
        drive_slot=drive_slot,
        action=action,
        server_id=server_id
    )


def pd_encryption_exists(handle, controller_type, controller_slot, drive_slot,
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
        True/False, MO/None

    Examples:
        enabled = pd_encryption_exists(handle, controller_type='SAS',
                                       controller_slot='HBA'', drive_slot=4')
    """
    mo = pd_get(handle, controller_type, controller_slot, drive_slot,
                server_id)
    if mo is None:
        return False, None

    if mo.fde_enabled.lower() not in ['yes', 'true']:
        return False, mo

    return True, mo


def pd_encryption_disable(handle, controller_type, controller_slot, drive_slot,
                          server_id=1):
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
    action = StorageLocalDiskConsts.ADMIN_ACTION_DISABLE_SELF_ENCRYPT
    return _pd_set_action(
        handle,
        controller_type=controller_type,
        controller_slot=controller_slot,
        drive_slot=drive_slot,
        action=action,
        server_id=server_id
    )
