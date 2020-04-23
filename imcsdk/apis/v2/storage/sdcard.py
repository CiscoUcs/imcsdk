# Copyright 2018 Cisco Systems, Inc.
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
This module implements all the sd card config
"""
import logging

from imcsdk.imcexception import ImcOperationError, ImcOperationErrorDetail
from imcsdk.imcconstants import NamingId
from imcsdk.imccoreutils import process_conf_mos_response, sanitize_message

log = logging.getLogger('imc')


class Slot(object):
    SLOT_1 = "slot-1"
    SLOT_2 = "slot-2"


vd_map_type_id_util_m4 = {
    'SCU': 1,
    'HUU': 2,
    'DRIVERS': 3,
    'USER': 4,
    'OS': 5
}

vd_map_id_type_util_m4 = {
    1: 'SCU',
    2: 'HUU',
    3: 'DRIVERS',
    4: 'USER',
    5: 'OS'
}

vd_map_type_id_util_m5 = {
    'SCU': 1,
    'DIAGNOSTICS': 2,
    'HUU': 3,
    'DRIVERS': 4,
    'USER': 5,
}

vd_map_id_type_util_m5 = {
    1: 'SCU',
    2: 'DIAGNOSTICS',
    3: 'HUU',
    4: 'DRIVERS',
    5: 'USER'
}


class VirtualDriveType(object):
    OS = "OS"
    SCU = "SCU"
    HUU = "HUU"
    DIAGNOSTICS = "Diagnostics"
    DRIVERS = "Drivers"
    USER = "UserPartition"


class VirtualDrive(object):
    def __init__(self, vd_type, vd_enable=None, vd_name=None):
        self.vd_type = vd_type
        self.vd_enable = vd_enable
        self.vd_name = vd_name

    def __str__(self):
        str = "vd_type: %s, vd_enable: %s, vd_name: %s" % (self.vd_type,
                                                           self.vd_enable,
                                                           self.vd_name)
        # if self.vd_type == "OS" and hasattr(self, 'vd_auto_sync'):
        #     str += ", vd_auto_sync: %s" % self.vd_auto_sync
        return str


def _get_platform(handle):
    from imcsdk import imccoreutils as ic

    if ic.is_platform_m4(handle):
        return "M4"
    elif ic.is_platform_m5(handle):
        return "M5"
    else:
        raise ImcOperationError(
            "_get_platform",
            "Invalid CIMC Platform '%s'" % handle.model)


def flexflash_controller_get(handle):
    controller = handle.query_classid(
        class_id=NamingId.STORAGE_FLEX_FLASH_CONTROLLER)
    if not controller:
        raise ImcOperationError("Get Flex Flash Controller",
                                "FlexFlash Controller not found")
    return controller[0]


def flexutil_controller_get(handle):
    controller = handle.query_classid(
        class_id=NamingId.STORAGE_FLEX_UTIL_CONTROLLER)
    if not controller:
        raise ImcOperationError("Get Flex Util Controller",
                                "FlexUtil Controller not found")
    return controller[0]


def flexflash_controller_set(handle, admin_action=None, auto_sync=None,
                             card_slot=None, configured_mode=None,
                             non_util_partition_name=None,
                             partition_name=None,
                             virtual_drive=None, **kwargs):

    mo = flexflash_controller_get(handle)
    params = {
        "admin_action": admin_action,
        "auto_sync": auto_sync,
        "card_slot": card_slot,
        "configured_mode": configured_mode,
        "partition_name": partition_name,
        "non_util_partition_name": non_util_partition_name,
        "virtual_drive": virtual_drive
    }

    mo.set_prop_multiple(**params)
    handle.set_mo(mo)
    return mo


def flexflash_controller_mode_mirror_set(handle, card_slot,
                                         partition_name="Hypervisor",
                                         auto_sync=None):
    from imcsdk.mometa.storage.StorageFlexFlashController import \
        StorageFlexFlashControllerConsts as const

    return flexflash_controller_set(
        handle,
        admin_action=const.ADMIN_ACTION_CONFIGURE_CARDS,
        configured_mode=const.CONFIGURED_MODE_MIRROR,
        card_slot=card_slot,
        partition_name=partition_name,
        auto_sync=auto_sync
    )


def flexflash_controller_mode_util_set(
        handle,
        card_slot,
        partition_name="Hypervisor",
        non_util_partition_name="UserPartition"):
    from imcsdk.mometa.storage.StorageFlexFlashController import \
        StorageFlexFlashControllerConsts as const

    return flexflash_controller_set(
        handle,
        admin_action=const.ADMIN_ACTION_CONFIGURE_CARDS,
        configured_mode=const.CONFIGURED_MODE_UTIL,
        card_slot=card_slot,
        partition_name=partition_name,
        non_util_partition_name=non_util_partition_name
    )


def flexflash_controller_get_hierarchy(handle):
    mos_dict = {}
    mos = handle.query_classid(class_id="StorageFlexFlashController",
                               hierarchy=True)
    if not mos:
        raise ImcOperationError("flexflash_controller_get",
                                "FlexFlash controller is not present")
    for mo in mos:
        class_id = mo.get_class_id()
        if class_id not in mos_dict:
            mos_dict[class_id] = []
        mos_dict[class_id].append(mo)

    flexflash_controller = mos_dict["StorageFlexFlashController"][0]
    flexflash_props = mos_dict["StorageFlexFlashControllerProps"][0]
    flexflash_pds = mos_dict["StorageFlexFlashPhysicalDrive"]
    flexflash_vds = mos_dict.get('StorageFlexFlashVirtualDrive', None)

    return {
        'flexflash_controller': flexflash_controller,
        'flexflash_props': flexflash_props,
        'flexflash_pds': flexflash_pds,
        'flexflash_vds': flexflash_vds
    }


def flexutil_controller_get_hierarchy(handle):
    mos_dict = {}
    mos = handle.query_classid("StorageFlexUtilController",
                               hierarchy=True)
    if not mos:
        raise ImcOperationError("flexutil_controller_get_hierarchy",
                                "FlexUtil controller is not present")
    for mo in mos:
        class_id = mo.get_class_id()
        if class_id not in mos_dict:
            mos_dict[class_id] = []
        mos_dict[class_id].append(mo)

    flexutil_controller = mos_dict["StorageFlexUtilController"][0]
    flexutil_pds = mos_dict["StorageFlexUtilPhysicalDrive"]
    flexutil_vds = mos_dict.get('StorageFlexUtilVirtualDrive', None)

    return {
        'flexutil_controller': flexutil_controller,
        'flexutil_pds': flexutil_pds,
        'flexutil_vds': flexutil_vds
    }


def _is_slot_ok(pd):
    if pd.pd_status == "missing":
        return False
    if pd.card_type == "unpartitioned card":
        return False
    if pd.card_status == "NA":
        return False
    if pd.card_mode == "NA":
        return False
    if pd.health == "NA":
        return False
    return True


def _choose_slot(pds):
    pds_dict = {}
    for pd in pds:
        pds_dict[pd.physical_drive_id] = pd

    if _is_slot_ok(pds_dict['1']):
        return "slot-1"
    elif _is_slot_ok(pds_dict['2']):
        return "slot-2"
    raise ImcOperationError(
        "_choose_slot",
        "Cards are missing in slot or not properly configured")


def _get_available_slots(pds):
    available_slots = []
    pds_dict = {}
    for pd in pds:
        pds_dict[pd.physical_drive_id] = pd

    if _is_slot_ok(pds_dict['1']):
        available_slots.append(Slot.SLOT_1)
    if _is_slot_ok(pds_dict['2']):
        available_slots.append(Slot.SLOT_2)

    return available_slots


def _set_admin_action_flash_vd(handle, partition_id, admin_action,
                               controller_dn):
    from imcsdk.mometa.storage.StorageFlexFlashVirtualDrive import \
        StorageFlexFlashVirtualDrive

    mo = StorageFlexFlashVirtualDrive(parent_mo_or_dn=controller_dn,
                                      partition_id=str(partition_id))
    mo.admin_action = admin_action
    return mo


def _apply_config_card_action_mirror(handle, mos_dict, vd):
    from imcsdk.mometa.storage.StorageFlexFlashVirtualDrive import \
        StorageFlexFlashVirtualDriveConsts
    # slot = _choose_slot(mos_dict['flexflash_pds'])

    # OS drive should always be created on:
    # "slot-1",  if both cards present
    # slot in which card is present, if only one card present
    # error, if no cards present
    pds = mos_dict['flexflash_pds']
    primary_slot = None
    available_slots = _get_available_slots(pds)
    available_slots_cnt = len(available_slots)
    if available_slots_cnt == 0:
        raise ImcOperationError("Cannot set operating system virtual drive",
                                "Cards are missing in both the slots")
    elif available_slots_cnt == 1:
        primary_slot = available_slots[0]
        auto_sync = "no"
    elif available_slots_cnt == 2:
        primary_slot = Slot.SLOT_1
        auto_sync = "yes"

    partition_name = vd.vd_name

    flexflash_controller_mode_mirror_set(
        handle,
        card_slot=primary_slot,
        partition_name=partition_name,
        auto_sync=auto_sync
    )

    if not vd.vd_enable:
        return
    log.debug("OS: enable-vd")
    controller_dn = mos_dict['flexflash_controller'].dn
    partition_id = '1'
    mo = _set_admin_action_flash_vd(
        handle,
        partition_id,
        StorageFlexFlashVirtualDriveConsts.ADMIN_ACTION_ENABLE_VD,
        controller_dn
    )
    handle.set_mo(mo)


def _apply_config_card_action_util(handle, mos_dict, vds):
    from imcsdk.mometa.storage.StorageFlexFlashVirtualDrive import \
        StorageFlexFlashVirtualDriveConsts
    # slot = _choose_slot(mos_dict['flexflash_pds'])

    # Utility drive should always be created on:
    # "slot-2",  if both cards present
    # slot in which card is present, if only one card present
    # error, if no cards present
    pds = mos_dict['flexflash_pds']
    primary_slot = None
    available_slots = _get_available_slots(pds)
    available_slots_cnt = len(available_slots)
    if available_slots_cnt == 0:
        raise ImcOperationError("Cannot set virtual drive",
                                "Cards are missing in both the slots")
    elif available_slots_cnt == 1:
        primary_slot = available_slots[0]
    elif available_slots_cnt == 2:
        primary_slot = Slot.SLOT_2

    partition_name = None
    non_util_partition_name = None
    if 'USER' in vds and hasattr(vds['USER'], 'vd_name'):
        partition_name = vds['USER'].vd_name
    if 'OS' in vds and hasattr(vds['OS'], 'vd_name'):
        non_util_partition_name = vds['OS'].vd_name
    flexflash_controller_mode_util_set(
        handle,
        card_slot=primary_slot,
        partition_name=partition_name,
        non_util_partition_name=non_util_partition_name
    )

    dn_to_vd_dict = {}
    api = "sd_card_virtual_drive_set"
    mos = []
    controller_dn = mos_dict['flexflash_controller'].dn
    for vd_type, vd in vds.items():
        if not vd.vd_enable:
            continue
        # skip OS if only one slot is available in utility mode in M4
        if vd_type == "OS" and available_slots_cnt == 1:
            continue
        partition_id = vd_map_type_id_util_m4[vd.vd_type]
        mo = _set_admin_action_flash_vd(
            handle,
            partition_id,
            StorageFlexFlashVirtualDriveConsts.ADMIN_ACTION_ENABLE_VD,
            controller_dn
        )
        mos.append(mo)
        dn_to_vd_dict[mo.dn] = vd.vd_type

    if len(mos) == 0:
        return

    response = handle.set_mos(mos)
    if response:
        ret = process_conf_mos_response(response, api, False,
                                        'Configuring virtual drives failed',
                                        util_mode_cb,
                                        dn_to_vd_dict)
        if len(ret) != 0:
            error_msg = 'Configuring virtual drives failed:\n'
            for item in ret:
                obj = item["Object"]
                error = item["Error"]
                error = sanitize_message(error)
                error_msg += "[Virtual drive " + obj + "] " + error + "\n"

            raise ImcOperationErrorDetail(api, error_msg, ret)

    results = {}
    results["changed"] = True
    results["msg"] = ""
    results["msg_params"] = ret

    return results


def util_mode_cb(dn, dn_to_vd_dict):
    return dn_to_vd_dict.get(dn, "Unknown Virtual drive:" + dn)


def util_vds_disable_all_m5(handle, mos_dict):
    api = "util_vds_disable_all_m5"
    flexutil_vds = mos_dict.get("flexutil_vds", None)
    if not flexutil_vds:
        return None
    admin_action = "disable-vd"
    dn_to_vd_dict = {}
    mos = []
    for vd in flexutil_vds:
        if vd.host_accessible == "Not-Connected":
            continue
        vd_type_ = vd_map_id_type_util_m5[int(vd.partition_id)]
        dn_to_vd_dict[vd.dn] = vd_type_
        log.debug("%s: %s" % (vd_type_, admin_action))
        vd.admin_action = admin_action
        mos.append(vd)
    response = handle.set_mos(mos)
    if response:
        _process_response(response, api,  vd_callback, dn_to_vd_dict)


def os_vd_disable_m5(handle, mos_dict):
    flexflash_vds = mos_dict.get("flexflash_vds", None)
    if not flexflash_vds:
        return None
    vd = flexflash_vds[0]
    admin_action = "disable-vd"
    vd.admin_action = admin_action
    handle.set_mo(vd)


def _compare(expected_vds, existing_vds):
    exists = True

    # change in count of virtual drives
    if len(expected_vds) != len(existing_vds):
        exists = False

    for exp_vd_type, exp_vd in expected_vds.items():
        if exp_vd_type not in existing_vds:
            exists = False
            break

        exist_vd = existing_vds[exp_vd_type]
        if exp_vd_type in ('OS', 'USER') and \
                exp_vd.vd_name != exist_vd.vd_name:
            exists = False
            break
        if exp_vd.vd_enable != exist_vd.vd_enable:
            exists = False
            break
    return exists


def _is_auto_sync(pds):
    primary_pd = None
    for pd in pds:
        if pd.card_mode == "mirror-primary":
            primary_pd = pd
            break
    if primary_pd is None:
        log.debug("No Primary Physical drive available")


def vd_callback(dn, dn_to_vd_dict):
    return dn_to_vd_dict.get(dn, "Unknown VD:" + dn)


def _process_response(response, api,  callback, dn_to_vd_dict):
    ret = process_conf_mos_response(response, api, False,
                                    'sd card config set m5',
                                    callback,
                                    dn_to_vd_dict)
    if len(ret) != 0:
        error_msg = 'cannot enable/disable virtual drive:\n'
        for item in ret:
            obj = item["Object"]
            error = item["Error"]
            error = sanitize_message(error)
            error_msg += "[virtual drive " + obj + "] " + error + "\n"

        raise ImcOperationErrorDetail(api, error_msg, ret)

    results = {}
    results["changed"] = True
    results["msg"] = ""
    results["msg_params"] = ret
    return results


def _sd_card_config_set_m4(handle, expected_vds, existing_vds, mos_dict=None):
    if mos_dict is None:
        mos_dict = _prepare_mos_dict(handle, expected_vds.keys())

    is_mode_changed = False
    expected_vds_count = len(expected_vds)
    existing_vds_count = len(existing_vds)

    if expected_vds_count == 1 and 'OS' in expected_vds:
        expected_mode = "mirror"
    else:
        expected_mode = "util"

    if existing_vds_count == 1 and 'OS' in existing_vds:
        existing_mode = "mirror"
    else:
        existing_mode = "util"

    if expected_mode != existing_mode:
        is_mode_changed = True

    if not is_mode_changed:
        log.debug("Mode is not changed")
        if expected_mode == "mirror":
            log.debug("Mode: Mirror")
            # both expected and existing have only OS virtual drive
            expected_vd = expected_vds['OS']
            existing_vd = existing_vds['OS']

            # check for change in name
            if expected_vd.vd_name != existing_vd.vd_name:
                log.debug("Apply configuration, name is changed")
                _apply_config_card_action_mirror(handle, mos_dict,
                                                 expected_vd)
                return
            if expected_vd.vd_enable != existing_vd.vd_enable:
                enabled = expected_vd.vd_enable
                admin_action = "enable-vd" if enabled else "disable-vd"
                log.debug("%s: %s" % (expected_vd.vd_type, admin_action))
                existing_vd.vd_mo.admin_action = admin_action
                handle.set_mo(existing_vd.vd_mo)
                return
        elif expected_mode == "util":
            log.debug("Mode: Util")
            mos = []
            dn_to_vd_dict = {}
            api = 'sd_card_config_set_m4'

            # incase of m4, OS + Util to Util only then disable OS
            if 'OS' not in expected_vds and 'OS' in existing_vds:
                existing_os_vd = existing_vds['OS']
                if existing_os_vd.vd_enable:
                    existing_os_vd.vd_mo.admin_action = "disable-vd"
                    handle.set_mo(existing_os_vd.vd_mo)

            for expected_vd_type, expected_vd in expected_vds.items():
                existing_vd = existing_vds.get(expected_vd_type, None)
                if existing_vd is None:
                    continue

                # check for change in name for util and non-util partition
                if expected_vd_type in ['OS', 'USER'] \
                        and expected_vd.vd_name != existing_vd.vd_name:
                    log.debug("Apply configuration, name is changed")
                    _apply_config_card_action_util(handle, mos_dict,
                                                   expected_vds)
                    return

                # check if vd is enable or disable
                if expected_vd.vd_enable != existing_vd.vd_enable:
                    enabled = expected_vd.vd_enable
                    admin_action = "enable-vd" if enabled else "disable-vd"
                    existing_vd.vd_mo.admin_action = admin_action
                    log.debug("%s: %s" % (expected_vd.vd_type, admin_action))
                    mos.append(existing_vd.vd_mo)
                    dn_to_vd_dict[existing_vd.vd_mo.dn] = expected_vd.vd_type
            response = handle.set_mos(mos)
            if response:
                return _process_response(response, api,  vd_callback,
                                         dn_to_vd_dict)
            return

    # if mode is changed
    log.debug("Mode is changed")
    log.debug("Applying configuration")
    if expected_mode == "mirror":
        log.debug("Mode: Mirror")
        _apply_config_card_action_mirror(handle, mos_dict, expected_vds['OS'])
    elif expected_mode == "util":
        log.debug("Mode: Util")
        mos = []
        _apply_config_card_action_util(handle, mos_dict, expected_vds)


def _sd_card_config_set_m5(handle, expected_vds, existing_vds, mos_dict):

    if 'OS' in expected_vds:
        expected_vd = expected_vds['OS']
        existing_vd = existing_vds.get('OS', None)
        if existing_vd is None:
            log.debug("OS drive does not exist")
            _apply_config_card_action_mirror(handle, mos_dict, expected_vd)
        elif expected_vd.vd_name != existing_vd.vd_name:
            log.debug("New name is different")
            _apply_config_card_action_mirror(handle, mos_dict, expected_vd)
        elif expected_vd.vd_enable != existing_vd.vd_enable:
            log.debug("Change in host connectivity")
            enabled = expected_vd.vd_enable
            admin_action = "enable-vd" if enabled else "disable-vd"
            existing_vd.vd_mo.admin_action = admin_action
            log.debug("%s: %s" % ('OS', admin_action))
            handle.set_mo(existing_vd.vd_mo)

        # incase of os only, disable all utility vds
        if len(expected_vds) == 1:
            util_vds_disable_all_m5(handle, mos_dict)
            return

    # disable OS, if not part of expected vds
    if 'OS' not in expected_vds:
        os_vd_disable_m5(handle, mos_dict)

    mos_enable = []
    mos_disable = []
    api = 'sd_card_config_set_m5'

    expected_vd_enable_cnt = 0
    for expected_vd in expected_vds.values():
        if expected_vd.vd_type == 'OS':
            continue
        if expected_vd.vd_enable:
            expected_vd_enable_cnt += 1
        if expected_vd_enable_cnt > 2:
            raise ImcOperationError("sd_card_config_set_m5",
                                    "Maximum two VD's can be enabled")

    for expected_type, expected_vd in expected_vds.items():
        if expected_type == 'OS':
            continue
        existing_vd = existing_vds.get(expected_type, None)
        if existing_vd is None:
            continue
        if expected_vd.vd_enable != existing_vd.vd_enable:
            enabled = expected_vd.vd_enable
            if enabled:
                admin_action = "enable-vd"
                mos_enable.append(existing_vd.vd_mo)
            else:
                admin_action = "disable-vd"
                mos_disable.append(existing_vd.vd_mo)

            existing_vd.vd_mo.admin_action = admin_action

    if mos_disable:
        dn_to_vd_dict = {}
        for mo in mos_disable:
            vd_type_ = vd_map_id_type_util_m5[int(mo.partition_id)]
            dn_to_vd_dict[mo.dn] = vd_type_
            log.debug("%s: %s" % (vd_type_, admin_action))
        response = handle.set_mos(mos_disable)
        if response:
            _process_response(response, api,  vd_callback, dn_to_vd_dict)

    if mos_enable:
        dn_to_vd_dict = {}
        for mo in mos_enable:
            vd_type_ = vd_map_id_type_util_m5[int(mo.partition_id)]
            dn_to_vd_dict[mo.dn] = vd_type_
            log.debug("%s: %s" % (vd_type_, admin_action))
        response = handle.set_mos(mos_enable)
        if response:
            _process_response(response, api,  vd_callback, dn_to_vd_dict)


def _get_existing_vds_m4(mos_dict):
    existing_vds = {}
    flexflash_vds = mos_dict.get("flexflash_vds", None)
    # flexflash_pds = mos_dict.get("flexflash_pds", None)
    if not flexflash_vds:
        return existing_vds

    # platform-M4, mode-mirror, only 1 vd present at end point
    if len(flexflash_vds) == 1:
        vd = flexflash_vds[0]

        vd_type = "OS"
        vd_enable = True if vd.host_accessible == "Connected" else False
        vd_name = vd.virtual_drive
        # vd_auto_sync = True if _is_auto_sync(flexflash_pds) else False

        virtual_drive = VirtualDrive(vd_type, vd_enable, vd_name)
        virtual_drive.vd_mo = vd

        # if vd_type == 'OS':
        #     virtual_drive.vd_auto_sync = vd_auto_sync

        existing_vds[vd_type] = virtual_drive
        return existing_vds

    # platform-M4, mode-util, more than 1 vds present at end point
    for vd in flexflash_vds:
        vd_type = vd_map_id_type_util_m4[int(vd.partition_id)]
        vd_enable = True if vd.host_accessible == "Connected" else False
        vd_name = None
        if vd_type in ("OS", 'USER'):
            vd_name = vd.virtual_drive

        virtual_drive = VirtualDrive(vd_type, vd_enable, vd_name)
        virtual_drive.vd_mo = vd

        existing_vds[vd_type] = virtual_drive

    return existing_vds


def _get_existing_vds_m5(mos_dict):
    log.debug("Fetch existing vds of M5 server")
    existing_vds = {}

    log.debug("Fetching vds of flexflash controller")
    flexflash_vds = mos_dict.get("flexflash_vds", None)
    # flexflash_pds = mos_dict.get("flexflash_pds", None)
    if flexflash_vds:
        vd = flexflash_vds[0]
        # log.debug(vd)
        vd_type = "OS"
        vd_enable = True if vd.host_accessible == "Connected" else False
        vd_name = vd.virtual_drive

        virtual_drive = VirtualDrive(vd_type, vd_enable, vd_name)
        virtual_drive.vd_mo = vd
        existing_vds[vd_type] = virtual_drive

    log.debug("Fetching vds of flexutil controller")
    flexutil_vds = mos_dict.get("flexutil_vds", None)
    # log.debug(flexutil_vds)
    if flexutil_vds:
        for vd in flexutil_vds:
            # log.debug(vd)
            vd_type = vd_map_id_type_util_m5[int(vd.partition_id)]
            vd_enable = True if vd.host_accessible == "Connected" else False

            virtual_drive = VirtualDrive(vd_type, vd_enable)
            virtual_drive.vd_mo = vd
            existing_vds[vd_type] = virtual_drive

    return existing_vds


def _get_existing_vds(platform, mos_dict):
    if platform == "M4":
        existing_vds = _get_existing_vds_m4(mos_dict)
    elif platform == "M5":
        existing_vds = _get_existing_vds_m5(mos_dict)

    return existing_vds


def _get_expected_vds(virtual_drives={}):
    vd_types = [vd for vd in dir(VirtualDriveType)
                if not vd.startswith('_')]
    expected_vds = {}

    for vd_type_ in virtual_drives:
        vd_ = virtual_drives[vd_type_]
        vd_type = vd_type_.upper()

        if vd_type not in vd_types:
            raise ImcOperationError("_prepare_config_set",
                                    "Unknown virtual drive'%s'" % vd_type_)

        enable = vd_.get('enable', None)

        if vd_type == 'OS':
            name = vd_.get('name', 'Hypervisor')
            # auto_sync = vd_.get('auto_sync', False)
        elif vd_type == 'USER':
            name = vd_.get('name', 'UserPartition')
        else:
            name = vd_.get('name', None)

        vd = VirtualDrive(vd_type=vd_type, vd_name=name, vd_enable=enable)
        # if vd_type == 'OS':
        #     vd.vd_auto_sync = auto_sync

        expected_vds[vd_type] = vd

    return expected_vds


def _get_config_str(vds):
    config_str = ""
    for vd_type, vd in vds.items():
        config_str += "%s: " % vd_type
        config_str += "{"
        config_str += str(vd)
        config_str += "}\n"

    return config_str


def _get_configs(handle, virtual_drives, mos_dict=None):
    if mos_dict is None:
        mos_dict = _prepare_mos_dict(handle, virtual_drives.keys())

    platform = _get_platform(handle)

    expected_vds = _get_expected_vds(virtual_drives)
    if platform == "M4" and 'DIAGNOSTICS' in expected_vds:
        expected_vds.pop('DIAGNOSTICS', None)
        log.debug("Removing 'DIAGNOSTICS' virtual drive from config for M4")
    log.debug("Expected configuration:\n%s" % _get_config_str(expected_vds))

    existing_vds = _get_existing_vds(platform, mos_dict)
    log.debug("Existing configuration:\n%s" % _get_config_str(existing_vds))
    return expected_vds, existing_vds


def _prepare_mos_dict(handle, vds):

    platform = _get_platform(handle)
    if platform == "M4":
        mos_dict = flexflash_controller_get_hierarchy(handle)
        return mos_dict

    # M5
    # If FlexFlash controller is present we need to process both OS and Util

    is_flexflash_controller_present = False
    mos_dict = {}

    try:
        mos_dict.update(flexflash_controller_get_hierarchy(handle))
        is_flexflash_controller_present = True
    except Exception:
        is_flexflash_controller_present = False

    # If FlexFlash controller is not present,
    #  In case of Util mode, we should not process OS vd.
    if not is_flexflash_controller_present and 'OS' in vds:
        raise ImcOperationError("sd_card_virtual_drive_set",
                                "FlexFlash controller is not present")

    flexutil_vds = handle.query_classid(class_id="StorageFlexUtilVirtualDrive")
    # If microSD card is missing,
    # and if only OS in vds then we should skip
    if not flexutil_vds and 'OS' in vds and len(vds) == 1:
        return mos_dict

    # and for Utility and OS plus Utility, we should error out
    if not flexutil_vds:
        raise ImcOperationError("sd_card_virtual_drive_set",
                                "Micro SD card is missing.")

    mos_dict['flexutil_vds'] = flexutil_vds

    return mos_dict


def sd_card_virtual_drive_set(handle, virtual_drives, mos_dict=None):
    if not virtual_drives and not isinstance(virtual_drives, dict):
        raise ImcOperationError(
            "sd_card_virtual_drive_set",
            "Parameter virtual_drives should be of type dict")

    platform = _get_platform(handle)
    log.debug("Platform is '%s'" % platform)

    if mos_dict is None:
        mos_dict = _prepare_mos_dict(handle, virtual_drives.keys())

    log.debug("Fetching expected and existing virtual drive")
    expected_vds, existing_vds = _get_configs(handle,
                                              virtual_drives,
                                              mos_dict)

    if platform == "M4":
        log.debug("Applying configuration on M4")
        _sd_card_config_set_m4(handle, expected_vds, existing_vds, mos_dict)
    elif platform == "M5":
        log.debug("Applying configuration on M5")
        _sd_card_config_set_m5(handle, expected_vds, existing_vds, mos_dict)


def sd_card_virtual_drive_exists(handle, virtual_drives):
    mos_dict = _prepare_mos_dict(handle, virtual_drives.keys())
    expected_vds, existing_vds = _get_configs(handle,
                                              virtual_drives,
                                              mos_dict)

    exists = _compare(expected_vds, existing_vds)
    return exists, mos_dict
