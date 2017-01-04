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
from imcsdk.mometa.comm.CommNtpProvider import CommNtpProvider
from imcsdk.imccoreutils import _is_valid_arg
from imcsdk.imcexception import ImcOperationError


def _get_ntp_mo(handle):

    mo = _create_ntp_mo()
    if handle is None:
        raise ImcOperationError("Get NTP Settings", "Handle is None")

    mo = handle.query_dn(mo.dn)
    if mo is None:
        raise ImcOperationError("Get NTP Settings", "MO doesn't exist")
    return mo


def _create_ntp_mo():
    return CommNtpProvider(parent_mo_or_dn="sys/svc-ext")


def _set_ntp_servers(mo, ntp_servers):
    if len(ntp_servers) > 4:
        raise ImcOperationError("Set NTP Servers",
                                "Cannot specify more than 4 servers")
    args = {"ntp_server" + str(x["id"]): x["ip"] for x in ntp_servers}
    mo.set_prop_multiple(**args)


def ntp_enable(handle, ntp_servers=[]):
    """
    Enable NTP

    Args:
        handle (ImcHandle)
        ntp_servers (list): List of dictionaries of the type
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

    mo = _create_ntp_mo()
    mo.ntp_enable = "yes"

    _set_ntp_servers(mo, ntp_servers)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def ntp_disable(handle):
    """
    Disable NTP
    Args:
        handle (ImcHandle)

    Returns:
        CommNtpProvider object
    """

    mo = _create_ntp_mo()
    mo.ntp_enable = "no"

    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def ntp_servers_modify(handle, ntp_servers=[]):
    """
    Modify the configured NTP servers
    Args:
        handle (ImcHandle)
        ntp_servers (list): List of dictionaries of the type
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
    mo = _get_ntp_mo(handle)
    mo.ntp_enable = mo.ntp_enable
    _set_ntp_servers(mo, ntp_servers)

    handle.set_mo(mo)
    return mo


def is_ntp_enabled(handle):
    """
    Check if NTP is enabled
    Args:
        handle (ImcHandle)

    Returns:
        bool
    """

    mo = _get_ntp_mo(handle)
    return (mo.ntp_enable.lower() in ["true", "yes"])


def _is_invalid_value(value):
    return value in ["", None]


def _check_ntp_server_match(ntp_mo, mo):
    for prop in ["ntp_server1", "ntp_server2",
                 "ntp_server3", "ntp_server4"]:
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

    ntp_mo = _get_ntp_mo(handle)

    if _is_valid_arg("ntp_enable", kwargs):
        if ntp_mo.ntp_enable != kwargs.get("ntp_enable"):
            return False, None

    if _is_valid_arg("ntp_servers", kwargs):
        mo = _create_ntp_mo()
        _set_ntp_servers(mo, kwargs.get("ntp_servers"))
        if not _check_ntp_server_match(ntp_mo, mo):
            return False, None

    return True, ntp_mo
