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
import imcsdk.imccoreutils as imccoreutils
from imcsdk.mometa.lsboot.LsbootDevPrecision import LsbootDevPrecision

log = logging.getLogger('imc')


def get_boot_order_precision(handle, dump=False, server_id=1):
    """
    Gets the precision boot order.
    This is supported from EP release onwards only

    Args:
        handle (ImcHandle)
        dump (bool): True or False
        server_id (int): Id of the server in case of C3260 platforms

    Returns:
        List of dict in the format
            [{"order": '2', "type": "pxe", "name": "pxe"}]

    Example:
        boot_order_precision(handle, dump=False)
    """

    server_dn = imccoreutils.get_server_dn(handle, server_id)
    parent_dn = server_dn + "/bios/bdgep"

    boot_order_list = []
    boot_device_list = handle.query_children(
        in_dn=parent_dn, class_id="BiosBootDevPrecision")

    for device in boot_device_list:
        boot_order_list.append({"order": device.order,
                                "type": device.type,
                                "name": device.name})

    sorted_boot_order_list = sorted(
        boot_order_list, key=lambda item: item["order"])

    if dump:
        log.info("Precision Boot Order is [Order, Type, Name]:")
        log.info("--------------------------------------------")
        for device in sorted_boot_order_list:
            log.info(" %s %s %s" % (device["order"].ljust(5),
                                    device["type"].ljust(10), device["name"].ljust(20)))

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


def _is_boot_order_precision(dn):
    return dn.find("precision") != -1


def _is_boot_order_policy(dn):
    return dn.find("policy") != -1


def _get_device(parent_dn, device_type, device_name):
    from imcsdk.imccoreutils import load_class

    if _is_boot_order_precision(parent_dn):
        if device_type not in precision_device_dict:
            return None
        class_struct = load_class(precision_device_dict[device_type])
        class_obj = class_struct(parent_mo_or_dn=parent_dn, name=device_name)
    elif _is_boot_order_policy(parent_dn):
        if device_type not in policy_device_dict:
            return None
        class_struct = load_class(policy_device_dict[device_type])
        class_obj = class_struct(parent_mo_or_dn=parent_dn)
    else:
        return None

    return class_obj


def _add_boot_device(handle, parent_dn, boot_device):
    """
    This method verifies and adds the boot device in the boot order
    Used by set_boot_order_precision and set_boot_order_policy

    Args:
        handle(ImcHandle)
        boot_device(dict): This is a tuple of the format
                    {"order":'1', "type":"vmedia", "name": "vmedia"}

    Returns:
        None
    """

    device = _get_device(parent_dn,
                         boot_device["type"],
                         boot_device["name"])
    if device is None:
        raise ValueError(
            "Unsupported boot-device %s with label %s" %
            (boot_device["type"], boot_device["name"]))

    device.order = boot_device["order"]
    if hasattr(device, "state"):
        device.state = "enabled"
    handle.add_mo(device, modify_present=True)


def set_boot_order_precision(
        handle, reboot_on_update=True, configured_boot_mode="Legacy",
        boot_devices=[], server_id=1):
    """
    This method will replace the existing boot order precision with the new one
        and also set the boot mode
    This functionality is available only in release EP and above

    Args:
        handle (ImcHandle)
        reboot_on_update (bool): True, False
        configured_boot_mode(string): "Legacy", "Uefi", "None"
        boot_devices (list of dict): format
            [{"order":'1', "type":"vmedia", "name":"vmedia"},
             {"order":'2', "type":"hdd", "name":"hdd"}]

            boot-order(string): Order
            boot-device-type(string): "hdd", "iscsi", "pchstorage", "pxe",
                                      "san", "sdcard", "uefishell", "usb",
                                      "vmedia"
            boot-device-name(string): Unique label for the boot device
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms

    Returns:
        LsBootDevPrecision object

    Examples:
        set_boot_order_precision(
            handle,
             reboot_on_update=False,
             configured_boot_mode="Uefi",
             boot_devices = [{"order":'1', "type":"vmedia", "name":"vmedia"},
                             {"order":'2', "type":"hdd", "name":"hdd"}]
    """

    # Insert version check here to gracefully handle older versions of CIMC

    server_dn = imccoreutils.get_server_dn(handle, server_id)
    lsbootdevprecision_mo = LsbootDevPrecision(
        parent_mo_or_dn=server_dn)
    lsbootdevprecision_mo.reboot_on_update = ("no", "yes")[reboot_on_update]
    lsbootdevprecision_mo.configured_boot_mode = configured_boot_mode

    handle.set_mo(lsbootdevprecision_mo)

    boot_order_child_mos = handle.query_children(
        in_dn=lsbootdevprecision_mo.dn)
    for mo in boot_order_child_mos:
        handle.remove_mo(mo)

    for device in boot_devices:
        _add_boot_device(handle, lsbootdevprecision_mo.dn, device)

    lsbootdevprecision_mo = handle.query_classid("LsbootDevPrecision")
    return lsbootdevprecision_mo


