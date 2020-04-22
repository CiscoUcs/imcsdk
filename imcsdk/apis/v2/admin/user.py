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
This module implements apis to create/delete/modify local users
"""

import logging
from imcsdk.imcexception import ImcOperationError, ImcOperationErrorDetail
from imcsdk.imccoreutils import process_conf_mos_response

log = logging.getLogger('imc')
MAX_USERS = 15


def password_strong_enable(handle):
    """
    This method will enable strong password policy for users

    Args:
        handle (ImcHandle)

    Returns:
        AaaUserPolicy object
    """

    mos = handle.query_classid("AaaUserPolicy")
    mo = mos[0]

    mo.user_password_policy = "enabled"
    handle.set_mo(mo)
    return mo


def password_strong_exists(handle):
    """
    This method will check if strong password policy is enabled

    Args:
        handle(ImcHandle)

    Returns:
        (True, Mo) or (False, None)
    """

    mos = handle.query_classid("AaaUserPolicy")
    if len(mos) == 0:
        raise ImcOperationError("Check Password Strength", "MO does not exist")

    mo = mos[0]
    if mo.user_password_policy != "enabled":
        return False, None
    return True, mo


def password_strong_disable(handle):
    """
    This method will disable strong password policy for users

    Args:
        handle (ImcHandle)

    Returns:
        AaaUserPolicy object
    """

    mos = handle.query_classid("AaaUserPolicy")
    mo = mos[0]

    mo.user_password_policy = "disabled"
    handle.set_mo(mo)
    return mo


def password_expire_enable(handle,
                           password_expiry_duration,
                           password_history=None,
                           password_notification_period=None,
                           password_grace_period=None):
    """
    This method sets up the password expiration policy for local users

    Args:
        handle(ImcHandle)
        password_expiry_duration(int): The time period after which the set
            password expires.
            Setting this to zero will disable password expiry.
        password_history(int): Specifies in number of instances, the
            new password entered should not have been used in the past.
        password_notification_period(int): Specifies in number of days, the
            user will be notified before password expiry.
        password_grace_period(int): Specifies in number of days, the
            old password will still be valid after the password expiry.

    Returns:
        AaaUserPasswordExpiration object
    """

    from imcsdk.mometa.aaa.AaaUserPasswordExpiration import \
        AaaUserPasswordExpiration

    mo = AaaUserPasswordExpiration(parent_mo_or_dn="sys/user-ext")
    if not password_expiry_duration > 0:
        raise ImcOperationError("Enable password expiration",
                                "password_expiry_duration should be > 0.")
    args = {
        "password_expiry_duration": str(password_expiry_duration)
        if password_expiry_duration is not None else None,
        "password_history": str(password_history)
        if password_history is not None else None,
        "password_notification_period": str(password_notification_period)
        if password_notification_period is not None else None,
        "password_grace_period": str(password_grace_period)
        if password_grace_period is not None else None,
    }

    mo.set_prop_multiple(**args)
    handle.set_mo(mo)


def password_expire_exists(handle, **kwargs):
    """
    This method will check if the password expiration policy exists

    Args:
        handle (ImcHandle)
        kwargs: key-value paired arguments

    Returns:
        (True, AaaUserPasswordExpiration) is policy exists, else (False, None)

    """
    from imcsdk.mometa.aaa.AaaUserPasswordExpiration import \
        AaaUserPasswordExpiration

    mo = AaaUserPasswordExpiration(parent_mo_or_dn="sys/user-ext")
    mo = handle.query_dn(mo.dn)
    if mo is None:
        return False, None

    if not int(mo.password_expiry_duration):
        return False, mo

    if not mo.check_prop_match(**kwargs):
        return False, mo

    return True, mo


def password_expire_disable(handle):
    """
    This method disables the password expiration policy for local users

    Args:
        handle(ImcHandle)

    Returns:
        AaaUserPasswordExpiration object
    """

    from imcsdk.mometa.aaa.AaaUserPasswordExpiration import \
        AaaUserPasswordExpiration

    mo = AaaUserPasswordExpiration(parent_mo_or_dn="sys/user-ext")

    args = {
        "password_expiry_duration": "0"
    }

    mo.set_prop_multiple(**args)
    handle.set_mo(mo)
    return mo

def password_properties_exists(handle, **kwargs):
    """
    This method will check if the password expiration policy exists

    Args:
        handle (ImcHandle)
        kwargs: key-value paired arguments

    Returns:
        (True, AaaUserPasswordExpiration) is policy exists, else (False, None)

    """
    from imcsdk.mometa.aaa.AaaUserPasswordExpiration import \
        AaaUserPasswordExpiration

    mo = AaaUserPasswordExpiration(parent_mo_or_dn="sys/user-ext")
    mo = handle.query_dn(mo.dn)
    if mo is None:
        return False, None

    if not mo.check_prop_match(**kwargs):
        return False, mo

    return True, mo


def password_properties_set(handle,
                           password_expiry_duration=None,
                           password_history=None,
                           password_notification_period=None,
                           password_grace_period=None):
    """
    This method configures password properties for local users

    Args:
        handle(ImcHandle)
        password_expiry_duration(int): The time period after which the set
            password expires.
            Setting this to zero will disable password expiry.
        password_history(int): Specifies in number of instances, the
            new password entered should not have been used in the past.
        password_notification_period(int): Specifies in number of days, the
            user will be notified before password expiry.
        password_grace_period(int): Specifies in number of days, the
            old password will still be valid after the password expiry.

    Returns:
        AaaUserPasswordExpiration object
    """

    from imcsdk.mometa.aaa.AaaUserPasswordExpiration import \
        AaaUserPasswordExpiration

    mo = AaaUserPasswordExpiration(parent_mo_or_dn="sys/user-ext")
    args = {
        "password_expiry_duration": str(password_expiry_duration)
        if password_expiry_duration is not None else None,
        "password_history": str(password_history)
        if password_history is not None else None,
        "password_notification_period": str(password_notification_period)
        if password_notification_period is not None else None,
        "password_grace_period": str(password_grace_period)
        if password_grace_period is not None else None,
    }

    mo.set_prop_multiple(**args)
    handle.set_mo(mo)


def local_users_get(handle, dump=False):
    """
    This method gets the list of local users configured on the server

    Args:
        handle (ImcHandle)
        dump (bool)

    Returns:
        List of AaaUser objects corresponding to the local users
    """

    aaa_users = _get_local_users(handle)
    users = [x for x in aaa_users if x.name]

    if dump:
        log.info("List of users (id, username, role, status)")
        log.info("------------------------------------------")

        for user in users:
            log.info(" %s %s %s %s" %
                     (user.id.rjust(3), user.name.center(15),
                      user.priv.center(15), user.account_status.center(15)))
    return users


def _get_local_users(handle):
    return handle.query_classid("AaaUser")


def _get_local_user(handle, name):
    users = _get_local_users(handle)
    for user in users:
        if user.name == name:
            return user
    return None


def _get_free_user_id(handle):
    from imcsdk.mometa.aaa.AaaUser import AaaUserConsts
    users = _get_local_users(handle)
    for user in users:
        if user.account_status == AaaUserConsts.ACCOUNT_STATUS_INACTIVE and \
                not user.name:
            return user.id

    raise ImcOperationError("Create Local User",
                            "Max number of users already configured")


def local_user_create(handle, name, pwd, priv="read-only",
                      account_status="active", change_password=False):
    """
    This method will create a new local user and setup it's role.

    Args:
        handle (ImcHandle)
        name (string): username
        pwd (string): pwd
        priv (string): "admin", "read-only", "user"
        account_status (string): "active", "inactive"

    Returns:
        AaaUser object corresponding to the user created

    Raises:
        Exception when limit on the number of users has exceeded
    """

    from imcsdk.mometa.aaa.AaaUser import AaaUser

    # (1) local_user_exists(handle, name, pwd, priv) would be used by Ansible.
    # (2) local_user_exists(handle, name) would be used by user scripts.
    # If the privileges have changed for an existing user,
    #   (1) will fail, but (2) will pass.
    # In that case, Ansible will call local_user_create, which will fail
    # because user exists.Hence, special handling is needed in
    # local_user_exists to handle modify case.

    user = _get_local_user(handle, name)
    if user:
        pwd = pwd if change_password else None
        return local_user_modify(handle, name=name, pwd=pwd, priv=priv,
                                 account_status=account_status)

    available_user_id = _get_free_user_id(handle)

    new_user = AaaUser(parent_mo_or_dn="sys/user-ext", id=available_user_id)
    args = {"name": name,
            "pwd": pwd,
            "priv": priv,
            "account_status": account_status}
    new_user.set_prop_multiple(**args)

    handle.set_mo(new_user)
    return new_user

def _delete_users(handle, users=None, endpoint_users=None):
    """
    This method deactivates those IMC users that are NOT part of input list of users.

    Args:
        handle (ImcHandle)
        users (list): list of user dict

    Returns:
        list: List of user ids that are NOT deactivated. Input users that are already present on IMC form this list.
        boolean: flag that indicates if users were deleted
    Raises:
        ImcOperationError if the user is not found
    """

    from imcsdk.mometa.aaa.AaaUser import AaaUserConsts

    api = "Update Local Users"
    user_mos = []
    skipped_user_ids = []
    aaa_user_prefix = "sys/user-ext/user-"
    dn_to_user_dict = {}
    delete_users = False

    for endpoint_user in endpoint_users:
        delete_user = True
        for user in users:
            if user['name'] == endpoint_user.name:
                delete_user = False
                skipped_user_ids.append(int(endpoint_user.id))
                break
        if delete_user and endpoint_user.name != 'admin':
            endpoint_user.account_status = AaaUserConsts.ACCOUNT_STATUS_INACTIVE
            endpoint_user.admin_action = AaaUserConsts.ADMIN_ACTION_CLEAR
            dn_to_user_dict[aaa_user_prefix+str(endpoint_user.id)] = endpoint_user.name
            user_mos.append(endpoint_user)
            delete_users = True
            # print("Need to delete:", endpoint_user.name)

    response = handle.set_mos(user_mos)
    if response:
        process_conf_mos_response(response, api, True,
                                  'Purging of previous state failed',
                                  user_mos_callback,
                                  dn_to_user_dict)
    return skipped_user_ids, delete_users


def local_users_update(handle, users=None):
    """
    This method will create, modify or delete local users.
    It could also be a combination of these operations.

    Args:
        handle (ImcHandle)
        users (list): list of user dict
          keys:
            name (string): username
            priv (string): "admin", "user", "read-only"
            pwd (string): password
            account_status(string): "active", "inactive"
            change_password(boolean): flag used to change password
          example:
            [{'name':'dummy',
              'pwd': '*****',
              'priv': 'admin',
              'change_password': true,
              'account_status': 'active'}]

    Returns:
        boolean: flag that indicates if users were created, modified or deleted. It could also be a combination of these operations.

    Raises:
        IMCOperationError for various failure scenarios. A sample IMC Exception looks something like this:
        "Update Local Users failed, error: User:dum1 - [ErrorCode]: 2003[ErrorDescription]: Operation failed. Matching old password(s), please enter a different password.;
    Note: This error msg format is being used in Cisco Intersight to map error messages to respective users. Please excercise caution before changing it in the API.
    """

    from imcsdk.mometa.aaa.AaaUser import AaaUser
    from imcsdk.imccoreutils import sanitize_message
    api = "Update Local Users"
    if users is None:
        users = []
    if len(users) > MAX_USERS:
        raise ImcOperationError(api, "Number of users exceeded max allowed limit on IMC")
    update_users = False
    create_users = False
    endpoint_users = _get_local_users(handle)
    used_ids, delete_users = _delete_users(handle, users, endpoint_users)
    all_ids= range(2, MAX_USERS + 1)
    free_ids = list(set(all_ids) - set(used_ids))
    create_mos = []
    modify_mos = []
    dn_to_user_dict = {}
    aaa_user_prefix = "sys/user-ext/user-"
    id = 0
    for user in users:
        if 'name' not in user:
            raise ImcOperationError(api, "User Name is invalid")
        if 'pwd' not in user:
            raise ImcOperationError(api, "Password is invalid")
        if 'priv' not in user:
            raise ImcOperationError(api, "Privilege is invalid")
        if 'account_status' not in user:
            account_status = "active"
        else:
            account_status = user['account_status']
        if 'change_password' not in user:
            change_password = False
        else:
            change_password = user['change_password']
        name = user['name']
        pwd  = user['pwd']
        priv = user['priv']
        args = {"name": name,
                "pwd": pwd,
                "priv": priv,
                "account_status": account_status}

        # Existing users are not touched and hence we can safely check the
        # endpoint users list if there is
        found_user = None
        l = [x for x in endpoint_users if x.name == name]
        if len(l) != 0:
            found_user = l[0]
        if found_user:
            if not change_password:
                args.pop('pwd', None)
            if not found_user.check_prop_match(**args):
                update_users = True
            dn_to_user_dict[aaa_user_prefix+str(found_user.id)] = name
            found_user.set_prop_multiple(**args)
            modify_mos.append(found_user)
            continue
        if len(free_ids) == 0 or id >= len(free_ids):
            raise ImcOperationError(api,"Cannot configure more users than allowed limit on IMC")
        create_users = True
        free_id = free_ids[id]
        dn_to_user_dict[aaa_user_prefix+str(free_id)] = name
        mo = AaaUser(parent_mo_or_dn="sys/user-ext", id=str(free_id))
        mo.set_prop_multiple(**args)
        create_mos.append(mo)
        id += 1
    ret = []
    mos = []

    mos.extend(modify_mos)
    mos.extend(create_mos)

    response = handle.set_mos(mos)
    if response:
        ret = process_conf_mos_response(response, api, False,
                                        'Create/Update local users failed',
                                        user_mos_callback,
                                        dn_to_user_dict)
        if len(ret) != 0:
            error_msg = 'Create/Update local users failed:\n'
            for item in ret:
                user = item["Object"]
                error = item["Error"]
                error = sanitize_message(error)
                error_msg += user + ": " + error + "\n"

            raise ImcOperationErrorDetail(api, error_msg, ret)

    results = {}
    # print(create_users, update_users, delete_users)
    results["changed"] = create_users or update_users or delete_users
    results["msg"] = ""
    results["msg_params"] = ret

    return results


def user_mos_callback(dn, dn_to_user_dict):
    return dn_to_user_dict.get(dn, "Unknown User:" + dn)


def local_user_exists(handle, name, change_password=False, **kwargs):
    """
    This method checks if a user exists with attributes passed

    Args:
        handle (ImcHandle)
        kwargs: key-value paired arguments used for user attributes

    Returns:
        (True, AaaUser)  Or (False, None)

    Examples:
        user_exists(handle, user="abcd", priv="admin")
    """

    user = _get_local_user(handle, name=name)
    if user is None:
        return False, None

    if not change_password:
        kwargs.pop('pwd', None)

    return user.check_prop_match(**kwargs), user


def local_user_modify(handle, name, **kwargs):
    """
    This method will modify the user with the username specified

    Args:
        handle (ImcHandle)
        name (string): username
        kwargs: key-value paired arguments

    Returns:
        AaaUser object corresponding to the user created

    Raises:
        Exception when user is not found
    """

    found_user = _get_local_user(handle, name=name)
    if found_user is None:
        raise ImcOperationError("Modify Local User", "User doesn't exist")

    found_user.set_prop_multiple(**kwargs)
    handle.set_mo(found_user)


def local_user_delete(handle, name):
    """
    This method deactivates the user referred to by the username passed

    Args:
        handle (ImcHandle)
        name (string): username

    Returns:
        None

    Raises:
        ImcOperationError if the user is not found
    """

    from imcsdk.mometa.aaa.AaaUser import AaaUserConsts

    found_user = _get_local_user(handle, name=name)
    if found_user is None:
        raise ImcOperationError("Delete Local User", "User doesn't exist")

    found_user.account_status = AaaUserConsts.ACCOUNT_STATUS_INACTIVE
    found_user.admin_action = AaaUserConsts.ADMIN_ACTION_CLEAR

    handle.set_mo(found_user)


def local_user_delete_all(handle):
    """
    This method deactivates all the user except admin user

    Args:
        handle (ImcHandle)

    Returns:
        None

    Raises:
        ImcOperationError if the user is not found
    """

    from imcsdk.mometa.aaa.AaaUser import AaaUserConsts

    users = _get_local_users(handle)
    for user in users:
        if user.name == 'admin':
            continue
        user.account_status = AaaUserConsts.ACCOUNT_STATUS_INACTIVE
        user.admin_action = AaaUserConsts.ADMIN_ACTION_CLEAR
        handle.set_mo(user)


def user_sessions_get(handle, dump=False):
    """
    This method gets the list of active user sessions
    Args:
        handle (ImcHandle)
        dump (bool)

    Returns:
        List of AaaSession objects
    """

    sessions = handle.query_classid("AaaSession")
    if dump:
        log.info(
            "List of Active User Sessions(username, host, type of session):")
        log.info(
            "--------------------------------------------------------------")
        for session in sessions:
            log.info(
                " %s \t%s \t%s" % (session.user, session.host, session.ui))

    return sessions


def user_validate_inputs(**kwargs):
    """
    This method will check if the input parameters are valid
    """
    from imcsdk.mometa.aaa.AaaUser import AaaUser
    np = {}
    for prop in AaaUser.naming_props:
        if prop in kwargs:
            np[prop] = kwargs[prop]
    return AaaUser(parent_mo_or_dn=None, **np).validate_inputs(**kwargs)
