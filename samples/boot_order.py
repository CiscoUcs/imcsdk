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
This module fetches the boot related information.
"""


def boot_order_precision(handle, dump=True):
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
    boot_device_list = handle.query_children(in_dn=
                                             "sys/rack-unit-1/boot-precision")

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
            log.info("    %s           %s" %(b_order, device_type))
    else:
        return boot_order_dict


def boot_order(handle, dump=True):
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
    boot_device_list = handle.query_children(in_dn=
                                             "sys/rack-unit-1/boot-policy")

    for device in boot_device_list:
        if hasattr(device, "order"):
            boot_order_dict[int(device.order)] = device
    if dump:
        log.info("   Boot Order is:")
        log.info("-------------------")
        log.info("   Order \t\t Device")
        for device in boot_device_list:
            log.info("    %s \t\t\t %s" %(device.order, device.type))
    else:
        return boot_order_dict
