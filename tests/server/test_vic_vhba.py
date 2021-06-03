# Copyright 2018 Cisco Systems, Inc.
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

from nose.tools import raises
from nose import SkipTest
from ..connection.info import custom_setup, custom_teardown

from imcsdk.imcexception import ImcOperationError, ImcException

from imcsdk.apis.server.vic import _get_adaptor_profile
from imcsdk.apis.server.vic import vhba_create, vhba_create_all
from imcsdk.apis.server.vic import vhba_delete_all


handle = None
ADAPTOR_ID = "2"
# ADAPTOR_ID = "MLOM"
# ADAPTOR_ID = "SIOC1"
VNTAG = False

adaptor_slot = "AdaptorUnit.Id"
vhba_name = "AdaptorHostFcIf.Name"


def setup_module():
    global handle
    global VNTAG
    handle = custom_setup()
    adaptor_profile = _get_adaptor_profile(handle, adaptor_slot=ADAPTOR_ID)
    vntag_mode = adaptor_profile.vntag_mode
    if vntag_mode.lower() == "enabled":
        VNTAG = True


def teardown_module():
    custom_teardown(handle)
    pass


@raises(ImcException)
def test_vhba_create():
    if not VNTAG:
        raise SkipTest("Skipping. VNTAG is disabled")
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "test_vhba"
    }
    vhba_create(handle, **props)


def test_vhba_create_with_channel():
    if not VNTAG:
        raise SkipTest("Skipping. VNTAG is disabled")
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "test_vhba",
        "AdaptorHostFcIf.ChannelNumber": "59"
    }
    vhba_create(handle, **props)


def test_vhba_create_repeat_without_channel():
    if not VNTAG:
        raise SkipTest("Skipping. VNTAG is disabled")
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "test_vhba",
    }
    vhba_create(handle, **props)


def test_vhba_create_vhbas():
    if not VNTAG:
        raise SkipTest("Skipping. VNTAG is disabled")

    vhbas = [
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: "vhba1",
        },
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: "vhba2",
        },
    ]
    vhba_create_all(handle, vhbas)


def test_vhba_create_vhbas_withchild():
    if not VNTAG:
        raise SkipTest("Skipping. VNTAG is disabled")

    vhbas = [
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: 'vhba1',
            "AdaptorHostFcIf.Cdn": "testcdn1",
            "AdaptorEthGenProfile.Order": "1",
            "AdaptorEthGenProfile.VlanMode": "ACCESS",
         },
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: 'vhba1',
            "AdaptorHostFcIf.Cdn": "testcdn1",
            "AdaptorEthGenProfile.Order": "2",
            "AdaptorEthGenProfile.VlanMode": "ACCESS",
         },
    ]
    vhba_create_all(handle, vhbas)


@raises(ImcException)
def test_vhba_create_vhbas_withchild_error1():
    if not VNTAG:
        raise SkipTest("Skipping. VNTAG is disabled")

    vhbas = [
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: 'vhba1',
            "AdaptorHostFcIf.unknown": "testcdn1",
            "AdaptorEthGenProfile.Order": "1",
            "AdaptorEthGenProfile.VlanMode": "ACCESS",
         },
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: 'vhba1',
            "AdaptorHostFcIf.Cdn": "testcdn1",
            "AdaptorEthGenProfile.Order": "2",
            "AdaptorEthGenProfile.VlanMode": "ACCESS",
         },
    ]
    vhba_create_all(handle, vhbas)


@raises(ValueError)
def test_vhba_create_vhbas_withchild_error2():
    if not VNTAG:
        raise SkipTest("Skipping. VNTAG is disabled")

    vhbas = [
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: 'vhba1',
            "AdaptorHostFcIf.UplinkPort": "11",
            "AdaptorEthGenProfile.Order": "1",
            "AdaptorEthGenProfile.VlanMode": "ACCESS",
         },
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: 'vhba2',
            "AdaptorHostFcIf.UplinkPort": "22",
            "AdaptorEthGenProfile.Order": "1",
            "AdaptorEthGenProfile.VlanMode": "ACCESS",
         },
    ]
    vhba_create_all(handle, vhbas)


def test_vhba_delete_all():
    if not VNTAG:
        raise SkipTest("Skipping. VNTAG is disabled")

    vhba_delete_all(handle, adaptor_slots=[ADAPTOR_ID])


def test_vhba_default_create():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "fc0"
    }
    vhba_create(handle, **props)


@raises(ImcException)
def test_vhba_default_create_with_channel():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "fc0",
        "AdaptorHostFcIf.ChannelNumber": "59"
    }
    vhba_create(handle, **props)


@raises(ImcOperationError)
def test_vhba_default_create_key_without_dot():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "fc0",
        "ChannelNumber": "59"
    }
    vhba_create(handle, **props)


