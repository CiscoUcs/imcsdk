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

import time
from ..connection.info import custom_setup, custom_teardown
from nose.tools import assert_equal, assert_not_equal

from imcsdk.apis.server.bios import bios_profile_backup_running, \
        bios_profile_upload, bios_profile_activate, bios_profile_delete,\
        bios_profile_get, bios_profile_generate_json, is_bios_profile_enabled,\
        bios_profile_exists


handle = None
REMOTE_SERVER = ''
REMOTE_FILE = ''
USER = ''
PASSWORD = ''

expected_output = {
    "name": "simple",
    "description": "Simple Profile",
    "tokens": {
        "TPMAdminCtrl": "Enabled",
        "TerminalType": "PC-ANSI"
    }
}


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_bios_profile_backup():
    bios_profile_backup_running(handle, server_id=1)
    assert_not_equal(bios_profile_get(handle, name='cisco_backup_profile'),
                     None)


def test_bios_profile_upload():
    bios_profile_upload(handle, remote_server=REMOTE_SERVER,
                        remote_file=REMOTE_FILE, protocol='scp',
                        user=USER, pwd=PASSWORD)
    time.sleep(2)
    assert_not_equal(bios_profile_get(handle, name='simple'),
                     None)


def test_bios_profile_activate():
    bios_profile_activate(handle, name='simple',
                          backup_on_activate=True, reboot_on_activate=False)
    assert_equal(is_bios_profile_enabled(handle,
                                         name='simple',
                                         server_id=1),
                 True)


def test_bios_profile_exists():
    match, mo = bios_profile_exists(handle, name='simple',
                                    enabled=True)
    assert_equal(match, True)


def test_bios_profile_not_exists():
    match, mo = bios_profile_exists(handle, name='complex')
    assert_equal(match, False)


def test_bios_profile_generate_json():
    diff = []
    output = bios_profile_generate_json(handle, name='simple')
    output_tokens = output.pop('tokens')
    expected_tokens = expected_output.pop('tokens')
    diff = [key for key in output if key in expected_output and
            output[key] != expected_output[key]]
    assert_equal(diff, [])
    diff = [key for key in output_tokens if
            key in expected_tokens and output_tokens[key] != expected_tokens[key]]
    assert_equal(diff, [])


def test_bios_profile_delete():
    bios_profile_delete(handle, name='simple')
    assert_equal(bios_profile_get(handle, name='simple'), None)
