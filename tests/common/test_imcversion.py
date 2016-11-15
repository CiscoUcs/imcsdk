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

from nose.tools import assert_equal
from imcsdk.imcmeta import VersionMeta
from imcsdk.imccoremeta import ImcVersion
from ..connection.info import custom_setup, custom_teardown


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_gt_same_major_version():
    version1 = VersionMeta.Version151f
    version2 = VersionMeta.Version151x
    assert_equal((version2 > version1), True)


def test_gt_different_major_version():
    version1 = VersionMeta.Version151x
    version2 = VersionMeta.Version202c
    assert_equal((version2 > version1), True)


def test_handle_version():
    global handle
    assert_equal(type(handle.version), ImcVersion)


def test_handle_mo_version():
    global handle
    mos = handle.query_classid("BiosUnit")
    mo_version = mos[0].get_version(platform=handle.platform)
    assert_equal((handle.version < mo_version), False)
