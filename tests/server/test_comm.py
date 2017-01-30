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
        is_kvm_enabled, sol_setup, sol_disable, is_sol_enabled, \
        vmedia_setup, vmedia_disable

handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_kvm_enable():
    kvm_setup(handle, max_sessions=3, port=2069)
    assert_equal(is_kvm_enabled(handle), True)


def test_kvm_disable():
    kvm_disable(handle)
    assert_equal(is_kvm_enabled(handle), False)


def test_sol_enable():
    sol_setup(handle, speed="9600", comport="com0", ssh_port=1026)
    assert_equal(is_sol_enabled(handle), True)


def test_sol_disable():
    sol_disable(handle)
    assert_equal(is_sol_enabled(handle), False)


def test_vmedia_setup():
    vmedia_setup(handle, encrypt=True, low_power_usb=True)


def test_vmedia_disable():
    vmedia_disable(handle)

