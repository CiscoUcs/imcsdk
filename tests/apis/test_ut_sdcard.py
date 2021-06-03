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

try:
    from unittest.mock import patch, MagicMock
except ImportError:
    from mock import patch, MagicMock

from nose.tools import raises

from imcsdk.imchandle import ImcHandle
from imcsdk.imcexception import ImcOperationError
from imcsdk.apis.storage.sdcard import flexflash_controller_get_hierarchy
from imcsdk.apis.storage.sdcard import sd_card_virtual_drive_set


handle = ImcHandle("192.168.1.1", "username", "password")
handle._ImcSession__model = "UCSC-C240-M5SX"
handle._ImcSession__cookie = "cookie"


def query_StorageFlexFlashController_with_hierarchy():
    from imcsdk.mometa.storage.StorageFlexFlashController import StorageFlexFlashController
    from imcsdk.mometa.storage.StorageFlexFlashControllerProps import StorageFlexFlashControllerProps
    from imcsdk.mometa.storage.StorageFlexFlashPhysicalDrive import StorageFlexFlashPhysicalDrive
    from imcsdk.mometa.storage.StorageFlexFlashVirtualDrive import StorageFlexFlashVirtualDrive

    st_cnt = StorageFlexFlashController(parent_mo_or_dn="sys/rack-unit-1/board", id="FlexFlash-0")
    st_props = StorageFlexFlashControllerProps(parent_mo_or_dn="sys/rack-unit-1/board/storage-flexflash-FlexFlash-0")
    st_pd1 = StorageFlexFlashPhysicalDrive(parent_mo_or_dn="sys/rack-unit-1/board/storage-flexflash-FlexFlash-0", physical_drive_id="1")
    object.__setattr__(st_pd1, "pd_status", "present")
    st_pd2 = StorageFlexFlashPhysicalDrive(parent_mo_or_dn="sys/rack-unit-1/board/storage-flexflash-FlexFlash-0", physical_drive_id="2")
    object.__setattr__(st_pd2, "pd_status", "present")
    st_vd1 = StorageFlexFlashVirtualDrive(parent_mo_or_dn="sys/rack-unit-1/board/storage-flexflash-FlexFlash-0", partition_id="1")

    mos = [st_cnt, st_props, st_pd1, st_pd2, st_vd1]
    return mos


def query_StorageFlexFlashController_with_hierarchy_flexflash_controller_absent():
    return None


def query_StorageFlexFlashController_with_hierarchy_flexflash_pds_absent():
    from imcsdk.mometa.storage.StorageFlexFlashController import StorageFlexFlashController
    from imcsdk.mometa.storage.StorageFlexFlashControllerProps import StorageFlexFlashControllerProps

    st_cnt = StorageFlexFlashController(parent_mo_or_dn="sys/rack-unit-1/board", id="FlexFlash-0")
    st_props = StorageFlexFlashControllerProps(parent_mo_or_dn="sys/rack-unit-1/board/storage-flexflash-FlexFlash-0")

    mos = [st_cnt, st_props]
    return mos

def query_StorageFlexFlashController():
    from imcsdk.mometa.storage.StorageFlexFlashController import StorageFlexFlashController

    st_cnt = StorageFlexFlashController(parent_mo_or_dn="sys/rack-unit-1/board", id="FlexFlash-0")
    mos = [st_cnt]
    return mos


def query_StorageFlexUtilVirtualDrive():
    from imcsdk.mometa.storage.StorageFlexUtilVirtualDrive import StorageFlexUtilVirtualDrive

    util_vd_1 = StorageFlexUtilVirtualDrive(parent_mo_or_dn="sys/rack-unit-1/board/storage-flexutil-Flexutil",
                                              partition_name="SCU")
    object.__setattr__(util_vd_1, "partition_id", "1")
    util_vd_2 = StorageFlexUtilVirtualDrive(parent_mo_or_dn="sys/rack-unit-1/board/storage-flexutil-Flexutil",
                                              partition_name="Diagnostics")
    object.__setattr__(util_vd_2, "partition_id", "2")
    util_vd_3 = StorageFlexUtilVirtualDrive(parent_mo_or_dn="sys/rack-unit-1/board/storage-flexutil-Flexutil",
                                              partition_name="HUU")
    object.__setattr__(util_vd_3, "partition_id", "3")
    util_vd_4 = StorageFlexUtilVirtualDrive(parent_mo_or_dn="sys/rack-unit-1/board/storage-flexutil-Flexutil",
                                              partition_name="Drivers")
    object.__setattr__(util_vd_4, "partition_id", "4")
    util_vd_5 = StorageFlexUtilVirtualDrive(parent_mo_or_dn="sys/rack-unit-1/board/storage-flexutil-Flexutil",
                                            partition_name="UserPartition")
    object.__setattr__(util_vd_5, "partition_id", "5")
    mos = [util_vd_1, util_vd_2, util_vd_3, util_vd_4, util_vd_5]
    return mos


