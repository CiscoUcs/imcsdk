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
from imcsdk.apis.admin.user import create_local_user, delete_local_user, user_exists
from imcsdk.apis.admin.snmp import snmp_enable, snmp_disable, snmp_enabled, \
    snmp_user_add, snmp_user_exists, snmp_user_remove, \
    snmp_trap_add, snmp_trap_exists, snmp_trap_remove

handle = None
snmp_trap_id = 0


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_local_user_create():
    global handle
    create_local_user(handle, "nosetest", "Nbv-12345", "admin")
    assert_equal(user_exists(handle, "nosetest", "admin"), True)


def test_local_user_delete():
    global handle
    delete_local_user(handle, "nosetest")
    assert_equal(user_exists(handle, "nosetest", "admin"), False)


def test_snmp_enable():
    global handle
    snmp_enable(handle, community="test", privilege="full",
                trap_community="test-trap",
                sys_contact="abcd@pqrs.com", sys_location="somewhere")
    assert_equal(snmp_enabled(handle), True)


def test_snmp_user_create():
    global handle
    snmp_user = snmp_user_add(handle, name="test-snmp-user",
                              security_level="authpriv",
                              auth_pwd="Nbv-12345", auth="MD5",
                              priv_pwd="Nbv-12345", priv="AES")
    assert_equal(snmp_user_exists(
        handle, name="test-snmp-user"), int(snmp_user.id))


def test_snmp_trap_create():
    global handle, snmp_trap_id
    snmp_trap = snmp_trap_add(handle, hostname="2.2.2.2", port="3000",
                              version="v3", notification_type="traps",
                              user="test-snmp-user")
    snmp_trap_id = int(snmp_trap.id)
    assert_equal(snmp_trap_exists(handle, hostname="2.2.2.2", port="3000",
                                  version="v3", notification_type="traps",
                                  user="test-snmp-user"), snmp_trap_id)


def test_snmp_trap_delete():
    global handle, snmp_trap_id
    snmp_trap_remove(handle, snmp_trap_id)
    assert_equal(snmp_trap_exists(handle, hostname="2.2.2.2", port="3000",
                                  version="v3", notification_type="traps",
                                  user="test-snmp-user"), 0)


def test_snmp_user_delete():
    global handle
    snmp_user_remove(handle, name="test-snmp-user")
    assert_equal(snmp_user_exists(handle, name="test-snmp-user"), 0)


def test_snmp_disable():
    global handle
    snmp_disable(handle)
    assert_equal(snmp_enabled(handle), False)
