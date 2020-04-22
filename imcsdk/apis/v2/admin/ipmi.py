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
This module implements all the communication services
"""
from imcsdk.mometa.comm.CommIpmiLan import CommIpmiLan
from imcsdk.imccoreutils import get_server_dn, IMC_PLATFORM


def _get_comm_mo_dn(handle, server_id=1):
    """
    Internal method to get the IPMI mo's parent_dn based \
            on the type of platform
    """
    from imcsdk.imcexception import ImcValidationException

    if handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        return("sys/svc-ext")
    elif handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        return(get_server_dn(handle, server_id) + "/svc-ext")
    else:
        raise ImcValidationException("Invalid platform detected:%s" %
                                     handle.platform)


def ipmi_enable(handle, priv=None, key=None, server_id=1):
    """
    Enable IPMI over LAN.

    Args:
        handle (ImcHandle)
        priv (string): Optional privilege level: 'admin', 'user', 'read-only'
        key (string): Optional encryption key as hexadecimal string
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        CommIpmiLan object

    Raises:
        ValueError if privilege or key are invalid

    Example:
        if ipmi_enable(handle):
            print("IPMI Enabled")
    """

    from imcsdk.imcexception import ImcOperationError
    # Enable policy if only user mode is ipmi
    mos = handle.query_classid(class_id="AaaUserPolicy")
    userPolicy = mos[0]

    if userPolicy.user_mode != None and userPolicy.user_mode == 'non-ipmi':
        raise ImcOperationError("Enable IPMI over LAN", 
                                "IPMI user mode is disabled on the endpoint.")

    # Verify key is a hex number
    try:
        if key:
            hex(int(key, 16))[2:]
    except ValueError:
        raise ValueError('{0}: ERROR: Encryption key is not hex number: ' +
                         '"{1}"'.format(handle.ip, key))

    # Create enabled IPMI object
    mo = CommIpmiLan(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    mo.admin_state = "enabled"
    mo.priv = priv
    mo.key = key

    # Configure IPMI object on CIMC
    handle.set_mo(mo)
    return mo


def ipmi_disable(handle, server_id=1):
    """
    Disable IPMI over LAN.
    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        CommIpmiLan object
    """

    # Create disabled IPMI object
    mo = CommIpmiLan(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    mo.admin_state = "disabled"

    # Configure IPMI object on CIMC
    handle.set_mo(mo)
    return mo


def ipmi_exists(handle, server_id=1, **kwargs):
    """
    Check if IPMI over LAN is enabled
    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        True/False, MO/None
    """

    mo = CommIpmiLan(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    mo = handle.query_dn(mo.dn)
    if mo is None:
        return False, None

    kwargs['admin_state'] = "enabled"
    mo_exists = mo.check_prop_match(**kwargs)
    return (mo_exists, mo)