def query_StorageFlexUtilVirtualDrive_missing():
    return None

def query_classid_patch_all_present(*args, **kwargs):
    param_count = len(kwargs)
    if param_count == 2 and kwargs['class_id'] == "StorageFlexFlashController":
        return query_StorageFlexFlashController_with_hierarchy()
    elif param_count == 1 and kwargs['class_id'] == "StorageFlexUtilVirtualDrive":
        return query_StorageFlexUtilVirtualDrive()
    elif param_count == 1 and kwargs['class_id'] in ["StorageFlexFlashController", "storageFlexFlashController"]:
        return query_StorageFlexFlashController()


def query_classid_patch_flexflash_controller_absent(*args, **kwargs):
    param_count = len(kwargs)
    if param_count == 2 and kwargs['class_id'] == "StorageFlexFlashController":
        return query_StorageFlexFlashController_with_hierarchy_flexflash_controller_absent()
    elif param_count == 1 and kwargs['class_id'] == "StorageFlexUtilVirtualDrive":
        return query_StorageFlexUtilVirtualDrive()
    elif param_count == 1 and kwargs['class_id'] in ["StorageFlexFlashController", "storageFlexFlashController"]:
        return None


def query_classid_patch_flexflash_pds_absent(*args, **kwargs):
    param_count = len(kwargs)
    if param_count == 2 and kwargs['class_id'] == "StorageFlexFlashController":
        return query_StorageFlexFlashController_with_hierarchy_flexflash_pds_absent()
    elif param_count == 1 and kwargs['class_id'] == "StorageFlexUtilVirtualDrive":
        return query_StorageFlexUtilVirtualDrive()
    elif param_count == 1 and kwargs['class_id'] in ["StorageFlexFlashController", "storageFlexFlashController"]:
        return query_StorageFlexFlashController()


def query_classid_patch_microsd_card_missing(*args, **kwargs):
    param_count = len(kwargs)
    if param_count == 2 and kwargs['class_id'] == "StorageFlexFlashController":
        return query_StorageFlexFlashController_with_hierarchy()
    elif param_count == 1 and kwargs['class_id'] == "StorageFlexUtilVirtualDrive":
        return query_StorageFlexUtilVirtualDrive_missing()
    elif param_count == 1 and kwargs['class_id'] in ["StorageFlexFlashController", "storageFlexFlashController"]:
        return query_StorageFlexFlashController()


def query_classid_patch_all_absent(*args, **kwargs):
    param_count = len(kwargs)
    if param_count == 2 and kwargs['class_id'] == "StorageFlexFlashController":
        return None
    elif param_count == 1 and kwargs['class_id'] == "StorageFlexUtilVirtualDrive":
        return None
    elif param_count == 1 and kwargs['class_id'] in ["StorageFlexFlashController", "storageFlexFlashController"]:
        return None


def set_mo_patch(mo):
    return


def set_mos_patch(mos):
    return


called_method_dict = {
    "util_vds_disable_all_m5": False,
    "os_vd_disable_m5": False
}


def setup():
    global called_method_dict
    called_method_dict['util_vds_disable_all_m5'] = False
    called_method_dict['os_vd_disable_m5'] = False


def util_vds_disable_all_m5_patch(*args, **kwargs):
    print("calling util_vds_disable_all_m5_patch")
    called_method_dict['util_vds_disable_all_m5'] = True


def os_vd_disable_m5_patch(*args, **kwargs):
    print("calling os_vd_disable_m5_patch")
    called_method_dict['os_vd_disable_m5'] = True


@raises(ImcOperationError)
@patch.object(ImcHandle, 'query_classid')
def test_flexflash_controller_get_hierarchy_not_present(query_classid_mock):
    query_classid_mock.return_value = None
    flexflash_controller_get_hierarchy(handle)


@patch.object(ImcHandle, 'query_classid')
def test_flexflash_controller_get_hierarchy_present(query_classid_mock):
    query_classid_mock.side_effect = query_classid_patch_all_present
    flexflash_controller_get_hierarchy(handle)


