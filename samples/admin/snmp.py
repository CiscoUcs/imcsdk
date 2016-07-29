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


def snmp_enable(handle, community=None,
                privilege="disabled", trap_community=None,
                sys_contact=None, sys_location=None, port="161"):
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
    from imcsdk.imcexception import ImcOperationError

    dn = "sys/svc-ext/snmp-svc"
    mo = handle.query_dn(dn)
    if not mo:
        raise ImcOperationError("snmp enable", "snmp config does not exist")

    mo.admin_state = CommSnmpConsts.ADMIN_STATE_ENABLED

    if community:
        mo.community = community
    if privilege:
        mo.com2_sec = privilege
    if trap_community:
        mo.trap_community = trap_community
    if sys_contact:
        mo.sys_contact = sys_contact
    if sys_location:
        mo.sys_location = sys_location
    mo.port = port

    handle.set_mo(mo)
    return mo


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
    from imcsdk.imcexception import ImcOperationError

    dn = "sys/svc-ext/snmp-svc"
    mo = handle.query_dn(dn)
    if not mo:
        raise ImcOperationError("snmp enable", "snmp config does not exist")

    mo.admin_state = CommSnmpConsts.ADMIN_STATE_DISABLED
    handle.set_mo(mo)
    return mo


def snmp_enabled(handle):
    """
    This method checks if snmp is enabled or not
    Args:
        handle (ImcHandle)

    Returns:
        bool
    """
    from imcsdk.mometa.comm.CommSnmp import CommSnmpConsts
    from imcsdk.imcexception import ImcOperationError

    dn = "sys/svc-ext/snmp-svc"
    mo = handle.query_dn(dn)
    if not mo:
        raise ImcOperationError("snmp enable", "snmp config does not exist")

    return (mo.admin_state == CommSnmpConsts.ADMIN_STATE_ENABLED)


def _get_free_snmp_trap_obj(handle):
    """
    This is internally used by trap add to get a free, unconfigured trap object

    Args:
        handle (ImcHandle)

    Returns:
        CommSnmpTrap object
    """

    from imcsdk.mometa.comm.CommSnmpTrap import CommSnmpTrapConsts
    traps = handle.query_children(in_dn="sys/svc-ext/snmp-svc",
                                  class_id="CommSnmpTrap")
    for trap in traps:
        if trap.admin_state == CommSnmpTrapConsts.ADMIN_STATE_DISABLED:
            return trap

    return None


def snmp_trap_add(handle, hostname, port, version="v3",
                  notification_type="traps", user=None):
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
    from imcsdk.imcexception import ImcOperationError

    mo = _get_free_snmp_trap_obj(handle)

    if mo is None:
        raise ImcOperationError("Snmp Trap Add",
                                "No free traps available to configure")

    mo.admin_state = CommSnmpTrapConsts.ADMIN_STATE_ENABLED
    mo.hostname = hostname
    mo.port = port
    mo.version = version
    mo.notification_type = notification_type
    mo.user = user

    handle.set_mo(mo)
    return mo


def snmp_trap_exists(handle, hostname, port, version="v3",
                     notification_type="traps", user=None):
    """
    checks if snmp trap exists

    Args:
        handle (ImcHandle)
        hostname (string): ip address
        port (number): port
        version (string): "v2c", "v3"
        notification_type (string): "informs", "traps"
            Required only for version "v2c" and "v3"
        user (string): username

    Returns:
        Int: 0 if trap not found, else returns the trap-id. Range is (1,15)

    Example:
        snmp_trap_exists(handle, hostname="10.10.10.10",
                      port="162",
                      version="v2c",
                      notification_type="informs",
                      user="username")

    """

    traps = handle.query_children(in_dn="sys/svc-ext/snmp-svc",
                                  class_id="CommSnmpTrap")
    for trap in traps:
        if ((trap.hostname == hostname) and
                (trap.port == port) and
                (trap.version == version) and
                (trap.notification_type == notification_type) and
                (trap.user == user)):
            return int(trap.id)
    return 0


