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
from nose.plugins.skip import SkipTest
from nose.tools import assert_equal

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
            {"order": "1", "device-type": "hdd", "name": "hdd"},
            {"order": "2", "device-type": "pxe", "name": "pxe"},
            {"order": "3", "device-type": "pxe", "name": "pxe2"}
        ],
        [
            {"order": "1", "device-type": "hdd", "name": "hdd"},
            {"order": "2", "device-type": "pxe", "name": "pxe2"},
            {"order": "3", "device-type": "pxe", "name": "pxe"}
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


def test_boot_order_precision():
    global handle, boot_order_prec_devices
    from imcsdk.apis.server.boot import boot_precision_configured_get

    boot_order_precision_set(handle, reboot_on_update="no",
                             configured_boot_mode="Legacy",
                             boot_devices=boot_order_prec_devices)

    rcvd_boot_order = boot_precision_configured_get(handle)
    devices = sorted(boot_order_prec_devices, key=lambda x: x["order"])
    for ctr in range(0, len(rcvd_boot_order)):
        if devices[ctr]["order"] != rcvd_boot_order[ctr]["order"] or \
           devices[ctr]["device-type"].lower() != rcvd_boot_order[ctr]["device-type"].lower():
            raise SkipTest


boot_order_prec_devices_2 = [
        {"order": '1', "device-type": "hdd", "name": "hdd"},
        {"order": '2', "device-type": "pxe", "name": "pxe", "slot": "10", "port": "100"},
        {"order": '3', "device-type": "pxe", "name": "pxe1"},
        {"order": '4', "device-type": "usb", "name": "usb0", "subtype": "usb-cd"}]


def test_boot_order_precision_2():
    global handle, boot_order_prec_devices
    from imcsdk.apis.server.boot import boot_precision_configured_get

    boot_order_precision_set(handle, reboot_on_update="no",
                             configured_boot_mode="Legacy",
                             boot_devices=boot_order_prec_devices_2)

    rcvd_boot_order = boot_precision_configured_get(handle)
    devices = sorted(boot_order_prec_devices_2, key=lambda x: x["order"])
    for ctr in range(0, len(rcvd_boot_order)):
        if devices[ctr]["order"] != rcvd_boot_order[ctr]["order"] or \
           devices[ctr]["device-type"].lower() != rcvd_boot_order[ctr]["device-type"].lower():
            raise SkipTest


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
    assert_equal(ret, True)
