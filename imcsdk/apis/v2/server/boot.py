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
import re

import imcsdk.imccoreutils as imccoreutils
from imcsdk.imcexception import ImcOperationError, ImcOperationErrorDetail
from imcsdk.mometa.lsboot.LsbootDevPrecision import LsbootDevPrecision

import imcsdk.apis.v2.server.pxe as pxe

log = logging.getLogger('imc')


def boot_order_precision_get(handle, dump=False, server_id=1):
    """
    Gets the precision boot order.
    This is supported from EP release onwards only

    Args:
        handle (ImcHandle)
        dump (bool): True or False
        server_id (int): Id of the server in case of C3260 platforms

    Returns:
        List of dict in the format
            [{"order": '2', "device-type": "pxe", "name": "pxe"}]

    Example:
        boot_order_precision(handle, dump=False)
    """

    server_dn = imccoreutils.get_server_dn(handle, server_id)
    parent_dn = server_dn + "/bios/bdgep"

    boot_order_list = []
    boot_device_list = handle.query_children(
        in_dn=parent_dn, class_id="BiosBootDevPrecision")

    for device in boot_device_list:
        device_type = device.type if device.type else str(device.type)
        boot_order_list.append({"order": device.order,
                                "device-type": device_type,
                                "name": device.name})

    sorted_boot_order_list = sorted(
        boot_order_list, key=lambda item: item["order"])

    if dump:
        log.info("Precision Boot Order is [Order, Type, Name]:")
        log.info("--------------------------------------------")
        for device in sorted_boot_order_list:
            log.info(" %s %s %s" % (device["order"].ljust(5),
                                    device["device-type"].ljust(10),
                                    device["name"].ljust(20)))

    return sorted_boot_order_list


precision_device_dict = {
    "hdd": {
        "class_id": "LsbootHdd",
        "type": "LOCALHDD"
    },
    "iscsi": {
        "class_id": "LsbootIscsi",
        "type": "ISCSI",
        "subtype": "ISCSI"
    },
    "pchstorage": {
        "class_id": "LsbootPchStorage",
        "type": "PCHSTORAGE"
    },
    "pxe": {
        "class_id": "LsbootPxe",
        "type": "PXE",
        "subtype": "PXE"
    },
    "san": {
        "class_id": "LsbootSan",
        "type": "SAN",
        "subtype": "SAN"
    },
    "sdcard": {
        "class_id": "LsbootSd",
        "type": "SDCARD"
    },
    "uefishell": {
        "class_id": "LsbootUefiShell",
        "type": "UEFISHELL"
    },
    "usb": {
        "class_id": "LsbootUsb",
        "type": "USB"
    },
    "vmedia": {
        "class_id": "LsbootVMedia",
        "type": "VMEDIA"
    },
    "nvme": {
        "class_id": "LsbootNVMe",
        "type": "NVME"
    },
    "cdd": {
        "class_id": "LsbootCdd",
        "type": "LOCALCDD"
    },
}


policy_device_dict = {
    "efi": {"class_id": "LsbootEfi", "access": "read-only"},
    "lan": {"class_id": "LsbootLan", "access": "read-only"},
    "storage": {"class_id": "LsbootStorage", "access": "read-write"},
    "cdrom": {"class_id": "LsbootVirtualMedia", "access": "read-only"},
    "fdd": {"class_id": "LsbootVirtualMedia", "access": "read-write"}
}


def _is_boot_order_precision(dn):
    return dn.find("precision") != -1


def _is_boot_order_policy(dn):
    return dn.find("policy") != -1


def _get_device_type(policy_type, in_device):
    if policy_type == "boot-order-policy":
        for device_type, device_props in policy_device_dict.items():
            if device_props["class_id"] == in_device._class_id and \
                    device_props["access"] == in_device.access:
                return device_type
    return ""


