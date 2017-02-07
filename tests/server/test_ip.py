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

import time
from nose.tools import assert_equal
from ..connection.info import custom_setup, custom_teardown

from imcsdk.apis.admin.ip import ip_blocking_enable, ip_blocking_disable, \
    is_ip_blocking_enabled, ip_blocking_exists,\
    ip_filtering_enable, ip_filtering_disable, \
    ip_filtering_modify, ip_filtering_clear, is_ip_filtering_enabled, \
    ip_filtering_exists

handle = None
SLEEP_TIME = 25


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_ip_blocking_enable():
    ip_blocking_enable(handle, fail_count='6', fail_window='120', penalty_time='800')
    assert_equal(is_ip_blocking_enabled(handle), True)


def test_ip_blocking_exists():
    match, mo = ip_blocking_exists(handle,
                                   fail_count='6',
                                   fail_window='120',
                                   penalty_time='800')
    assert_equal(match, True)
    match, mo = ip_blocking_exists(handle,
                                   fail_count='8',
                                   fail_window='120',
                                   penalty_time='500')
    assert_equal(match, False)


def test_ip_blocking_disable():
    ip_blocking_disable(handle)
    assert_equal(is_ip_blocking_enabled(handle), False)


ip_filters = [{"id": 1, "filter": "1.1.1.1-255.255.255.255"},
              {"id": 2, "filter": "2.2.2.2"},
              ]

ip_filters_2 = [{"id": 1, "filter": "1.1.1.0-255.255.255.255"},
                {"id": 3, "filter": "2.2.2.5"},
                ]


def test_ip_filtering_enable():
    ip_filtering_clear(handle, filter_id='all')
    handle.logout()
    time.sleep(SLEEP_TIME)
    handle.login()
    ip_filtering_enable(handle, filters=ip_filters)
    handle.logout()
    time.sleep(SLEEP_TIME)
    handle.login()
    assert_equal(is_ip_filtering_enabled(handle), True)


def test_ip_filtering_exists():
    match, mo = ip_filtering_exists(handle, enable='yes', filters=ip_filters)
    assert_equal(match, True)
    match, mo = ip_filtering_exists(handle, enable='yes', filters=ip_filters_2)
    assert_equal(match, False)


def test_ip_filtering_modify():
    ip_filtering_modify(handle, filters=ip_filters_2)
    handle.logout()
    time.sleep(SLEEP_TIME)
    handle.login()
    match, mo = ip_filtering_exists(handle, enable='yes',
                    filters=[{"id": 1, "filter": "1.1.1.0-255.255.255.255"},
                             {"id": 2, "filter": "2.2.2.2"},
                             {"id": 3, "filter": "2.2.2.5"},
                             ])
    assert_equal(match, True)


def test_ip_filtering_clear():
    ip_filtering_clear(handle, filter_id='3')
    handle.logout()
    time.sleep(SLEEP_TIME)
    handle.login()
    match, mo = ip_filtering_exists(handle, enable='yes',
                    filters=[{"id": 1, "filter": "1.1.1.0-255.255.255.255"},
                             {"id": 2, "filter": "2.2.2.2"}
                             ])
    assert_equal(match, True)


def test_ip_filtering_disable():
    ip_filtering_disable(handle)
    handle.logout()
    time.sleep(SLEEP_TIME)
    handle.login()
    assert_equal(is_ip_blocking_enabled(handle), False)


def test_ip_filtering_clear_all():
    ip_filtering_clear(handle, filter_id='all')
    match, mo = ip_filtering_exists(handle, enable='no',
                                    filters=[{"id": 1, "filter": ""},
                                             {"id": 2, "filter": ""}
                                             ])
    assert_equal(match, True)


