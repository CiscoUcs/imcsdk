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
import json
import imcsdk.imccoreutils as imccoreutils
from imcsdk.mometa.lsboot.LsbootDevPrecision import LsbootDevPrecision
from imcsdk.imcexception import ImcOperationError
from imcsdk.apis.utils import _is_valid_arg

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
        boot_order_list.append({"order": device.order,
                                "device-type": device.type,
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
        "type": "SDCARD",
        "subtype": "SDCARD"
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
        for device_type, device_props in policy_device_dict.iteritems():
            if device_props["class_id"] == in_device._class_id and \
                    device_props["access"] == in_device.access:
                return device_type
    return ""


def _get_device(parent_dn, device_type, device_name):
    from imcsdk.imccoreutils import load_class

    if _is_boot_order_precision(parent_dn):
        if device_type not in precision_device_dict:
            return None
        class_struct = load_class(precision_device_dict[device_type]["class_id"])
        class_obj = class_struct(parent_mo_or_dn=parent_dn, name=device_name)
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


def _add_boot_device(handle, parent_dn, boot_device):
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

    device = _get_device(parent_dn,
                         boot_device["device-type"],
                         boot_device["name"])
    if device is None:
        raise ValueError(
            "Unsupported boot-device %s with label %s" %
            (boot_device["device-type"], boot_device["name"]))

    device.order = boot_device["order"]
    device_props = {key: value for key, value in boot_device.iteritems() if key not in ["order", "device-type", "name"]}
    device.set_prop_multiple(**device_props)
    if hasattr(device, "state"):
        device.state = "enabled"
    handle.add_mo(device, modify_present=True)


def boot_order_precision_set(
        handle,
        reboot_on_update=False,
        reapply=False,
        configured_boot_mode="Legacy",
        boot_devices=[],
        server_id=1):
    """
    This method will replace the existing boot order precision with the new one
        and also set the boot mode
    This functionality is available only in release EP and above

    Args:
        handle (ImcHandle)
        reboot_on_update (bool): True, False
        reapply(bool): True, False
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
            reboot_on_update=False,
            reapply=False,
            configured_boot_mode="Uefi",
            boot_devices = [{"order":'1', "device-type":"vmedia", "name":"vmedia"},
                            {"order":'2', "device-type":"hdd", "name":"hdd"}]
    """

    # Insert version check here to gracefully handle older versions of CIMC

    # IMC expects the devices to be configured in sorted order
    boot_devices = sorted(boot_devices, key=lambda x: x["order"])

    server_dn = imccoreutils.get_server_dn(handle, server_id)
    lsbootdevprecision_mo = LsbootDevPrecision(parent_mo_or_dn=server_dn)

    lsbootdevprecision_mo.reboot_on_update = "no"
    if reboot_on_update:
        lsbootdevprecision_mo.reboot_on_update = "yes"

    lsbootdevprecision_mo.reapply = "no"
    if reapply:
        lsbootdevprecision_mo.reapply = "yes"

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
        device = {"order": mo.order,
                  "device-type": class_to_name_dict[mo._class_id],
                  "name": mo.name}
        configured_boot_order.append(device)
    return sorted(configured_boot_order, key=lambda x: x["order"])


def boot_order_precision_exists(handle, **kwargs):
    from imcsdk.imccoreutils import _set_server_dn
    from imcsdk.apis.utils import _is_valid_arg

    server_dn = _set_server_dn(handle, kwargs)
    mos = handle.query_children(in_dn=server_dn,
                                class_id="LsbootDevPrecision")
    if len(mos) == 0:
        return False, "no Mos found"

    mo = mos[0]

    reboot_on_update = kwargs.get("reboot_on_update")
    if isinstance(reboot_on_update, bool):
        reboot_on_update = ("no", "yes")[reboot_on_update]

    args = {"reboot_on_update": reboot_on_update,
            "configured_boot_mode": kwargs.get("configured_boot_mode")}
    if not mo.check_prop_match(**args):
        return False, "parent MO property values do not match"

    if _is_valid_arg("boot_devices", kwargs):
        in_boot_order = sorted(
            kwargs["boot_devices"],
            key=lambda x: x["order"])
        configured_boot_order = boot_precision_configured_get(
            handle, kwargs.get("server_id"))

        if len(in_boot_order) != len(configured_boot_order):
            return False, "length mismatch"
        for i in range(0, len(in_boot_order)):
            if not (in_boot_order[i]["order"] == configured_boot_order[i]["order"] and
                    in_boot_order[i]["device-type"] == configured_boot_order[i]["device-type"] and
                    in_boot_order[i]["name"] == configured_boot_order[i]["name"]):
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
        boot_order_list, key=lambda x: x["order"])

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


def boot_order_policy_set(handle, reboot_on_update=False,
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
            reboot_on_update=False,
            secure_boot=True,
            boot_devices = [{"order":'1', "device-type":"cdrom", "name":"cdrom0"},
                            {"order":'2', "device-type":"lan", "name":"lan"}]


    """

    # IMC expects the devices to be configured in sorted order
    boot_devices = sorted(boot_devices, key=lambda x: x["order"])

    from imcsdk.mometa.lsboot.LsbootDef import LsbootDef
    from imcsdk.mometa.lsboot.LsbootBootSecurity import LsbootBootSecurity

    server_dn = imccoreutils.get_server_dn(handle, server_id)

    boot_policy = LsbootDef(parent_mo_or_dn=server_dn)
    boot_policy.reboot_on_update = ("no", "yes")[reboot_on_update]
    handle.set_mo(boot_policy)

    secure_boot_policy = LsbootBootSecurity(parent_mo_or_dn=boot_policy.dn)
    # Secure boot policy is supported only from ImcVersion 2.0(1a)
    if handle.version >= secure_boot_policy.get_version(handle.platform):
        secure_boot_policy.secure_boot = ("disabled", "enabled")[secure_boot]
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


def _get_bios_dn(handle, server_id=1):
    server_dn = imccoreutils.get_server_dn(handle, server_id)
    return (server_dn + '/bios')


def _get_bios_profile_mo(handle, name, server_id=1):
    bios_dn = _get_bios_dn(handle, server_id)
    parent_dn = bios_dn + '/profile-mgmt'
    mos = handle.query_children(in_dn=parent_dn)
    for mo in mos:
        if mo._class_id == 'BiosProfile' and mo.name == name:
            return mo
    return None


def _get_bios_profile(handle, name, server_id=1):
    mo = _get_bios_profile_mo(handle, name=name, server_id=server_id)
    if mo is None:
        raise ImcOperationError("Get BiosProfile: %s " % name,
                                "Managed Object not found")
    return mo


def bios_profile_backup_running(handle, server_id=1, **kwargs):
    """
    Backups up the running configuration of various bios tokens to create a
    'cisco_backup_profile'.
    Will overwrite the existing backup profile if it exists.

    Args:
        handle (ImcHandle)
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms
        kwargs : Key-Value paired arguments for future use

    Returns:
        BiosProfile object corresponding to the backup profile created

    Raises:
        ImcOperationError if the backup profile is not created

    Examples:
        bios_profile_backup_running(handle, server_id=1)
    """

    from imcsdk.mometa.bios.BiosProfileManagement import BiosProfileManagement,\
        BiosProfileManagementConsts
    mo = BiosProfileManagement(parent_mo_or_dn=_get_bios_dn(handle, server_id))
    mo.admin_action = BiosProfileManagementConsts.ADMIN_ACTION_BACKUP
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)

    return _get_bios_profile(handle, name='cisco_backup_profile',
                             server_id=server_id)


def bios_profile_upload(handle, remote_server, remote_file, protocol='tftp',
                        user=None, pwd=None, server_id=1, **kwargs):
    """
    Uploads a user configured bios profile in json format.
    Cisco IMC supports uploading a maximum of 3 profiles

    Args:
        handle (ImcHandle)
        remote_server (str): Remote Server IP or Hostname
        remote_file (str): Remote file path
        protocol (str): Protocol for downloading the certificate
                        ['tftp', 'ftp', 'http', 'scp', 'sftp']
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms
        kwargs: Key-Value paired arguments for future use

    Returns:
        UploadBiosProfile object

    Examples:
        bios_profile_upload(handle, remote_server='1.1.1.1',
                        remote_file='/tmp/bios_profile', protocol='scp',
                        user='abcd', pwd='pqrs')
    """

    from imcsdk.mometa.upload.UploadBiosProfile import UploadBiosProfile
    bios_dn = _get_bios_dn(handle, server_id=server_id)
    mo = UploadBiosProfile(
            parent_mo_or_dn=bios_dn + '/profile-mgmt')
    params = {
        'remote_server': remote_server,
        'remote_file': remote_file,
        'protocol': protocol,
        'user': user,
        'pwd': pwd
    }
    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def bios_profile_get(handle, name, server_id=1):
    """
    Gets the bios profile corresponding to the name specified

    Args:
        handle (ImcHandle)
        name (str): Name of the bios profile.
                    Corresponds to the name field in the json file.
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms

    Returns:
        BiosProfile object corresponding to the name specified

    Raises:
        ImcOperationError if the bios profile is not found

    Examples:
        bios_profile_get(handle, name='simple')
    """

    return _get_bios_profile_mo(handle, name=name, server_id=server_id)


def bios_profile_activate(handle, name, backup_on_activate=True,
                          reboot_on_activate=False, server_id=1, **kwargs):
    """
    Activates the bios profile specified by name on the Cisco IMC Server

    Args:
        handle (ImcHandle)
        name (str): Name of the bios profile.
                    Corresponds to the name field in the json file.
        backup_on_activate (bool): Backup running bios configuration
                                   before activating this profile.
                                   Will overwrite the previous backup.
        reboot_on_activate (bool): Reboot the host/server for the newer bios
                                   configuration to be applied.
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms.
        kwargs: Key-Value paired arguments for future use.

    Returns:
        BiosProfile object corresponding to the name specified

    Raises:
        ImcOperationError if the bios profile is not found

    Examples:
        bios_profile_activate(handle, name='simple',
                              backup_on_activate=True,
                              reboot_on_activate=False)
    """

    from imcsdk.mometa.bios.BiosProfile import BiosProfileConsts
    mo = _get_bios_profile(handle, name=name, server_id=server_id)
    params = {
        'backup_on_activate': ('no', 'yes')[backup_on_activate],
        'reboot_on_activate': ('no', 'yes')[reboot_on_activate],
        'enabled': 'yes',
        'admin_action': BiosProfileConsts.ADMIN_ACTION_ACTIVATE
    }
    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def bios_profile_delete(handle, name, server_id=1):
    """
    Deletes the bios profile specified by the name on the Cisco IMC server

    Args:
        handle (ImcHandle)
        name (str): Name of the bios profile.
                    Corresponds to the name field in the json file.
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms.

    Returns:
        None

    Raises:
        ImcOperationError if the bios profile is not found

    Examples:
        bios_profile_delete(handle, name='simple', server_id=2)
    """
    from imcsdk.mometa.bios.BiosProfile import BiosProfileConsts
    mo = _get_bios_profile(handle, name=name, server_id=server_id)
    mo.admin_action = BiosProfileConsts.ADMIN_ACTION_DELETE
    handle.set_mo(mo)


def is_bios_profile_enabled(handle, name, server_id=1):
    """
    Args:
        handle (ImcHandle)
        name (str): Name of the bios profile.
                    Corresponds to the name field in the json file.
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms.

    Returns:
        bool

    Raises:
        ImcOperationError if the bios profile is not found

    Examples:
        is_bios_profile_enabled(handle,
                                name='simple',
                                server_id=1)
    """
    mo = _get_bios_profile(handle, name=name, server_id=server_id)
    return mo.enabled.lower() in ['yes', 'true']


def bios_profile_exists(handle, name, server_id=1, **kwargs):
    """
    Checks if the bios profile with the specified params exists

    Args:
        handle (ImcHandle)
        name (str): Name of the bios profile.
                    Corresponds to the name field in the json file.
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms.
        kwargs: Key-Value paired arguments relevant to BiosProfile object

    Returns:
        (True, BiosProfile) if the settings match, else (False, None)

    Examples:
        match, mo = bios_profile_exists(handle, name='simple',
                                        enabled=True)
    """

    mo = _get_bios_profile_mo(handle, name=name, server_id=server_id)
    if mo is None:
        return False, None

    params = {}

    if _is_valid_arg('enabled', kwargs):
        params['enabled'] = ('No', 'Yes')[kwargs.pop('enabled')]

    if not mo.check_prop_match(**params):
        return False, None

    if not mo.check_prop_match(**kwargs):
        return False, None

    return True, mo


def bios_profile_generate_json(handle, name, server_id=1, file_name=None):
    """
    Generates a json output of the bios profile specified by the name on
    the Cisco IMC server.
    If a file name is specified, it writes the output to the file.

    Args:
        handle (ImcHandle)
        name (str): Name of the bios profile.
                    Corresponds to the name field in the json file.
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms.

    Returns:
        JSON Output of the Bios Tokens

    Raises:
        ImcOperationError if the bios profile is not found

    Examples:
        bios_profile_generate_json(handle, name='simple', server_id=2)
    """

    output = {}
    output['tokens'] = {}

    mo = _get_bios_profile(handle, name=name, server_id=server_id)
    output['name'] = mo.name
    output['description'] = mo.description

    tokens = handle.query_children(in_dn=mo.dn)
    output['tokens'] = {x.name: x.configured_value for x in tokens}

    if file_name:
        f = open(file_name, 'w')
        f.write(json.dumps(output))
        f.close()

    return output
