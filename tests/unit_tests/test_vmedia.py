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

from mock import patch, call, MagicMock
from nose.tools import assert_raises
from imcsdk.imchandle import ImcHandle
from imcsdk.imcexception import ImcOperationError
from imcsdk.mometa.comm.CommVMediaMap import CommVMediaMap
from imcsdk.apis.server.vmedia import vmedia_mount_iso_uri, \
                                              vmedia_mount_remove_all, \
                                              vmedia_get_existing_uri, \
                                              vmedia_get_existing_status
from imcsdk.imccoreutils import IMC_PLATFORM


@patch.object(ImcHandle, 'query_children')
@patch.object(ImcHandle, 'login')
def test_vmedia_get_existing_uri(login_mock, query_mock):
    # Patch ImcHandle.login to create a Faux ImcHandle w/o real CIMC
    # Patch ImcHandle.query_children to simulate CIMC interaction
    login_mock.return_value = True
    test_cimc = ImcHandle(ip='169.254.1.1',
                          username='admin',
                          password='right')
    test_cimc._set_platform(platform=IMC_PLATFORM.TYPE_CLASSIC)

    # Scenario: No pre-existing mappings
    query_mock.return_value = []
    assert vmedia_get_existing_uri(test_cimc) == []
    #  Assert query_children called with correct in_dn
    assert query_mock.mock_calls[0] == \
        call(in_dn='sys/svc-ext/vmedia-svc')

    # Scenario: Three pre-existing mappings
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
    query_mock.return_value = [vmedia1, vmedia2, vmedia3]
    assert vmedia_get_existing_uri(test_cimc) == \
        ["http://169.254.1.2/One.iso",
         "http://169.254.1.2/Two.iso",
         "http://169.254.1.2/Three.iso"]


@patch.object(ImcHandle, 'query_children')
@patch.object(ImcHandle, 'login')
def test_vmedia_get_existing_status(login_mock, query_mock):
    # Patch ImcHandle.login to create a Faux ImcHandle w/o real CIMC
    # Patch ImcHandle.query_children to simulate CIMC interaction
    login_mock.return_value = True
    test_cimc = ImcHandle(ip='169.254.1.1',
                          username='admin',
                          password='right')
    test_cimc._set_platform(platform=IMC_PLATFORM.TYPE_CLASSIC)

    # Scenario: No pre-existing mappings
    query_mock.return_value = []
    assert vmedia_get_existing_status(test_cimc) == []
    #  Assert query_children called with correct in_dn
    assert query_mock.mock_calls[0] == \
        call(in_dn='sys/svc-ext/vmedia-svc')

    # Scenario: Three pre-existing mappings
    # mapping_status is not a read-write property, so mock it.
    vmedia1 = MagicMock()
    vmedia1.mapping_status = "In-Progress"
    vmedia2 = MagicMock()
    vmedia2.mapping_status = "OK"
    vmedia3 = MagicMock()
    vmedia3.mapping_status = "Error"
    query_mock.return_value = [vmedia1, vmedia2, vmedia3]
    assert vmedia_get_existing_status(test_cimc) == \
        ["In-Progress", "OK", "Error"]


