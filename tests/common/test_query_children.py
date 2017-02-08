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

from nose.tools import assert_equal
from ..connection.info import custom_setup, custom_teardown
from imcsdk.imccoreutils import IMC_PLATFORM

handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    custom_teardown(handle)


def test_default():
    mos = handle.query_children(in_dn="sys/user-ext", class_id="aaaUser")
    for mo in mos:
        assert_equal(mo._class_id, "AaaUser")


def test_hierarchy():
    mos = handle.query_children(in_dn="sys/svc-ext", hierarchy=True)
    assert_equal(len(mos) > 30, True)


def test_hierarchy_with_empty_class_id():
    mos = handle.query_children(in_dn="sys/svc-ext", hierarchy=True, class_id="")
    assert_equal(len(mos) > 30, True)


def test_hierarchy_with_class_id():
    mos = handle.query_children(in_dn="sys/svc-ext", class_id="commSnmpUser",
                                hierarchy=True)
    for mo in mos:
        assert_equal(mo._class_id, "CommSnmpUser")


def test_full_hierarchy():
    mos = handle.query_children(in_dn='sys', hierarchy=True)
