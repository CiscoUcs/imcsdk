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
This module implements apis to setup redfish support
"""

import logging
from imcsdk.mometa.comm.CommRedfish import CommRedfish, CommRedfishConsts

log = logging.getLogger('imc')


def redfish_enable(handle):
    """
    This method will enable redfish support

    Args:
        handle (ImcHandle)
        enable (bool)

    Returns:
        CommRedfish object
    """

    mo = CommRedfish(parent_mo_or_dn="sys/svc-ext")
    mo.admin_state = CommRedfishConsts.ADMIN_STATE_ENABLED
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def redfish_disable(handle):
    """
    This method will disable redfish support

    Args:
        handle (ImcHandle)
        enable (bool)

    Returns:
        CommRedfish object
    """

    mo = CommRedfish(parent_mo_or_dn="sys/svc-ext")
    mo.admin_state = CommRedfishConsts.ADMIN_STATE_DISABLED
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def is_redfish_enabled(handle):
    """
    This method will check if redfish support is enabled

    Args:
        handle(ImcHandle)

    Returns:
        True if enabled, else False
    """

    mos = handle.query_classid("CommRedfish")
    return (mos[0].admin_state == CommRedfishConsts.ADMIN_STATE_ENABLED)