@raises(ImcOperationError)
def test_vhba_default_create_key_without_mo():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "fc0",
        ".ChannelNumber": "59"
    }
    vhba_create(handle, **props)


@raises(ImcOperationError)
def test_vhba_default_create_key_without_prop():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "fc0",
        "AdaptorHostFcIf.": "59"
    }
    vhba_create(handle, **props)


@raises(ImcException)
def test_vhba_default_create_using_uplink_port():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "fc0",
        "AdaptorHostFcIf.UplinkPort": "1"
    }
    vhba_create(handle, **props)


def test_vhba_default_create_using_correct_key():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "fc0",
        "AdaptorHostFcIf.SanBoot": "enabled"
    }
    vhba_create(handle, **props)


@raises(ImcException)
def test_vhba_default_create_known_prop_empty():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "fc0",
        "AdaptorHostFcIf.Wwnn": ""
    }
    vhba_create(handle, **props)


def test_vhba_default_create_known_prop_none():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "fc0",
        "AdaptorHostFcIf.Wwnn": None
    }
    vhba_create(handle, **props)


@raises(ImcException)
def test_vhba_default_create_unknown_prop():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "fc0",
        "AdaptorHostFcIf.unknown": "enabled",
    }
    vhba_create(handle, **props)


def test_vhba_default_create_unknown_mo():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "fc0",
        "AdaptorHostXXX.SanBoot": "enabled",
    }
    vhba_create(handle, **props)


def test_vhba_default_create_multi_props():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "fc0",
        "AdaptorHostFcIf.SanBoot": "enabled",
        "AdaptorFcGenProfile.PciLink": "1",
        "AdaptorFcErrorRecoveryProfile.ErrorDetectTimeout": "3000"
    }
    vhba_create(handle, **props)


def test_vhba_default_create_multi_props_none():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vhba_name: "fc0",
        "AdaptorHostFcIf.SanBoot": "enabled",
        "AdaptorFcGenProfile.PciLink": None,
        "AdaptorFcErrorRecoveryProfile.ErrorDetectTimeout": "3000"
    }
    vhba_create(handle, **props)


def test_vhba_default_create_missing_vhbas():
    vhba_create_all(handle)


def test_vhba_default_create_no_vhbas():
    vhba_create_all(handle, vhbas=[])


def test_vhba_default_create_vhbas():
    vhbas = [
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: "fc0",
            "AdaptorHostFcIf.SanBoot": "enabled",
        },
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: "fc1",
        }
    ]
    vhba_create_all(handle, vhbas)


def test_vhba_default_create_vhbas_withchild():
    vhbas = [
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: "fc0",
            "AdaptorHostFcIf.SanBoot": "enabled",
            "AdaptorFcGenProfile.PciLink": "1",
            "AdaptorFcErrorRecoveryProfile.ErrorDetectTimeout": "3000"
         },
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: "fc1",
            "AdaptorHostFcIf.SanBoot": "enabled",
            "AdaptorFcGenProfile.PciLink": "1",
            "AdaptorFcErrorRecoveryProfile.ErrorDetectTimeout": "3000"
         },
    ]
    vhba_create_all(handle, vhbas)


def test_vhba_default_create_vhbas_withchild_pcilink():
    vhbas = [
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: "fc0",
            "AdaptorHostFcIf.SanBoot": "enabled",
            "AdaptorFcGenProfile.PciLink": "0",
            "AdaptorFcErrorRecoveryProfile.ErrorDetectTimeout": "3000"
         },
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: "fc1",
            "AdaptorHostFcIf.SanBoot": "enabled",
            "AdaptorFcGenProfile.PciLink": "1",
            "AdaptorFcErrorRecoveryProfile.ErrorDetectTimeout": "3000"
         },
    ]
    vhba_create_all(handle, vhbas)


@raises(ImcException)
def testx_vhba_default_create_vhbas_withchild_error1():
    vhbas = [
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: "fc0",
            "AdaptorHostFcIf.unknown": "enabled",
            "AdaptorFcGenProfile.PciLink": "1",
            "AdaptorFcErrorRecoveryProfile.ErrorDetectTimeout": "3000"
         },
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: "fc1",
            "AdaptorHostFcIf.SanBoot": "enabled",
            "AdaptorFcGenProfile.PciLink": "1",
            "AdaptorFcErrorRecoveryProfile.ErrorDetectTimeout": "3000"
         },
    ]
    vhba_create_all(handle, vhbas)


def testx_vhba_default_create_vhbas_with_order():
    vhbas = [
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: "fc0",
            "AdaptorFcGenProfile.Order": "1",
         },
        {
            adaptor_slot: ADAPTOR_ID,
            vhba_name: "fc1",
            "AdaptorFcGenProfile.Order": "0",
         },
    ]
    vhba_create_all(handle, vhbas)

def testx_vhba_default_delete_all():
    vhba_delete_all(handle, adaptor_slots=[ADAPTOR_ID])
