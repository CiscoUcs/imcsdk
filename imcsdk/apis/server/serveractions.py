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


def _wait_for_power_state(handle, state, timeout=60, interval=5):
    """
    This method should be called after a power state change has been triggered.
    It will poll the server and return when the desired state is achieved.

    Args:
        handle(ImcHandle)
        state(str)

    Returns:
        bool
    """
    import time
    from imcsdk.imcexception import ImcOperationError

    # Verify desired state is valid
    if state not in ("on", "off"):
        raise ValueError("ERROR invalid state: {0}".format(state))

    # Verify interval not set to zero
    if interval < 1 or type(interval) is not int:
        raise ValueError("ERROR: interval must be positive integer")

    wait_time = 0
    while get_server_power_state(handle) != state:
        # Raise error if we've reached timeout
        if wait_time > timeout:
            raise ImcOperationError(
                'Power State Change',
                '{0}: ERROR - Power {1} did not complete within ' +
                '{2} sec'.format(handle.ip, state, timeout)
            )
        # Wait interval sec between checks
        time.sleep(interval)
        wait_time += interval


def power_up_server(handle, timeout=60, interval=5):
    """
    This method will send the server the power up signal, and then polls
    the server every $interval until either $timeout or it comes online.

    Args:
        handle(ImcHandle)
        timeout(int)
        interval(int)

    Returns:
        ComputeRackUnit object

    Example:
        power_up_server(handle)
    """

    from imcsdk.mometa.compute.ComputeRackUnit import ComputeRackUnit,\
        ComputeRackUnitConsts

    # Turn power on only if not already powered up
    if get_server_power_state(handle) != "on":
        rack_mo = ComputeRackUnit(parent_mo_or_dn="sys", server_id="1")
        rack_mo.admin_power = ComputeRackUnitConsts.ADMIN_POWER_UP
        handle.set_mo(rack_mo)

    # Poll until the server is powered up
    _wait_for_power_state(handle, "on", timeout=timeout, interval=interval)

    # Return object with current state
    return handle.query_dn("sys/rack-unit-1")


def power_down_server(handle, timeout=60, interval=5):
    """
    This method will power down the rack server, even if tasks are still
    running on it.  Then polls the server every $interval until either $timeout
    or it comes online.

    Args:
        handle(ImcHandle)
        timeout(int)
        interval(int)

    Returns:
        ComputeRackUnit object

    Example:
        power_down_server(handle)
    """

    from imcsdk.mometa.compute.ComputeRackUnit import ComputeRackUnit,\
        ComputeRackUnitConsts

    # Turn power off only if not already powered down
    if get_server_power_state(handle) != "off":
        rack_mo = ComputeRackUnit(parent_mo_or_dn="sys", server_id="1")
        rack_mo.admin_power = ComputeRackUnitConsts.ADMIN_POWER_DOWN
        handle.set_mo(rack_mo)

    # Poll until the server is powered up
    _wait_for_power_state(handle, "off", timeout=timeout, interval=interval)

    return handle.query_dn("sys/rack-unit-1")


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

    # Gracefully power off only if not already powered down
    if get_server_power_state(handle) != "off":
        rack_mo = ComputeRackUnit(parent_mo_or_dn="sys", server_id="1")
        rack_mo.admin_power = ComputeRackUnitConsts.ADMIN_POWER_SOFT_SHUT_DOWN
        handle.set_mo(rack_mo)

    # Poll until the server is powered up
    _wait_for_power_state(handle, "off", timeout=60, interval=5)

    return handle.query_dn("sys/rack-unit-1")


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

    # Poll until the server is powered up
    _wait_for_power_state(handle, "on", timeout=60, interval=5)

    return handle.query_dn("sys/rack-unit-1")


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

    from imcsdk.mometa.equipment.EquipmentLocatorLed \
        import EquipmentLocatorLed, EquipmentLocatorLedConsts

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

    from imcsdk.mometa.equipment.EquipmentLocatorLed \
        import EquipmentLocatorLed, EquipmentLocatorLedConsts

    led_mo = EquipmentLocatorLed(parent_mo_or_dn="sys/rack-unit-1")
    led_mo.admin_state = EquipmentLocatorLedConsts.ADMIN_STATE_OFF
    handle.set_mo(led_mo)
