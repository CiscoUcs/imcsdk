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

from imcsdk.imcmeta import VersionMeta
from imcsdk.imccoremeta import ImcVersion

class TestImcVersion(unittest.TestCase):
    def test_nightly_version1(self):
        version1 = ImcVersion("2.0(13aS6)")
        version2 = ImcVersion("3.0(1S10)")
        assert (version1 < version2) == True


    def test_nightly_version2(self):
        version1 = ImcVersion("2.0(13aS6)")
        version2 = ImcVersion("2.0(1S10)")
        assert (version1 > version2) == True


    def test_nightly_version3(self):
        # 2.0(2cS6) will be considered as 2.0(2d) internally
        version1 = ImcVersion("2.0(2cS6)")
        version2 = ImcVersion("2.0(2c)")
        assert (version1 == version2) == False


    def test_nightly_version4(self):
        version1 = ImcVersion("2.0(2cS6)")
        version2 = ImcVersion("2.0(3)")
        assert (version1 < version2) == True


    def test_spin_version1(self):
        # version interpreted as 4.0(2b)
        version1 = ImcVersion("4.0(2aS3)")
        version2 = ImcVersion("4.0(2b)")
        assert (version1 == version2) == True


    def test_spin_version2(self):
        # version interpreted as 4.0(234c)
        version1 = ImcVersion("4.0(234bS3)")
        version2 = ImcVersion("4.0(234c)")
        assert (version1 == version2) == True


    def test_spin_version3(self):
        # version interpreted as 4.0(2z)
        version1 = ImcVersion("4.0(2S3)")
        version2 = ImcVersion("4.0(2z)")
        assert (version1 == version2) == True


    def test_spin_version4(self):
        # version interpreted as 4.0(234z)
        version1 = ImcVersion("4.0(234S3)")
        version2 = ImcVersion("4.0(234z)")
        assert (version1 == version2) == True


    def test_patch_version1(self):
        # version interpreted as 4.0(235a)
        version1 = ImcVersion("4.0(234.5)")
        version2 = ImcVersion("4.0(235a)")
        assert (version1 == version2) == True


    def test_gt_same_major_version(self):
        version1 = VersionMeta.Version151f
        version2 = VersionMeta.Version151x
        assert (version1 < version2) == True


    def test_gt_different_major_version(self):
        version1 = VersionMeta.Version151x
        version2 = VersionMeta.Version202c
        assert (version1 < version2) == True


    def test_patch_versions(self):
        version1 = ImcVersion("2.0(12b)")
        version2 = ImcVersion("2.0(12)")
        assert (version1 > version2) == True

