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

from nose.tools import assert_equal, raises
# from ..connection.info import custom_setup, custom_teardown
from imcsdk.apis.server.storage import _flatten_list
from imcsdk.apis.server.storage import _flatten_to_string
from imcsdk.apis.server.storage import _vd_name_derive
from imcsdk.apis.server.storage import _human_to_bytes
from imcsdk.apis.server.storage import _bytes_to_human


def test_flatten_list():
    tests = [{"input": [[1]], "expected": [1]},
             {"input": [[1, 2]], "expected": [1, 2]},
             {"input": [[1, 2], [3, 4]], "expected": [1, 2, 3, 4]}]
    for test in tests:
        assert_equal(_flatten_list(test["input"]), test["expected"])


@raises(Exception)
def test_flatten_list_error():
    _flatten_list([1])


def test_flatten_to_string():
    tests = [{"input": [[1]], "expected": '1'},
             {"input": [[1, 2]], "expected": '12'},
             {"input": [[1, 2], [3, 4]], "expected": '1234'}]
    for test in tests:
        assert_equal(_flatten_to_string(test["input"]), test["expected"])


def test_vd_name_derive():
    tests = [{"dg": [[1]], "raid": 0, "expected": 'RAID0_1'},
             {"dg": [[1, 2]], "raid": 1, "expected": 'RAID1_12'},
             {"dg": [[1, 2], [3, 4]], "raid": 10, "expected": 'RAID10_1234'}]
    for test in tests:
        assert_equal(_vd_name_derive(test["raid"], test["dg"]),
                     test["expected"])


def test_human_to_bytes():
    tests = [{"input": "1 KB", "expected": 1024},
             {"input": "100 MB", "expected": 100 * 1024*1024},
             {"input": "121 GB", "expected": 121 * 1024*1024*1024},
             {"input": "1 TB", "expected": 1024*1024*1024*1024},
             {"input": "1 PB", "expected": 1024*1024*1024*1024*1024},
             {"input": "1 EB", "expected": 1024*1024*1024*1024*1024*1024},
             {"input": "1 ZB", "expected": 1024*1024*1024*1024*1024*1024*1024},
             {"input": "1 YB", "expected": 1024*1024*1024*1024*1024*1024*1024*1024}]
    for test in tests:
        assert_equal(_human_to_bytes(test["input"]), test["expected"])


def test_bytes_to_human():
    tests = [{"input": 100*1024*1024, "expected": "100 MB"},
             {"input": 100*1024*1024*1024, "expected": "100 GB"},
             {"input": 100*1024*1024*1024, "format": "MB", "expected": "102400 MB"}]
    for test in tests:
        if "format" in test:
            assert_equal(_bytes_to_human(test["input"], test["format"]), test["expected"])
        else:
            assert_equal(_bytes_to_human(test["input"]), test["expected"])
