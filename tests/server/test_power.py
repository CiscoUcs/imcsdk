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
from imcsdk.apis.server.serveractions import server_power_down, \
    server_power_up, server_power_cycle, server_power_state_get
from imcsdk.mometa.compute.ComputeRackUnit import ComputeRackUnitConsts

handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_power_down_server():
    global handle
    server_power_down(handle)
    assert_equal(server_power_state_get(handle),
                 ComputeRackUnitConsts.OPER_POWER_OFF)


def test_power_up_server():
    global handle
    server_power_up(handle)
    assert_equal(server_power_state_get(handle),
                 ComputeRackUnitConsts.OPER_POWER_ON)


def test_power_cycle_server():
    global handle
    server_power_cycle(handle, timeout=180)
    assert_equal(server_power_state_get(handle),
                 ComputeRackUnitConsts.OPER_POWER_ON)
