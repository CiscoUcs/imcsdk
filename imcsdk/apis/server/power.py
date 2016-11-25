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

import logging
log = logging.getLogger('imc')

# This list is currently maintained manually.
# Ideally all such config/capabilites should come from a capability file
supported_models = ['UCSC-C220-M4', 'UCSC-C240-M4', 'UCSC-C3X60-M4']


def is_supported_model(handle):
    for model in supported_models:
        if handle.model.find(model) != -1:
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


def get_power_budget(handle, server_id=1):
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
    server_dn = get_server_dn(handle, server_id)
    power_budget_mo = handle.query_children(in_dn=server_dn,
                                            class_id="PowerBudget")
    if not power_budget_mo:
        raise ImcOperationError("Get Power Budget",
                                "Invalid Server Id configured")

    return power_budget_mo[0]


def set_power_characterization(handle, run_at_boot="yes", server_id=1):
    """
    This api sets the property
    Args:
        handle (ImcHandle)
        run_at_boot (string) : "yes", "no"
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        PowerBudget object
    """

    from imcsdk.mometa.power.PowerBudget import PowerBudget, PowerBudgetConsts
    if not is_supported_model(handle):
        return
    server_dn = get_server_dn(handle, server_id)
    power_budget_mo = PowerBudget(parent_mo_or_dn=server_dn)
    power_budget_mo.admin_action = \
            PowerBudgetConsts.ADMIN_ACTION_START_POWER_CHAR
    power_budget_mo.admin_state = "enabled"
    handle.set_mo(power_budget_mo)
    return power_budget_mo


def set_standard_power_cap(handle, throttle="no", power_limit=0,
                           correction_time=3, corrective_action="alert",
                           hard_cap="no", server_id=1):
    """
    This method sets up the standard power cap configuration profile

    Args:
        handle (ImcHandle)
        throttle (string): "yes", "no"
        power_limit (int): Power limit in Watts. Range (157-300) W
        correction_time (int): Time in seconds before power_limit is enforced
            and corrective action is taken. Range (1-600)s
        corrective_action (string): "none","alert","shutdown","alert,shutdown"
        hard_cap (string): "yes", "no"
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        StandardPowerProfile object

    Examples:
        set_standard_power_cap(handle,
                               correction_time=5,
                               corrective_action="alert")
        set_standard_power_cap(handle, throttle=True,
                               power_limit=200, correction_time=5,
                               corrective_action="alert, shutdown")
    """

    from imcsdk.mometa.standard.StandardPowerProfile import StandardPowerProfile
    if not is_supported_model(handle):
        return
    server_dn = get_server_dn(handle, server_id)
    power_budget_dn = server_dn + "/budget"
    stdpowerprof_mo = StandardPowerProfile(
        parent_mo_or_dn=power_budget_dn)

    stdpowerprof_mo.allow_throttle = throttle
    stdpowerprof_mo.power_limit = str(power_limit)
    stdpowerprof_mo.corr_time = str(correction_time)
    stdpowerprof_mo.corr_action = corrective_action
    stdpowerprof_mo.profile_enabled = "yes"
    stdpowerprof_mo.hard_cap = hard_cap

    handle.set_mo(stdpowerprof_mo)
    return stdpowerprof_mo


def disable_standard_cap(handle, server_id=1):
    """
    This method disables the standard power profile

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        None
    """

    from imcsdk.mometa.standard.StandardPowerProfile import StandardPowerProfile
    if not is_supported_model(handle):
        return
    server_dn = get_server_dn(handle, server_id)
    power_budget_dn = server_dn + "/budget"
    stdpowerprof_mo = StandardPowerProfile(
        parent_mo_or_dn=power_budget_dn)

    stdpowerprof_mo.profile_enabled = "no"
    handle.set_mo(stdpowerprof_mo)