def get_configured_boot_precision(handle, server_id=1):
    from imcsdk.imccoreutils import get_server_dn

    configured_boot_order = []

    class_to_name_dict = {value: key for key, value in precision_device_dict.items()}

    server_dn = get_server_dn(handle, server_id)
    pmo = LsbootDevPrecision(parent_mo_or_dn=server_dn)
    mos = handle.query_children(in_dn=pmo.dn)
    for mo in mos:
        device = {"order": mo.order,
                  "type": class_to_name_dict[mo._class_id],
                  "name": mo.name}
        configured_boot_order.append(device)
    return sorted(configured_boot_order, key=lambda x: x["order"])


def boot_order_precision_exists(handle, **kwargs):
    from imcsdk.imccoreutils import _is_valid_arg, _set_server_dn

    server_dn = _set_server_dn(handle, kwargs)
    mos = handle.query_children(in_dn=server_dn,
                                class_id="LsbootDevPrecision")
    if len(mos) == 0:
        return False, "no Mos found"

    mo = mos[0]

    args = {"reboot_on_update": ("no", "yes")[kwargs.get("reboot_on_update") == True],
            "configured_boot_mode": kwargs.get("configured_boot_mode")}
    if not mo.check_prop_match(**args):
        return False, "parent MO property values do not match"

    if _is_valid_arg("boot_devices", kwargs):
        in_boot_order = sorted(kwargs["boot_devices"], key=lambda x: x["order"])
        configured_boot_order = get_configured_boot_precision(handle, kwargs.get("server_id"))

        if len(in_boot_order) != len(configured_boot_order):
            return False, "length mismatch"
        for i in range(0, len(in_boot_order)):
            if not (in_boot_order[i]["order"] == configured_boot_order[i]["order"] and
                    in_boot_order[i]["type"] == configured_boot_order[i]["type"] and
                    in_boot_order[i]["name"] == configured_boot_order[i]["name"]):
                return False, "dictionaries do not match"
    return True, "exists"


def get_boot_order_policy(handle, dump=False, server_id=1):
    """
    Gets the boot order. This is the legacy boot order

    Args:
        handle (ImcHandle)
        dump (bool): True or False
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms

    Returns:
        List of dict in the format
            [{"order": '1', "type": "pxe", "name": "pxe"}]

    Example:
        get_boot_order_policy(handle, dump=False)
    """

    from imcsdk.mometa.lsboot.LsbootBootSecurity import LsbootBootSecurity

    server_dn = imccoreutils.get_server_dn(handle, server_id)
    parent_dn = server_dn + "/boot-policy"

    boot_order_list = []
    child_mo_list = handle.query_children(
        in_dn=parent_dn)
    boot_security_policy = LsbootBootSecurity(
        parent_mo_or_dn=parent_dn)

    for device in child_mo_list:
        if device.dn == boot_security_policy.dn:
            continue

        device_name = "NA"
        if hasattr(device, "name"):
            device_name = device.name

        boot_order_list.append({"order": device.order,
                                "type": device.type,
                                "name": device_name})

    sorted_boot_order_list = sorted(
        boot_order_list, key=lambda x: x["order"])

    if dump:
        log.info("Boot Order according to Policy is [Order, Type, Name]:")
        log.info("------------------------------------------------------")

        for device_tuple in sorted_boot_order_list:
            log.info(
                " %s %s %s" %
                (device_tuple["order"].ljust(5),
                 device_tuple["type"].center(10),
                 device_tuple["name"].center(20)))

    return sorted_boot_order_list


def set_boot_order_policy(handle, reboot_on_update=False,
                          secure_boot=False, boot_devices=[], server_id=1):
    """
    This method will set the boot order policy passed from the user
    This is the deprecated way of setting the boot order
        and is applicable releases older than EP

    Args:
        handle (ImcHandle)
        reboot_on_update (bool): True, False
        secure_boot (bool): secure boot
        boot_devices (list of dict): format
            [{"order":'1', "type":"vmedia", "name":"vmedia"},
             {"order":'2', "type":"lan", "name":"lan"}]

            boot-order(string): Order
            boot-device-type(string): "efi", "lan", "storage", "vmedia"
            boot-device-name(string): Unique label for the boot device
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms
    Returns:
        LsBootDef object

    Examples:
        set_boot_order_policy(
            handle,
            reboot_on_update=False,
            secure_boot=True,
            boot_devices = [{"order":'1', "type":"vmedia", "name":"vmedia"},
                            {"order":'2', "type":"lan", "name":"lan"}]


    """

    from imcsdk.mometa.lsboot.LsbootDef import LsbootDef
    from imcsdk.mometa.lsboot.LsbootBootSecurity import LsbootBootSecurity

    server_dn = imccoreutils.get_server_dn(handle, server_id)

    boot_policy = LsbootDef(parent_mo_or_dn=server_dn)
    boot_policy.reboot_on_update = ("no", "yes")[reboot_on_update]
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

    for device in boot_devices:
        _add_boot_device(handle, boot_policy.dn, device)

    boot_policy = handle.query_classid("LsbootDef")
    return boot_policy