def _get_device(parent_mo_or_dn, device_type, device_name):
    from imcsdk.imccoreutils import load_class

    # precision boot order supports hierarchy in configConfMO
    # legacy boot order does not
    # so passing parent Mo to class_struct in case of precision boot order
    # in case of legacy boot order, only dn is passed
    if type(parent_mo_or_dn) is str:
        parent = parent_mo_or_dn
        parent_dn = parent_mo_or_dn
    else:
        parent = parent_mo_or_dn
        parent_dn = parent_mo_or_dn.dn

    if _is_boot_order_precision(parent_dn):
        if device_type not in precision_device_dict:
            return None
        class_struct = load_class(
            precision_device_dict[device_type]["class_id"])
        class_obj = class_struct(parent_mo_or_dn=parent, name=device_name)
        if "type" in precision_device_dict[device_type]:
            class_obj.type = precision_device_dict[device_type]["type"]
        if "subtype" in precision_device_dict[device_type]:
            class_obj.subtype = precision_device_dict[device_type]["subtype"]
    elif _is_boot_order_policy(parent_dn):
        if device_type not in policy_device_dict:
            return None
        class_struct = load_class(policy_device_dict[device_type]["class_id"])
        access = policy_device_dict[device_type]["access"]
        '''
        cdrom and fdd are of type LsbootVirtualMedia and have "access" as the
        naming property. Other objects under LsbootDef do not need this.
        Hence cdrom and fdd need special handling below.
        '''
        if device_type in ["cdrom", "fdd"]:
            class_obj = class_struct(parent_mo_or_dn=parent_dn, access=access)
        else:
            class_obj = class_struct(parent_mo_or_dn=parent_dn)
            class_obj.access = access
    else:
        return None

    return class_obj


def _add_boot_device(handle, parent_mo_or_dn, boot_device):
    """
    This method verifies and adds the boot device in the boot order
    Used by boot_order_precision_set and boot_order_policy_set

    Args:
        handle(ImcHandle)
        boot_device(dict): This is a dictionary of the format
                    {"order":'1', "device-type":"vmedia", "name": "vmedia"}

    Returns:
        None
    """

    from imcsdk.imccoreutils import is_platform_m4

    log.debug("######### %s" % boot_device)
    device = _get_device(parent_mo_or_dn,
                         boot_device["device-type"],
                         boot_device["name"])
    if device is None:
        raise ValueError(
            "Unsupported boot-device %s with label %s" %
            (boot_device["device-type"], boot_device["name"]))

    device.order = boot_device["order"]
    device_props = {key: str(value)
                    for key, value in boot_device.items()
                    if key not in ["order", "device-type", "name"]}

    # For M4, mac_address will not be sent
    if boot_device['device-type'] == 'pxe' and is_platform_m4(handle):
        device_props.pop("mac_address", None)

    if boot_device['device-type'] == 'pxe':
        device_props.pop("interface_source", None)

    # If slot == "", do not send it in xml request
    if boot_device['device-type'] in ['hdd', 'pxe', 'san', 'iscsi']:
        slot = device_props.get("slot")
        if slot is None or slot == "":
            device_props.pop("slot", None)

    # If subtype == "", do not send it in xml request
    if boot_device['device-type'] in ['vmedia', 'sdcard', 'usb']:
        subtype = device_props.get("subtype")
        if subtype is None or subtype == "":
            device_props.pop("subtype", None)

    device.set_prop_multiple(**device_props)
    if hasattr(device, "state"):
        device.state = boot_device['state']

    # applies for legacy boot order only
    if type(parent_mo_or_dn) is str:
        handle.add_mo(device, modify_present=True)


