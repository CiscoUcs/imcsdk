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

import unittest

import imcsdk.imccoreutils as cutil

class TestImcCoreUtils(unittest.TestCase):
    def test_001_get_naming_props(self):
        rn_pattern = "fault-[code]-[name]-[type]-xyz-[state]"
        rn_str = "fault-F35275-fault-c2-xyz-on"
        np = cutil.get_naming_props(rn_str, rn_pattern)
        assert np['code'] == 'F35275'
        assert np['name'] == 'fault'
        assert np['type'] == 'c2'
        assert np['state'] == 'on'


    def test_002_get_naming_props(self):
        rn_pattern = "[suport_type][card_param_type]"
        rn_str = "11"
        np = cutil.get_naming_props(rn_str, rn_pattern)
        assert np['suport_type'] == '1'
        assert np['card_param_type'] == '1'


    def test_003_get_naming_props(self):
        rn_pattern = "[suport_type][card_param_type]"
        rn_str = "1122"
        np = cutil.get_naming_props(rn_str, rn_pattern)
        assert np['suport_type'] == '112'
        assert np['card_param_type'] == '2'
