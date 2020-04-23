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
This module performs the operations related to snmp server, user and traps.
"""
import time
import datetime
import logging

from imcsdk.imcexception import ImcOperationError, ImcOperationErrorDetail
from imcsdk.imcexception import ImcException
from imcsdk.apis.v2.utils import _get_mo
from imcsdk.imccoreutils import process_conf_mos_response, sanitize_message
from imcsdk.apis.v2.versionconstraints.snmp import \
    snmp_multiple_config_with_configcommit_for_hp_and_above
from imcsdk.apis.v2.versionconstraints.snmp import \
    snmp_commit_explicitly_for_hp_and_above


log = logging.getLogger('imc')

SNMP_DN = 'sys/svc-ext/snmp-svc'


def _set_snmp(handle, mo, timeout=90):
    start = datetime.datetime.now()
    while True:
        try:
            handle.set_mo(mo)
            return mo
        except ImcException as e:
            log.debug(str(e))
            engine_id_error = "configuration changes in progress"
            if engine_id_error not in e.error_descr.lower():
                raise
        if (datetime.datetime.now() - start).total_seconds() > timeout:
            raise ImcOperationError("SNMP Enable",
                                    "Error: %s" % str(e))
        time.sleep(10)


def _reset(handle, local_mo, community, trap_community, engine_id_key):
    '''
    The following issues exist when server in a factory reset condition, and if
    enabling SNMP with any of the community, trap_community, engine_id_key
    property with value as empty string.

    GP, GPMR1:
    CIMC returns an error - "CIMC may be running any critical operation or in
    error state. Retry after sometime or reboot CIMC if necessary"

    GPMR2, HP:
    CIMC does not return error, but SNMP remains disabled.

    Bug Ids - CSCvf87365, CSCvi17984

    This function sets and unsets the above properties if both new and
    existing value of any of these properties is empty string.
    '''

    import random
    from imcsdk.mometa.comm.CommSnmp import CommSnmpConsts

    input_params = locals()
    mo = _get_mo(handle, dn=SNMP_DN)

    params = {
        "community": "init",
        "trap_community": "init",
        "engine_id_key": str(random.randint(1, 101))
    }

    reset = False
    for prop, val in params.items():
        if getattr(mo, prop) == "" and input_params[prop] == "":
            log.debug("Reset %s." % prop)
            setattr(mo, prop, val)
            reset = True

    if reset:
        log.debug("Initiating reset.")
        mo.admin_state = CommSnmpConsts.ADMIN_STATE_ENABLED
        _set_snmp(handle, mo)
        log.debug("Ending reset.")


def snmp_enable(handle, port=None, community=None,
                com2_sec=None, trap_community=None,
                sys_contact=None, sys_location=None,
                engine_id_key=None, **kwargs):
    """
    Enables SNMP.

    Args:
        handle (ImcHandle)
        port (int): port on which SNMP agent runs
        community (string): community
        com2_sec (string): "disabled", "limited", "full"
        trap_community(string): community to be used when generating traps
        sys_contact (string): sys_contact
        sys_location (string): sys_location
        engine_id_key (string): engine id key
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

    # always reset if any of the community, trap_community, engine_id_key
    # is empty string both in CIMC and in modify request.
    _reset(handle, mo, community, trap_community, engine_id_key)

    params = {
        'admin_state': CommSnmpConsts.ADMIN_STATE_ENABLED,
        'port': str(port) if port is not None else None,
        'community': community,
        'com2_sec': com2_sec,
        'trap_community': trap_community,
        'sys_contact': sys_contact,
        'sys_location': sys_location,
        'engine_id_key': engine_id_key
        }

    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)

    log.debug("Configuring SNMP.")
    return _set_snmp(handle, mo)


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


def snmp_exists(handle, **kwargs):
    """
    Checks if snmp is enabled or not

    Args:
        handle (ImcHandle)
        kwargs: Key-Value paired arguments relevant to CommSnmp object

    Returns:
        True/false, CommSnmp MO/None

    Example:
        snmp_exists(handle)
    """
    from imcsdk.mometa.comm.CommSnmp import CommSnmpConsts

    mo = _get_mo(handle, dn=SNMP_DN)
    kwargs['admin_state'] = CommSnmpConsts.ADMIN_STATE_ENABLED
    return mo.check_prop_match(**kwargs), mo


