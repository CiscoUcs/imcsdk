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

from imcsdk.apis.admin.ntp import ntp_enable, ntp_disable, is_ntp_enabled, \
        ntp_setting_exists, ntp_servers_modify, ntp_servers_clear

handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


ntp_servers = [{"id": 1, "ip": "192.168.1.1"},
               {"id": 2, "ip": "192.168.1.2"},
               {"id": 3, "ip": "192.168.1.3"},
               {"id": 4, "ip": "1.2.3.4"}]

ntp_servers_2 = [{"id": 1, "ip": "192.168.1.1"},
                 {"id": 2, "ip": ""},
                 {"id": 3, "ip": "192.168.1.3"},
                 {"id": 4, "ip": "1.1.1.1"},
                 {"id": 5, "ip": "2.2.2.2"}]


ntp_servers_3 = [{"id": 1, "ip": "192.168.1.1"},
                 {"id": 2, "ip": ""},
                 {"id": 3, "ip": "192.168.1.3"},
                 {"id": 4, "ip": "1.1.1.1"}]


def test_ntp_enable():
    ntp_enable(handle, ntp_servers=ntp_servers)
    assert_equal(is_ntp_enabled(handle), True)


def test_ntp_setting_exists():
    match, mo = ntp_setting_exists(handle,
                                   ntp_enable="yes",
                                   ntp_servers=ntp_servers)
    assert_equal(match, True)


@raises(Exception)
def test_ntp_enable_2():
    ntp_enable(handle, ntp_servers=ntp_servers_2)
    match, mo = ntp_setting_exists(handle,
                                   ntp_servers=ntp_servers_2)
    assert_equal(match, True)


@raises(Exception)
def test_ntp_setting_exists_2():
    match, mo = ntp_setting_exists(handle,
                                   ntp_enable="yes",
                                   ntp_servers=ntp_servers_2)
    assert_equal(match, True)


def test_ntp_setting_exists_3():
    match, mo = ntp_setting_exists(handle,
                                   ntp_enable="yes")
    assert_equal(match, True)


def test_ntp_servers_modify():
    ntp_servers_modify(handle, ntp_servers=ntp_servers_3)
    match, mo = ntp_setting_exists(handle,
                                   ntp_enable="yes",
                                   ntp_servers=ntp_servers_3)
    assert_equal(match, True)


def test_ntp_servers_clear():
    ntp_servers_clear(handle, ntp_servers=["192.168.1.3", "1.1.1.1"])
    match, mo = ntp_setting_exists(handle, ntp_enable="yes",
                                   ntp_servers=[{"id": 1, "ip": "192.168.1.1"}])
    assert_equal(match, True)


@raises(Exception)
def test_ntp_servers_clear_all_enabled():
    ntp_servers_clear(handle)
    match, mo = ntp_setting_exists(handle, ntp_enable="yes",
                                   ntp_servers=[{"id": 1, "ip": ""},
                                                {"id": 2, "ip": ""},
                                                {"id": 3, "ip": ""},
                                                {"id": 4, "ip": ""}])


def test_ntp_disable():
    ntp_disable(handle)
    assert_equal(is_ntp_enabled(handle), False)


def test_ntp_servers_clear_all_disabled():
    ntp_servers_clear(handle)
    match, mo = ntp_setting_exists(handle, ntp_enable="no",
                                   ntp_servers=[{"id": 1, "ip": ""},
                                                {"id": 2, "ip": ""},
                                                {"id": 3, "ip": ""},
                                                {"id": 4, "ip": ""}])
