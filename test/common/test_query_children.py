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

from nose.tools import *
from ..connection.info import custom_setup, custom_teardown

handle = None
user_list = []


def setup_module():
    from imcsdk.mometa.aaa.AaaUser import AaaUser

    global handle
    handle = custom_setup()
    # user_class = handle.query_dn("sys/user-ext")
    #
    # user_TEST = AaaUser(parent_mo_or_dn=user_class, name="TEST", pwd="Nbv12345",
    #                     id="12", priv="read-only")
    # handle.add_mo(user_TEST, True)
    # user_list.append(user_TEST)
    #
    # user_TEST1 = AaaUser(parent_mo_or_dn=user_class, name="TEST1",
    #                      pwd="Nbv12345", id="13", priv="read-only")
    # handle.add_mo(user_TEST1, True)
    # user_list.append(user_TEST1)


def teardown_module():
    # for us in user_list:
    #     handle.remove_mo(us)
    custom_teardown(handle)


def test_default():
    mos = handle.query_children(in_dn="sys/user-ext", class_id="aaaUser")
    for mo in mos:
        assert_equal(mo._class_id,"AaaUser")

