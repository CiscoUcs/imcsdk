# Copyright 2015 Cisco Systems, Inc.
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
This module provides APIs for the boot policy related operations.
"""

import operator
import logging

logging.basicConfig()
log = logging.getLogger('imc')
log.setLevel(logging.DEBUG)


def get_boot_order_precision(handle, dump=True):
    """
    Gets the precession boot order.

    Args:
        handle (ImcHandle)
        dump (bool): True or False

    Returns:
        Dictionary of Boot Order Id and corresponding Device MO

    Example:
        boot_order_precision(handle, dump=False)

    """

    boot_order_dict = {}
    boot_device_list = handle.query_children(
        in_dn="sys/rack-unit-1/boot-precision")

    for device in boot_device_list:
        if hasattr(device, "order"):
            boot_order_dict[int(device.order)] = device

    if dump:
        log.info("   Precision Boot Order is:")
        log.info("------------------------------")
        log.info("   Order \t\t Device")
        for b_order in sorted(boot_order_dict.keys()):
            if hasattr(boot_order_dict[b_order], "subtype") and \
                            boot_order_dict[b_order].subtype is not None:
                device_type = boot_order_dict[b_order].type + "  " + \
                       boot_order_dict[b_order].subtype
            else:
                device_type = boot_order_dict[b_order].type
            log.info("    %s           %s" % (b_order, device_type))
    else:
        return boot_order_dict


def get_boot_order(handle, dump=True):
    """
    Gets the boot order.

    Args:
        handle (ImcHandle)
        dump (bool): True or False

    Returns:
        Dictionary of Boot Order Id and corresponding Device MO

    Example:
        boot_order(handle, dump=False)

    """

    boot_order_dict = {}
    boot_device_list = handle.query_children(
        in_dn="sys/rack-unit-1/boot-policy")

    for device in boot_device_list:
        if hasattr(device, "order"):
            boot_order_dict[int(device.order)] = device
    if dump:
        log.info("   Boot Order is:")
        log.info("-------------------")
        log.info("   Order \t\t Device")
        for device in boot_device_list:
            log.info("    %s \t\t\t %s" % (device.order, device.type))
    else:
        return boot_order_dict


def _get_boot_obj(boot_dev):
    """
    This method is being used by 'set_boot_order'

    Args:
        boot_dev: Boot device

    Returns:
        Boot device object
    """

    if boot_dev == "CDROM":
        from imcsdk.mometa.lsboot.LsbootVirtualMedia import LsbootVirtualMedia
        boot_obj = LsbootVirtualMedia(
            parent_mo_or_dn="sys/rack-unit-1/boot-policy", access="read-only")
    elif boot_dev == "FDD":
        from imcsdk.mometa.lsboot.LsbootVirtualMedia import LsbootVirtualMedia
        boot_obj = LsbootVirtualMedia(
            parent_mo_or_dn="sys/rack-unit-1/boot-policy", access="read-write")
    elif boot_dev == "PXE":
        from imcsdk.mometa.lsboot.LsbootLan import LsbootLan
        boot_obj = LsbootLan(
            parent_mo_or_dn="sys/rack-unit-1/boot-policy", access="read-only")
    elif boot_dev == "EFI":
        from imcsdk.mometa.lsboot.LsbootEfi import LsbootEfi
        boot_obj = LsbootEfi(
            parent_mo_or_dn="sys/rack-unit-1/boot-policy", access="read-only")
    elif boot_dev == "HDD":
        from imcsdk.mometa.lsboot.LsbootStorage import LsbootStorage
        boot_obj = LsbootStorage(
            parent_mo_or_dn="sys/rack-unit-1/boot-policy", access="read-write")
    else:
        boot_obj = None

    return boot_obj


def _verify_boot_device(boot_dev_dict):
    """
    This method is being used by 'set_boot_order' to verify boot device.

    Args:
        boot_dev_dict: Dictionary of Boot devices

    Returns:
        Verified dictionary of Boot devices
    """
    phy_boot_dev_list = ["CDROM", "FDD", "PXE", "EFI", "HDD"]

    for boot_dev in boot_dev_dict.keys():
        if boot_dev.upper() in phy_boot_dev_list and \
                                0 < int(boot_dev_dict[boot_dev]) <= 5:
            continue
        else:
            del boot_dev_dict[boot_dev]
            log.warn("Ignoring Invalid Device <%s>" % boot_dev)
    return boot_dev_dict


def set_boot_order(handle, boot_dev_dict={}, dump=True):
    """
    This method updates the boot devices and there order in the boot policy.

    Args:

        handle : ImcHandle
        boot_dev_dict: Dictionary with key as device and value as order.
                       Available Device <HDD,FDD,CDROM,PXE,EFI>
                       Available Order <1,2,3,4,5>)

                       Eg: {"CDROM":"1","FDD":"2"}

        dump (bool): True or False

    """
    from imcsdk.imccoreutils import write_object

    boot_dev_dict = _verify_boot_device(boot_dev_dict)
    sorted_boot_dev_dict = sorted(boot_dev_dict.iteritems(),
                                  key=operator.itemgetter(1))

    existing_boot_devices = get_boot_order(handle, dump=False)
    existing_boot_device_rn_list = []

    for current_device in existing_boot_devices.values():
        existing_boot_device_rn_list.append(current_device.rn)

    for (device, order) in sorted_boot_dev_dict:
        device_obj = _get_boot_obj(device.upper())
        if device_obj is not None:
            device_obj.order = order
            if device_obj.rn in existing_boot_device_rn_list:
                handle.set_mo(device_obj)
            else:
                handle.add_mo(device_obj)
        if dump:
            write_object(device_obj)
