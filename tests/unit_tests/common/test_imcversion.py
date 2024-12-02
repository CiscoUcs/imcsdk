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

class TestIMCVersion(unittest.TestCase):
    def test_nightly_version1(self):
        version1 = ImcVersion("2.0(13aS6)")
        version2 = ImcVersion("3.0(1S10)")
        self.assertTrue(version1 < version2)

    def test_nightly_version2(self):
        version1 = ImcVersion("2.0(13aS6)")
        version2 = ImcVersion("2.0(1S10)")
        self.assertTrue(version1 > version2)

    def test_nightly_version3(self):
        # 2.0(2cS6) will be considered as 2.0(2d) internally
        version1 = ImcVersion("2.0(2cS6)")
        version2 = ImcVersion("2.0(2c)")
        self.assertFalse(version1 == version2)

    def test_nightly_version4(self):
        version1 = ImcVersion("2.0(2cS6)")
        version2 = ImcVersion("2.0(3)")
        self.assertTrue(version1 < version2)

    def test_spin_version1(self):
        # version interpreted as 4.0(2b)
        version1 = ImcVersion("4.0(2aS3)")
        version2 = ImcVersion("4.0(2b)")
        self.assertFalse(version1 == version2)

    def test_spin_version2(self):
        # version interpreted as 4.0(234c)
        version1 = ImcVersion("4.0(234bS3)")
        version2 = ImcVersion("4.0(234c)")
        self.assertFalse(version1 == version2)

    def test_spin_version3(self):
        # version interpreted as 4.0(2z)
        version1 = ImcVersion("4.0(2S3)")
        version2 = ImcVersion("4.0(2z)")
        self.assertFalse(version1 == version2)

    def test_spin_version4(self):
        # version interpreted as 4.0(234z)
        version1 = ImcVersion("4.0(234S3)")
        version2 = ImcVersion("4.0(234z)")
        self.assertFalse(version1 == version2)

    def test_patch_version1(self):
        version1 = ImcVersion("4.0(234.5)")
        version2 = ImcVersion("4.0(235a)")
        self.assertFalse(version1 == version2)

    def test_gt_same_major_version(self):
        version1 = VersionMeta.Version151f
        version2 = VersionMeta.Version151x
        self.assertTrue(version1 < version2)

    def test_gt_different_major_version(self):
        version1 = VersionMeta.Version151x
        version2 = VersionMeta.Version202c
        self.assertTrue(version1 < version2)

    def test_patch_versions(self):
        # when we don't see a patch version we use z
        # so 2.0(12) will be considerde as 2.0(12z)
        version1 = ImcVersion("2.0(12b)")
        version2 = ImcVersion("2.0(12)")
        self.assertFalse(version1 > version2)

    def test_patch_spin_versions(self):
        # Create instances for testing patch and spin versions
        alpha_ver1 = ImcVersion("4.2(1a)")
        alpha_ver2 = ImcVersion("4.2(1b)")
        alpha_ver3 = ImcVersion("4.2(2a)")
        alpha_ver4 = ImcVersion("4.2(3a)")
        alpha_ver5 = ImcVersion("4.3(1a)")
        num_ver1 = ImcVersion("4.3(2.230190)")
        num_ver2 = ImcVersion("4.3(2.230191)")
        num_ver3 = ImcVersion("4.3(3.230000)")
        num_ver4 = ImcVersion("4.4(1.230000)")
        # Verify version parts
        self.assertEqual(alpha_ver1.major, "4")
        self.assertEqual(alpha_ver1.minor, "2")
        self.assertEqual(alpha_ver1.mr, "1")
        self.assertEqual(alpha_ver1.patch, "a")
        self.assertIsNone(alpha_ver1.spin)
        self.assertEqual(num_ver1.major, "4")
        self.assertEqual(num_ver1.minor, "3")
        self.assertEqual(num_ver1.mr, "2")
        self.assertIsNone(num_ver1.patch)
        self.assertEqual(num_ver1.spin, "230190")
        # Compare Patch versions
        self.assertTrue(alpha_ver1 < alpha_ver2)
        self.assertTrue(alpha_ver2 > alpha_ver1)
        self.assertFalse(alpha_ver1 > alpha_ver2)
        self.assertFalse(alpha_ver2 < alpha_ver1)
        self.assertFalse(alpha_ver2 == alpha_ver1)
        self.assertTrue(alpha_ver2 == alpha_ver2)
        self.assertTrue(alpha_ver2 < alpha_ver3)
        self.assertTrue(alpha_ver3 < alpha_ver4)
        self.assertTrue(alpha_ver4 < alpha_ver5)
        # Compare Patch versions with Spin versions.
        self.assertTrue(alpha_ver5 < num_ver1)
        self.assertTrue(alpha_ver5 <= num_ver1)
        self.assertFalse(alpha_ver5 > num_ver1)
        self.assertFalse(alpha_ver5 >= num_ver1)
        self.assertTrue(alpha_ver4 < num_ver4)
        self.assertTrue(alpha_ver4 < num_ver4)
        self.assertFalse(alpha_ver3 > num_ver3)
        # Compare Spin Versions.
        self.assertTrue(num_ver1 < num_ver2)
        self.assertTrue(num_ver2 > num_ver1)
        self.assertTrue(num_ver2 >= num_ver1)
        self.assertTrue(num_ver2 >= num_ver2)
        self.assertFalse(num_ver1 >= num_ver2)
        self.assertTrue(num_ver2 <= num_ver2)
        self.assertFalse(num_ver2 <= num_ver1)
        self.assertTrue(num_ver1 <= num_ver2)
        self.assertTrue(num_ver1 <= num_ver1)
        self.assertFalse(num_ver1 > num_ver2)
        self.assertFalse(num_ver2 < num_ver1)
        self.assertFalse(num_ver2 == num_ver1)
        self.assertTrue(num_ver2 == num_ver2)
        self.assertTrue(num_ver2 < num_ver3)
        self.assertTrue(num_ver3 < num_ver4)
