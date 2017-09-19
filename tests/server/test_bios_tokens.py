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
from ..connection.info import custom_setup, custom_teardown
from nose.tools import assert_equal, assert_not_equal

from imcsdk.apis.server.bios import bios_tokens_set, bios_tokens_exist

handle = None

tokens = {
        "BaudRate": "19200",
        "IntelVTDATSSupport": "enabled",
        "ConsoleRedirection": "com-1",
        "FlowControl": "rts-cts"
}

tokens_1 = {
        "BaudRate": "9600",
        "IntelVTDATSSupport": "enabled",
        "ConsoleRedirection": "com-1",
        "FlowControl": "rts-cts"
}

tokens_2 = {
    "BaudRate": "platform-default",
    "IntelVTDATSSupport": "enabled",
    "ConsoleRedirection": "com-1",
    "FlowControl": "rts-cts"
}

tokens_3 = {
        "BaudRate": "platform-default",
        "IntelVTDATSSupport": "enabled",
        "ConsoleRedirection": "platform-default",
        "FlowControl": "rts-cts"
}


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_bios_tokens_set():
    bios_tokens_set(handle, tokens=tokens)
    match = bios_tokens_exist(handle, tokens=tokens)
    assert_equal(match, True)


def test_bios_tokens_exist():
    match = bios_tokens_exist(handle, tokens=tokens_1)
    assert_equal(match, False)
    match = bios_tokens_exist(handle, tokens=tokens_2)
    assert_equal(match, True)


def test_bios_tokens_set_2():
    bios_tokens_set(handle, tokens=tokens_3)
    match = bios_tokens_exist(handle, tokens=tokens_3)
    assert_equal(match, True)
