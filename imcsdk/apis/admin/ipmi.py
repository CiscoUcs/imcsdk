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
from imcsdk.mometa.comm.CommIpmiLan import CommIpmiLan, CommIpmiLanConsts
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


def ipmi_enable(handle, priv=CommIpmiLanConsts.PRIV_ADMIN,
                key='0'*40, server_id=1):
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

    # Verify key is a hex number
    try:
        hex(int(key, 16))[2:]
    except ValueError:
        raise ValueError('{0}: ERROR: Encryption key is not hex number: ' +
                         '"{1}"'.format(handle.ip, key))

    # Create enabled IPMI object
    ipmi_mo = CommIpmiLan(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    ipmi_mo.admin_state = "enabled"
    ipmi_mo.priv = priv
    ipmi_mo.key = key

    # Configure IPMI object on CIMC
    handle.set_mo(ipmi_mo)
    return handle.query_dn(ipmi_mo.dn)


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
    ipmi_mo = CommIpmiLan(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    ipmi_mo.admin_state = "disabled"

    # Configure IPMI object on CIMC
    handle.set_mo(ipmi_mo)
    return handle.query_dn(ipmi_mo.dn)


def is_ipmi_enabled(handle, server_id=1, **kwargs):
    """
    Check if IPMI over LAN is enabled
    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        True if enabled, else False
    """

    mo = CommIpmiLan(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    mo = handle.query_dn(mo.dn)

    kwargs['admin_state'] = "enabled"
    mo_exists = mo.check_prop_match(**kwargs)
    return (mo_exists, mo if mo_exists else None)
