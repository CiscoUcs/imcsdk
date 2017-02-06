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
from nose.tools import assert_equal, assert_not_equal
from ..connection.info import custom_setup, custom_teardown
from imcsdk.apis.server.adaptor import adaptor_properties_set, \
    adaptor_properties_get, adaptor_reset, vnic_create, vnic_delete, vnic_get, \
    vhba_create, vhba_delete, vhba_get


handle = None
ADAPTOR_ID = "1"
ADAPTOR_ID = "MLOM"
# ADAPTOR_ID = "SIOC1"


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    custom_teardown(handle)


def test_non_vntag_mode():
    adaptor_properties_set(handle, adaptor_slot=ADAPTOR_ID, fip_mode=True,
                                 vntag_mode=False)
    mo = adaptor_properties_get(handle, adaptor_slot=ADAPTOR_ID)
    assert_equal(mo.vntag_mode.lower(), "disabled")


def test_non_vntag_create_vnic():
    vnic_mo = vnic_create(handle, adaptor_slot=ADAPTOR_ID, name="sdk-test-vnic-nv",
                          class_of_service=5, mac="00:11:22:33:44:56",
                          mtu=1500, pxe_boot=True, uplink_port=0)
    rcvd_mo = vnic_get(handle, adaptor_slot=ADAPTOR_ID, name="sdk-test-vnic-nv")
    assert_not_equal(rcvd_mo, None)
    assert_equal(vnic_mo.name, rcvd_mo.name)
    assert_equal(vnic_mo.class_of_service, rcvd_mo.class_of_service)


def test_non_vntag_delete_vnic():
    vnic_delete(handle, adaptor_slot=ADAPTOR_ID, name="sdk-test-vnic-nv")
    assert_equal(vnic_get(handle, adaptor_slot=ADAPTOR_ID, name="sdk-test-vnic-nv"), None)


def test_vntag_mode():
    adaptor_properties_set(handle, adaptor_slot=ADAPTOR_ID, fip_mode=True,
                                 vntag_mode=True, num_vmfex_ifs=5, lldp=True)
    adaptor_reset(handle, adaptor_slot=ADAPTOR_ID)
    time.sleep(5)
    mo = adaptor_properties_get(handle, adaptor_slot=ADAPTOR_ID)
    assert_equal(mo.vntag_mode.lower(), "enabled")
    assert_equal(mo.fip_mode.lower(), "enabled")
    assert_equal(mo.lldp.lower(), "enabled")


def test_vntag_create_vnic():
    vnic_mo = vnic_create(handle, adaptor_slot=ADAPTOR_ID, name="sdk-test-vnic",
                          channel_number=100, mac="00:11:22:33:44:55",
                          mtu=1500, pxe_boot=True, uplink_port=0)
    rcvd_mo = vnic_get(handle, adaptor_slot=ADAPTOR_ID, name="sdk-test-vnic")
    assert_not_equal(rcvd_mo, None)
    assert_equal(vnic_mo.name, rcvd_mo.name)
    assert_equal(vnic_mo.channel_number, rcvd_mo.channel_number)


def test_vntag_delete_vnic():
    vnic_delete(handle, adaptor_slot=ADAPTOR_ID, name="sdk-test-vnic")
    assert_equal(vnic_get(handle, adaptor_slot=ADAPTOR_ID, name="sdk-test-vnic"), None)


def test_vntag_create_vhba():
    vhba_mo = vhba_create(handle, adaptor_slot=ADAPTOR_ID, name="sdk-test-vhba",
                          channel_number=101, wwnn="10:00:11:3A:7D:D0:9A:43",
                          wwpn="20:00:11:3A:7D:D0:9A:43",
                          san_boot=True, uplink_port=0)
    rcvd_mo = vhba_get(handle, adaptor_slot=ADAPTOR_ID, name="sdk-test-vhba")
    assert_not_equal(rcvd_mo, None)
    assert_equal(vhba_mo.name, rcvd_mo.name)
    assert_equal(vhba_mo.channel_number, rcvd_mo.channel_number)


def test_vntag_delete_vhba():
    vhba_delete(handle, adaptor_slot=ADAPTOR_ID, name="sdk-test-vhba")
    assert_equal(vhba_get(handle, adaptor_slot=ADAPTOR_ID, name="sdk-test-vhba"), None)


def test_disable_vntag_mode():
    adaptor_properties_set(handle, adaptor_slot=ADAPTOR_ID, fip_mode=False,
                                 vntag_mode=False, num_vmfex_ifs=5, lldp=False)
    adaptor_reset(handle, adaptor_slot=ADAPTOR_ID)
    time.sleep(5)
    mo = adaptor_properties_get(handle, adaptor_slot=ADAPTOR_ID)
    assert_equal(mo.vntag_mode.lower(), "disabled")
    assert_equal(mo.fip_mode.lower(), "disabled")
    assert_equal(mo.lldp.lower(), "disabled")
