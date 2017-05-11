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
from imcsdk.imcexception import ImcOperationError

log = logging.getLogger('imc')


def strong_password_set(handle, enable=True):
    """
    This method will enable/disable strong password policy for users

    Args:
        handle (ImcHandle)
        enable (bool)

    Returns:
        AaaUserPolicy object
    """

    mos = handle.query_classid("AaaUserPolicy")
    user_policy = mos[0]

    user_policy.user_password_policy = ("disabled", "enabled") [enable]

    handle.set_mo(user_policy)
    return user_policy


def is_strong_password_set(handle):
    """
    This method will check if strong password policy is enabled

    Args:
        handle(ImcHandle)

    Returns:
        bool
    """

    mos = handle.query_classid("AaaUserPolicy")
    if len(mos) == 0:
        raise ImcOperationError("Check Password Strength", "MO does not exist")
    return (mos[0].user_password_policy == "enabled")


def password_expiration_set(handle,
                            password_expiry_duration,
                            password_history=0,
                            password_notification_period=15,
                            password_grace_period=0):
    """
    This method sets up the password expiration policy for local users

    Args:
        handle(ImcHandle)
        password_expiry_duration(int): The time period after which the set password expires.
                                       Setting this to zero will disable password expiry.
        password_history(int): Specifies in number of instances,
                               the new password entered should not have been used in the past.
        password_notification_period(int): Specifies in number of days,
                                            the user will be notified before password expiry
        password_grace_period(int): Specifies in number of days,
                                    the old password will still be valid after the password expiry

    Returns:
        AaaUserPasswordExpiration object
    """

    from imcsdk.mometa.aaa.AaaUserPasswordExpiration import \
        AaaUserPasswordExpiration

    mo = AaaUserPasswordExpiration(parent_mo_or_dn="sys/user-ext")
    args = {
            "password_expiry_duration": str(password_expiry_duration),
            "password_history": str(password_history),
            "password_notification_period": str(password_notification_period),
            "password_grace_period": str(password_grace_period)
            }
    mo.set_prop_multiple(**args)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def password_expiration_exists(handle, **kwargs):
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

    for k, v in kwargs.items():
        if isinstance(v, int):
            kwargs[k] = str(v)

    return (mo.check_prop_match(**kwargs), mo)


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


def local_user_create(handle, name, pwd, priv="read-only"):
    """
    This method will create a new local user and setup it's role.

    Args:
        handle (ImcHandle)
        name (string): username
        pwd (string): pwd
        priv (string): "admin", "read-only", "user"

    Returns:
        AaaUser object corresponding to the user created

    Raises:
        Exception when limit on the number of users has exceeded
    """

    from imcsdk.mometa.aaa.AaaUser import AaaUser, AaaUserConsts

    # (1) local_user_exists(handle, name, pwd, priv) would be used by Ansible.
    # (2) local_user_exists(handle, name) would be used by user scripts.
    # If the privileges have changed for an existing user, (1) will fail, but (2) will pass
    # In that case, Ansible will call local_user_create, which will fail because user exists
    # Hence, special handling is needed in local_user_exists to handle modify case.

    user = _get_local_user(handle, name)
    if user:
        return local_user_modify(handle, name=name, pwd=pwd, priv=priv)

    available_user_id = _get_free_user_id(handle)

    new_user = AaaUser(parent_mo_or_dn="sys/user-ext", id=available_user_id)
    args = {"name": name,
            "pwd": pwd,
            "priv": priv,
            "account_status": AaaUserConsts.ACCOUNT_STATUS_ACTIVE}
    new_user.set_prop_multiple(**args)

    handle.set_mo(new_user)
    return new_user


def local_user_exists(handle, **kwargs):
    """
    This method checks if a user exists with attributes passed

    Args:
        handle (ImcHandle)
        kwargs: key-value paired arguments used for user attributes

    Returns:
        (True, AaaUser) if the user exists with the properties, else (False, None)

    Examples:
        user_exists(handle, user="abcd", priv="admin")
    """

    users = _get_local_users(handle)
    for user in users:
        if user.check_prop_match(**kwargs):
            return True, user
    return False, None


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
    found_user.priv = AaaUserConsts.PRIV_READ_ONLY
    found_user.admin_action = AaaUserConsts.ADMIN_ACTION_CLEAR

    handle.set_mo(found_user)


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
        log.info("List of Active User Sessions(username, host, type of session):")
        log.info("--------------------------------------------------------------")
        for session in sessions:
            log.info(" %s \t%s \t%s" % (session.user, session.host, session.ui))

    return sessions
