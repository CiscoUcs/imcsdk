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
from imcsdk.apis.server.inventory import get_inventory

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
    get_inventory(handle, file_format="html", file_name="inventory.html")
    get_inventory(handle, component="cpu", file_format="csv",
                  file_name="inventory.csv")
    get_inventory(handle, component="disks", file_format="json",
                  file_name="inventory.json")
    get_inventory(handle, component="vic")


@raises(Exception)
def test_get_inventory_error():
    get_inventory(handle, component="vic", file_format="csv")