# FlexFlash controller and both card present
# FlexUtil with SD card present
# I/P - Only OS
# Configure FlexFlash
# Disable all FlexUtil vds
@patch('imcsdk.apis.storage.sdcard.util_vds_disable_all_m5')
@patch.object(ImcHandle, 'set_mos')
@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_classid')
def test_vd_set_os_only_all_present(query_classid_mock, set_mo_mock, set_mos_mock, util_vds_disable_all_m5_mock):
    query_classid_mock.side_effect = query_classid_patch_all_present
    set_mo_mock.side_effect = set_mo_patch
    set_mos_mock.side_effect = set_mos_patch
    util_vds_disable_all_m5_mock.side_effect = util_vds_disable_all_m5_patch

    virtual_drives = {"OS": {"enable": False}}
    sd_card_virtual_drive_set(handle, virtual_drives)

    assert called_method_dict['util_vds_disable_all_m5']


# FlexFlash controller absent
# FlexUtil with SD card present
# I/P - Only OS
# Exception
@raises(ImcOperationError)
@patch.object(ImcHandle, 'query_classid')
def test_vd_set_os_only_flash_cnt_not_present(query_classid_mock):
    query_classid_mock.return_value = None
    virtual_drives = {"OS": {"enable": False}}
    sd_card_virtual_drive_set(handle, virtual_drives)


# FlexFlash controller present, sd cards absent
# FlexUtil with SD card present
# I/P - Only OS
# Exception
@raises(ImcOperationError)
@patch('imcsdk.apis.storage.sdcard.util_vds_disable_all_m5')
@patch.object(ImcHandle, 'set_mos')
@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_classid')
def test_vd_set_os_only_flash_sd_cards_missing(query_classid_mock, set_mo_mock, set_mos_mock, util_vds_disable_all_m5_mock):
    query_classid_mock.side_effect = query_classid_patch_flexflash_pds_absent
    set_mo_mock.side_effect = set_mo_patch
    set_mos_mock.side_effect = set_mos_patch
    util_vds_disable_all_m5_mock.side_effect = util_vds_disable_all_m5_patch

    virtual_drives = {"OS": {"enable": True}}
    sd_card_virtual_drive_set(handle, virtual_drives)


# FlexFlash controller present, cards present
# FlexUtil with SD card missing
# I/P - Only OS
# Pass
@patch.object(ImcHandle, 'set_mos')
@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_classid')
def test_vd_set_os_only_microsd_card_missing(query_classid_mock, set_mo_mock, set_mos_mock):
    query_classid_mock.side_effect = query_classid_patch_microsd_card_missing
    set_mo_mock.side_effect = set_mo_patch
    set_mos_mock.side_effect = set_mos_patch

    virtual_drives = {"OS": {"enable": True}}
    sd_card_virtual_drive_set(handle, virtual_drives)


# FlexFlash controller and both card present
# FlexUtil with SD card present
# I/P - Only Utils
# Configure FlexUtils
# Disable OS vd
@patch('imcsdk.apis.storage.sdcard.os_vd_disable_m5')
@patch.object(ImcHandle, 'set_mos')
@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_classid')
def test_vd_set_utils_only_all_present(query_classid_mock, set_mo_mock, set_mos_mock, os_vd_disable_m5_mock):
    query_classid_mock.side_effect = query_classid_patch_all_present
    set_mo_mock.side_effect = set_mo_patch
    set_mos_mock.side_effect = set_mos_patch
    os_vd_disable_m5_mock.side_effect = os_vd_disable_m5_patch

    virtual_drives = {"SCU": {"enable": True}}
    sd_card_virtual_drive_set(handle, virtual_drives)

    assert called_method_dict['os_vd_disable_m5']


# FlexFlash controller and both card present
# FlexUtil with SD card missing
# I/P - Only Utils
# Error
@patch.object(ImcHandle, 'set_mos')
@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_classid')
@raises(ImcOperationError)
def test_vd_set_utils_only_microsd_card_missing(query_classid_mock, set_mo_mock, set_mos_mock):
    query_classid_mock.side_effect = query_classid_patch_microsd_card_missing
    set_mo_mock.side_effect = set_mo_patch
    set_mos_mock.side_effect = set_mos_patch

    virtual_drives = {"SCU": {"enable": True}}
    sd_card_virtual_drive_set(handle, virtual_drives)


