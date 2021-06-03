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
from imcsdk.apis.server.bios import bios_tokens_set, bios_tokens_exist

handle = None

tokens = {
    "baudRate": "19200",
    "intelVtdatsSupport": "enabled",
    "consoleRedirection": "com-1",
    "flowControl": "rts-cts",
    "sataModeSelect": "platform-default",
    "txtSupport": "platform-default",
    "packageCstateLimit": "C0 C1 State"
}

tokens_1 = {
    "baudRate": "9600",
    "intelVtdatsSupport": "enabled",
    "consoleRedirection": "com-1",
    "flowControl": "rts-cts",
    "psata": "AHCI"
}

tokens_2 = {
    "baudRate": "platform-default",
    "intelVtdatsSupport": "enabled",
    "consoleRedirection": "com-1",
    "flowControl": "rts-cts"
}

tokens_3 = {
    "baudRate": "platform-default",
    "intelVtdatsSupport": "enabled",
    "consoleRedirection": "platform-default",
    "flowControl": "rts-cts"
}

tokens_4 = {
    "baudRate": "19200",
    "intelVtdatsSupport": "enabled",
    "consoleRedirection": "com-1",
    "flowControl": "rts-cts",
    "test-dummy-token": "undefined-value"
}

tokens_5 = {
    "flowControl": "DUMMY",
}

# On C220 slot6 does not exist, but it exists on C240
# On C240 slot10 does not exist, but it exists on C480
# Hence, the following set of tokens should get skipped appropriately
tokens_6 = {
    "baudRate": "19200",
    "slot6state": "enabled",
    "slot10state": "disabled"
}

tokens_7 = {
    "qpiSnoopMode": "platform-default"
}

tokens_8 = {
    "qpiSnoopMode": "early-snoop"
}

tokens_batch = {
    "baudRate": "platform-default",
    "consoleRedirection": "platform-default",
    "flowControl": "platform-default",
    "slot1state": "platform-default",
    "slot2state": "platform-default",
    "txtSupport": "platform-default",
    "tpmControl": "enabled",
    "usbPortFront": "disabled"
}

# slot1State token below will lead to ValueError exception in the sdk
# osBootWatchdogTimerPolicy will lead to failure on the endpoint
# the idea is to catch all such issues and not lead this to an error
tokens_error = {
    "baudRate": "19200",
    "slot1state": "laknclanc",
    "osBootWatchdogTimerPolicy": "do-nothing"
}


def setup_module():
    global handle
    handle = custom_setup()
    # handle.set_dump_xml()


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


def test_bios_tokens_set_3():
    bios_tokens_set(handle, tokens=tokens_4)


# This should not raise an exception
def test_bios_tokens_set_4():
    bios_tokens_set(handle, tokens=tokens_5)


def test_bios_tokens_set_5():
    bios_tokens_set(handle, tokens=tokens_6)
    match = bios_tokens_exist(handle, tokens=tokens_6)
    assert_equal(match, True)

def test_bios_tokens_set_batch():
    bios_tokens_set(handle, tokens=tokens_batch)
    match = bios_tokens_exist(handle, tokens=tokens_batch)
    assert_equal(match, True)


def test_bios_tokens_set_error():
    bios_tokens_set(handle, tokens=tokens_error)


def test_bios_tokens_set_7():
    bios_tokens_set(handle, tokens=tokens_7)
    match = bios_tokens_exist(handle, tokens=tokens_7)
    assert_equal(match, True)


def test_bios_tokens_set_8():
    bios_tokens_set(handle, tokens=tokens_8)
    match = bios_tokens_exist(handle, tokens=tokens_8)
    assert_equal(match, True)
