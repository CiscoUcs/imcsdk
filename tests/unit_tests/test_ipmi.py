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

from mock import patch
from nose.tools import assert_raises
from imcsdk.imchandle import ImcHandle
from imcsdk.mometa.comm.CommIpmiLan import CommIpmiLanConsts
from imcsdk.apis.admin.ipmi import disable_ipmi, enable_ipmi


@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'login')
def test_valid_enable_ipmi(login_mock, set_mo_mock):
    # Patch ImcHandle.login to create a Faux ImcHandle object w/o real CIMC
    # Patch ImcHandle.set_mo to simulate CIMC interaction w/o real CIMC
    login_mock.return_value = True
    set_mo_mock.return_value = True
    test_cimc = ImcHandle(ip='169.254.1.1',
                          username='admin',
                          password='right')

    # Scenario: Enable IPMI default values
    assert enable_ipmi(test_cimc) is True
    # Assert values of the object passed to add_mo()
    test_ipmi_mo = set_mo_mock.call_args[0][0]
    assert test_ipmi_mo.admin_state == "enabled"
    assert test_ipmi_mo.priv == CommIpmiLanConsts.PRIV_ADMIN
    assert test_ipmi_mo.key == '0'*40

    # Scenario: Enable IPMI custom priv and key
    assert enable_ipmi(test_cimc, priv="user", key='1'*40) is True
    test_ipmi_mo = set_mo_mock.call_args[0][0]
    assert test_ipmi_mo.admin_state == "enabled"
    assert test_ipmi_mo.priv == "user"
    assert test_ipmi_mo.key == '1'*40


@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'login')
def test_invalid_enable_ipmi(login_mock, set_mo_mock):
    # Patch ImcHandle.login to create a Faux ImcHandle object w/o real CIMC
    # Patch ImcHandle.set_mo to simulate CIMC interaction w/o real CIMC
    login_mock.return_value = True
    set_mo_mock.return_value = True
    test_cimc = ImcHandle(ip='169.254.1.1',
                          username='admin',
                          password='right')

    # Scenario: Invalid priv value
    assert_raises(ValueError, enable_ipmi, test_cimc, priv="Wrong")

    # Scenario: Invalid key
    assert_raises(ValueError, enable_ipmi, test_cimc, key='bacon')


@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'login')
def test_valid_disable_ipmi(login_mock, set_mo_mock):
    # Patch ImcHandle.login to create a Faux ImcHandle object w/o real CIMC
    # Patch ImcHandle.set_mo to simulate CIMC interaction w/o real CIMC
    login_mock.return_value = True
    set_mo_mock.return_value = True
    test_cimc = ImcHandle(ip='169.254.1.1',
                          username='admin',
                          password='right')

    # Scenario: Enable IPMI default values
    assert disable_ipmi(test_cimc) is True
    # Assert values of the object passed to add_mo()
    test_ipmi_mo = set_mo_mock.call_args[0][0]
    assert test_ipmi_mo.admin_state == "disabled"