def _get_snmp_traps(handle):
    return handle.query_children(in_dn=SNMP_DN, class_id="CommSnmpTrap")


def _get_free_snmp_trap(handle):
    traps = _get_snmp_traps(handle)
    for trap in traps:
        if trap.hostname == "0.0.0.0":
            return trap
    return None


def snmp_trap_get(handle, hostname):
    traps = _get_snmp_traps(handle)
    for trap in traps:
        if trap.hostname == hostname:
            return trap
    return None


def snmp_trap_add(handle, hostname, version, notification_type,
                  admin_state="enabled", user=None, port=None,
                  **kwargs):
    """
    Adds snmp trap.

    Args:
        handle (ImcHandle)
        hostname (string): ip address
        admin_state (string): enabled, disabled
        version (string): "v2c", "v3"
        notification_type (string): "informs", "traps"
            Required only for version "v2c" and "v3"
        user (string): send traps for a specific user
        port (int): port
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

    if version == CommSnmpTrapConsts.VERSION_V2C and user:
        user = None

    mo = snmp_trap_get(handle, hostname)
    if mo is None:
        mo = _get_free_snmp_trap(handle)
    if mo is None:
        raise ImcOperationError("Snmp Trap Add",
                                "No free traps available to configure")

    params = {
        'hostname': hostname,
        'version': version,
        'notification_type': notification_type,
        'admin_state': admin_state,
        'port': str(port) if port is not None else None,
        'user': user
        }

    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return mo


def snmp_trap_exists(handle, hostname, **kwargs):
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
    from imcsdk.mometa.comm.CommSnmpTrap import CommSnmpTrapConsts

    mo = snmp_trap_get(handle, hostname)
    if mo is None:
        return False, None

    if mo.version == CommSnmpTrapConsts.VERSION_V2C:
        kwargs.pop('user', None)

    return mo.check_prop_match(**kwargs), mo


def snmp_trap_modify(handle, hostname, **kwargs):
    """
    Modifies snmp trap referred to by id

    Args:
        handle (ImcHandle)
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
    mo = snmp_trap_get(handle, hostname)
    if mo is None:
        raise ImcOperationError("Modify SNMP trap", "Trap does not exist.")

    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return mo


def snmp_trap_delete(handle, hostname):
    """
    Deletes snmp trap.

    Args:
        handle (ImcHandle)
        hostname (string): SNMP hostname

    Returns:
        None

    Raises:
        ImcOperationError if trap not found

    Example:
        snmp_trap_delete(handle, trap_id=6)
    """
    from imcsdk.mometa.comm.CommSnmpTrap import CommSnmpTrapConsts

    mo = snmp_trap_get(handle, hostname)
    mo.admin_state = CommSnmpTrapConsts.ADMIN_STATE_DISABLED
    mo.admin_action = CommSnmpTrapConsts.ADMIN_ACTION_CLEAR
    handle.set_mo(mo)


