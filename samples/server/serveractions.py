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
This module implements all the server actions
"""


def get_server_power_state(handle):
    """
    This method will return the oper power status of the rack server

    Args:
        handle (ImcHandle)

    Returns:
        oper power state(string)
    """

    rack_mo = handle.query_dn("sys/rack-unit-1")
    return rack_mo.oper_power


def power_up_server(handle):
    """
    This method will power up the rack server

    Args:
        handle(ImcHandle)

    Returns:
        ComputeRackUnit object

    Example:
        power_up_server(handle)
    """

    from imcsdk.mometa.compute.ComputeRackUnit import ComputeRackUnit,\
        ComputeRackUnitConsts

    rack_mo = ComputeRackUnit(parent_mo_or_dn="sys", server_id="1")
    rack_mo.admin_power = ComputeRackUnitConsts.ADMIN_POWER_UP
    handle.set_mo(rack_mo)
    return rack_mo


def power_down_server(handle):
    """
    This method will power down the rack server, even if tasks are running on it

    Args:
        handle(ImcHandle)

    Returns:
        ComputeRackUnit object

    Example:
        power_down_server(handle)
    """

    from imcsdk.mometa.compute.ComputeRackUnit import ComputeRackUnit,\
        ComputeRackUnitConsts

    rack_mo = ComputeRackUnit(parent_mo_or_dn="sys", server_id="1")
    rack_mo.admin_power = ComputeRackUnitConsts.ADMIN_POWER_DOWN
    handle.set_mo(rack_mo)
    return rack_mo


def power_down_server_gracefully(handle):
    """
    This method will power down the rack server gracefully

    Args:
        handle(ImcHandle)

    Returns:
        ComputeRackUnit object

    Example:
        power_down_server_gracefully(handle)
    """

    from imcsdk.mometa.compute.ComputeRackUnit import ComputeRackUnit,\
        ComputeRackUnitConsts

    rack_mo = ComputeRackUnit(parent_mo_or_dn="sys", server_id="1")
    rack_mo.admin_power = ComputeRackUnitConsts.ADMIN_POWER_SOFT_SHUT_DOWN
    handle.set_mo(rack_mo)
    return rack_mo


def power_cycle_server(handle):
    """
    This method will power cycle the rack server immediately.

    Args:
        handle(ImcHandle)

    Returns:
        ComputeRackUnit object

    Example:
        power_cycle_server(handle)
    """

    from imcsdk.mometa.compute.ComputeRackUnit import ComputeRackUnit,\
        ComputeRackUnitConsts

    rack_mo = ComputeRackUnit(parent_mo_or_dn="sys", server_id="1")
    rack_mo.admin_power = ComputeRackUnitConsts.ADMIN_POWER_CYCLE_IMMEDIATE
    handle.set_mo(rack_mo)
    return rack_mo


def locator_led_on(handle):
    """
    This method will turn on the locator led on the server

    Args:
        handle(ImcHandle)

    Returns:
        None

    Example:
        locator_led_on(handle)
    """

    from imcsdk.mometa.equipment.EquipmentLocatorLed import EquipmentLocatorLed,\
        EquipmentLocatorLedConsts

    led_mo = EquipmentLocatorLed(parent_mo_or_dn="sys/rack-unit-1")
    led_mo.admin_state = EquipmentLocatorLedConsts.ADMIN_STATE_ON
    handle.set_mo(led_mo)


def locator_led_off(handle):
    """
    This method will turn off the locator led on the server

    Args:
        handle(ImcHandle)

    Returns:
        None

    Example:
        locator_led_off(handle)
    """

    from imcsdk.mometa.equipment.EquipmentLocatorLed import EquipmentLocatorLed,\
        EquipmentLocatorLedConsts

    led_mo = EquipmentLocatorLed(parent_mo_or_dn="sys/rack-unit-1")
    led_mo.admin_state = EquipmentLocatorLedConsts.ADMIN_STATE_OFF
    handle.set_mo(led_mo)