def boot_order_precision_set(
        handle,
        reboot_on_update="no",
        reapply="no",
        configured_boot_mode="Legacy",
        secure_boot="no",
        boot_devices=[],
        server_id=1):
    """
    This method will replace the existing boot order precision with the new one
        and also set the boot mode
    This functionality is available only in release EP and above

    Args:
        handle (ImcHandle)
        reboot_on_update (string): "yes", "no"
        reapply(string): "yes", "no"
        configured_boot_mode(string): "Legacy", "Uefi", "None"
        boot_devices (list of dict): format
            [{"order":'1', "device-type":"vmedia", "name":"vmedia"},
             {"order":'2', "device-type":"hdd", "name":"hdd"}]

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
        boot_order_precision_set(
            handle,
            reboot_on_update="no",
            reapply="no",
            configured_boot_mode="Uefi",
            boot_devices = [{"order":'1', "device-type":"vmedia",
                            "name":"vmedia"},
                            {"order":'2', "device-type":"hdd", "name":"hdd"}]
    """
    from imcsdk.mometa.lsboot.LsbootDef import LsbootDef
    from imcsdk.mometa.lsboot.LsbootBootSecurity import LsbootBootSecurity
    from imcsdk.imccoreutils import is_platform_m4

    boot_devices = sanitize_input_from_intersight(handle, boot_devices)

    # Insert version check here to gracefully handle older versions of CIMC

    # IMC expects the devices to be configured in sorted order
    boot_devices = sorted(boot_devices, key=lambda x: int(x["order"]))

    # filter pxe device
    # enable pxe boot on respective interface
    # derive logical port
    pxe.disable_pxeboot_vnics_all(handle)
    pxe.prepare_pxe_devices(handle, boot_devices)

    server_dn = imccoreutils.get_server_dn(handle, server_id)

    # secure boot is a part of LsBootDef
    boot_policy = LsbootDef(parent_mo_or_dn=server_dn)
    secure_boot_mo = LsbootBootSecurity(parent_mo_or_dn=boot_policy.dn)
    if secure_boot == "yes":
        secure_boot_mo.secure_boot = "enabled"
    else:
        secure_boot_mo.secure_boot = "disabled"
    handle.set_mo(secure_boot_mo)

    lsbootdev = LsbootDevPrecision(parent_mo_or_dn=server_dn)

    # clean existing configuration
    # Need to check if doing this everytime will have any adverse impact
    boot_order_child_mos = handle.query_children(in_dn=lsbootdev.dn)

    #check the version as CSCvh47929 fix is applied to later versions
    for mo in boot_order_child_mos:
        if str(handle.version) < "3.1(3a)" and mo.get_class_id() == "LsbootCdd":
            # Deletion of LsbootCdd is not supported using XML API for older versions
            # although CSCvh47929 is fixed
            # Existing Cdd device will automatically move down the
            # order when configuring other devices with CDD device's order
            continue
        handle.remove_mo(mo)

    # set the boot order precision related properties and devices
    lsbootdev.reboot_on_update = reboot_on_update
    lsbootdev.reapply = reapply
    if secure_boot == "no":
        lsbootdev.configured_boot_mode = configured_boot_mode


    i = 0
    #check the version and skip if the device is of type localcdd
    for device in boot_devices:
        if device["device-type"] == "cdd" and (is_platform_m4(handle) or str(handle.version) < "3.1(3a)"):
            i = i + 1
            continue
        if device['device-type'] == 'pxe' and is_platform_m4(handle) and device['interface_source'] == 'mac':
            i = i + 1
            continue

        #if the list has cdd, reorder the policy types that are after cdd  as cdd will be skipped
        #and CIMC expects the devices in sorted order.
        if i != 0:
            device["order"] = str(int(device["order"]) - i)
        _add_boot_device(handle, lsbootdev, device)
    handle.set_mo(lsbootdev)
    return lsbootdev



def boot_precision_configured_get(handle, server_id=1):
    from imcsdk.imccoreutils import get_server_dn

    configured_boot_order = []

    class_to_name_dict = {
        value["class_id"]: key for key,
        value in precision_device_dict.items()}

    server_dn = get_server_dn(handle, server_id)
    pmo = LsbootDevPrecision(parent_mo_or_dn=server_dn)
    mos = handle.query_children(in_dn=pmo.dn)
    for mo in mos:
        if mo._class_id not in class_to_name_dict:
            print("unknown boot device type " + mo._class_id)
            continue
        device = {"order": mo.order,
                  "device-type": class_to_name_dict[mo._class_id],
                  "name": mo.name}
        configured_boot_order.append(device)
    return sorted(configured_boot_order, key=lambda x: int(x["order"]))