def snmp_trap_add_all(handle, traps=None):
    """
    Adds snmp trap.

    Args:
        handle (ImcHandle)
        traps (list): list of trap dict
          keys:
            hostname (string): ip address
            admin_state (string): enabled, disabled
            version (string): "v2c", "v3"
            notification_type (string): "informs", "traps"
                Required only for version "v2c" and "v3"
            user (string): send traps for a specific user
            port (int): port

    Returns:
        list: List of CommSnmpTrap Managed Object

    Example:
        snmp_trap_add_all(handle,
                          traps=[{hostname: "10.10.10.10",
                                 port: "162",
                                 version:"v2c",
                                 notification_type:"informs"}]
                         )
    """
    from imcsdk.mometa.comm.CommSnmp import CommSnmpConsts
    from imcsdk.mometa.comm.CommSnmpTrap import CommSnmpTrap
    from imcsdk.mometa.comm.CommSnmpTrap import CommSnmpTrapConsts

    api = 'snmp_trap_add_all'
    parent_mo = _get_mo(handle, dn=SNMP_DN)
    if parent_mo.admin_state != CommSnmpConsts.ADMIN_STATE_ENABLED:
        raise ImcOperationError(api, 'SNMP is not enabled.')

    dn_to_trap_dict = {}
    mos = []
    id = 0
    for trap in traps:
        hostname = trap.pop('hostname', None)
        _validate_api_prop('hostname', hostname, api)

        version = trap.pop('version', None)
        _validate_api_prop('version', version, api, True,
                           [CommSnmpTrapConsts.VERSION_V1,
                            CommSnmpTrapConsts.VERSION_V2C,
                            CommSnmpTrapConsts.VERSION_V3])

        notification_type = trap.pop('notification_type', None)
        _validate_api_prop('notification_type', notification_type, api,
                           True,
                           [CommSnmpTrapConsts.NOTIFICATION_TYPE_INFORMS,
                            CommSnmpTrapConsts.NOTIFICATION_TYPE_TRAPS])

        admin_state = trap.pop('admin_state', 'enabled')
        _validate_api_prop('admin_state', admin_state, api, True,
                           [CommSnmpTrapConsts.ADMIN_STATE_ENABLED,
                            CommSnmpTrapConsts.ADMIN_STATE_DISABLED])

        user = trap.pop('user', None)
        port = trap.pop('port', None)

        if version == CommSnmpTrapConsts.VERSION_V2C and user:
            user = None
        if version == CommSnmpTrapConsts.VERSION_V3:
            notification_type = CommSnmpTrapConsts.NOTIFICATION_TYPE_TRAPS

        params = {
            'hostname': hostname,
            'version': version,
            'notification_type': notification_type,
            'admin_state': admin_state,
            'port': str(port) if port else None,
            'user': user
            }

        id += 1
        mo = CommSnmpTrap(parent_mo_or_dn=parent_mo, id=str(id))
        mo.set_prop_multiple(**params)
        mos.append(mo)
        dn_to_trap_dict[mo.dn] = mo.hostname

    # Optimize SNMP transaction performance for CIMC version HP(4.0) and above
    # via setting parameter 'config_change' to 'no-commit'
    mos = snmp_multiple_config_with_configcommit_for_hp_and_above(handle, mos)

    response = handle.set_mos(mos)
    if response:
        ret = process_conf_mos_response(response, api, False,
                                        'Create SNMP traps failed',
                                        snmp_traps_callback,
                                        dn_to_trap_dict)
        if len(ret) != 0:
            error_msg = 'Create/Update SNMP traps failed:\n'
            for item in ret:
                obj = item["Object"]
                error = item["Error"]
                error = sanitize_message(error)
                error_msg += "[Trap " + obj + "] " + error + "\n"

            raise ImcOperationErrorDetail(api, error_msg, ret)

    # Optimize SNMP transaction performance for CIMC version HP(4.0) and above
    # via doing explicit commit using newly introduced MO 'CommSnmpConfigCommit'
    snmp_commit_explicitly_for_hp_and_above(handle, SNMP_DN)

    results = {}
    results["changed"] = True
    results["msg"] = ""
    results["msg_params"] = ret

    return results


def snmp_traps_callback(dn, dn_to_trap_dict):
    return dn_to_trap_dict.get(dn, "Unknown Trap:" + dn)


def snmp_trap_delete_all(handle):
    """
    delete all snmp traps.

    Args:
        handle (ImcHandle)

    Returns:
        None

    Raises:
        ImcOperationError if trap not found

    Example:
        snmp_trap_delete_all(handle)
    """
    from imcsdk.mometa.comm.CommSnmpTrap import CommSnmpTrapConsts
    from imcsdk.mometa.comm.CommSnmp import CommSnmpConsts

    api = 'snmp_trap_delete_all'
    parent_mo = _get_mo(handle, dn=SNMP_DN)
    if parent_mo.admin_state != CommSnmpConsts.ADMIN_STATE_ENABLED:
        raise ImcOperationError(api, 'SNMP is not enabled.')

    mos = []
    traps = _get_snmp_traps(handle)
    for trap in traps:
        if trap.hostname == "0.0.0.0":
            continue
        trap.admin_state = CommSnmpTrapConsts.ADMIN_STATE_DISABLED
        trap.admin_action = CommSnmpTrapConsts.ADMIN_ACTION_CLEAR
        mos.append(trap)

    # Optimize SNMP transaction performance for CIMC version HP(4.0) and above
    # via setting parameter 'config_change' to 'no-commit'
    mos = snmp_multiple_config_with_configcommit_for_hp_and_above(handle, mos)

    response = handle.set_mos(mos)
    if response:
        process_conf_mos_response(response, api)

    # Optimize SNMP transaction performance for CIMC version HP(4.0) and above
    # via doing explicit commit using newly introduced MO 'CommSnmpConfigCommit'
    snmp_commit_explicitly_for_hp_and_above(handle, SNMP_DN)


