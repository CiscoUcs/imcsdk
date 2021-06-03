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

from ..connection.info import custom_setup, custom_teardown

from imcsdk.apis.storage.sdcard import sd_card_virtual_drive_set
from imcsdk.apis.storage.sdcard import sd_card_virtual_drive_exists

handle = None

virtual_drives_os = {
    "OS": {"enable", True}
}

virtual_drives_util = {
    "SCU": {"enable", True}
}


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_vd_set_os_disable():
    virtual_drives = {"OS": {"enable": False}}
    sd_card_virtual_drive_set(handle, virtual_drives)


def test_vd_set_os_enable():
    virtual_drives = {"OS": {"enable": True}}
    sd_card_virtual_drive_set(handle, virtual_drives)


def test_vd_set_os_enable_name_change():
    virtual_drives = {
        "OS": {"enable": True, "name": "hypervisor"},
    }
    sd_card_virtual_drive_set(handle, virtual_drives)


def test_vd_set_os_disable_name_change():
    virtual_drives = {
        "OS": {"enable": False, "name": "hypervisor"},
    }
    sd_card_virtual_drive_set(handle, virtual_drives)


def test_vd_set_utils_all_enable():
    virtual_drives = {
        "USER": {"enable": True},
        "SCU": {"enable": True},
        "HUU": {"enable": True},
        "DRIVERS": {"enable": True},
        "DIAGNOSTICS": {"enable": True},
    }
    sd_card_virtual_drive_set(handle, virtual_drives)


def test_vd_set_util_user_name_change_enable():
    virtual_drives = {
        "USER": {"enable": True, "name": "userpartition"},
        "SCU": {"enable": True},
        "HUU": {"enable": True},
        "DRIVERS": {"enable": True},
        "DIAGNOSTICS": {"enable": True},
    }
    sd_card_virtual_drive_set(handle, virtual_drives)


def test_vd_set_util_user_name_change_disable():
    virtual_drives = {
        "USER": {"enable": True, "name": "userpartition"},
        "SCU": {"enable": True},
        "HUU": {"enable": True},
        "DRIVERS": {"enable": True},
        "DIAGNOSTICS": {"enable": True},
    }
    sd_card_virtual_drive_set(handle, virtual_drives)


def test_vd_set_os_utils_all_disable():
    virtual_drives = {
        "OS": {"enable": False},
        "USER": {"enable": False},
        "SCU": {"enable": False},
        "HUU": {"enable": False},
        "DRIVERS": {"enable": False},
        "DIAGNOSTICS": {"enable": False},
    }
    sd_card_virtual_drive_set(handle, virtual_drives)


def test_vd_set_utils_all_enable_name_change():
    virtual_drives = {
        "OS": {"enable": True, "name": "hypervisor"},
        "USER": {"enable": True, "name": "userpartition"},
        "SCU": {"enable": True},
        "HUU": {"enable": True},
        "DRIVERS": {"enable": True},
        "DIAGNOSTICS": {"enable": True},
    }
    sd_card_virtual_drive_set(handle, virtual_drives)


def test_vd_set_utils_all_disable_name_change():
    virtual_drives = {
        "OS": {"enable": True, "name": "hypervisor"},
        "USER": {"enable": True, "name": "userpartition"},
        "SCU": {"enable": True},
        "HUU": {"enable": True},
        "DRIVERS": {"enable": True},
        "DIAGNOSTICS": {"enable": True},
    }
    sd_card_virtual_drive_set(handle, virtual_drives)


def test_vd_set_m5_utils_enable_withoutimage():
    virtual_drives = {
        "HUU": {"enable": True},
        "DRIVERS": {"enable": True},
    }
    sd_card_virtual_drive_set(handle, virtual_drives)


def test_vd_set_m5_utils_enable_withimage():
    virtual_drives = {
        "SCU": {"enable": True},
        "DIAGNOSTICS": {"enable": True},
    }
    sd_card_virtual_drive_set(handle, virtual_drives)


def test_vd_set_utils_all_disable():
    virtual_drives = {
        "USER": {"enable": False},
        "SCU": {"enable": False},
        "HUU": {"enable": False},
        "DRIVERS": {"enable": False},
        "DIAGNOSTICS": {"enable": False},
    }
    sd_card_virtual_drive_set(handle, virtual_drives)


def test_vd_exists():
    virtual_drives = {"OS": {"enable": True}}
    print((sd_card_virtual_drive_exists(handle, virtual_drives)))
