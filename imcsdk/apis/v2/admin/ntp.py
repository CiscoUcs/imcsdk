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
This module implements all the ntp related functionality
"""

from imcsdk.imcexception import ImcOperationError
from imcsdk.apis.v2.utils import _get_mo, _is_invalid_value, _is_valid_arg

import logging

log = logging.getLogger('imc')

COMM_EXT_DN = "sys/svc-ext"
NTP_DN = "sys/svc-ext/ntp-svc"
_NTP_SERVER_LIST = ["ntp_server1", "ntp_server2", "ntp_server3", "ntp_server4"]


def _get_ntp_servers(ntp_servers):
    return {"ntp_server" + str(x["id"]): x["ip"] for x in ntp_servers}


def _set_ntp_servers(mo, ntp_servers):
    if len(ntp_servers) > len(_NTP_SERVER_LIST):
        raise ImcOperationError("Set NTP Servers",
                                "Cannot specify more than %d servers"
                                % len(_NTP_SERVER_LIST))
    args = _get_ntp_servers(ntp_servers)
    mo.set_prop_multiple(**args)


def ntp_enable(handle, ntp_servers=[]):
    """
    Enables NTP and configures the NTP servers provided

    Args:
        handle (ImcHandle)
        ntp_servers (list): List of dictionaries in the format
                            [{"id": 1, "ip": "192.168.1.1"},
                             {"id": 2, "ip": "192.168.1.2"}]
                            Upto 4 ntp servers can be specified.

    Returns:
        CommNtpProvider object

    Example:
        ntp_enable(handle,
                   ntp_servers = [{"id": 1, "ip": "192.168.1.1"},
                                  {"id": 2, "ip": "192.168.1.2"}]
    """

    log.warning('IPMI Set SEL Time command will disable if NTP is enabled.')
    mo = _get_mo(handle, dn=NTP_DN)
    mo.ntp_enable = "yes"

    _set_ntp_servers(mo, ntp_servers)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def ntp_disable(handle):
    """
    Disables NTP
    Args:
        handle (ImcHandle)

    Returns:
        CommNtpProvider object
    """

    log.warning(
        'Disabling NTP may cause Cisco IMC to lose timesync with server/s')
    mo = _get_mo(handle, dn=NTP_DN)
    mo.ntp_enable = "no"

    handle.set_mo(mo)
    return mo


def ntp_servers_clear(handle, ntp_servers=[]):
    """
    Clears the NTP servers provided in the arguments.
    Clears all the NTP servers, only if ntp is disabled.

    Args:
        handle (ImcHandle)
        ntp_servers (list): List of NTP servers in the format
                            ["192.168.1.1", "192.168.1.2"]

    Returns:
        CommNtpProvider object
    """

    mo = _get_mo(handle, dn=NTP_DN)
    args = {}

    if ntp_servers:
        args = {x: "" for x in _NTP_SERVER_LIST
                if getattr(mo, x) in ntp_servers}
    else:
        args = {x: "" for x in _NTP_SERVER_LIST}

    if mo.ntp_enable.lower() in ["yes", "true"] and \
            len(args) == len(_NTP_SERVER_LIST):
        raise ImcOperationError(
            "Clear NTP Servers",
            "Cannot clear all NTP servers when NTP is enabled")

    mo.set_prop_multiple(**args)
    mo.ntp_enable = mo.ntp_enable
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def ntp_servers_modify(handle, ntp_servers=[]):
    """
    Modifies the configured NTP servers
    Args:
        handle (ImcHandle)
        ntp_servers (list): List of dictionaries in the format
                            [{"id": 1, "ip": "192.168.1.1"},
                             {"id": 2, "ip": "192.168.1.2"}]
                            Upto 4 ntp servers can be specified.

    Returns:
        CommNtpProvider object

    Example:
        ntp_servers_modify(handle,
                           ntp_servers = [{"id": 1, "ip": "192.168.1.1"},
                                          {"id": 2, "ip": "192.168.1.2"},
                                          {"id": 3, "ip": ""}]
    """

    # While sending the modified list of servers, it is imperative to send
    # ntp_enable property in the request.
    # Hence, query the MO and reassign the same value to ntp_enable
    mo = _get_mo(handle, dn=NTP_DN)
    mo.ntp_enable = mo.ntp_enable
    _set_ntp_servers(mo, ntp_servers)

    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def is_ntp_enabled(handle):
    """
    Check if NTP is enabled
    Args:
        handle (ImcHandle)

    Returns:
        bool
    """

    mo = _get_mo(handle, dn=NTP_DN)
    return (mo.ntp_enable.lower() in ["true", "yes"])


def _check_ntp_server_match(ntp_mo, mo):
    for prop in _NTP_SERVER_LIST:
        configured_value = getattr(ntp_mo, prop)
        in_value = getattr(mo, prop)

        if _is_invalid_value(configured_value) and \
                _is_invalid_value(in_value):
            continue
        if configured_value != in_value:
            return False

    return True


def ntp_setting_exists(handle, **kwargs):
    """
    Check if the specified NTP settings are already applied
    Args:
        handle (ImcHandle)
        kwargs: key-value paired arguments

    Returns:
        (True, CommNtpProvider) if settings match, (False, None) otherwise
    """

    mo = _get_mo(handle, dn=NTP_DN)
    if mo is None:
        return False, None

    kwargs['ntp_enable'] = "yes"

    if _is_valid_arg("ntp_servers", kwargs):
        args = _get_ntp_servers(kwargs['ntp_servers'])
        del kwargs['ntp_servers']
        kwargs.update(args)

    if not mo.check_prop_match(**kwargs):
        return False, mo

    return True, mo