# FlexFlash controller absent
# FlexUtil with SD card present
# I/P - Only Utils
# Configure Util Vds
@patch.object(ImcHandle, 'set_mos')
@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_classid')
def test_vd_set_utils_only_flash_cnt_absent(query_classid_mock, set_mo_mock, set_mos_mock):
    query_classid_mock.side_effect = query_classid_patch_flexflash_controller_absent
    set_mo_mock.side_effect = set_mo_patch
    set_mos_mock.side_effect = set_mos_patch

    virtual_drives = {"SCU": {"enable": True}}
    sd_card_virtual_drive_set(handle, virtual_drives)


# FlexFlash controller present, SD cards missing
# FlexUtil with SD card present
# I/P - Only Utils
# Configure Util Vds
@patch.object(ImcHandle, 'set_mos')
@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_classid')
def test_vd_set_utils_only_flash_sdcards_absent(query_classid_mock, set_mo_mock, set_mos_mock):
    query_classid_mock.side_effect = query_classid_patch_flexflash_pds_absent
    set_mo_mock.side_effect = set_mo_patch
    set_mos_mock.side_effect = set_mos_patch

    virtual_drives = {"SCU": {"enable": True}}
    sd_card_virtual_drive_set(handle, virtual_drives)


# FlexFlash controller and both card present
# FlexUtil with SD card present
# I/P - Both OS and Utils
# Configure Flexflash & FlexUtils
@patch.object(ImcHandle, 'set_mos')
@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_classid')
def test_vd_set_both_all_present(query_classid_mock, set_mo_mock, set_mos_mock):
    query_classid_mock.side_effect = query_classid_patch_all_present
    set_mo_mock.side_effect = set_mo_patch
    set_mos_mock.side_effect = set_mos_patch

    virtual_drives = {"OS": {"enable": True},
                      "SCU": {"enable": True}}
    sd_card_virtual_drive_set(handle, virtual_drives)


# FlexFlash controller absent
# FlexUtil with SD card present
# I/P - Both OS and Utils
# Exception
@patch.object(ImcHandle, 'set_mos')
@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_classid')
@raises(ImcOperationError)
def test_vd_set_both_flash_cnt_absent(query_classid_mock, set_mo_mock, set_mos_mock):
    query_classid_mock.side_effect = query_classid_patch_flexflash_controller_absent
    set_mo_mock.side_effect = set_mo_patch
    set_mos_mock.side_effect = set_mos_patch

    virtual_drives = {"OS": {"enable": True},
                     "SCU": {"enable": True}}
    sd_card_virtual_drive_set(handle, virtual_drives)


# FlexFlash controller present, SD cards missing
# FlexUtil with SD card present
# I/P - Both OS and Utils
# Exception
@patch.object(ImcHandle, 'set_mos')
@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_classid')
@raises(ImcOperationError)
def test_vd_set_both_flash_sdcards_absent(query_classid_mock, set_mo_mock, set_mos_mock):
    query_classid_mock.side_effect = query_classid_patch_flexflash_pds_absent
    set_mo_mock.side_effect = set_mo_patch
    set_mos_mock.side_effect = set_mos_patch

    virtual_drives = {"OS": {"enable": True},
                      "SCU": {"enable": True}}
    sd_card_virtual_drive_set(handle, virtual_drives)


# FlexFlash controller and both card present
# FlexUtil with SD card missing
# I/P - Both OS and Utils
# Error
@patch.object(ImcHandle, 'set_mos')
@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_classid')
@raises(ImcOperationError)
def test_vd_set_both_microsd_card_missing(query_classid_mock, set_mo_mock, set_mos_mock):
    query_classid_mock.side_effect = query_classid_patch_microsd_card_missing
    set_mo_mock.side_effect = set_mo_patch
    set_mos_mock.side_effect = set_mos_patch

    virtual_drives = {"OS": {"enable": True},
                      "SCU": {"enable": True}}
    sd_card_virtual_drive_set(handle, virtual_drives)


# FlexFlash controller and both card absent
# FlexUtil with SD card missing
# I/P - Both OS and Utils
# Error
@patch.object(ImcHandle, 'set_mos')
@patch.object(ImcHandle, 'set_mo')
@patch.object(ImcHandle, 'query_classid')
@raises(ImcOperationError)
def test_vd_set_both_all_absent(query_classid_mock, set_mo_mock, set_mos_mock):
    query_classid_mock.side_effect = query_classid_patch_all_absent
    set_mo_mock.side_effect = set_mo_patch
    set_mos_mock.side_effect = set_mos_patch

    virtual_drives = {"OS": {"enable": True},
                      "SCU": {"enable": True}}
    sd_card_virtual_drive_set(handle, virtual_drives)
