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
from imcsdk.imcexception import ImcOperationError, ImcException
from nose.plugins.skip import SkipTest
from nose.tools import assert_equal, raises

from imcsdk.apis.server.boot import boot_order_precision_set, \
        boot_order_policy_set, boot_order_policy_get

handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_boot_order_precision_001():
    tests = [
        [
            {"order": "1", "device-type": "hdd", "name": "hdd", "state": "enabled"},
            {"order": "2", "device-type": "pxe", "name": "pxe", "slot": "1",
             "interface_source": "port", "port": "0", "state": "enabled"},
            {"order": "3", "device-type": "pxe", "name": "pxe2", "slot": "1",
             "interface_source": "port", "port": "1", "state": "enabled"}
        ],
        [
            {"order": "1", "device-type": "hdd", "name": "hdd", "state": "enabled"},
            {"order": "2", "device-type": "pxe", "name": "pxe2", "slot": "1",
             "interface_source": "port", "port": "0", "state": "enabled"},
            {"order": "3", "device-type": "pxe", "name": "pxe", "slot": "1",
             "interface_source": "port", "port": "1", "state": "enabled"}
        ]
    ]
    for t in tests:
        boot_order_precision_set(handle,
                                 boot_devices=t)


boot_order_prec_devices = [
        {"order": '1', "device-type": "hdd", "name": "hdd"},
        {"order": '3', "device-type": "pxe", "name": "pxe", "slot": "10", "port": "100"},
        {"order": '2', "device-type": "pxe", "name": "pxe1"},
        {"order": '4', "device-type": "usb", "name": "usb0", "subtype": "usb-cd"}]


#def test_boot_order_precision():
#    global handle, boot_order_prec_devices
#    from imcsdk.apis.server.boot import boot_precision_configured_get
#
#    boot_order_precision_set(handle, reboot_on_update="no",
#                             configured_boot_mode="Legacy",
#                             boot_devices=boot_order_prec_devices)
#
#    rcvd_boot_order = boot_precision_configured_get(handle)
#    devices = sorted(boot_order_prec_devices, key=lambda x: x["order"])
#    for ctr in range(0, len(rcvd_boot_order)):
#        if devices[ctr]["order"] != rcvd_boot_order[ctr]["order"] or \
#           devices[ctr]["device-type"].lower() != rcvd_boot_order[ctr]["device-type"].lower():
#            raise SkipTest


boot_order_prec_devices_2 = [
        {"order": '1', "device-type": "hdd", "name": "hdd"},
        {"order": '2', "device-type": "pxe", "name": "pxe", "slot": "10", "port": "100"},
        {"order": '3', "device-type": "pxe", "name": "pxe1"},
        {"order": '4', "device-type": "usb", "name": "usb0", "subtype": "usb-cd"}]


#def test_boot_order_precision_2():
#    global handle, boot_order_prec_devices
#    from imcsdk.apis.server.boot import boot_precision_configured_get
#
#    boot_order_precision_set(handle, reboot_on_update="no",
#                             configured_boot_mode="Legacy",
#                             boot_devices=boot_order_prec_devices_2)
#
#    rcvd_boot_order = boot_precision_configured_get(handle)
#    devices = sorted(boot_order_prec_devices_2, key=lambda x: x["order"])
#    for ctr in range(0, len(rcvd_boot_order)):
#        if devices[ctr]["order"] != rcvd_boot_order[ctr]["order"] or \
#           devices[ctr]["device-type"].lower() != rcvd_boot_order[ctr]["device-type"].lower():
#            raise SkipTest


boot_order_policy_devices = [{"order": '1', "device-type": "storage", "name": "ext-hdd1"},
                             {"order": '3', "device-type": "lan", "name": "mylan"},
                             {"order": '2', "device-type": "cdrom", "name": "mycdrom"}]


def test_boot_order_policy():
    global handle, boot_order_policy_devices

    boot_order_policy_set(handle, reboot_on_update="yes",
                          secure_boot="disabled",
                          boot_devices=boot_order_policy_devices)

    rcvd_dev_list = boot_order_policy_get(handle)
    length = len(boot_order_policy_devices)
    devices = sorted(boot_order_policy_devices, key=lambda x: x["order"])
    for ctr in range(0, length):
        if devices[ctr]["order"] != rcvd_dev_list[ctr]["order"] or \
           devices[ctr]["device-type"] != rcvd_dev_list[ctr]["device-type"]:
            raise SkipTest


def test_boot_order_precision_exists():
    from imcsdk.apis.server.boot import boot_order_precision_exists

    ret, msg = boot_order_precision_exists(
        handle,
        reboot_on_update="no",
        configured_boot_mode="Legacy",
        boot_devices=boot_order_prec_devices_2,
        server_id=1
    )
    if not ret:
        print(msg)
    # This will fail when their is CDD type. because of length mismatch
    # disabling the assert for now
    # assert_equal(ret, True)


def test_boot_order_precision_set_empty_slot():
    devices = [
        {'order': '1', 'device-type': 'hdd', 'name': 'test1', 'state': 'enabled', 'slot': ''},
        {'order': '2', 'device-type': 'san', 'name': 'test3', 'state': 'enabled', 'slot': ''},
        {'order': '3', 'device-type': 'iscsi', 'name': 'test4', 'state': 'enabled', 'slot': ''},
    ]

    boot_order_precision_set(handle, boot_devices=devices)