@patch('imcsdk.apis.server.vmedia.vmedia_get_existing_status')
@patch('imcsdk.apis.server.vmedia.vmedia_get_existing_uri')
@patch('imcsdk.apis.server.vmedia.vmedia_mount_create')
@patch.object(ImcHandle, 'login')
def test_valid_vmedia_mount_iso_uri(login_mock, add_mount_mock,
                                    exist_mock, state_mock):
    # Patch ImcHandle.login to create a Faux ImcHandle object w/o real CIMC
    # Patch vmedia_mount_create to simulate CIMC interaction w/o real CIMC
    # Patch vmedia_get_existing_uri to simulate existing ISOs
    # Patch vmedia_get_existing_status to simulate ISO status
    login_mock.return_value = True
    add_mount_mock.return_value = True
    test_cimc = ImcHandle(ip='169.254.1.1',
                          username='admin',
                          password='right')
    test_cimc._set_platform(platform=IMC_PLATFORM.TYPE_CLASSIC)

    # http mapping succeeded
    exist_mock.return_value = ["http://169.254.1.2/test.iso"]
    state_mock.side_effect = [['In Progress'], ['OK']]
    assert vmedia_mount_iso_uri(
        test_cimc,
        'http://169.254.1.2/test.iso',
        interval=1
    ) is True
    # Assert values of the mount options
    assert add_mount_mock.call_args[1] == {
        'volume_name': 'test.iso',
        'map': 'www',
        'mount_options': 'noauto',
        'remote_share': "http://169.254.1.2/",
        'remote_file': 'test.iso',
        'username': '',
        'password': '',
        'server_id': 1
    }

    # https mapping succeeded
    exist_mock.return_value = ["https://169.254.1.2/test.iso"]
    state_mock.side_effect = [['In Progress'], ['OK']]
    assert vmedia_mount_iso_uri(
        test_cimc,
        'https://169.254.1.2/test.iso',
        interval=1
    ) is True
    # Assert values of the mount options
    assert add_mount_mock.call_args[1] == {
        'volume_name': 'test.iso',
        'mount_options': 'noauto',
        'map': 'www',
        'remote_share': "https://169.254.1.2/",
        'remote_file': 'test.iso',
        'username': '',
        'password': '',
        'server_id': 1
    }

    # CIFS mapping succeeded
    exist_mock.return_value = ["//169.254.1.2/test.iso"]
    state_mock.side_effect = [['In Progress'], ['OK']]
    assert vmedia_mount_iso_uri(
        test_cimc,
        '//169.254.1.2/test.iso',
        interval=1
    ) is True
    # Assert values of the object passed to add_mo()
    assert add_mount_mock.call_args[1] == {
        'volume_name': 'test.iso',
        'mount_options': 'noauto',
        'map': 'cifs',
        'remote_share': "//169.254.1.2/",
        'remote_file': 'test.iso',
        'username': '',
        'password': '',
        'server_id': 1
    }

    # NFS mapping succeeded
    exist_mock.return_value = ["169.254.1.2:/test.iso"]
    state_mock.side_effect = [['In Progress'], ['OK']]
    assert vmedia_mount_iso_uri(
        test_cimc,
        '169.254.1.2:/test.iso',
        interval=1
    ) is True
    # Assert values of the object passed to add_mo()
    assert add_mount_mock.call_args[1] == {
        'volume_name': 'test.iso',
        'mount_options': 'noauto',
        'map': 'nfs',
        'remote_share': "169.254.1.2:/",
        'remote_file': 'test.iso',
        'username': '',
        'password': '',
        'server_id': 1
    }


@patch('imcsdk.apis.server.vmedia.vmedia_get_existing_status')
@patch('imcsdk.apis.server.vmedia.vmedia_get_existing_uri')
@patch('imcsdk.apis.server.vmedia.vmedia_mount_create')
@patch.object(ImcHandle, 'login')
def test_invalid_vmedia_mount_iso_uri(login_mock, add_mount_mock,
                                      exist_mock, state_mock):
    # Patch ImcHandle.login to create a Faux ImcHandle object w/o real CIMC
    # Patch vmedia_mount_create to simulate CIMC interaction w/o real CIMC
    # Patch vmedia_get_existing_uri to simulate existing ISOs
    # Patch vmedia_get_existing_status to simulate ISO status
    login_mock.return_value = True
    add_mount_mock.return_value = True
    test_cimc = ImcHandle(ip='169.254.1.1',
                          username='admin',
                          password='right')
    test_cimc._set_platform(platform=IMC_PLATFORM.TYPE_CLASSIC)

    # Scenario: Zero value passed in as check interval
    assert_raises(ValueError, vmedia_mount_iso_uri, test_cimc,
                  'http://1.1.1.1/test.iso', interval=0)

    # Scenario: Invalid protocol
    exist_mock.side_effect = [[], ["britt://1.1.1.1/test.iso"]]
    assert_raises(ValueError, vmedia_mount_iso_uri, test_cimc,
                  'britt://1.1.1.1/test.iso', interval=1)

    # Scenario: Mapping failed
    exist_mock.side_effect = [[], []]
    assert_raises(ImcOperationError, vmedia_mount_iso_uri, test_cimc,
                  'http://169.254.1.2/test.iso', interval=1)

    # Scenario: Timeout on state change
    exist_mock.side_effect = [[], ["http://169.254.1.2/test.iso"]]
    state_mock.side_effect = [['In Progress'], ['In Progress']]
    assert_raises(ImcOperationError, vmedia_mount_iso_uri, test_cimc,
                  'http://169.254.1.2/test.iso', interval=1, timeout=0)

    # State returns Error
    exist_mock.side_effect = [[], ["http://169.254.1.2/test.iso"]]
    state_mock.side_effect = [['In Progress'],
                              ['ERROR: [404] File not found. ']]
    assert_raises(ImcOperationError, vmedia_mount_iso_uri, test_cimc,
                  'http://169.254.1.2/test.iso', interval=1)


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
    test_cimc._set_platform(platform=IMC_PLATFORM.TYPE_CLASSIC)

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
    # query_mocked call first time in remove_existing_virtual_media
    # query_mock called a second time in get_existing_virtual_media_uri
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
    test_cimc._set_platform(platform=IMC_PLATFORM.TYPE_CLASSIC)

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
