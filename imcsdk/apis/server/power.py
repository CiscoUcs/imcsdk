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
This module implements apis for power policy and power cap related config
"""

from imcsdk.imccoreutils import get_server_dn
from imcsdk.imcexception import ImcOperationError
from imcsdk.mometa.power.PowerBudget import PowerBudget, PowerBudgetConsts
from imcsdk.mometa.standard.StandardPowerProfile import StandardPowerProfile

import logging
log = logging.getLogger('imc')

# This list is currently maintained manually.
# Ideally all such config/capabilites should come from a capability file
supported_models = ['UCSC-C220-M4', 'UCSC-C240-M4', 'UCSC-C3K-M4']
supported_variants = ['M4', 'M5']


def is_supported_model(handle):
    for variant in supported_variants:
        if handle.model.find(variant) != -1:
            return True
    log.info("Current Model:'%s' does not support Power Cap and Budgeting" %
             handle.model)
    return False


def get_supported_models():
    """
    This api returns the list of rack server models that support power cap and
    power budgeting
    """
    return supported_models


def server_power_budget_get(handle, server_id=1):
    """
    This api gets the min and max power limits for the platform, cpu and memory
        for this specific server

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        PowerBudget object
    """

    if not is_supported_model(handle):
        return

    power_budget_mo = handle.query_children(in_dn=get_server_dn(handle, server_id),
                                            class_id="PowerBudget")
    if not power_budget_mo:
        raise ImcOperationError("Get Power Budget",
                                "Invalid Server Id configured")

    return power_budget_mo[0]


def server_power_characterization_enable(handle, server_id=1):
    """
    Enables power characterization.

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        PowerBudget object
    """
    if not is_supported_model(handle):
        return
    power_budget_mo = PowerBudget(
        parent_mo_or_dn=get_server_dn(handle, server_id))
    power_budget_mo.pow_char_enable = "enabled"
    handle.set_mo(power_budget_mo)
    return power_budget_mo


def server_power_characterization_start(handle, server_id=1):
    """
    Starts a power characterization run.
    From 3.0(1c) onwards, server_power_characterization_enable needs to be
    explicitly done, before invoking this api.

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        PowerBudget object
    """
    if not is_supported_model(handle):
        return
    power_budget_mo = PowerBudget(parent_mo_or_dn=get_server_dn(handle, server_id))

    power_budget_mo.admin_action = \
        PowerBudgetConsts.ADMIN_ACTION_START_POWER_CHAR
    handle.set_mo(power_budget_mo)
    return power_budget_mo


def server_power_capping_enable(handle, server_id=1):
    """
    Enables power capping feature on the server.

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        PowerBudget object
    """

    if not is_supported_model(handle):
        return
    power_budget_mo = PowerBudget(parent_mo_or_dn=get_server_dn(handle, server_id))
    power_budget_mo.admin_state = "enabled"
    handle.set_mo(power_budget_mo)
    return power_budget_mo


def server_standard_power_cap_set(handle, power_limit, throttle=False,
                                  correction_time=3, corrective_action="alert",
                                  hard_cap=False, server_id=1):
    """
    This method sets up the standard power cap configuration profile

    Args:
        handle (ImcHandle)
        throttle (bool)
        power_limit (int): Power limit in Watts.
                           Range can be retrieved from min_power and max_power
                           fields of PowerBudget object
        correction_time (int): Time in seconds before power_limit is enforced
            and corrective action is taken. Range (1-600)s
        corrective_action (string): "none","alert","shutdown","alert,shutdown"
        hard_cap (bool): Enable hard power cap
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        StandardPowerProfile object

    Examples:
        server_standard_power_cap_set(handle,
                                      correction_time=5,
                                      corrective_action="alert")
        server_standard_power_cap_set(handle, throttle=True,
                               power_limit=200, correction_time=5,
                               corrective_action="alert, shutdown")
    """

    if not is_supported_model(handle):
        return

    power_budget_dn = get_server_dn(handle, server_id) + "/budget"
    stdpowerprof_mo = StandardPowerProfile(
        parent_mo_or_dn=power_budget_dn)

    params = {
        "allow_throttle": ("no", "yes")[throttle],
        "power_limit": str(power_limit),
        "corr_time": str(correction_time),
        "corr_action": corrective_action,
        "profile_enabled": "yes",
        "hard_cap": ("no", "yes")[hard_cap]
    }

    stdpowerprof_mo.set_prop_multiple(**params)
    handle.set_mo(stdpowerprof_mo)
    return stdpowerprof_mo


def server_standard_power_cap_disable(handle, server_id=1):
    """
    This method disables the standard power profile

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        None
    """

    if not is_supported_model(handle):
        return
    server_dn = get_server_dn(handle, server_id)
    power_budget_dn = server_dn + "/budget"
    stdpowerprof_mo = StandardPowerProfile(
        parent_mo_or_dn=power_budget_dn)

    stdpowerprof_mo.profile_enabled = "no"
    handle.set_mo(stdpowerprof_mo)