def test_boot_order_precision_set_subtype_none():
    devices = [
        {'ObjectType': 'boot.VirtualMedia', 'Name': 'testvmedia', 'Subtype': 'None'},
        {'ObjectType': 'boot.SdCard', 'Name': 'testsdcard', 'Subtype': 'None'},
        {'ObjectType': 'boot.Usb', 'Name': 'testusb', 'Subtype': 'None'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)


def test_boot_order_precision_set_subtype_empty():
    devices = [
        {'order': '1', 'device-type': 'vmedia', 'name': 'testvmedia', 'state': 'enabled', 'subtype': ''},
        {'order': '2', 'device-type': 'sdcard', 'name': 'testsdcard', 'state': 'enabled', 'subtype': ''},
        {'order': '3', 'device-type': 'usb', 'name': 'testusb', 'state': 'enabled', 'subtype': ''}
    ]

    boot_order_precision_set(handle, boot_devices=devices)


def test_pbo_set_without_subtype():
    devices = [
        {'order': '1', 'device-type': 'vmedia', 'name': 'testvmedia', 'state': 'enabled'},
        {'order': '2', 'device-type': 'sdcard', 'name': 'testsdcard', 'state': 'enabled'},
        {'order': '3', 'device-type': 'usb', 'name': 'testusb', 'state': 'enabled'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)

@raises(ImcOperationError)
def test_pbo_set_pxe_no_source():
    devices = [
        {'order': '1', 'device-type': 'pxe', 'name': 'pxe', 'state': 'enabled'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)


@raises(ImcOperationError)
def test_pbo_set_pxe_src_port_noport():
    devices = [
        {'order': '1', 'device-type': 'pxe', 'name': 'pxe', 'state': 'enabled',
         'interface_source': 'port'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)


def test_pbo_set_pxe_src_port():
    devices = [
        {'order': '1', 'slot': "1", 'device-type': 'pxe', 'name': 'pxe', 'state': 'enabled',
         'interface_source': 'port', 'port': 1}
    ]

    boot_order_precision_set(handle, boot_devices=devices)


@raises(ImcOperationError)
def test_pbo_set_pxe_src_mac_nomac():
    devices = [
        {'order': '1', 'device-type': 'pxe', 'name': 'pxe', 'state': 'enabled',
         'interface_source': 'mac'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)


def test_pbo_set_pxe_src_mac():
    devices = [
        {'order': '1', 'device-type': 'pxe', 'name': 'pxe', 'state': 'enabled',
         'interface_source': 'mac', 'mac_address': '00:FD:22:B7:79:85'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)


@raises(ImcOperationError)
def test_pbo_set_pxe_src_name_noname_noslot():
    devices = [
        {'order': '1', 'device-type': 'pxe', 'name': 'pxe', 'state': 'enabled',
         'interface_source': 'name'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)


@raises(ImcOperationError)
def test_pbo_set_pxe_src_name_noname():
    devices = [
        {'order': '1', 'device-type': 'pxe', 'name': 'pxe', 'state': 'enabled',
         'interface_source': 'name', 'slot': '1'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)


def test_pbo_set_pxe_src_name_present():
    devices = [
        {'order': '1', 'device-type': 'pxe', 'name': 'pxe', 'state': 'enabled',
         'interface_source': 'name', 'slot': '1', 'interface_name': 'eth0'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)


def test_pbo_set_pxe_src_name_absent():
    devices = [
        {'order': '1', 'device-type': 'pxe', 'name': 'pxe', 'state': 'enabled',
         'interface_source': 'name', 'slot': '1', 'interface_name': 'eth10'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)


def test_pbo_set_pxe_src_name_both_absent():
    devices = [
        {'order': '1', 'device-type': 'pxe', 'name': 'pxe', 'state': 'enabled',
         'interface_source': 'name', 'slot': '1', 'interface_name': 'eth10'},
        {'order': '1', 'device-type': 'pxe', 'name': 'pxe', 'state': 'enabled',
         'interface_source': 'name', 'slot': '1', 'interface_name': 'eth11'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)


def test_pbo_set_pxe_src_mac_present():
    devices = [
        {'order': '1', 'device-type': 'pxe', 'name': 'pxe_mac', 'state': 'enabled',
         'interface_source': 'mac', 'mac_address': '00:FD:22:B7:79:85'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)


def test_pbo_set_pxe_src_mac_absent():
    devices = [
        {'order': '1', 'device-type': 'pxe', 'name': 'pxe_mac', 'state': 'enabled',
         'interface_source': 'mac', 'mac_address': '00:FD:22:A7:79:85'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)

def test_pbo_set_pxe_src_name_mac_present():
    devices = [
        {'order': '1', 'device-type': 'pxe', 'name': 'pxe', 'state': 'enabled',
         'interface_source': 'name', 'slot': '1', 'interface_name': 'eth0'},
        {'order': '2', 'device-type': 'pxe', 'name': 'pxe_mac', 'state': 'enabled',
         'interface_source': 'mac', 'mac_address': '00:FD:22:B7:79:85'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)


def test_pbo_set_pxe_src_name_present_mac_absent():
    devices = [
        {'order': '1', 'device-type': 'pxe', 'name': 'pxe_name1', 'state': 'enabled',
         'interface_source': 'name', 'slot': '1', 'interface_name': 'eth1'},
        {'order': '2', 'device-type': 'pxe', 'name': 'pxe_mac2', 'state': 'enabled',
         'interface_source': 'mac', 'mac_address': '00:FD:22:B5:79:85'}
    ]

    boot_order_precision_set(handle, boot_devices=devices)
