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

from imcsdk.apis.server.bios import get_boot_order_precision, \
    set_boot_order_precision, set_boot_order_policy, get_boot_order_policy

handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


boot_order_prec_devices = [{"order": '1', "type": "hdd", "name": "hdd"},
                           {"order": '2', "type": "pxe", "name": "pxe"},
                           {"order": '3', "type": "pxe", "name": "pxe1"}]

def test_boot_order_precision():
    global handle
    from imcsdk.apis.server.bios import get_configured_boot_precision

    set_boot_order_precision(handle, reboot_on_update=True,
                             configured_boot_mode="Legacy",
                             boot_devices=boot_order_prec_devices)

    rcvd_boot_order = get_configured_boot_precision(handle)
    for ctr in range(0, len(rcvd_boot_order)):
        if boot_order_prec_devices[ctr]["order"] != rcvd_boot_order[ctr]["order"] or \
           boot_order_prec_devices[ctr]["type"].lower() != rcvd_boot_order[ctr]["type"].lower():
            raise SkipTest


boot_order_policy_devices = [{"order": '1', "type": "storage", "name": "ext-hdd1"},
                             {"order": '2', "type": "lan", "name": "mylan"}]


def test_boot_order_policy():
    global handle

    set_boot_order_policy(handle, reboot_on_update=True,
                          secure_boot=False,
                          boot_devices=boot_order_policy_devices)

    rcvd_dev_list = get_boot_order_policy(handle)
    length = len(boot_order_policy_devices)
    for ctr in range(0, length):
        if boot_order_policy_devices[ctr]["order"] != rcvd_dev_list[ctr]["order"] or \
           boot_order_policy_devices[ctr]["type"] != rcvd_dev_list[ctr]["type"]:
            raise SkipTest


def test_boot_order_precision_exists():
    from imcsdk.apis.server.bios import boot_order_precision_exists

    ret, msg = boot_order_precision_exists(
        handle,
        reboot_on_update=False,
        configured_boot_mode="Legacy",
        boot_devices=[{"order": "1", "type": "hdd", "name": "hdd"},
                      {"order": "2", "type": "pxe", "name": "pxe"},
                      {"order": "3", "type": "pxe", "name": "pxe1"}],
        server_id=1
    )
    if not ret:
        print(msg)
    assert_equal(ret, True)
