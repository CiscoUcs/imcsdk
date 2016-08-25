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
This module implements apis to create/delete/modify local/ldap users
"""

import logging

logging.basicConfig()
log = logging.getLogger('imc')
log.setLevel(logging.DEBUG)


def set_strong_password(handle, enable=False):
    """
    This method will enable/disable strong password policy for users

    Args:
        handle (ImcHandle)
        enable (bool)

    Returns:
        AaaUserPolicy object
    """

    user_policy = handle.query_classid("AaaUserPolicy")

    if enable:
        user_policy.user_password_policy = "enabled"
    else:
        user_policy.user_password_policy = "disabled"

    handle.set_mo(user_policy)
    return user_policy


def get_local_users(handle, dump=False):
    """
    This method gets the list of local users configured on the server

    Args:
        handle (ImcHandle)
        dump (bool)

    Returns:
        List of AaaUser objects corresponding to the active users
    """

    from imcsdk.mometa.aaa.AaaUser import AaaUserConsts

    aaa_users = handle.query_classid("AaaUser")
    active_users = []
    for user in aaa_users:
        if user.account_status == AaaUserConsts.ACCOUNT_STATUS_ACTIVE:
            active_users.append(user)
    if dump:
        log.info("List of active users (id, username, role):")
        log.info("------------------------------------------")

        for user in active_users:
            log.info(" %s \t%s \t%s" % (user.id, user.name, user.priv))
    return active_users


def create_local_user(handle, username, password, privilege="read-only"):
    """
    This method will create a new local user and setup it's role.

    Args:
        handle (ImcHandle)
        username (string): username
        password (string): password
        privilege (string): "admin", "read-only", "user"

    Returns:
        AaaUser object corresponding to the user created

    Raises:
        Exception when limit on the number of users has exceeded
    """

    from imcsdk.mometa.aaa.AaaUser import AaaUser, AaaUserConsts
    from imcsdk.imcexception import ImcOperationError

    aaa_users = handle.query_classid("AaaUser")
    inactive_users = []

    for user in aaa_users:
        if user.account_status == AaaUserConsts.ACCOUNT_STATUS_INACTIVE:
            inactive_users.append(user)

    if len(inactive_users) is 0:
        raise ImcOperationError("Create Local User",
                                "Max number of users already configured")

    available_user_id = inactive_users[0].id

    new_user = AaaUser(parent_mo_or_dn="sys/user-ext", id=available_user_id)
    new_user.account_status = AaaUserConsts.ACCOUNT_STATUS_ACTIVE
    new_user.name = username
    new_user.pwd = password
    new_user.priv = privilege

    handle.set_mo(new_user)
    return new_user


def user_exists(handle, username=None, privilege=None):
    """
    This method checks if a user exists with attributes passed

    Args:
        handle (ImcHandle)
        username (string): username
        privilege (string): "admin", "read-only", "user"

    Returns:
        True if the user exists, else False

    Examples:
        user_exists(handle, username="abcd", privilege="admin")
    """

    from imcsdk.mometa.aaa.AaaUser import AaaUserConsts
    aaausers = handle.query_classid("AaaUser")
    for user in aaausers:
        if ((user.account_status == AaaUserConsts.ACCOUNT_STATUS_ACTIVE) and
                (user.name == username) and
                (user.priv == privilege)):
            return True
    return False


def modify_local_user(handle, username=None, password=None, privilege=None):
    """
    This method will modify the user with the username specified

    Args:
        handle (ImcHandle)
        username (string): username
        password (string): password
        privilege (string): "admin", "read-only", "user"

    Returns:
        AaaUser object corresponding to the user created

    Raises:
        Exception when user is not found
    """

    from imcsdk.mometa.aaa.AaaUser import AaaUserConsts
    from imcsdk.imcexception import ImcOperationError

    found_user = None
    aaausers = handle.query_classid("AaaUser")
    for user in aaausers:
        if ((user.account_status == AaaUserConsts.ACCOUNT_STATUS_ACTIVE) and
                (user.name == username)):
            found_user = user
            break

    if found_user is None:
        raise ImcOperationError("Modify Local User", "User doesn't exist")

    if password:
        found_user.pwd = password

    if privilege:
        found_user.priv = privilege

    handle.set_mo(found_user)


def delete_local_user(handle, username):
    """
    This method deactivates the user referred to by the username passed

    Args:
        handle (ImcHandle)
        username (string): username

    Returns:
        None

    Raises:
        ImcOperationError if the user is not found
    """

    from imcsdk.mometa.aaa.AaaUser import AaaUserConsts
    from imcsdk.imcexception import ImcOperationError

    found_user = None
    aaausers = handle.query_classid("AaaUser")
    for user in aaausers:
        if user.name == username:
            found_user = user
            break

    if found_user is None:
        raise ImcOperationError("Delete Local User", "User doesn't exist")

    found_user.account_status = AaaUserConsts.ACCOUNT_STATUS_INACTIVE
    found_user.priv = AaaUserConsts.PRIV_READ_ONLY
    found_user.admin_action = AaaUserConsts.ADMIN_ACTION_CLEAR

    handle.set_mo(found_user)


def get_active_user_sessions(handle, dump=False):
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
