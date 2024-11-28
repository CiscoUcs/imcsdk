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

from mock import patch, MagicMock
from nose.tools import assert_raises
from imcsdk.imchandle import ImcHandle
from imcsdk.imcexception import ImcOperationError
from imcsdk.apis.server.serveractions import server_power_down, server_power_up
from imcsdk.imccoreutils import IMC_PLATFORM


@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_dn')
@patch.object(ImcHandle, 'login')
def test_valid_power_down_server(login_mock, query_dn_mock, set_mo_mock):
    # Patch ImcHandle.login to create a Faux ImcHandle object w/o real CIMC
    # Patch ImcHandle.query_dn to simulate CIMC interaction w/o real CIMC
    # Patch ImcHandle.set_mo to simulate CIMC interaction w/o real CIMC
    login_mock.return_value = True
    set_mo_mock.return_value = True
    pwrd_off_mock = MagicMock()
    pwrd_off_mock.oper_power = "off"
    pwrd_on_mock = MagicMock()
    pwrd_on_mock.oper_power = "on"
    test_cimc = ImcHandle(ip='169.254.1.1',
                          username='admin',
                          password='right')
    test_cimc._set_platform(platform=IMC_PLATFORM.TYPE_CLASSIC)

    # Scenario: server starts powered off
    query_dn_mock.return_value = pwrd_off_mock
    assert server_power_down(test_cimc, 0, 1) is pwrd_off_mock

    # Scenario: server starts powered on, and powers off successfully
    query_dn_mock.side_effect = [pwrd_on_mock, pwrd_off_mock, pwrd_off_mock, pwrd_off_mock]
    assert server_power_down(test_cimc, 0, 1) is pwrd_off_mock


@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_dn')
@patch.object(ImcHandle, 'login')
def test_invalid_power_down_server(login_mock, query_dn_mock, set_mo_mock):
    # Patch ImcHandle.login to create a Faux ImcHandle object w/o real CIMC
    # Patch ImcHandle.query_dn to simulate CIMC interaction w/o real CIMC
    # Patch ImcHandle.set_mo to simulate CIMC interaction w/o real CIMC
    # Patch ComputeRackUnit.oper_power to simulate power state
    login_mock.return_value = True
    set_mo_mock.return_value = True
    pwrd_off_mock = MagicMock()
    pwrd_off_mock.oper_power = "off"
    pwrd_on_mock = MagicMock()
    pwrd_on_mock.oper_power = "on"
    test_cimc = ImcHandle(ip='169.254.1.1',
                          username='admin',
                          password='right')
    test_cimc._set_platform(platform=IMC_PLATFORM.TYPE_CLASSIC)

    # Scenario: Zero value passed in as check interval
    assert_raises(ValueError, server_power_down, test_cimc, 0, 0)

    # Scenario: server starts power on, and doesn't power off
    query_dn_mock.return_value = pwrd_on_mock
    assert_raises(ImcOperationError, server_power_down, test_cimc, 0, 1)


@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_dn')
@patch.object(ImcHandle, 'login')
def test_valid_power_up_server(login_mock, query_dn_mock, set_mo_mock):
    # Patch ImcHandle.login to create a Faux ImcHandle object w/o real CIMC
    # Patch ImcHandle.query_dn to simulate CIMC interaction w/o real CIMC
    # Patch ImcHandle.set_mo to simulate CIMC interaction w/o real CIMC
    login_mock.return_value = True
    set_mo_mock.return_value = True
    pwrd_off_mock = MagicMock()
    pwrd_off_mock.oper_power = "off"
    pwrd_on_mock = MagicMock()
    pwrd_on_mock.oper_power = "on"
    test_cimc = ImcHandle(ip='169.254.1.1',
                          username='admin',
                          password='right')
    test_cimc._set_platform(platform=IMC_PLATFORM.TYPE_CLASSIC)

    # Scenario: server starts powered on
    query_dn_mock.return_value = pwrd_on_mock
    assert server_power_up(test_cimc, 0, 1) is pwrd_on_mock

    # Scenario: server starts powered off, and powers on successfully
    query_dn_mock.side_effect = [pwrd_off_mock, pwrd_on_mock, pwrd_on_mock, pwrd_on_mock]
    assert server_power_up(test_cimc, 0, 1) is pwrd_on_mock


@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_dn')
@patch.object(ImcHandle, 'login')
def test_invalid_power_up_server(login_mock, query_dn_mock, set_mo_mock):
    # Patch ImcHandle.login to create a Faux ImcHandle object w/o real CIMC
    # Patch ImcHandle.query_dn to simulate CIMC interaction w/o real CIMC
    # Patch ImcHandle.set_mo to simulate CIMC interaction w/o real CIMC
    login_mock.return_value = True
    set_mo_mock.return_value = True
    pwrd_off_mock = MagicMock()
    pwrd_off_mock.oper_power = "off"
    pwrd_on_mock = MagicMock()
    pwrd_on_mock.oper_power = "on"
    test_cimc = ImcHandle(ip='169.254.1.1',
                          username='admin',
                          password='right')
    test_cimc._set_platform(platform=IMC_PLATFORM.TYPE_CLASSIC)

    # Scenario: Zero value passed in as check interval
    assert_raises(ValueError, server_power_up, test_cimc, 0, 0)

    # Scenario: server starts power off, and doesn't power on
    query_dn_mock.return_value = pwrd_off_mock
    assert_raises(ImcOperationError, server_power_up, test_cimc, 0, 1)
