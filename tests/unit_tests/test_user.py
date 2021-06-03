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


from imcsdk.apis.admin.user import user_validate_inputs
from nose.tools import eq_


def test_user_validation_success():
    params = {
        "id": 1,
        "name": "test",
        "priv": "admin"
    }

    validation_errors = user_validate_inputs(**params)
    print(validation_errors)
    eq_(len(validation_errors), 0)


def test_user_validation_failure_priv():
    params = {
        "id": 1,
        "name": "test",
        "priv": "abcd"
    }

    validation_errors = user_validate_inputs(**params)
    print(validation_errors)
    eq_(len(validation_errors), 1)


def test_user_validation_failure_id():
    params = {
        "id": "abcd",
        "name": "test",
        "priv": "admin"
    }

    validation_errors = user_validate_inputs(**params)
    print(validation_errors)
    eq_(len(validation_errors), 1)