def boot_order_precision_exists(handle, **kwargs):
    from imcsdk.imccoreutils import _set_server_dn
    from imcsdk.apis.v2.utils import _is_valid_arg

    server_dn = _set_server_dn(handle, kwargs)
    mos = handle.query_children(in_dn=server_dn,
                                class_id="LsbootDevPrecision")
    if len(mos) == 0:
        return False, "no Mos found"

    mo = mos[0]

    args = {
        "configured_boot_mode": kwargs.get("configured_boot_mode")
    }
    if not mo.check_prop_match(**args):
        return False, "parent MO property values do not match"

    if _is_valid_arg("boot_devices", kwargs):
        boot_devices = kwargs["boot_devices"]
        boot_devices = sanitize_input_from_intersight(handle, boot_devices)

        in_boot_order = sorted(
            boot_devices,
            key=lambda x: int(x["order"]))
        configured_boot_order = boot_precision_configured_get(
            handle, kwargs.get("server_id"))

        if len(in_boot_order) != len(configured_boot_order):
            return False, "length mismatch"
        for i in range(0, len(in_boot_order)):
            bt_ord = in_boot_order[i]
            cfg_bt_ord = configured_boot_order[i]
            if not (bt_ord["order"] == cfg_bt_ord["order"] and
                    bt_ord["device-type"] == cfg_bt_ord["device-type"] and
                    bt_ord["name"] == cfg_bt_ord["name"]):
                return False, "dictionaries do not match"
    return True, None


