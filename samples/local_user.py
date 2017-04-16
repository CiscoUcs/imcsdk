# Copyright 2015 Cisco Systems, Inc.
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
This module performs the operation related to user.
"""


def user_create(handle, id, name, pwd, account_status="active",
                priv="read-only"):
    """
    Creates user and assign role to it.

    Args:
        handle (ImcHandle)
        id (string): user id
        name (string): name
        pwd (string): pwd
        account_status (string): account_status
        priv (string): user role

    Returns:
        AaaUser: Managed Object

    Example:
        user_create(handle, id=4, name="test",
                  pwd="p@ssw0rd",account_status="active")
    """

    from imcsdk.mometa.aaa.AaaUser import AaaUser

    mo = AaaUser(parent_mo_or_dn="sys/user-ext", id=id,
                 name=name,
                 pwd=pwd,
                 priv=priv,
                 account_status=account_status)

    handle.add_mo(mo, True)
    return mo


def user_exists(handle, name, priv="read-only",account_status="active"):
    """
    checks if user exists

    Args:
        handle (UcsHandle)
        name (string): name
        priv (string): user role
        account_status (string): account_status

    Returns:
        True/False

    Example:
        user_exists(handle, name="test",
                  pwd="p@ssw0rd", account_status="active")
    """

    dn = "sys/user-ext"
    mo_list = handle.query_children(in_dn=dn,class_id="aaaUser")
    for mo in mo_list:
        if ((mo.name == name) and
                (mo.priv == priv) and
                (mo.account_status == account_status)):
            return True
    return False


def user_modify(handle, id, name=None,pwd=None, priv=None,
                account_status=None):
    """
    modifies user

    Args:
        handle (UcsHandle)
        id (string): user id
        name (string): name
        pwd (string): pwd
        priv (string): user role
        account_status (string): account_status

    Returns:
        AaaUser: Managed Object

    Raises:
        ValueError: If AaaUser is not present

    Example:
        user_modify(handle, id, name="test",
                  account_status="active")
    """

    dn = "sys/user-ext/user-" + id
    mo = handle.query_dn(dn)
    if not mo:
        raise ValueError("User does not exist.")

    if pwd is not None:
        mo.pwd = pwd
    if name is not None:
        mo.name = name
    if priv is not None:
        mo.priv = priv
    if account_status is not None:
        mo.account_status = account_status

    handle.set_mo(mo)
    return mo


def user_delete(handle, name):
    """
    deletes user

    Args:
        handle (UcsHandle)
        name (string): name

    Returns:
        None

    Raises:
        ValueError: If AaaUser is not present

    Example:
        user_modify(handle, name="test")
    """
    user_exist = 0
    dn = "sys/user-ext"
    mo_list = handle.query_children(in_dn=dn,class_id="aaaUser")
    for mo in mo_list:
        if mo.name != name:
            continue
        else:
            mo.admin_action = "clear"
            handle.set_mo(mo)
            user_exist +=1
            break
    if not user_exist:
        raise ValueError("User does not exist.")
