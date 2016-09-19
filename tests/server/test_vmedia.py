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

from mock import patch, call
from nose.tools import assert_raises
from imcsdk.imchandle import ImcHandle
from imcsdk.imcexception import ImcOperationError
from imcsdk.mometa.comm.CommVMediaMap import CommVMediaMap
from imcsdk.apis.server.remotepresence import vmedia_mount_remove_all


@patch.object(ImcHandle, 'remove_mo')
@patch.object(ImcHandle, 'query_children')
@patch.object(ImcHandle, 'login')
def test_valid_remove_vmedia_all(login_mock, query_mock, remove_mock):
    # Patch ImcHandle.login to create a Faux ImcHandle object w/o real CIMC
    # Patch ImcHandle.query_children to simulate CIMC interaction w/o real CIMC
    # Patch ImcHandle.remove_mo to simulate CIMC interaction w/o real CIMC
    login_mock.return_value = True
    test_cimc = ImcHandle(ip='169.254.1.1',
                          username='admin',
                          password='right')

    # Scenario: server has no vmedia mounts
    query_mock.return_value = []
    assert vmedia_mount_remove_all(test_cimc) is True
    assert remove_mock.mock_calls == []

    # Scenario: Three pre-exising mounts, removed successfully
    vmedia1 = CommVMediaMap(parent_mo_or_dn="sys/svc-ext/vmedia-svc",
                            volume_name="One.iso")
    vmedia1.remote_share = "http://169.254.1.2/"
    vmedia1.remote_file = "One.iso"
    vmedia2 = CommVMediaMap(parent_mo_or_dn="sys/svc-ext/vmedia-svc",
                            volume_name="Two")
    vmedia2.remote_share = "http://169.254.1.2/"
    vmedia2.remote_file = "Two.iso"
    vmedia3 = CommVMediaMap(parent_mo_or_dn="sys/svc-ext/vmedia-svc",
                            volume_name="Three")
    vmedia3.remote_share = "http://169.254.1.2/"
    vmedia3.remote_file = "Three.iso"
    # children_mocked call first time in remove_existing_virtual_media
    # children_mock called a second time in get_existing_virtual_media_uri
    query_mock.side_effect = [[vmedia1, vmedia2, vmedia3], []]
    assert vmedia_mount_remove_all(test_cimc) is True
    assert remove_mock.mock_calls == [call(vmedia1),
                                      call(vmedia2),
                                      call(vmedia3)]


@patch.object(ImcHandle, 'remove_mo')
@patch.object(ImcHandle, 'query_children')
@patch.object(ImcHandle, 'login')
def test_invalid_remove_vmedia_all(login_mock, query_mock, remove_mock):
    # Patch ImcHandle.login to create a Faux ImcHandle object w/o real CIMC
    # Patch ImcHandle.query_children to simulate CIMC interaction w/o real CIMC
    # Patch ImcHandle.remove_mo to simulate CIMC interaction w/o real CIMC
    login_mock.return_value = True
    test_cimc = ImcHandle(ip='169.254.1.1',
                          username='admin',
                          password='right')

    # Scenario: Three pre-exising mounts, only two unsuccessfully
    vmedia1 = CommVMediaMap(parent_mo_or_dn="sys/svc-ext/vmedia-svc",
                            volume_name="One.iso")
    vmedia1.remote_share = "http://169.254.1.2/"
    vmedia1.remote_file = "One.iso"
    vmedia2 = CommVMediaMap(parent_mo_or_dn="sys/svc-ext/vmedia-svc",
                            volume_name="Two")
    vmedia2.remote_share = "http://169.254.1.2/"
    vmedia2.remote_file = "Two.iso"
    vmedia3 = CommVMediaMap(parent_mo_or_dn="sys/svc-ext/vmedia-svc",
                            volume_name="Three")
    vmedia3.remote_share = "http://169.254.1.2/"
    vmedia3.remote_file = "Three.iso"
    query_mock.side_effect = [[vmedia1, vmedia2, vmedia3], [vmedia1]]
    assert_raises(ImcOperationError, vmedia_mount_remove_all, test_cimc)
