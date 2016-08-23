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
This module provides APIs for bios related configuration like boot order
"""

import logging

logging.basicConfig()
log = logging.getLogger('imc')
log.setLevel(logging.DEBUG)


def get_boot_order_precision(handle, dump=False):
    """
    Gets the precision boot order.
    This is supported from EP release onwards only

    Args:
        handle (ImcHandle)
        dump (bool): True or False

    Returns:
        List of tuples of the format:
            [(boot-order, boot-device-type, boot-device-name)]

    Example:
        boot_order_precision(handle, dump=False)
    """

    boot_order_list = []
    boot_device_list = handle.query_children(
        in_dn="sys/rack-unit-1/bios/bdgep", class_id="BiosBootDevPrecision")

    for device in boot_device_list:
        device_tuple = (device.order, device.type, device.name)
        boot_order_list.append(device_tuple)

    sorted_boot_order_list = sorted(
        boot_order_list, key=lambda item: item[0])

    if dump:
        log.info("Precision Boot Order is [Order, Type, Name]:")
        log.info("--------------------------------------------")
        for device in sorted_boot_order_list:
            log.info(" %s \t%s \t%s" % (device[0], device[1], device[2]))

    return sorted_boot_order_list


precision_device_dict = {
    "hdd": "LsbootHdd",
    "iscsi": "LsbootIscsi",
    "pchstorage": "LsbootPchStorage",
    "pxe": "LsbootPxe",
    "san": "LsbootSan",
    "sdcard": "LsbootSd",
    "uefishell": "LsbootUefiShell",
    "usb": "LsbootUsb",
    "vmedia": "LsbootVMedia"
}


policy_device_dict = {
    "efi": "LsbootEfi",
    "lan": "LsbootLan",
    "storage": "LsbootStorage",
    "vmedia": "LsbootVirtualMedia",
}


def _get_boot_device_obj(parent_dn, device_type, device_name):
    from imcsdk.imccoreutils import load_class

    if parent_dn == "sys/rack-unit-1/boot-precision":
        if device_type not in precision_device_dict.keys():
            return None
        class_struct = load_class(precision_device_dict[device_type])
    elif parent_dn == "sys/rack-unit-1/boot-policy":
        if device_type not in policy_device_dict.keys():
            return None
        class_struct = load_class(policy_device_dict[device_type])
    else:
        return None

    if "name" in class_struct.prop_map.keys():
        class_obj = class_struct(parent_mo_or_dn=parent_dn, name=device_name)
    else:
        class_obj = class_struct(parent_mo_or_dn=parent_dn)

    return class_obj


def _add_boot_device(handle, parent_dn, boot_device):
    """
    This method verifies and adds the boot device in the boot order
    Used by set_boot_order_precision and set_boot_order_policy

    Args:
        handle(ImcHandle)
        boot_device(tuple): This is a tuple of the format
                    [(boot-order, boot-device-type, boot-device-name)]

    Returns:
        None
    """

    boot_device_obj = _get_boot_device_obj(
        parent_dn, boot_device[1], boot_device[2])
    if boot_device_obj is None:
        raise ValueError(
            "Unsupported boot-device %s with label %s" %
            (boot_device[1], boot_device[2]))

    boot_device_obj.order = boot_device[0]
    if hasattr(boot_device_obj, "state"):
        boot_device_obj.state = "enabled"
    handle.add_mo(boot_device_obj, modify_present=True)


def set_boot_order_precision(
        handle, reboot_on_update="yes", boot_mode="Legacy", boot_devices=[]):
    """
    This method will replace the existing boot order precision with the new one
        and also set the boot mode
    This functionality is available only in release EP and above

    Args:
        handle (ImcHandle)
        reboot_on_update (string): "yes", "no"
        boot_mode (string): "Legacy", "Uefi", "None"
        boot_devices (list of tuples): format
            [(boot-order, boot-device-type, boot-device-name)]
            boot-order(string): Order
            boot-device-type(string): "hdd", "iscsi", "pchstorage", "pxe", "san", "sdcard", "uefishell", "usb", "vmedia"
            boot-device-name(string): Unique label for the boot device

    Returns:
        LsBootDevPrecision object

    Examples:
        set_boot_order_precision(
            handle,
             reboot_on_update="yes",
             boot_mode="Uefi",
             boot_devices = [("1", "hdd", "ext-hdd1"), ("2", "cdrom", "cdrom")]
    """

    # Insert version check here to gracefully handle older versions of CIMC

    from imcsdk.mometa.lsboot.LsbootDevPrecision import LsbootDevPrecision

    lsbootdevprecision_mo = LsbootDevPrecision(
        parent_mo_or_dn="sys/rack-unit-1")
    lsbootdevprecision_mo.reboot_on_update = reboot_on_update
    lsbootdevprecision_mo.configured_boot_mode = boot_mode

    handle.set_mo(lsbootdevprecision_mo)

    boot_order_child_mos = handle.query_children(
        in_dn=lsbootdevprecision_mo.dn)
    for mo in boot_order_child_mos:
        handle.remove_mo(mo)

    for device_tuple in boot_devices:
        _add_boot_device(handle, lsbootdevprecision_mo.dn, device_tuple)

    lsbootdevprecision_mo = handle.query_classid("LsbootDevPrecision")
    return lsbootdevprecision_mo


def get_boot_order_policy(handle, dump=False):
    """
    Gets the boot order. This is the legacy boot order

    Args:
        handle (ImcHandle)
        dump (bool): True or False

    Returns:
        List of tuples of the format:
            [(boot-order, boot-device-type, boot-device-name)]

    Example:
        get_boot_order_policy(handle, dump=False)
    """

    from imcsdk.mometa.lsboot.LsbootBootSecurity import LsbootBootSecurity

    boot_order_list = []
    child_mo_list = handle.query_children(
        in_dn="sys/rack-unit-1/boot-policy")
    boot_security_policy = LsbootBootSecurity(
        parent_mo_or_dn="sys/rack-unit-1/boot-policy")

    for mo in child_mo_list:
        if mo.dn == boot_security_policy.dn:
            continue
        if hasattr(mo, "name"):
            device_tuple = (mo.order, mo.type, mo.name)
        else:
            device_tuple = (mo.order, mo.type, "NA")
        boot_order_list.append(device_tuple)

    sorted_boot_order_list = sorted(
        boot_order_list, key=lambda device: device[0])

    if dump:
        log.info("Boot Order according to Policy is [Order, Type, Name]:")
        log.info("------------------------------------------------------")

        for device_tuple in sorted_boot_order_list:
            log.info(
                " %s \t%s \t%s" %
                (device_tuple[0],
                 device_tuple[1],
                 device_tuple[2]))

    return sorted_boot_order_list


def set_boot_order_policy(handle, reboot_on_update="yes",
                          secure_boot=False, boot_devices=[]):
    """
    This method will set the boot order policy passed from the user
    This is the deprecated way of setting the boot order
        and is applicable releases older than EP

    Args:
        handle (ImcHandle)
        reboot_on_update (string): "yes", "no"
        secure_boot (bool): secure boot
        boot_devices (list of tuples): format
            [(boot-order, boot-device-type, boot-device-name)]
            boot-order(string): Order
            boot-device-type(string): "efi", "lan", "storage", "vmedia"
            boot-device-name(string): Unique label for the boot device

    Returns:
        LsBootDef object

    Examples:
        set_boot_order_policy(
            handle,
             reboot_on_update="yes",
             secure_boot="yes"
             boot_devices = [("1", "storage", "ext-hdd1"), ("2", "lan", "office-lan")])
    """

    from imcsdk.mometa.lsboot.LsbootDef import LsbootDef
    from imcsdk.mometa.lsboot.LsbootBootSecurity import LsbootBootSecurity

    boot_policy = LsbootDef(parent_mo_or_dn="sys/rack-unit-1")
    boot_policy.reboot_on_update = reboot_on_update
    handle.set_mo(boot_policy)

    secure_boot_policy = LsbootBootSecurity(parent_mo_or_dn=boot_policy.dn)
    if secure_boot:
        secure_boot_policy.secure_boot = "enabled"
    else:
        secure_boot_policy.secure_boot = "disabled"
    handle.set_mo(secure_boot_policy)

    boot_policy_child_mos = handle.query_children(in_dn=boot_policy.dn)
    for mo in boot_policy_child_mos:
        if mo.dn == secure_boot_policy.dn:
            continue
        # handle.remove_mo(mo)

    for device_tuple in boot_devices:
        _add_boot_device(handle, boot_policy.dn, device_tuple)

    boot_policy = handle.query_classid("LsbootDef")
    return boot_policy
