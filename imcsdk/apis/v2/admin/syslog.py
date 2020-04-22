# Copyright 2017 Cisco Systems, Inc.
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
This module performs the operations related to system logs
"""

from imcsdk.imcexception import ImcOperationError
from imcsdk.mometa.comm.CommSyslogClient import CommSyslogClientConsts

SYSLOG_DN = 'sys/svc-ext/syslog'

def syslog_get(handle, caller="syslog_get"):
    """
    Gets syslog.

    Args:
        handle (ImcHandle)
        caller (string): name of the calling function

    Returns:
        CommSyslog: Managed object

    Raises:
        ImcOperationError

    Example:
        mo = syslog_get(handle)
    """
    mo = handle.query_dn(dn=SYSLOG_DN)
    if mo is None:
        raise ImcOperationError(caller, "syslog '%s' does not exist" %
                                SYSLOG_DN)
    return mo


def syslog_configure(handle,
                     local_severity=None,
                     remote_severity=None,
                     **kwargs):
    """
    Configures syslog.

    Args:
        handle (ImcHandle)
        local_severity (string): local minimmum severity to report
         valid values are "alert", "critical", "debug", "emergency", "error",
          "informational", "notice", "warning"
        remote_severity (string): remote minimmum severity to report
         valid values are "alert", "critical", "debug", "emergency", "error",
          "informational", "notice", "warning"
        kwargs: key-value paired arguments for future use

    Returns:
        CommSyslog: Managed object

    Raises:
        ImcOperationError

    Example:
        mo = syslog_configure(handle, local_severity="notice")
    """
    mo = syslog_get(handle)

    params = {
        'local_severity': local_severity,
        'remote_severity': remote_severity
        }

    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return mo


def syslog_exists(handle, **kwargs):
    """
    checks if syslog exists

    Args:
        handle (ImcHandle)
        kwargs: Key-Value paired arguments relevant to CommSyslog object

    Returns:
        True, CommSyslog  MO if found, else False, None

    Example:
        syslog_exists(handle, local_severity="debug")
    """
    try:
        mo = syslog_get(handle)
    except ImcOperationError:
        return (False, None)
    mo_exists = mo.check_prop_match(**kwargs)
    return (mo_exists, mo if mo_exists else None)


def syslog_remote_get(handle, name, caller="syslog_remote_get"):
    """
    Gets syslog for remote client

    Args:
        handle (ImcHandle)
        caller (string): name of the calling function

    Returns:
        CommSyslog: Managed object

    Raises:
        ImcOperationError

    Example:
        mo = syslog_remote_get(handle, name="primary", caller="myfunc")
    """
    dn = SYSLOG_DN + "/client-" + name
    mo = handle.query_dn(dn=dn)
    if mo is None:
        raise ImcOperationError(caller,
                                "syslog remote client '%s' does not exist" %
                                dn)
    return mo


def syslog_remote_enable(handle, hostname, name, port="514",
                         **kwargs):
    """
    Enables Syslog on Remote Client.

    Args:
        handle (ImcHandle)
        hostname (string): ip address of remote host
        name (string): "primary", "secondary"
        port(string): port
        kwargs: key-value paired arguments for future use

    Returns:
        CommSyslogClient: Managed object

    Raises:
        ImcOperationError: If CommSyslogClient Mo is not present

    Example:
        mo = syslog_remote_enable(handle, hostname="10.10.10.10",
                                  name="primary")
    """

    mo = syslog_remote_get(handle, name, caller="syslog_remote_enable")

    params = {
        'admin_state': CommSyslogClientConsts.ADMIN_STATE_ENABLED,
        'hostname': hostname,
        'port': port
    }
    mo.set_prop_multiple(**params)
    kwargs.pop('state', None)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return mo


def syslog_remote_disable(handle, name, **kwargs):
    """
    Disables System log on Remote Client.

    Args:
        handle (ImcHandle)

    Returns:
        CommSyslogClient: Managed Object

    Raises:
        ImcOperationError: If CommSyslogClient Mo is not present

    Example:
        syslog_remote_disable(handle, name)
    """

    mo = syslog_remote_get(handle, name)
    mo.admin_state = CommSyslogClientConsts.ADMIN_STATE_DISABLED
    kwargs.pop('state', None)
    if 'hostname' in kwargs:
        if not kwargs['hostname'] or kwargs['hostname'] == "0.0.0.0" :
            kwargs.pop('hostname')
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return mo


def is_syslog_remote_enabled(handle, name, **kwargs):
    """
    Checks if system log is enabled or not on remote server

    Args:
        handle (ImcHandle)
        name (string): "primary", "secondary", "tertiary"
        kwargs: Key-Value paired arguments relevant to CommSyslogClient object

    Returns:
        True, CommSyslogClient MO if found, else False, None

    Example:
        is_syslog_remote_enabled(handle, name)
    """

    try:
        mo = syslog_remote_get(handle, name)
    except ImcOperationError:
        return (False, None)

    kwargs['admin_state'] = CommSyslogClientConsts.ADMIN_STATE_ENABLED

    mo_exists = mo.check_prop_match(**kwargs)
    return (mo_exists, mo if mo_exists else None)


def is_syslog_remote_clear(handle, name):
    """
    Checks if configuration of remote system log is at default

    Args:
        handle (ImcHandle)

    Returns:
        True/False, CommSyslogClient MO, None

    Raises:
        ImcOperationError: If CommSyslogClient Mo is not present

    Example:
        issyslog_remote_clear(handle, name)
    """

    try:
        mo = syslog_remote_get(handle, name)
    except ImcOperationError:
        return (False, None)

    kwargs = {
        'admin_state': CommSyslogClientConsts.ADMIN_STATE_DISABLED,
        'hostname': '0.0.0.0',
        'port': '514'
    }

    mo_exists = mo.check_prop_match(**kwargs)
    return (mo_exists, mo if mo_exists else None)


def syslog_remote_clear(handle, name):
    """
    Clears System log on Remote Client.

    Args:
        handle (ImcHandle)

    Returns:
        CommSyslogClient: Managed Object

    Raises:
        ImcOperationError: If CommSyslogClient Mo is not present

    Example:
        syslog_remote_clear(handle, name)
    """

    mo = syslog_remote_get(handle, name)
    mo.admin_action = CommSyslogClientConsts.ADMIN_ACTION_CLEAR
    handle.set_mo(mo)
    return mo


def syslog_remote_exists(handle, name, **kwargs):
    """
    checks if syslog remote client exists

    Args:
        handle (ImcHandle)
        kwargs: Key-Value paired arguments relevant to CommSyslogClient object

    Returns:
        True, CommSyslogClient  MO if found, else False, None

    Example:
        syslog_remote_exists(handle, name)
    """

    try:
        mo = syslog_remote_get(handle, name)
    except ImcOperationError:
        return (False, None)
    admin_state = kwargs.pop('state', None)
    if admin_state == 'present':
        kwargs['admin_state'] = CommSyslogClientConsts.ADMIN_STATE_ENABLED
    elif admin_state == 'absent':
        kwargs['admin_state'] = CommSyslogClientConsts.ADMIN_STATE_DISABLED
    mo_exists = mo.check_prop_match(**kwargs)
    return (mo_exists, mo)


