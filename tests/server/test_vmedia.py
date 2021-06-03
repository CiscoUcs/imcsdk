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

from imcsdk.apis.server.vmedia import vmedia_enable
from imcsdk.apis.server.vmedia import vmedia_disable
from imcsdk.apis.server.vmedia import vmedia_exists
from imcsdk.apis.server.vmedia import vmedia_mount_create_all
import logging

log = logging.getLogger('imc')
handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_vmedia_setup():
    vmedia_enable(handle, encryption_state="enabled", low_power_usb="enabled")
    assert_equal(vmedia_exists(handle)[0], True)


def test_vmedia_disable():
    vmedia_disable(handle)
    assert_equal(vmedia_exists(handle)[0], False)

def test_vmedia_mount_create_all_sec_ntlm():
    mappings=[{"volume_name": "test_sec_ntlm",
               "map": "cifs",
               "mount_options": "sec=ntlm",
               "remote_share": "//[2001:420:5446:2014::206:ca]/file",
               "remote_file": "esx65u3.iso",
               "username": "user",
               "password": ""}]
    results = vmedia_mount_create_all(handle, mappings)
    assert_equal(results["changed"], True)

def test_vmedia_mount_create_all_sec_none():
    mappings=[{"volume_name": "test_sec_none",
               "map": "cifs",
               "mount_options": "sec=none",
               "remote_share": "//[2001:420:5446:2014::206:ca]/file",
               "remote_file": "esx65u3.iso",
               "username": "user",
               "password": ""}]
    results = vmedia_mount_create_all(handle, mappings)
    assert_equal(results["changed"], True)

