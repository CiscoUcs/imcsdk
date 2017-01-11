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

from imcsdk.apis.admin.redfish import redfish_enable, redfish_disable,\
        is_redfish_enabled

handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_redfish_enable():
    redfish_enable(handle)
    assert_equal(is_redfish_enabled(handle), True)


def test_redfish_disable():
    redfish_disable(handle)
    assert_equal(is_redfish_enabled(handle), False)
