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

from nose.tools import raises, assert_equal
from ..connection.info import custom_setup, custom_teardown
from imcsdk.apis.server.inventory import inventory_get
from imcsdk.apis.server.serveractions import tag_server, tag_chassis
from imcsdk.imccoreutils import IMC_PLATFORM

handle = None


def _delete_file(file_name):
    import os
    if os.path.exists(file_name):
        os.remove(file_name)


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    custom_teardown(handle)
    _delete_file("inventory.json")
    _delete_file("inventory.csv")
    _delete_file("inventory.html")


def test_get_inventory():
    inventory_get(handle, file_format="html", file_name="inventory.html")
    inventory_get(handle, component=["cpu", "disks"], file_format="html",
                  file_name="inventory.html")
    inventory_get(handle, component=["cpu", "disks", "all"],
                  file_format="html", file_name="inventory.html")
    inventory_get(handle, component="cpu", file_format="csv",
                  file_name="inventory.csv")
    inventory_get(handle, component="disks", file_format="json",
                  file_name="inventory.json")
    inventory_get(handle, component="vic")


@raises(Exception)
def test_get_inventory_error():
    inventory_get(handle, component="vic", file_format="csv")


@raises(Exception)
def test_get_inventory_invalid_component():
    inventory_get(handle, component="invalid", file_format="csv")


def test_asset_tag_server():
    if handle.platform != IMC_PLATFORM.TYPE_CLASSIC:
        return
    mo = tag_server(handle, tag='ABCD-1234')
    mo = handle.query_dn(mo.dn)
    assert_equal(mo.asset_tag, 'ABCD-1234')


def test_asset_tag_chassis():
    if handle.platform != IMC_PLATFORM.TYPE_MODULAR:
        return
    mo = tag_chassis(handle, tag='ABCD-1234')
    mo = handle.query_dn(mo.dn)
    assert_equal(mo.asset_tag, 'ABCD-1234')
