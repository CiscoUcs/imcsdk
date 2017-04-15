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
This module performs the operations related to snmp server, user and traps.
"""

from imcsdk.imcexception import ImcOperationError
from imcsdk.apis.utils import _get_mo

SNMP_DN = 'sys/svc-ext/snmp-svc'


def snmp_enable(handle, community=None,
                privilege="disabled", trap_community=None,
                sys_contact=None, sys_location=None, port="161", **kwargs):
    """
    Enables SNMP.

    Args:
        handle (ImcHandle)
        community (string): community
        privilege (string): "disabled", "limited", "full"
        trap_community(string): community to be used when generating traps
        sys_contact (string): sys_contact
        sys_location (string): sys_location
        port (string): port on which SNMP agent runs
        kwargs: key-value paired arguments for future use

    Returns:
        CommSnmp: Managed object

    Raises:
        ImcOperationError: If CommSnmp Mo is not present

    Example:
        mo = snmp_enable(handle,
                    community="username",
                    sys_contact="user contact",
                    sys_location="user location")
    """

    from imcsdk.mometa.comm.CommSnmp import CommSnmpConsts

    mo = _get_mo(handle, dn=SNMP_DN)

    params = {
        'admin_state': CommSnmpConsts.ADMIN_STATE_ENABLED,
        'community': community,
        'com2_sec': privilege,
        'trap_community': trap_community,
        'sys_contact': sys_contact,
        'sys_location': sys_location,
        'port': port,
        }

    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def snmp_disable(handle):
    """
    Disables SNMP.

    Args:
        handle (ImcHandle)

    Returns:
        CommSnmp: Managed Object

    Raises:
        ValueError: If CommSnmp Mo is not present

    Example:
        snmp_disable(handle)
    """

    from imcsdk.mometa.comm.CommSnmp import CommSnmpConsts

    mo = _get_mo(handle, dn=SNMP_DN)

    mo.admin_state = CommSnmpConsts.ADMIN_STATE_DISABLED
    handle.set_mo(mo)
    return mo


def is_snmp_enabled(handle, **kwargs):
    """
    Checks if snmp is enabled or not

    Args:
        handle (ImcHandle)
        kwargs: Key-Value paired arguments relevant to CommSnmp object

    Returns:
        True/false, CommSnmp MO/None

    Example:
        is_snmp_enabled(handle)
    """
    from imcsdk.mometa.comm.CommSnmp import CommSnmpConsts

    mo = _get_mo(handle, dn=SNMP_DN)

    kwargs['admin_state'] = CommSnmpConsts.ADMIN_STATE_ENABLED

    mo_exists = mo.check_prop_match(**kwargs)
    return (mo_exists, mo if mo_exists else None)



def _get_free_snmp_trap_obj(handle):

    from imcsdk.mometa.comm.CommSnmpTrap import CommSnmpTrapConsts
    traps = handle.query_children(in_dn=SNMP_DN,
                                  class_id="CommSnmpTrap")
    for trap in traps:
        if trap.admin_state == CommSnmpTrapConsts.ADMIN_STATE_DISABLED:
            return trap

    return None


def snmp_trap_add(handle, hostname, port, version="v3",
                  notification_type="traps", user=None,
                  **kwargs):
    """
    Adds snmp trap.

    Args:
        handle (ImcHandle)
        hostname (string): ip address
        port (string): port
        version (string): "v2c", "v3"
        notification_type (string): "informs", "traps"
            Required only for version "v2c" and "v3"
        user (string): send traps for a specific user
        kwargs: Key-Value paired arguments for future use

    Returns:
        CommSnmpTrap: Managed Object

    Raises:
        ImcOperationError if all traps are configured

    Example:
        snmp_trap_add(handle, hostname="10.10.10.10",
                      port="162",
                      version="v2c",
                      notification_type="informs")
    """

    from imcsdk.mometa.comm.CommSnmpTrap import CommSnmpTrapConsts

    mo = _get_free_snmp_trap_obj(handle)

    if mo is None:
        raise ImcOperationError("Snmp Trap Add",
                                "No free traps available to configure")

    params = {
        'admin_state': CommSnmpTrapConsts.ADMIN_STATE_ENABLED,
        'hostname': hostname,
        'port': port,
        'version': version,
        'notification_type': notification_type,
        }

    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)

    if version != "v2c":
        mo.user = user

    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def snmp_trap_exists(handle, **kwargs):
    """
    checks if snmp trap exists

    Args:
        handle (ImcHandle)
        kwargs: Key-Value paired arguments relevant to CommSnmpTrap object

    Returns:
        True, CommSnmpTrap MO if found, else False, None

    Example:
        snmp_trap_exists(handle, hostname="10.10.10.10",
                      port="162",
                      version="v2c",
                      notification_type="informs",
                      user="username")

    """

    traps = handle.query_children(in_dn=SNMP_DN,
                                  class_id="CommSnmpTrap")

    for trap in traps:
        if trap.check_prop_match(**kwargs):
            return True, trap

    return False, None


def snmp_trap_modify(handle, trap_id, **kwargs):
    """
    Modifies snmp trap referred to by id

    Args:
        handle (ImcHandle)
        trap_id (int) : Range is (1,15)
        kwargs : Key-Value paired arguments relevant to CommSnmpTrap object

    Returns:
        CommSnmpTrap: Managed Object

    Raises:
        ImcOperationError if trap not found

    Example:
        snmp_trap_modify(handle, id="5", hostname="10.10.10.10",
                          port="162",
                          version="v3",
                          notification_type="traps",
                          user="username")
    """

    dn = SNMP_DN + '/snmp-trap-' + str(trap_id)
    mo = _get_mo(handle, dn=dn)

    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def snmp_trap_remove(handle, trap_id):
    """
    Modifies snmp trap.

    Args:
        handle (ImcHandle)
        trap_id (int): Trap id

    Returns:
        None

    Raises:
        ImcOperationError if trap not found

    Example:
        snmp_trap_remove(handle, trap_id=6)
    """

    from imcsdk.mometa.comm.CommSnmpTrap import CommSnmpTrapConsts

    dn = SNMP_DN + '/snmp-trap-' + str(trap_id)
    mo = _get_mo(handle, dn=dn)

    mo.admin_state = CommSnmpTrapConsts.ADMIN_STATE_DISABLED
    mo.admin_action = CommSnmpTrapConsts.ADMIN_ACTION_CLEAR
    handle.set_mo(mo)


def _get_free_snmp_user(handle):
    users = handle.query_children(in_dn=SNMP_DN,
                                  class_id="CommSnmpUser")
    for user in users:
        if user.name == "":
            return user

    raise ImcOperationError("Snmp User Add",
                            "Maximum number of users already configured")


def snmp_user_add(handle, name, security_level="authpriv",
                  auth_pwd=None, auth="MD5",
                  privacy_pwd=None, privacy="AES", **kwargs):
    """
    Adds snmp user.

    Args:
        handle (ImcHandle)
        name (string): snmp username
        security_level (string): "authpriv", "authnopriv", "noauthnopriv"
        auth_pwd (string): password
        auth (string): "MD5", "SHA"
        privacy_pwd (string): privacy password
        privacy (string): "AES", "DES"

    Returns:
        CommSnmpUser: Managed Object

    Raises:
        ImcOperationError is maximum number of users already configured

    Example:
        snmp_user_add(handle, name="snmpuser",
            security_level="authpriv", auth_pwd="abcd",
            auth="MD5", privacy_pwd="xyz", privacy="DES")
    """

    from imcsdk.mometa.comm.CommSnmpUser import CommSnmpUserConsts

    mo = _get_free_snmp_user(handle)

    params = {
        'name': name,
        'security_level': security_level
        }
    mo.set_prop_multiple(**params)
    params = {}
    if security_level == CommSnmpUserConsts.SECURITY_LEVEL_AUTHNOPRIV:
        params = {
            'auth': auth,
            'auth_pwd': auth_pwd
            }

    if security_level == CommSnmpUserConsts.SECURITY_LEVEL_AUTHPRIV:
        params = {
            'auth': auth,
            'auth_pwd': auth_pwd,
            'privacy': privacy,
            'privacy_pwd': privacy_pwd
            }

    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def snmp_user_get(handle, name):
    """
    Gets the snmp user

    Args:
        handle (ImcHandle)
        name (str): snmp username

    Returns:
        CommSnmpUser object

    Examples:
        user = snmp_user_get(handle, name = "snmp-user")
    """
    users = handle.query_children(in_dn=SNMP_DN,
                                  class_id="CommSnmpUser")
    for user in users:
        if user.name == name:
            return user

    return None


def snmp_user_exists(handle, name, **kwargs):
    """
    checks if snmp user exists.

    Args:
        handle (ImcHandle)
        name (string): snmp username

    Returns:
        True, CommSnmpUser MO if found, else False, None

    Example:
        snmp_user_exists(handle, name="snmpuser")
    """
    kwargs.pop('auth_pwd', None)
    kwargs.pop('privacy_pwd', None)

    user = snmp_user_get(handle, name=name)
    if user and user.check_prop_match(**kwargs):
        return (True, user)
    return (False, None)


def snmp_user_modify(handle, user_id, **kwargs):
    """
    Modifies snmp user. Use this after getting the id from snmp_user_exists

    Args:
        handle (ImcHandle)
        user_id (int) : unique id for the user
        kwargs: Key-Value paired arguments relevant to CommSnmpUser object

    Returns:
        CommSnmpUser: Managed Object

    Raises:
        ImcOperationError: If user is not present

    Example:
        snmp_user_modify(handle, user_id=1, name="snmpuser",
                         security_level="authpriv", auth_pwd="password",
                         auth="MD5", privacy="AES", privacy_pwd="password")
    """

    dn = SNMP_DN + "/snmpv3-user-" + str(user_id)
    mo = _get_mo(handle, dn=dn)

    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def snmp_user_remove(handle, name):
    """
    removes snmp user.

    Args:
        handle (ImcHandle)
        name (string): snmp username

    Returns:
        None

    Raises:
        ImcOperationError: If user is not present

    Example:
        snmp_user_remove(handle, name="snmpuser")

    """

    from imcsdk.mometa.comm.CommSnmpUser import CommSnmpUserConsts

    found_user = snmp_user_get(handle, name=name)
    if found_user is None:
        raise ImcOperationError("Snmp User Delete", "User does not exist")

    found_user.name = ""
    found_user.admin_action = CommSnmpUserConsts.ADMIN_ACTION_CLEAR
    handle.set_mo(found_user)