def boot_order_policy_get(handle, dump=False, server_id=1):
    """
    Gets the boot order. This is the legacy boot order

    Args:
        handle (ImcHandle)
        dump (bool): True or False
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms

    Returns:
        List of dict in the format
            [{"order": '1', "device-type": "pxe", "name": "pxe"}]

    Example:
        boot_order_policy_get(handle, dump=False)
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

        device_type = _get_device_type("boot-order-policy", device)
        boot_order_list.append({"order": device.order,
                                "device-type": device_type,
                                "name": device_name})

    sorted_boot_order_list = sorted(
        boot_order_list, key=lambda x: int(x["order"]))

    if dump:
        log.info("Boot Order according to Policy is [Order, Type, Name]:")
        log.info("------------------------------------------------------")

        for device_tuple in sorted_boot_order_list:
            log.info(
                " %s %s %s" %
                (device_tuple["order"].ljust(5),
                 device_tuple["device-type"].center(10),
                 device_tuple["name"].center(20)))

    return sorted_boot_order_list


def boot_order_policy_set(handle, reboot_on_update="no",
                          secure_boot="no",
                          boot_devices=[],
                          server_id=1):
    """
    This method will set the boot order policy passed from the user
    This is the deprecated way of setting the boot order
        and is applicable releases older than EP

    Args:
        handle (ImcHandle)
        reboot_on_update (string): "yes", "no"
        secure_boot (string): "enabled", "disabled"
        boot_devices (list of dict): format
            [{"order":'1', "device-type":"cdrom", "name":"cdrom0"},
             {"order":'2', "device-type":"lan", "name":"lan"}]

            boot-order(string): Order
            boot-device-type(string): "efi", "lan", "storage", "cdrom", "fdd"
            boot-device-name(string): Unique label for the boot device
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms
    Returns:
        LsBootDef object

    Examples:
        boot_order_policy_set(
            handle,
            reboot_on_update="yes",
            secure_boot="no",
            boot_devices = [{"order":'1', "device-type":"cdrom",
                            "name":"cdrom0"},
                            {"order":'2', "device-type":"lan", "name":"lan"}]


    """

    # IMC expects the devices to be configured in sorted order
    boot_devices = sorted(boot_devices, key=lambda x: int(x["order"]))

    from imcsdk.mometa.lsboot.LsbootDef import LsbootDef
    from imcsdk.mometa.lsboot.LsbootBootSecurity import LsbootBootSecurity

    server_dn = imccoreutils.get_server_dn(handle, server_id)

    boot_policy = LsbootDef(parent_mo_or_dn=server_dn)
    boot_policy.reboot_on_update = reboot_on_update
    handle.set_mo(boot_policy)

    secure_boot_policy = LsbootBootSecurity(parent_mo_or_dn=boot_policy.dn)
    # Secure boot policy is supported only from ImcVersion 2.0(1a)
    if handle.version >= secure_boot_policy.get_version(handle.platform):
        if secure_boot == "yes":
            secure_boot_policy.secure_boot = "enabled"
        else:
            secure_boot_policy.secure_boot = "disabled"
        handle.set_mo(secure_boot_policy)

    boot_policy_child_mos = handle.query_children(in_dn=boot_policy.dn)
    for mo in boot_policy_child_mos:
        if mo.dn == secure_boot_policy.dn:
            continue
        handle.remove_mo(mo)

    for device in boot_devices:
        _add_boot_device(handle, boot_policy.dn, device)

    boot_policy = handle.query_classid("LsbootDef")
    return boot_policy


def convert_type(intersight_type):
    switcher = {
        "boot.LocalDisk": "hdd",
        "boot.Pxe": "pxe",
        "boot.Iscsi": "iscsi",
        "boot.Nvme": "nvme",
        "boot.PchStorage": "pchstorage",
        "boot.San": "san",
        "boot.SdCard": "sdcard",
        "boot.UefiShell": "uefishell",
        "boot.Usb": "usb",
        "boot.VirtualMedia": "vmedia",
        "boot.LocalCdd": "cdd"
    }
    return switcher.get(intersight_type, None)


def sanitize_input_from_intersight(handle, boot_devices):
    """
        Intersight always sends boot devices in the right order. For this
        reason the order propery is not populated by intersight policy
        service. We populate the order property here.

        We also convert from intersight device type to sdk device type
    """
    import copy
    from imcsdk.apis.v2.versionconstraints.boot import fix_bootloader_options
    log.debug("##### Input boot devices %s" % boot_devices)
    # if order is present, then it is not an input from intersight
    if len(boot_devices) > 0 and "order" in boot_devices[0]:
        return boot_devices

    bd_copy = copy.deepcopy(boot_devices)
    order = 0
    bd = []
    for each in bd_copy:
        order += 1
        each["order"] = str(order)
        each["device-type"] = convert_type(each["ObjectType"])
        if each["device-type"] is None:
            print("Unknown device type " + each["ObjectType"])
            continue

        enabled = each.get("Enabled", True)
        if enabled:
            each["state"] = "enabled"
        else:
            each["state"] = "disabled"

        # convert MacAddress to mac_address
        if each["device-type"] == "pxe":
            if each["MacAddress"]:
                each["mac_address"] = each["MacAddress"]
            each.pop("MacAddress", None)
            if each["InterfaceSource"]:
                each["interface_source"] = each["InterfaceSource"]
            each.pop("InterfaceSource", None)
            if each["InterfaceName"]:
                each["interface_name"] = each["InterfaceName"]
            each.pop("InterfaceName", None)
        elif each["device-type"] in ["vmedia", "sdcard", "usb"]:
            if each["Subtype"] == "None":
                each.pop("Subtype")

        each.pop("ObjectType", None)
        each.pop("Type", None)
        each.pop("Enabled", None)

        fix_bootloader_options(handle, each)

        # Check for any other properties which are "None" and pop them out
        each = {k: v for k, v in each.items() if v != "None"}

        bd.append({k.lower(): v for k, v in each.items()})
    log.debug("##### Sanitized boot devices %s" % bd)
    return bd
