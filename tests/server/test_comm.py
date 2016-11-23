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

from imcsdk.apis.server.remotepresence import kvm_setup, kvm_disable, \
        is_kvm_enabled, sol_setup, sol_disable, is_sol_enabled

handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_kvm_enable():
    global handle

    kvm_setup(handle, max_sessions=3, port=2069)
    assert_equal(is_kvm_enabled(handle), True)


def test_kvm_disable():
    global handle

    kvm_disable(handle)
    assert_equal(is_kvm_enabled(handle), False)


def test_sol_enable():
    global handle

    sol_setup(handle, speed="9600", com_port="com0", ssh_port="1026")
    assert_equal(is_sol_enabled(handle), True)


def test_sol_disable():
    global handle

    sol_disable(handle)
    assert_equal(is_sol_enabled(handle), False)
