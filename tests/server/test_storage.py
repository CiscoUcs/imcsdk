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
from ..connection.info import custom_setup, custom_teardown
from imcsdk.apis.server.storage import _list_to_string
from imcsdk.apis.server.storage import _flatten_list
from imcsdk.apis.server.storage import _flatten_to_string
from imcsdk.apis.server.storage import _vd_name_derive
from imcsdk.apis.server.storage import _human_to_bytes
from imcsdk.apis.server.storage import _bytes_to_human
from imcsdk.apis.server.storage import _pd_min_size_get
from imcsdk.apis.server.storage import _pd_total_size_get
from imcsdk.apis.server.storage import _vd_span_depth_get
from imcsdk.apis.server.storage import _raid_max_size_get
from imcsdk.apis.server.storage import virtual_drive_create
from imcsdk.apis.server.storage import virtual_drive_delete
from imcsdk.imccoreutils import get_server_dn


def test_list_to_string():
    tests = [{"input": [[1]], "expected": '[1]'},
             {"input": [[1, 2]], "expected": '[1,2]'},
             {"input": [[1, 2], [3, 4]], "expected": '[1,2][3,4]'},
             {"input": [[1], [4, 5, 6], [7]], "expected": '[1][4,5,6][7]'}]
    for t in tests:
        assert_equal(_list_to_string(t["input"]), t["expected"])


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
             {"input": "1 YB", "expected": 1024*1024*1024*1024*1024*1024*1024*1024},
             {"input": "3814697 MB", "expected": 3814697*1024*1024}]
    for test in tests:
        assert_equal(_human_to_bytes(test["input"]), test["expected"])


def test_bytes_to_human():
    tests = [{"input": 100*1024*1024, "expected": "100 MB"},
             {"input": 100*1024*1024*1024, "expected": "100 GB"},
             {"input": 100*1024*1024*1024, "format": "MB", "expected": "102400 MB"},
             {"input": 3814697*1024*1024, "format": "MB", "expected": "3814697 MB"}]
    for test in tests:
        if "format" in test:
            assert_equal(_bytes_to_human(test["input"], test["format"]), test["expected"])
        else:
            assert_equal(_bytes_to_human(test["input"]), test["expected"])


def test_pd_min_size_get():
    tests = [{"input": [1024*1024, 1024*1024*1024], "expected": 1024*1024},
             {"input": [1024*1024*1024, 1024], "expected": 1024},
             {"input": [1024*1024*1024, 1024, 1024*10], "expected": 1024}]
    for test in tests:
        assert_equal(_pd_min_size_get(test["input"]), test["expected"])


def test_pd_total_size_get():
    tests = [{"input": [1024*1024, 1024*1024*1024],
              "expected": 1024*1024 + 1024*1024*1024},
             {"input": [1024*1024*1024, 1024],
              "expected": 1024*1024*1024 + 1024},
             {"input": [1024*1024*1024, 1024, 1024*10],
              "expected": 1024*1024*1024+1024+1024*10}]
    for test in tests:
        assert_equal(_pd_total_size_get(test["input"]), test["expected"])


def test_vd_spand_depth_get():
    tests = [{"input": [[1]], "expected": 1},
             {"input": [[1, 2], [3, 4]], "expected": 2},
             {"input": [[1, 2, 3], [4], [5, 6]], "expected": 3},
             {"input": [[1], [2], [3], [4], [5, 6]], "expected": 5}]
    for test in tests:
        assert_equal(_vd_span_depth_get(test["input"]), test["expected"])


def test_raid_max_size_get():
    tests = [{"r": 0,
              "s": 1000*1024*1024*1024,
              "ms": 1000*1024*1024*1024,
              "sd": 1,
              "expected": 1000*1024*1024*1024},
             {"r": 1,
              "s": 1000*1024*1024*1024,
              "ms": 1000*1024*1024*1024,
              "sd": 1,
              "expected": (1000*1024*1024*1024)/2},
             {"r": 5,
              "s": 6*1000*1024*1024*1024,
              "ms": 1000*1024*1024*1024,
              "sd": 2,
              "expected": (6*1000*1024*1024*1024) - (2*1*1000*1024*1024*1024)},
             {"r": 50,
              "s": 6*1000*1024*1024*1024,
              "ms": 1000*1024*1024*1024,
              "sd": 2,
              "expected": (6*1000*1024*1024*1024) - (2*1*1000*1024*1024*1024)},
             {"r": 6,
              "s": 6*1000*1024*1024*1024,
              "ms": 1000*1024*1024*1024,
              "sd": 2,
              "expected": (6*1000*1024*1024*1024) - (2*2*1000*1024*1024*1024)},
             {"r": 60,
              "s": 6*1000*1024*1024*1024,
              "ms": 1000*1024*1024*1024,
              "sd": 2,
              "expected": (6*1000*1024*1024*1024) - (2*2*1000*1024*1024*1024)}]
    for t in tests:
        assert_equal(_raid_max_size_get(t["r"], t["s"], t["ms"], t["sd"]),
                     t["expected"])


handle = None


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    custom_teardown(handle)


def test_vd_create_delete():
    # Guarding check to execute only on servers that have a "MEZZ" controller
    # and have drive 1-6 present
    server_dn = get_server_dn(handle, server_id=1)
    slot_dn = server_dn + "/board/storage-SAS-SLOT-MEZZ"
    mo = handle.query_dn(slot_dn)
    if mo is None:
        return
    for i in range(1, 7):
        mo = handle.query_dn(slot_dn + "/pd-" + str(i))
        if mo is None:
            return

    tests = [{"dg": [[1]], "cs": "MEZZ", "r": 0},
             {"dg": [[1, 2, 3, 4]], "cs": "MEZZ", "r": 1},
             {"dg": [[1, 2, 3]], "cs": "MEZZ", "r": 5},
             {"dg": [[1, 2, 3]], "cs": "MEZZ", "r": 6},
             {"dg": [[1, 2], [3, 4], [5, 6]], "cs": "MEZZ", "r": 10},
             {"dg": [[1, 2, 3], [4, 5, 6]], "cs": "MEZZ", "r": 50},
             {"dg": [[1, 2, 3], [4, 5, 6]], "cs": "MEZZ", "r": 60}]

    for t in tests:
        vd = virtual_drive_create(handle=handle,
                                  drive_group=t["dg"],
                                  controller_slot=t["cs"],
                                  raid_level=t["r"])
        virtual_drive_delete(handle=handle,
                             controller_slot=t["cs"],
                             name=vd.virtual_drive_name)
