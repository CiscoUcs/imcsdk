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

import time
from imcsdk.imcexception import ImcOperationError
from imcsdk.mometa.compute.ComputeRackUnit import ComputeRackUnit,\
        ComputeRackUnitConsts
from imcsdk.mometa.equipment.EquipmentChassis import EquipmentChassis
from imcsdk.mometa.compute.ComputeServerNode import ComputeServerNodeConsts
from imcsdk.mometa.equipment.EquipmentLocatorLed \
    import EquipmentLocatorLed, EquipmentLocatorLedConsts
from imcsdk.mometa.equipment.EquipmentChassisLocatorLed \
    import EquipmentChassisLocatorLed, EquipmentChassisLocatorLedConsts
from imcsdk.imccoreutils import get_server_dn, IMC_PLATFORM, _set_server_dn
from imcsdk.apis.utils import _is_valid_arg


def _set_power_state(handle, server_dn, state):
    server_mo = handle.query_dn(server_dn)
    if handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        mo_class = ComputeRackUnitConsts
    elif handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        mo_class = ComputeServerNodeConsts
    else:
        raise ImcOperationError("Set Power State", "Unknown platform:%s found" %
                                handle.platform)

    state_dict = {
        "up": mo_class.ADMIN_POWER_UP,
        "down": mo_class.ADMIN_POWER_DOWN,
        "graceful-down": mo_class.ADMIN_POWER_SOFT_SHUT_DOWN,
        "cycle": mo_class.ADMIN_POWER_CYCLE_IMMEDIATE
    }

    server_mo.admin_power = state_dict[state]
    handle.set_mo(server_mo)


def server_power_state_get(handle, server_id=1):
    """
    This method will return the oper power status of the rack server

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Examples:
        For classic or non-C3260 series servers:-
        server_power_state_get(handle)

        For modular or C3260 series servers, server_id should also be passed
        in the params:-
        server_power_state_get(handle, server_id=1)
        If server_id is not specified, this will assume server_id="1"

    Returns:
        oper power state(string)
    """

    server_dn = get_server_dn(handle, server_id)
    server_mo = handle.query_dn(server_dn)
    if server_mo:
        return server_mo.oper_power

    raise ImcOperationError("Get Server Power State",
                            "Managed Object not found for dn:%s" % server_dn)


def _wait_for_power_state(handle, state, timeout=60, interval=5, server_id=1):
    """
    This method should be called after a power state change has been triggered.
    It will poll the server and return when the desired state is achieved.

    Args:
        handle(ImcHandle)
        state(str)
        timeout(int)
        interval(int)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        bool
    """
    # Verify desired state is valid
    if state not in ("on", "off"):
        raise ValueError("ERROR invalid state: {0}".format(state))

    # Verify interval not set to zero
    if interval < 1 or type(interval) is not int:
        raise ValueError("ERROR: interval must be positive integer")

    wait_time = 0
    while server_power_state_get(handle, server_id) != state:
        # Raise error if we've reached timeout
        if wait_time > timeout:
            raise ImcOperationError(
                'Power State Change',
                '{%s}: ERROR - Power {%s} did not complete within '
                '{%s} sec' % (handle.ip, state, timeout)
            )
        # Wait interval sec between checks
        time.sleep(interval)
        wait_time += interval


def server_power_up(handle, timeout=60, interval=5, server_id=1, **kwargs):
    """
    This method will send the server the power up signal, and then polls
    the server every $interval until either $timeout or it comes online.

    Args:
        handle(ImcHandle)
        timeout (int)
        interval (int)
        server_id (int): Server Id to be specified for C3260 platforms
        kwargs: key=value paired arguments

    Returns:
        ComputeRackUnit object for non-C3260 platform
        ComputeServerNode object for C3260 platform

    Example:
        server_power_up(handle)
        server_power_up(handle, timeout=120, interval=10)
        server_power_up(handle, server_id=2, timeout=60)
    """

    server_dn = get_server_dn(handle, server_id)
    # Turn power on only if not already powered up
    if server_power_state_get(handle, server_id) != "on":
        _set_power_state(handle, server_dn, "up")

    # Poll until the server is powered up
    _wait_for_power_state(handle, "on", timeout=timeout,
                          interval=interval, server_id=server_id)

    # Return object with current state
    return handle.query_dn(server_dn)


def server_power_down(handle, timeout=60, interval=5, server_id=1, **kwargs):
    """
    This method will power down the rack server, even if tasks are still
    running on it.  Then polls the server every $interval until either $timeout
    or it comes online.

    Args:
        handle(ImcHandle)
        timeout(int)
        interval(int)
        server_id (int): Server Id to be specified for C3260 platforms
        kwargs: key=value paired arguments

    Returns:
        ComputeRackUnit object for non-C3260 platform
        ComputeServerNode object for C3260 platform

    Example:
        server_power_down(handle)
        server_power_down(handle, timeout=120, interval=10)
        server_power_down(handle, server_id=2, timeout=60)
    """

    server_dn = get_server_dn(handle, server_id)
    # Turn power off only if not already powered down
    if server_power_state_get(handle, server_id) != "off":
        _set_power_state(handle, server_dn, "down")

    # Poll until the server is powered up
    _wait_for_power_state(handle, "off", timeout=timeout,
                          interval=interval, server_id=server_id)

    return handle.query_dn(server_dn)


