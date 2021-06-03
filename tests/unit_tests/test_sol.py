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


from imcsdk.apis.server.sol import sol_validate_inputs
from nose.tools import eq_


def test_sol_validation_success():
    params = {
        "admin_state": "enable",
        "speed": "115200",
        "comport": "com0",
        "ssh_port": "3000"
    }

    validation_errors = sol_validate_inputs(**params)
    print(validation_errors)
    eq_(len(validation_errors), 0)


def test_sol_validation_fail_admin_state():
    params = {
        "admin_state": "ok",
        "speed": "115200",
        "comport": "com0",
        "ssh_port": "3000"
    }

    validation_errors = sol_validate_inputs(**params)
    eq_(len(validation_errors), 1)


def test_sol_validation_fail_speed_string():
    params = {
        "admin_state": "enable",
        "speed": "2300",
        "comport": "com0",
        "ssh_port": "3000"
    }

    validation_errors = sol_validate_inputs(**params)
    eq_(len(validation_errors), 1)


def test_sol_validation_fail_speed_int():
    params = {
        "admin_state": "enable",
        "speed": 2300,
        "comport": "com0",
        "ssh_port": "3000"
    }

    validation_errors = sol_validate_inputs(**params)
    eq_(len(validation_errors), 1)


def test_sol_validation_fail_multiple():
    params = {
        "admin_state": "enable",
        "speed": "115200",
        "comport": "com2",
        "ssh_port": "10"
    }

    validation_errors = sol_validate_inputs(**params)
    eq_(len(validation_errors), 2)
    print(validation_errors)
