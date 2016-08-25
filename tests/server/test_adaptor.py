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

from nose.tools import assert_equal, assert_not_equal
from ..connection.info import custom_setup, custom_teardown
from imcsdk.apis.server.adaptor import setup_vic_adaptor_properties, \
    get_vic_adaptor_properties, create_vnic, delete_vnic, get_vnic, \
    create_vhba, delete_vhba, get_vhba


handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    custom_teardown(handle)


def test_enable_adaptor_properties():
    global handle
    setup_vic_adaptor_properties(handle, adaptor_slot=1, fip_mode=True,
                                 vntag_mode=True, num_vmfex_ifs=5)
    mo = get_vic_adaptor_properties(handle, adaptor_slot=1)
    assert_equal(mo.vntag_mode.lower(), "enabled")
    assert_equal(mo.fip_mode.lower(), "enabled")


def test_create_vnic():
    global handle
    vnic_mo = create_vnic(handle, adaptor_slot=1, name="sdk-test-vnic",
                          channel_number=100, cos="", mac="00:11:22:33:44:55",
                          mtu=1500, port_profile="",
                          pxe_boot=True, uplink_port=0)
    rcvd_mo = get_vnic(handle, adaptor_slot=1, name="sdk-test-vnic")
    assert_not_equal(rcvd_mo, None)
    assert_equal(vnic_mo.name, rcvd_mo.name)
    assert_equal(vnic_mo.channel_number, rcvd_mo.channel_number)


def test_delete_vnic():
    global handle
    delete_vnic(handle, adaptor_slot=1, name="sdk-test-vnic")
    assert_equal(get_vnic(handle, adaptor_slot=1, name="sdk-test-vnic"), None)


def test_create_vhba():
    global handle
    vhba_mo = create_vhba(handle, adaptor_slot=1, name="sdk-test-vhba",
                          channel_number=101, wwnn="10:00:11:3A:7D:D0:9A:43",
                          wwpn="20:00:11:3A:7D:D0:9A:43", port_profile="",
                          san_boot=True, uplink_port=0)
    rcvd_mo = get_vhba(handle, adaptor_slot=1, name="sdk-test-vhba")
    assert_not_equal(rcvd_mo, None)
    assert_equal(vhba_mo.name, rcvd_mo.name)
    assert_equal(vhba_mo.channel_number, rcvd_mo.channel_number)


def test_delete_vhba():
    global handle
    delete_vhba(handle, adaptor_slot=1, name="sdk-test-vhba")
    assert_equal(get_vhba(handle, adaptor_slot=1, name="sdk-test-vhba"), None)


def test_disable_adaptor_properties():
    global handle
    setup_vic_adaptor_properties(handle, adaptor_slot=1, fip_mode=False,
                                 vntag_mode=False, num_vmfex_ifs=5)
    mo = get_vic_adaptor_properties(handle, adaptor_slot=1)
    assert_equal(mo.vntag_mode.lower(), "disabled")
    assert_equal(mo.fip_mode.lower(), "disabled")
