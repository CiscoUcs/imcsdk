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

from nose.tools import assert_equal
from ..connection.info import custom_setup, custom_teardown
from imcsdk.apis.admin.user import local_user_create, local_user_delete, \
    local_user_exists, strong_password_set, is_strong_password_set, \
    password_expiration_set, password_expiration_exists
from imcsdk.apis.admin.snmp import snmp_enable, snmp_disable, is_snmp_enabled,\
    snmp_user_add, snmp_user_exists, snmp_user_remove, snmp_user_modify, \
    snmp_trap_add, snmp_trap_exists, snmp_trap_remove


handle = None
snmp_trap_id = 0


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_set_strong_password():
    strong_password_set(handle)
    assert_equal(is_strong_password_set(handle), True)


def test_unset_strong_password():
    strong_password_set(handle, enable=False)
    assert_equal(is_strong_password_set(handle), False)


def test_set_password_expiration():
    mo = password_expiration_set(handle, password_expiry_duration=1000, password_history=4, password_notification_period=10)
    match, mo = password_expiration_exists(handle, password_expiry_duration=1000, password_history=4, password_notification_period=10)
    assert_equal(match, True)


def test_unset_password_expiration():
    mo = password_expiration_set(handle, password_expiry_duration=0)
    match, mo = password_expiration_exists(handle, password_expiry_duration=0)
    assert_equal(match, True)


def test_local_user_create():
    local_user_create(handle, "nosetest", "Nbv-12345", "admin")
    exists, mo = local_user_exists(handle, name="nosetest", priv="admin")
    assert_equal(exists, True)


def test_local_user_delete():
    local_user_delete(handle, "nosetest")
    exists, mo = local_user_exists(handle, name="nosetest", priv="admin")
    assert_equal(exists, False)


def test_snmp_enable():
    snmp_enable(handle, community="test", privilege="full",
                trap_community="test-trap",
                sys_contact="abcd@pqrs.com", sys_location="somewhere")
    match, mo = is_snmp_enabled(handle)
    assert_equal(match, True)


def test_snmp_user_create():
    snmp_user = snmp_user_add(handle, name="test-snmp-user",
                              security_level="authpriv",
                              auth_pwd="Nbv-12345", auth="MD5",
                              privacy_pwd="Nbv-12345", privacy="AES")
    match, mo = snmp_user_exists(handle, name="test-snmp-user")
    assert_equal(match, True)

    snmp_user = snmp_user_add(handle, name="test-snmp-user2",
                              security_level="authnopriv",
                              auth_pwd="Nbv-12345", auth="MD5",
                              privacy_pwd="Nbv-12345", privacy="AES")
    match, mo = snmp_user_exists(handle, name="test-snmp-user2")
    assert_equal(match, True)

    snmp_user = snmp_user_add(handle, name="test-snmp-user3",
                              security_level="noauthnopriv",
                              auth_pwd="Nbv-12345", auth="MD5",
                              privacy_pwd="Nbv-12345", privacy="AES")
    match, mo = snmp_user_exists(handle, name="test-snmp-user3")
    assert_equal(match, True)


def test_snmp_user_modify():
    match, mo = snmp_user_exists(handle, name="test-snmp-user")
    snmp_user = snmp_user_modify(handle, user_id=mo.id,
                                 auth_pwd="Nbv-56789",
                                 security_level="authnopriv")
    assert_equal(snmp_user.security_level, "authnopriv")


def test_snmp_trap_create():
    global snmp_trap_id
    snmp_trap = snmp_trap_add(handle, hostname="2.2.2.2", port="3000",
                              version="v3", notification_type="traps",
                              user="test-snmp-user")
    snmp_trap_id = int(snmp_trap.id)
    match, mo = snmp_trap_exists(handle, hostname="2.2.2.2", port="3000",
                                      version="v3", notification_type="traps",
                                      user="test-snmp-user")
    assert_equal(match, True)


def test_snmp_trap_delete():
    snmp_trap_remove(handle, snmp_trap_id)
    match, mo = snmp_trap_exists(handle, hostname="2.2.2.2", port="3000",
                                      version="v3", notification_type="traps",
                                      user="test-snmp-user")
    assert_equal(match, False)


def test_snmp_user_delete():
    snmp_user_remove(handle, name="test-snmp-user")
    match, mo = snmp_user_exists(handle, name="test-snmp-user")
    assert_equal(match, False)

    snmp_user_remove(handle, name="test-snmp-user2")
    match, mo = snmp_user_exists(handle, name="test-snmp-user2")
    assert_equal(match, False)

    snmp_user_remove(handle, name="test-snmp-user3")
    match, mo = snmp_user_exists(handle, name="test-snmp-user3")
    assert_equal(match, False)


def test_snmp_disable():
    snmp_disable(handle)
    match, mo = is_snmp_enabled(handle)
    assert_equal(match, False)
