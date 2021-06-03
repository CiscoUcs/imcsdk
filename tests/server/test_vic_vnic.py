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

from nose.tools import raises
from ..connection.info import custom_setup, custom_teardown

from imcsdk.imcexception import ImcOperationError, ImcException, ImcOperationErrorDetail
from imcsdk.apis.server.vic import vnic_create, vnic_create_all
from imcsdk.apis.server.vic import vnic_delete_all


handle = None
ADAPTOR_ID = "2"
# ADAPTOR_ID = "MLOM"
# ADAPTOR_ID = "SIOC1"

adaptor_slot = "AdaptorUnit.Id"
vic_name = "AdaptorHostEthIf.Name"


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    custom_teardown(handle)


def test_vnic_create():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vic_name: "test_vnic"
    }
    vnic_create(handle, **props)


@raises(ImcOperationError)
def test_vnic_create_key_without_underscore():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vic_name: "test_vnic",
        "unknown": "unknown",
    }
    vnic_create(handle, **props)


@raises(ImcOperationError)
def test_vnic_create_key_without_mo():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vic_name: "test_vnic",
        ".Cdn": "unknown",
    }
    vnic_create(handle, **props)


@raises(ImcOperationError)
def test_vnic_create_key_without_prop():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vic_name: "test_vnic",
        "AdaptorHostEthIf.": "unknown",
    }
    vnic_create(handle, **props)


@raises(ImcOperationError)
def test_vnic_create_key_without_prop1():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vic_name: "test_vnic",
        "AdaptorHostEthIf": "unknown",
    }
    vnic_create(handle, **props)


def test_vnic_create_using_correct_key():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vic_name: "test_vnic",
        "AdaptorHostEthIf.Cdn": "testcdn",
    }
    vnic_create(handle, **props)


def test_vnic_create_known_prop_empty():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vic_name: "test_vnic",
        "AdaptorHostEthIf.Cdn": "",
    }
    vnic_create(handle, **props)


def test_vnic_create_known_prop_none():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vic_name: "test_vnic",
        "AdaptorHostEthIf.Cdn": None,
    }
    vnic_create(handle, **props)


@raises(ImcException)
def test_vnic_create_unknown_prop():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vic_name: "test_vnic",
        "AdaptorHostEthIf.unknown": "unknown",
    }
    vnic_create(handle, **props)


def test_vnic_create_multi_props():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vic_name: "test_vnic",
        "AdaptorHostEthIf.Cdn": "testcdn",
        "AdaptorEthGenProfile.Order": "2",
        "AdaptorEthGenProfile.VlanMode": "ACCESS",
    }
    vnic_create(handle, **props)


def test_vnic_create_multi_props_none():
    props = {
        adaptor_slot: ADAPTOR_ID,
        vic_name: "test_vnic",
        "AdaptorHostEthIf.Cdn": "testcdn",
        "AdaptorEthGenProfile.Order": None,
        "AdaptorEthGenProfile.VlanMode": "ACCESS",
    }
    vnic_create(handle, **props)


def test_vnic_create_default():
    vnic_create_all(handle)


def test_vnic_create_no_vnics():
    vnic_create_all(handle, vnics=[])


def test_vnic_create_default_vnics():
    vnics = [
        {
            adaptor_slot: ADAPTOR_ID,
            vic_name: "vnic1",
        },
        {
            adaptor_slot: ADAPTOR_ID,
            vic_name: "vnic2",
        }
    ]
    vnic_create_all(handle, vnics)


@raises(ImcOperationErrorDetail)
def test_vnic_create_vnics_samecdn():
    vnics = [
        {
            adaptor_slot: ADAPTOR_ID,
            vic_name: "vnic1",
            "AdaptorHostEthIf.Cdn": "samecdn"
        },
        {
            adaptor_slot: ADAPTOR_ID,
            vic_name: "vnic2",
            "AdaptorHostEthIf.Cdn": "samecdn"
        }
    ]
    vnic_create_all(handle, vnics)


def test_vnic_create_vnics_withchild():
    vnics = [
        {
            adaptor_slot: ADAPTOR_ID,
            vic_name: "vnic1",
            "AdaptorHostEthIf.Cdn": "testcdn1",
            "AdaptorEthGenProfile.Order": "1",
            "AdaptorEthGenProfile.VlanMode": "ACCESS",
         },
        {
            adaptor_slot: ADAPTOR_ID,
            vic_name: "vnic2",
            "AdaptorHostEthIf.Cdn": "testcdn2",
            "AdaptorEthGenProfile.Order": "2",
            "AdaptorEthGenProfile.VlanMode": "ACCESS",
         },
    ]
    vnic_create_all(handle, vnics)


def test_vnic_create_vnics_withchild_pcilink():
    vnics = [
        {
            adaptor_slot: ADAPTOR_ID,
            vic_name: "vnic1",
            "AdaptorHostEthIf.Cdn": "testcdn1",
            "AdaptorEthGenProfile.Order": "1",
            "AdaptorEthGenProfile.VlanMode": "ACCESS",
            "AdaptorEthGenProfile.PciLink": "0"
         },
        {
            adaptor_slot: ADAPTOR_ID,
            vic_name: "vnic2",
            "AdaptorHostEthIf.Cdn": "testcdn2",
            "AdaptorEthGenProfile.Order": "2",
            "AdaptorEthGenProfile.VlanMode": "ACCESS",
            "AdaptorEthGenProfile.PciLink": "1"
         },
    ]
    vnic_create_all(handle, vnics)


@raises(ImcException)
def test_vnic_create_vnics_withchild_error1():
    vnics = [
        {
            adaptor_slot: ADAPTOR_ID,
            vic_name: "vnic1",
            "AdaptorHostEthIf.unknown": "testcdn1",
            "AdaptorEthGenProfile.Order": "1",
            "AdaptorEthGenProfile.VlanMode": "ACCESS",
         },
        {
            adaptor_slot: ADAPTOR_ID,
            vic_name: "vnic2",
            "AdaptorHostEthIf.Cdn": "testcdn2",
            "AdaptorEthGenProfile.Order": "2",
            "AdaptorEthGenProfile.VlanMode": "ACCESS",
         },
    ]
    vnic_create_all(handle, vnics)


@raises(ValueError)
def test_vnic_create_vnics_withchild_error2():
    vnics = [
        {
            adaptor_slot: ADAPTOR_ID,
            vic_name: "vnic1",
            "AdaptorHostEthIf.UplinkPort": "11",
            "AdaptorEthGenProfile.Order": "1",
            "AdaptorEthGenProfile.VlanMode": "ACCESS",
         },
        {
            adaptor_slot: ADAPTOR_ID,
            vic_name: "vnic2",
            "AdaptorHostEthIf.Cdn": "testcdn2",
            "AdaptorHostEthIf.UplinkPort": "22",
            "AdaptorEthGenProfile.Order": "1",
            "AdaptorEthGenProfile.VlanMode": "ACCESS",
         },
    ]
    vnic_create_all(handle, vnics)


def test_vnic_create_vnic_with_usnic():
    vnics = [
        {
            adaptor_slot: ADAPTOR_ID,
            vic_name: "vnic_usnic",
            "AdaptorHostEthIf.Cdn": "testcdnusnic",
            "AdaptorEthUSNICProfile.usnicCount": "1",
            "AdaptorEthUSNICProfile.TransmitQueueCount": "10"
         },
    ]
    vnic_create_all(handle, vnics)


def test_vnic_delete_all():
    vnic_delete_all(handle, adaptor_slots=[ADAPTOR_ID])