def snmp_trap_exists_any(handle):
    """
    Checks if any snmp trap exists.

    Args:
        handle (ImcHandle)

    Returns:
        None

    Raises:
        ImcOperationError if trap not found

    Example:
        snmp_trap_exists_any(handle)
    """
    mos = _get_snmp_traps(handle)
    for mo in mos:
        if mo.hostname != "0.0.0.0":
            return True
    return False


def _get_snmp_users(handle):
    return handle.query_children(in_dn=SNMP_DN, class_id="CommSnmpUser")


def _get_free_snmp_user(handle):
    users = _get_snmp_users(handle)
    for user in users:
        if user.name == "":
            return user

    raise ImcOperationError("Snmp User Add",
                            "Maximum number of users already configured")


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
    users = _get_snmp_users(handle)
    for user in users:
        if user.name == name:
            return user
    return None


def snmp_user_add(handle, name, security_level,
                  auth=None, auth_pwd=None, change_auth_pwd=False,
                  privacy=None, privacy_pwd=None, change_privacy_pwd=False,
                  **kwargs):
    """
    Adds snmp user.

    Args:
        handle (ImcHandle)
        name (string): snmp username
        security_level (string): "authpriv", "authnopriv", "noauthnopriv"
        auth (string): "MD5", "SHA"
        auth_pwd (string): password
        change_auth_pwd (bool): set to True, if wants to change password for
                                existing user
        privacy (string): "AES", "DES"
        privacy_pwd (string): privacy password
        change_privacy_pwd (bool): set to True, if wants to change password for
                                   existing user

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

    auth_type = (
        CommSnmpUserConsts.SECURITY_LEVEL_AUTHNOPRIV,
        CommSnmpUserConsts.SECURITY_LEVEL_AUTHPRIV
    )

    priv_type = (
        CommSnmpUserConsts.SECURITY_LEVEL_AUTHPRIV
    )

    mo = snmp_user_get(handle, name)
    if mo:
        params = {}
        if mo.security_level != security_level:
            params['security_level'] = security_level
    else:
        mo = _get_free_snmp_user(handle)
        params = {
            'name': name,
            'security_level': security_level
            }

    if mo is None:
        raise ImcOperationError("Add SNMP user",
                                "No free user available.")

    if security_level in auth_type:
        if mo.auth and mo.auth == auth:
            params['auth_pwd'] = auth_pwd if change_auth_pwd else None
        else:
            params['auth'] = auth
            params['auth_pwd'] = auth_pwd

    if security_level in priv_type:
        if mo.privacy and mo.privacy == privacy:
            params['privacy_pwd'] = privacy_pwd if change_privacy_pwd else None
        else:
            params['privacy'] = privacy
            params['privacy_pwd'] = privacy_pwd

    if not params:
        return mo

    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return mo


def snmp_user_exists(handle, name, security_level, change_auth_pwd=False,
                     change_privacy_pwd=False, **kwargs):
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
    from imcsdk.mometa.comm.CommSnmpUser import CommSnmpUserConsts

    mo = snmp_user_get(handle, name)
    if mo is None:
        return False, None

    if not change_auth_pwd:
        kwargs.pop('auth_pwd', None)

    if not change_privacy_pwd:
        kwargs.pop('privacy_pwd', None)

    if security_level == CommSnmpUserConsts.SECURITY_LEVEL_NOAUTHNOPRIV:
        kwargs.pop('auth', None)
        kwargs.pop('auth_pwd', None)
        kwargs.pop('privacy', None)
        kwargs.pop('privacy_pwd', None)
    elif security_level == CommSnmpUserConsts.SECURITY_LEVEL_AUTHNOPRIV:
        kwargs.pop('privacy', None)
        kwargs.pop('privacy_pwd', None)

    kwargs['security_level'] = security_level

    return mo.check_prop_match(**kwargs), mo


def snmp_user_modify(handle, name, **kwargs):
    """
    Modifies snmp user. Use this after getting the id from snmp_user_exists

    Args:
        handle (ImcHandle)
        name (string) : SNMP user name
        kwargs: Key-Value paired arguments relevant to CommSnmpUser object

    Returns:
        CommSnmpUser: Managed Object

    Raises:
        ImcOperationError: If user is not present

    Example:
        snmp_user_modify(handle, name="snmpuser",
                         security_level="authpriv", auth_pwd="password",
                         auth="MD5", privacy="AES", privacy_pwd="password")
    """
    mo = snmp_user_get(handle, name)
    if mo is None:
        raise ImcOperationError("Modify SNMP User", "User doesn't exist")

    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return mo


def snmp_user_delete(handle, name):
    """
    deletes snmp user.

    Args:
        handle (ImcHandle)
        name (string): snmp username

    Returns:
        None

    Raises:
        ImcOperationError: If user is not present

    Example:
        snmp_user_delete(handle, name="snmpuser")

    """
    from imcsdk.mometa.comm.CommSnmpUser import CommSnmpUserConsts

    mo = snmp_user_get(handle, name=name)
    if mo is None:
        raise ImcOperationError("Snmp User Delete", "User does not exist")

    mo.name = ""
    mo.admin_action = CommSnmpUserConsts.ADMIN_ACTION_CLEAR
    handle.set_mo(mo)
    return mo


def _validate_api_prop(prop, value, api, validate_value=False,
                       valid_values=None):
    if value is None:
        raise ImcOperationError(api, "Required property '%s' missing." % (
           api, prop))
    if validate_value and value not in valid_values:
        raise ImcOperationError(
            api, "['%s'] Invalid value '%s'. Valid values are %s" % (
                prop, value, str(valid_values)))


def snmp_user_add_all(handle, users=None):
    """
    Adds snmp user.

    Args:
        handle (ImcHandle)
        users (list): list of user dict
          keys:
            name (string): snmp username
            security_level (string): "authpriv", "authnopriv", "noauthnopriv"
            auth (string): "MD5", "SHA"
            auth_pwd (string): password
                for existing user
            privacy (string): "AES", "DES"
            privacy_pwd (string): privacy password
                for existing user
          example:
            [{'name': 'snmpuser',
              'security_level': 'authpriv',
              'auth': 'MD5',
              'auth_pwd': 'password',
              'privacy': 'AES',
              'privacy_pwd': 'password'}
            ]

    Returns:
        list: List of CommSnmpUser Managed Object

    Raises:
        ImcOperationError is maximum number of users already configured

    Example:
        snmp_user_add_all( handle,
                    users = [{'name': 'snmpuser',
                            'security_level': 'authpriv',
                            'auth': 'MD5', 'auth_pwd': 'password',
                            'privacy': 'AES', 'privacy_pwd': 'password'])
    """
    from imcsdk.mometa.comm.CommSnmpUser import CommSnmpUser
    from imcsdk.mometa.comm.CommSnmpUser import CommSnmpUserConsts
    from imcsdk.mometa.comm.CommSnmp import CommSnmpConsts

    api = 'snmp_user_add_all'
    parent_mo = _get_mo(handle, dn=SNMP_DN)
    if parent_mo.admin_state != CommSnmpConsts.ADMIN_STATE_ENABLED:
        raise ImcOperationError(api, 'SNMP is not enabled.')

    dn_to_user_dict = {}
    mos = []
    id = 0
    for user in users:
        name = user.pop('name', None)
        security_level = user.pop('security_level', None)
        _validate_api_prop('name', name, api)
        _validate_api_prop('security_level', security_level, api)

        auth = user.pop('auth', None)
        auth_pwd = user.pop('auth_pwd', None)
        privacy = user.pop('privacy', None)
        privacy_pwd = user.pop('privacy_pwd', None)

        params = {
            'name': name,
            'security_level': security_level
            }

        if security_level == CommSnmpUserConsts.SECURITY_LEVEL_AUTHNOPRIV:
            _validate_api_prop('auth_pwd', auth_pwd, api)
            params['auth'] = auth
            params['auth_pwd'] = auth_pwd
        elif security_level == CommSnmpUserConsts.SECURITY_LEVEL_AUTHPRIV:
            _validate_api_prop('auth', auth, api, True, ['MD5', 'SHA'])
            _validate_api_prop('auth_pwd', auth_pwd, api)
            _validate_api_prop('privacy', privacy, api, True, ['AES', 'DES'])
            _validate_api_prop('privacy_pwd', privacy_pwd, api)
            params['auth'] = auth
            params['auth_pwd'] = auth_pwd
            params['privacy'] = privacy
            params['privacy_pwd'] = privacy_pwd

        id += 1
        mo = CommSnmpUser(parent_mo_or_dn=parent_mo, id=str(id))
        mo.set_prop_multiple(**params)
        mos.append(mo)
        dn_to_user_dict[mo.dn] = mo.name

    # Optimize SNMP transaction performance for CIMC version HP(4.0) and above
    # via setting parameter 'config_change' to 'no-commit'
    mos = snmp_multiple_config_with_configcommit_for_hp_and_above(handle, mos)

    response = handle.set_mos(mos)
    if response:
        ret = process_conf_mos_response(response, api, False,
                                        'Create SNMP users failed',
                                        snmp_users_callback,
                                        dn_to_user_dict)
        if len(ret) != 0:
            error_msg = 'Create/Update SNMP users failed:\n'
            for item in ret:
                obj = item["Object"]
                error = item["Error"]
                error = sanitize_message(error)
                error_msg += "[User " + obj + "] " + error + "\n"

            raise ImcOperationErrorDetail(api, error_msg, ret)

    # Optimize SNMP transaction performance for CIMC version HP(4.0) and above
    # via doing explicit commit using newly introduced MO 'CommSnmpConfigCommit'
    snmp_commit_explicitly_for_hp_and_above(handle, SNMP_DN)

    results = {}
    results["changed"] = True
    results["msg"] = ""
    results["msg_params"] = ret

    return results


def snmp_users_callback(dn, dn_to_user_dict):
    return dn_to_user_dict.get(dn, "Unknown User:" + dn)


def snmp_user_delete_all(handle):
    """
    delete all snmp users.

    Args:
        handle (ImcHandle)

    Returns:
        None

    Raises:
        ImcOperationError: If user is not present

    Example:
        snmp_user_delete_all(handle)

    """
    from imcsdk.mometa.comm.CommSnmpUser import CommSnmpUserConsts
    from imcsdk.mometa.comm.CommSnmp import CommSnmpConsts

    api = 'snmp_user_delete_all'
    parent_mo = _get_mo(handle, dn=SNMP_DN)
    if parent_mo.admin_state != CommSnmpConsts.ADMIN_STATE_ENABLED:
        raise ImcOperationError(api, 'SNMP is not enabled.')

    mos = []
    users = _get_snmp_users(handle)
    for user in users:
        if user.name == "":
            continue
        user.admin_action = CommSnmpUserConsts.ADMIN_ACTION_CLEAR
        mos.append(user)

    # Optimize SNMP transaction performance for CIMC version HP(4.0) and above
    # via setting parameter 'config_change' to 'no-commit'
    mos = snmp_multiple_config_with_configcommit_for_hp_and_above(handle, mos)

    response = handle.set_mos(mos)
    if response:
        process_conf_mos_response(response, api)

    # Optimize SNMP transaction performance for CIMC version HP(4.0) and above
    # via doing explicit commit using newly introduced MO 'CommSnmpConfigCommit'
    snmp_commit_explicitly_for_hp_and_above(handle, SNMP_DN)


def snmp_user_exists_any(handle):
    """
    Checks if any snmp user exists.

    Args:
        handle (ImcHandle)

    Returns:
        None

    Raises:
        ImcOperationError: If user is not present

    Example:
        snmp_user_exists_any(handle)

    """
    mos = _get_snmp_users(handle)
    for mo in mos:
        if mo.name != "":
            return True
    return False
