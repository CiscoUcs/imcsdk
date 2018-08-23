# Copyright 2015 Cisco Systems, Inc.
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

from nose.tools import assert_equal, raises
from imcsdk.imchandle import ImcHandle
from ..connection.info import custom_setup, custom_teardown
from imcsdk.imccoreutils import get_server_dn


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_001_create_uri():
    # Create an object of type LsServer with parent dn specified
    # check if the object has the right values populated
    temp_handle = ImcHandle("192.168.1.1", "admin", "password")

    assert_equal(
        temp_handle._ImcSession__create_uri(
            port=None,
            secure=None),
        'https://192.168.1.1:443')

    assert_equal(
        temp_handle._ImcSession__create_uri(
            port=8080,
            secure=None),
        'https://192.168.1.1:8080')

    assert_equal(
        temp_handle._ImcSession__create_uri(
            port=None,
            secure=True),
        'https://192.168.1.1:443')

    assert_equal(
        temp_handle._ImcSession__create_uri(
            port=None,
            secure=False),
        'http://192.168.1.1:80')

    assert_equal(
        temp_handle._ImcSession__create_uri(
            port=444,
            secure=False),
        'http://192.168.1.1:444')


def test_imc_no_timeout():

    global handle
    server_dn = get_server_dn(handle)
    mo = handle.query_dn(server_dn, timeout=600)
    usr_lbl = "test-lbl1"
    mo.usr_lbl = usr_lbl
    handle.set_mo(mo, timeout=600)

    mo = handle.query_dn(server_dn)
    assert_equal(mo.usr_lbl, usr_lbl)


@raises(Exception)
def test_imc_timeout():

    from six.moves import urllib

    global handle
    server_dn = get_server_dn(handle)
    mo = handle.query_dn(server_dn, timeout=600)
    usr_lbl = "test-lbl2"
    mo.usr_lbl = usr_lbl
    try:
        handle.set_mo(mo, timeout=1)
    except urllib.error.URLError:
        print("Hit expected error")
        raise Exception


def test_imc_context_manager_no_timeout():
    from six.moves import configparser
    from imcsdk.imchandle import ImcHandle
    from ..connection import info

    host = 'imc'
    config = configparser.RawConfigParser()
    config.read(info.CONNECTION_CFG_FILEPATH)
    hostname = config.get(host, "hostname")
    username = config.get(host, "username")
    password = config.get(host, "password")

    handle = ImcHandle(hostname, username, password)
    with handle:
        server_dn = get_server_dn(handle)
        mo = handle.query_dn(server_dn, timeout=600)
        usr_lbl = "test-lbl2"
        mo.usr_lbl = usr_lbl
        handle.set_mo(mo, timeout=600)
        mo = handle.query_dn(server_dn)

    assert_equal(mo.usr_lbl, usr_lbl)
