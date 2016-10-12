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


def enable_ipmi(handle, priv=CommIpmiLanConsts.PRIV_ADMIN, key='0'*40):
    """
    Enable IPMI over LAN.

    Args:
        handle (ImcHandle)
        priv (string): Optional privilege level: 'admin', 'user', 'read-only'
        key (string): Optional encryption key as hexadecimal string

    Returns:
        True

    Raises:
        ValueError if privilege or key are invalid

    Example:
        if enable_ipmi(handle):
            print "IPMI Enabled"
    """
    # Verify priv string is valid privilege level
    if priv is not CommIpmiLanConsts.PRIV_ADMIN and \
       priv is not CommIpmiLanConsts.PRIV_USER and \
       priv is not CommIpmiLanConsts.PRIV_READ_ONLY:
        raise ValueError('{0}: ERROR: invalid privilege level: ' +
                         '"{1}"'.format(handle.ip, priv))

    # Verify key is a hex number
    try:
        hex(int(key, 16))[2:]
    except ValueError:
        raise ValueError('{0}: ERROR: Encryption key is not hex number: ' +
                         '"{1}"'.format(handle.ip, key))

    # Create enabled IPMI object
    ipmi_mo = CommIpmiLan(parent_mo_or_dn="sys/svc-ext",
                          admin_state="enabled", priv=priv, key=key)

    # Configure IPMI object on CIMC
    handle.set_mo(ipmi_mo)
    return True


def disable_ipmi(handle):
    """
    Disable IPMI over LAN.
    Args:
        handle (ImcHandle)

    Returns:
        True

    """
    # Create disabled IPMI object
    ipmi_mo = CommIpmiLan(parent_mo_or_dn="sys/svc-ext",
                          admin_state="disabled")
    # Configure IPMI object on CIMC
    handle.set_mo(ipmi_mo)
    return True
