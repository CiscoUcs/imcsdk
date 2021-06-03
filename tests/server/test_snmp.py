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

from nose.tools import raises

from ..connection.info import custom_setup, custom_teardown

from imcsdk.imcexception import ImcException
from imcsdk.apis.admin.snmp import snmp_enable
from imcsdk.apis.admin.snmp import snmp_disable
from imcsdk.apis.admin.snmp import snmp_user_add_all
from imcsdk.apis.admin.snmp import snmp_user_delete_all
from imcsdk.apis.admin.snmp import snmp_trap_add_all
from imcsdk.apis.admin.snmp import snmp_trap_delete_all

handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_snmp_enable():
    snmp_enable(handle)


def test_snmp_enable_b2b():
    snmp_enable(handle)


def test_snmp_enable_default():
    params = {
        "port": 161,
        "com2_sec": "disabled",
        "sys_contact": "contact",
        "sys_location": "location"
    }
    snmp_enable(handle, **params)


def test_snmp_enable_with_empty_string():
    params = {
        "port": 161,
        "com2_sec": "disabled",
        "community": "",
        "trap_community": "",
        "engine_id_key": "",
        "sys_contact": "contact",
        "sys_location": "location"
    }
    snmp_enable(handle, **params)


def test_snmp_v2_enable_v3_disable():
    params = {
        "port": 161,
        "com2_sec": "full",
        "community": "cisco",
        "trap_community": "cisco",
        "sys_contact": "cisco",
        "sys_location": "cisco",
        "snmpv2_enable": "enabled",
        "snmpv3_enable": "disabled"
    }
    snmp_enable(handle, **params)


def test_snmp_v2_disable_v3_enable():
    params = {
        "port": 161,       
        "sys_contact": "cisco",
        "sys_location": "cisco",
        "engine_id_key": "cisco",
        "snmpv2_enable": "disabled",
        "snmpv3_enable": "enabled"
    }
    snmp_enable(handle, **params)


def test_snmp_v2_v3_enable():
    params = {
        "port": 161,
        "com2_sec": "full",
        "community": "cisco",
        "trap_community": "cisco",
        "engine_id_key": "cisco",
        "sys_contact": "cisco",
        "sys_location": "cisco",
        "snmpv2_enable": "enabled",
        "snmpv3_enable": "enabled"
    }
    snmp_enable(handle, **params)


@raises(ImcException)
def test_snmp_enable_syslocation_empty():
    params = {
        "sys_contact": "",
    }
    snmp_enable(handle, **params)


@raises(ImcException)
def test_snmp_enable_syscontact_empty():
    params = {
        "sys_location": ""
    }
    snmp_enable(handle, **params)


def test_snmp_mutltiple_config_with_configcommit_for_hp_and_above():
    from imcsdk.apis.versionconstraints.snmp import \
        snmp_multiple_config_with_configcommit_for_hp_and_above

    mos = handle.query_classid("CommSnmpUser")
    snmp_multiple_config_with_configcommit_for_hp_and_above(handle, mos)


def test_snmp_user_add_all():
    users = []
    for i in range(1, 16):
        name = "user" + str(i)
        security_level = 'noauthnopriv'
        user = {'name': name, 'security_level': security_level}
        users.append(user)
    snmp_user_add_all(handle, users)


def test_snmp_user_delete_all():
    snmp_user_delete_all(handle)


def test_snmp_trap_add_all():
    traps = []
    for i in range(1, 16):
        hostname = "10.10.10." + str(i)
        port = 162
        version = "v2c"
        notification_type = "informs"
        trap_community_string = "cisco"
        trap = {'hostname': hostname,
                'port': port,
                'version': version,
                'notification_type': notification_type,
                'trap_community_string': trap_community_string}
        traps.append(trap)
    snmp_trap_add_all(handle, traps)


def test_snmp_trap_delete_all():
    snmp_trap_delete_all(handle)


def test_snmp_disable():
    snmp_disable(handle)