def snmp_trap_modify(handle, trap_id=0, hostname=None, port=None,
                     version=None, notification_type=None, user=None):
    """
    Modifies snmp trap referred to by id

    Args:
        handle (ImcHandle)
        trap_id (int) : Range is (1,15)
        hostname (string): ip address
        port (number): port
        version (string): "v2c", "v3"
        notification_type (string): "informs", "traps"
            Required only for version "v2c" and "v3"
        user (string): username

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

    from imcsdk.imcexception import ImcOperationError

    dn = "sys/svc-ext/snmp-svc/snmp-trap-" + str(trap_id)
    mo = handle.query_dn(dn)
    if not mo:
        raise ImcOperationError("Snmp Trap Modify", "Trap not found")

    if hostname:
        mo.hostname = hostname
    if port:
        mo.port = port
    if version:
        mo.version = version
    if notification_type:
        mo.notification_type = notification_type
    if user:
        mo.user = user

    handle.set_mo(mo)
    return mo


def snmp_trap_remove(handle, trap_id=0):
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

    from imcsdk.imcexception import ImcOperationError
    from imcsdk.mometa.comm.CommSnmpTrap import CommSnmpTrapConsts

    dn = "sys/svc-ext/snmp-svc/snmp-trap-" + str(trap_id)
    mo = handle.query_dn(dn)
    if not mo:
        raise ImcOperationError("Snmp Trap Remove", "Trap not found")

    mo.admin_state = CommSnmpTrapConsts.ADMIN_STATE_DISABLED
    mo.admin_action = CommSnmpTrapConsts.ADMIN_ACTION_CLEAR
    handle.set_mo(mo)


def snmp_user_add(handle, name, security_level="authpriv",
                  auth_pwd=None, auth="MD5",
                  priv_pwd=None, priv="AES"):
    """
    Adds snmp user.

    Args:
        handle (ImcHandle)
        name (string): snmp username
        security_level (string): "authpriv", "authnopriv", "noauthnopriv"
        auth_pwd (string): password
        auth (string): "MD5", "SHA"
        priv_pwd (string): privacy password
        priv (string): "AES", "DES"

    Returns:
        CommSnmpUser: Managed Object

    Raises:
        ImcOperationError is maximum number of users already configured

    Example:
        snmp_user_add(handle, name="snmpuser",
            security_level="authpriv", auth_pwd="abcd",
            auth="md5", priv_pwd="xyz", priv="des")
    """

    from imcsdk.imcexception import ImcOperationError

    users = handle.query_children(in_dn="sys/svc-ext/snmp-svc",
                                  class_id="CommSnmpUser")
    free_user = None
    for user in users:
        if user.name == "":
            free_user = user
            break

    if free_user is None:
        raise ImcOperationError("Snmp User Add",
                                "Maximum number of users already configured")

    free_user.name = name
    free_user.security_level = security_level
    free_user.auth_pwd = auth_pwd
    free_user.auth = auth
    free_user.privacy_pwd = priv_pwd
    free_user.privacy = priv

    handle.set_mo(free_user)
    return free_user


def snmp_user_exists(handle, name):
    """
    checks if snmp user exists.

    Args:
        handle (ImcHandle)
        name (string): snmp username

    Returns:
        Int: 0 is user does not exist, user-id(1-15) if user exists

    Example:
        snmp_user_exists(handle, name="snmpuser")
    """

    users = handle.query_children(in_dn="sys/svc-ext/snmp-svc",
                                  class_id="CommSnmpUser")
    for user in users:
        if user.name == name:
            return int(user.id)
    return 0


def snmp_user_modify(handle, user_id, username=None, security_level=None,
                     auth_pwd=None, auth=None,
                     priv_pwd=None, priv=None):
    """
    Modifies snmp user. Use this after getting the id from snmp_user_exists

    Args:
        handle (ImcHandle)
        user_id (int) : unique id for the user
        username (string): snmp username
        security_level (string): "authpriv", "authnopriv", "noauthnopriv"
        auth_pwd (string): password
        auth (string): "md5", "sha"
        priv_pwd (string): privacy password
        priv (string): "aes", "des"

    Returns:
        CommSnmpUser: Managed Object

    Raises:
        ImcOperationError is user not found

    Example:
        snmp_user_modify(handle, name="snmpuser", descr="",
                          pwd="password", privpwd="password",
                          auth="md5", use_aes="no")
    """

    from imcsdk.imcexception import ImcOperationError

    dn = "sys/svc-ext/snmp-svc/snmpv3-user-" + str(user_id)
    mo = handle.query_dn(dn)
    if not mo:
        raise ImcOperationError("Snmp User Modify", "User does not exist")

    if username:
        mo.name = username
    if security_level:
        mo.com2_sec = security_level
    if auth_pwd:
        mo.auth_pwd = auth_pwd
    if auth:
        mo.auth = auth
    if priv_pwd:
        mo.privacy_pwd = priv_pwd
    if priv:
        mo.privacy = priv

    handle.set_mo(mo)
    return mo


def snmp_user_remove(handle, name):
    """
    removes snmp user.

    Args:
        handle (ImcHandle)
        name (string): snmp username

    Returns:
        None

    Raises:
        ValueError: If CommSnmpUser Mo is not present

    Example:
        snmp_user_remove(handle, name="snmpuser")

    """

    from imcsdk.imcexception import ImcOperationError
    from imcsdk.mometa.comm.CommSnmpUser import CommSnmpUserConsts

    users = handle.query_children(in_dn="sys/svc-ext/snmp-svc",
                                  class_id="CommSnmpUser")
    found_user = None
    for user in users:
        if user.name == name:
            found_user = user
            break

    if found_user is None:
        raise ImcOperationError("Snmp User Delete", "User does not exist")

    found_user.name = ""
    found_user.admin_action = CommSnmpUserConsts.ADMIN_ACTION_CLEAR
    handle.set_mo(found_user)
