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

from nose.tools import assert_equal, raises
from ..connection.info import custom_setup, custom_teardown

from imcsdk.apis.admin.ldap import ldap_enable, ldap_exists,\
        ldap_role_group_create, ldap_role_group_exists, ldap_role_group_delete,\
        ldap_certificate_management_enable, ldap_certificate_management_disable,\
        is_ldap_certificate_management_enabled

handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


ldap_servers = [{"id": 1, "ip": "192.168.1.1", "port": 400},
                {"id": 2, "ip": "192.168.1.2", "port": 500},
                {"id": 3, "ip": "192.168.1.3", "port": 600},
                {"id": 4, "ip": "1.2.3.4", "port": 700}]

ldap_servers_2 = [{"id": 1, "ip": "192.168.1.1", "port": 400},
                  {"id": 2, "ip": "192.168.1.2", "port": 500},
                  {"id": 3, "ip": "192.168.1.3", "port": 600},
                  {"id": 4, "ip": "1.2.3.4", "port": 700},
                  {"id": 5, "ip": "192.168.1.5", "port": 600},
                  {"id": 6, "ip": "192.168.1.63", "port": 600},
                  {"id": 7, "ip": "192.168.1.13", "port": 600}]

ldap_servers_3 = [{"id": 1, "ip": "192.168.1.1", "port": 400},
                  {"id": 2, "ip": "192.168.1.2", "port": 500},
                  {"id": 3, "ip": "192.168.1.100", "port": 600},
                  {"id": 4, "ip": "1.2.3.4", "port": 800}]


def test_ldap_enable():
    ldap_enable(
        handle,
        basedn='DC=QATCSLABTPI02,DC=cisco,DC=com',
        domain='QATCSLABTPI02.cisco.com',
        timeout=20, group_auth="enabled",
        bind_dn='CN=administrator,CN=Users,DC=QATCSLABTPI02,DC=cisco,DC=com',
        password='abcdefg', ldap_servers=ldap_servers)
    match, mo = ldap_exists(
        handle,
        basedn='DC=QATCSLABTPI02,DC=cisco,DC=com',
        domain='QATCSLABTPI02.cisco.com',
        timeout=20, group_auth="enabled",
        bind_dn='CN=administrator,CN=Users,DC=QATCSLABTPI02,DC=cisco,DC=com',
        password='abcdefg', ldap_servers=ldap_servers)
    assert_equal(match, True)


def test_ldap_mismatch_config():
    match, mo = ldap_exists(
        handle,
        basedn='DC=QATCSLABTPI02,DC=cisco,DC=com',
        domain='QATCSLABTPI02.cisco.com',
        timeout=100, group_auth="disabled",
        bind_dn='CN=administrator,CN=Users,DC=QATCSLABTPI02,DC=cisco,DC=com',
        password='abcdefg', ldap_servers=ldap_servers)
    assert_equal(match, False)


def test_ldap_mismatch_config_servers():
    match, mo = ldap_exists(
        handle,
        basedn='DC=QATCSLABTPI02,DC=cisco,DC=com',
        domain='QATCSLABTPI02.cisco.com',
        timeout=20, group_auth="enabled",
        bind_dn='CN=administrator,CN=Users,DC=QATCSLABTPI02,DC=cisco,DC=com',
        password='abcdefg', ldap_servers=ldap_servers_3)
    assert_equal(match, False)


@raises(Exception)
def test_ldap_enable_invalid_servers():
    ldap_enable(
        handle,
        basedn='DC=QATCSLABTPI02,DC=cisco,DC=com',
        domain='QATCSLABTPI02.cisco.com',
        timeout=20, group_auth="enabled",
        bind_dn='CN=administrator,CN=Users,DC=QATCSLABTPI02,DC=cisco,DC=com',
        password='abcdefg', ldap_servers=ldap_servers_2)


def test_ldap_role_group_create():
    ldap_role_group_create(handle, domain='abcd.pqrs.com', name='abcd', role='user')
    match, mo = ldap_role_group_exists(handle, domain='abcd.pqrs.com', name='abcd', role='user')
    assert_equal(match, True)


def test_ldap_role_group_delete():
    ldap_role_group_delete(handle, domain='abcd.pqrs.com', name='abcd')
    match, mo = ldap_role_group_exists(handle, domain='abcd.pqrs.com', name='abcd', role='user')
    assert_equal(match, False)


def test_ldap_cert_mgmt_enable():
    ldap_certificate_management_enable(handle)
    assert_equal(is_ldap_certificate_management_enabled(handle), True)


def test_ldap_cert_mgmt_disable():
    ldap_certificate_management_disable(handle)
    assert_equal(is_ldap_certificate_management_enabled(handle), False)


def test_ldap_disable():
    ldap_enable(handle)
