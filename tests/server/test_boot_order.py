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

from imcsdk.apis.server.bios import get_boot_order_precision, \
    set_boot_order_precision, set_boot_order_policy, get_boot_order_policy

handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


boot_order_prec_devices = [
    ("1", "hdd", "hdd"), ("2", "pxe", "pxe"), ("3", "pxe", "pxe1")]


def test_boot_order_precision():
    global handle

    set_boot_order_precision(handle, reboot_on_update="yes", boot_mode="Legacy",
                             boot_devices=boot_order_prec_devices)

    rcvd_boot_order = get_boot_order_precision(handle)
    length = len(boot_order_prec_devices)
    for ctr in range(0, length):
        assert_equal(boot_order_prec_devices[ctr][0], rcvd_boot_order[ctr][0])
        assert_equal(boot_order_prec_devices[ctr][1].lower(), rcvd_boot_order[ctr][1].lower())


'''
boot_order_policy_devices = [
    ("1", "storage", "ext-hdd1"),
    ("2", "lan", "mylan")]


def test_boot_order_policy():
    global handle

    set_boot_order_policy(handle, reboot_on_update="yes",
                               secure_boot=False,
                               boot_devices=boot_order_policy_devices)

    rcvd_dev_list = get_boot_order_policy(handle)
    length = len(boot_order_policy_devices)
    for ctr in range(0, length):
        assert_equal(boot_order_policy_devices[ctr][0], rcvd_dev_list[ctr][0])
        assert_equal(boot_order_policy_devices[ctr][1], rcvd_dev_list[ctr][1])

'''
