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
This module performs the operation related to admin power of Rack unit.
"""


def admin_power_state_status(handle):
    """
    Checks for Current Power State of rack unit

    Args:
        handle (ImcHandle)

    Returns:
        admin_power of rack unit.

    Example:
        current_power_state(handle)
    """

    rack_mo = handle.query_dn("sys/rack-unit-1")
    return rack_mo.admin_power


def admin_power_state_up(handle):
    """
    Sets Admin Power State to Up

    Args:
        handle (ImcHandle)

    Returns:
        None

    Example:
        admin_power_state_up(handle)
    """

    from imcsdk.mometa.compute.ComputeRackUnit import ComputeRackUnit, \
        ComputeRackUnitConsts

    rack_mo = ComputeRackUnit(parent_mo_or_dn="sys", server_id="1",
                              admin_power=ComputeRackUnitConsts.ADMIN_POWER_UP)
    handle.set_mo(rack_mo)


def admin_power_state_down(handle):
    """
    Sets Admin Power State to Down

    Args:
        handle (ImcHandle)

    Returns:
        None

    Example:
        admin_power_state_down(handle)
    """

    from imcsdk.mometa.compute.ComputeRackUnit import ComputeRackUnit, \
        ComputeRackUnitConsts

    rack_mo = ComputeRackUnit(parent_mo_or_dn="sys", server_id="1",
                              admin_power=
                              ComputeRackUnitConsts.ADMIN_POWER_DOWN)
    handle.set_mo(rack_mo)
