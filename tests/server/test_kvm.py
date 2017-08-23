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

from imcsdk.apis.server.kvm import kvm_enable
from imcsdk.apis.server.kvm import kvm_disable
from imcsdk.apis.server.kvm import kvm_exists

handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_kvm_enable():
    kvm_enable(handle, total_sessions=3, port=2069)
    assert_equal(kvm_exists(handle)[0], True)


def test_kvm_disable():
    kvm_disable(handle)
    assert_equal(kvm_exists(handle)[0], False)