def server_power_down_gracefully(handle, timeout=120, interval=5,
                                 server_id=1, **kwargs):
    """
    This method will power down the rack server gracefully

    Args:
        handle(ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms
        kwargs: key=value paired arguments

    Returns:
        ComputeRackUnit object for non-C3260 platform
        ComputeServerNode object for C3260 platform

    Example:
        server_power_down_gracefully(handle)
        server_power_down_gracefully(handle, timeout=120, interval=10)
        server_power_down_gracefully(handle, server_id=2, timeout=60)
    """

    server_dn = get_server_dn(handle, server_id)
    # Gracefully power off only if not already powered down
    if server_power_state_get(handle, server_id) != "off":
        _set_power_state(handle, server_dn, "graceful-down")

    # Poll until the server is powered up
    _wait_for_power_state(handle, "off", timeout=timeout,
                          interval=interval, server_id=server_id)

    return handle.query_dn(server_dn)


def server_power_cycle(handle, timeout=120, interval=5, server_id=1, **kwargs):
    """
    This method will power cycle the rack server immediately.

    Args:
        handle(ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms
        kwargs: key=value paired arguments


    Returns:
        ComputeRackUnit object for non-C3260 platform
        ComputeServerNode object for C3260 platform

    Example:
        server_power_cycle(handle) for non-C3260 platforms
        server_power_cycle(handle, timeout=120, interval=10) \
                for non-C3260 platforms
        server_power_cycle(handle, server_id=2, timeout=60) for C3260 platforms
    """

    server_dn = get_server_dn(handle, server_id)
    _set_power_state(handle, server_dn, "cycle")

    # Poll until the server is powered up
    _wait_for_power_state(handle, "on", timeout=timeout,
                          interval=interval, server_id=server_id)

    return handle.query_dn(server_dn)


def _set_chassis_locator_led_state(handle, enabled, kwargs):
    chassis_id = str(kwargs["chassis_id"])
    chassis_dn = "sys/chassis-" + chassis_id
    led_mo = EquipmentChassisLocatorLed(parent_mo_or_dn=chassis_dn)
    led_mo.admin_state = (EquipmentChassisLocatorLedConsts.ADMIN_STATE_OFF,
                          EquipmentChassisLocatorLedConsts.ADMIN_STATE_ON)\
                            [enabled]
    handle.set_mo(led_mo)


def _set_server_locator_led_state(handle, enabled, kwargs):
    server_dn = _set_server_dn(handle, kwargs)
    led_mo = EquipmentLocatorLed(parent_mo_or_dn=server_dn)
    led_mo.admin_state = (EquipmentLocatorLedConsts.ADMIN_STATE_OFF,
                          EquipmentLocatorLedConsts.ADMIN_STATE_ON)[enabled]
    handle.set_mo(led_mo)


def locator_led_on(handle, **kwargs):
    """
    This method will turn on the locator led on the server or chassis

    Args:
        handle(ImcHandle)
        kwargs: key=value paired arguments

    Returns:
        None

    Example:
        locator_led_on(handle) for non-C3260 platforms.
            Turns on locator led on the server.
        locator_led_on(handle, server_id=1) for C3260 platforms.
            Turns on locator led on the specified server.
        locator_led_on(handle, chassis_id=1) for C3260 platforms.
            Turns on locator led on the chassis.
    """

    if _is_valid_arg("chassis_id", kwargs):
        _set_chassis_locator_led_state(handle, True, kwargs)

    if _is_valid_arg("server_id", kwargs) or \
            handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        _set_server_locator_led_state(handle, True, kwargs)


def locator_led_off(handle, **kwargs):
    """
    This method will turn off the locator led on the server or on the chassis

    Args:
        handle(ImcHandle)
        kwargs: key=value paired arguments

    Returns:
        None

    Example:
        locator_led_off(handle) for non-C3260 platforms.
            Turns off locator led on the server.
        locator_led_off(handle, server_id=1) for C3260 platforms.
            Turns off locator led on the specified server.
        locator_led_off(handle, chassis_id=1) for C3260 platforms.
            Turns off locator led on the chassis.
    """

    if _is_valid_arg("chassis_id", kwargs):
        _set_chassis_locator_led_state(handle, False, kwargs)

    if _is_valid_arg("server_id", kwargs) or \
            handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        _set_server_locator_led_state(handle, False, kwargs)


def tag_server(handle, tag):
    """
    This method will tag the server with the label specified.
    Applicable to non-C3260 platforms

    Args:
        handle(ImcHandle)
        tag (str): Label to be used to tag the asset

    Returns:
        ComputeRackUnit object

    Example:
        tag_server(handle, tag="Row21-Rack10-Slot5")
    """
    mo = ComputeRackUnit(parent_mo_or_dn="sys", server_id='1')
    mo.asset_tag = str(tag)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def tag_chassis(handle, tag):
    """
    This method will tag the chassis with the label specified.
    Applicable to C3260 platforms

    Args:
        handle(ImcHandle)
        tag (str): Label to be used to tag the asset

    Returns:
        EquipmentChassis object

    Example:
        tag_server(handle, tag="Row21-Rack10-Slot10")
    """
    mo = EquipmentChassis(parent_mo_or_dn="sys")
    mo.asset_tag = str(tag)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)
