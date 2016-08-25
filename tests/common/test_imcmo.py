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
from imcsdk.imcmo import ManagedObject


@raises(Exception)
def test_001_create_mo_directly():
    # Create a Managed Object by specifying the classId and parent dn
    # this should raise an exception as the associated Meta's will not
    # be initialised.
    ManagedObject("aaaUser", "sys/user-ext/user-1")


def test_002_create_specific_obj():
    # Create an object of type AaaUser with parent dn specified
    # check if the object has the right values populated
    from imcsdk.mometa.aaa.AaaUser import AaaUser
    obj = AaaUser(parent_mo_or_dn="sys/user-ext", id="10")
    assert_equal(obj.id, "10")
    assert_equal(obj.dn, "sys/user-ext/user-10")
