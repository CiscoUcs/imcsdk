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
from nose.tools import assert_equal, raises
from imcsdk.apis.server.bios import bios_tokens_set

handle = None


def setup_module():
    global handle
    handle = custom_setup()
    # handle.set_dump_xml()


def teardown_module():
    global handle
    custom_teardown(handle)


tokens_nondefault = {
        "sataModeSelect": "LSI SW RAID"
}

tokens_default = {
        "sataModeSelect": "platform-default"
}


def test_bios_token_sataModeSelect_nondefault():
    bios_tokens_set(handle, tokens=tokens_nondefault)


def test_bios_token_sataModeSelect_default():
    bios_tokens_set(handle, tokens=tokens_default)
