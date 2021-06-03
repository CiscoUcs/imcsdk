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

from nose.tools import assert_equal
from ..connection.info import custom_setup, custom_teardown
from imcsdk.apis.admin.user import local_users_update
from imcsdk.apis.admin.user import password_properties_set 
from imcsdk.apis.admin.user import password_properties_exists 


handle = None


def setup_module():
    global handle
    handle = custom_setup()
    # handle.set_dump_xml()


def teardown_module():
    global handle
    custom_teardown(handle)


def test_local_users_create_failure_users_missing():
    try:
        local_users_update(handle)
    except:
        print("Invalid Users")


def test_local_users_create_failure_name_missing():
    try:
        local_users_update(handle, users=[{"pwd": "Nbv-12345", "priv": "read-only", "account_status": "active"}, {
            "name": "nosetest2", "pwd": "Nbv-12345", "priv": "user", "account_status": "active"}])
    except:
        print("Invalid User Name")


def test_local_users_create_failure_pwd_missing():
    try:
        local_users_update(handle, users=[{"name": "nosetest1", "priv": "read-only", "account_status": "active"}, {
            "name": "nosetest2", "pwd": "Nbv-12345", "priv": "user", "account_status": "active"}])
    except:
        print("Invalid Password")


def test_local_users_create_failure_priv_missing():
    try:
        local_users_update(handle, users=[{"name": "nosetest1", "priv": "Nbv-12345", "account_status": "active"}, {
            "name": "nosetest2", "pwd": "Nbv-12345", "priv": "user", "account_status": "active"}])
    except:
        print("Invalid Privilege")


def test_local_users_create_users():
    create = local_users_update(handle, users=[{"name": "nosetest1", "pwd": "Nbv-12345", "priv": "read-only", "account_status": "active"}, {
                                "name": "nosetest2", "pwd": "Nbv-12345", "priv": "user", "account_status": "active"}])
    assert_equal(create["changed"], True)


def test_local_users_create_users_no_change():
    create = local_users_update(handle, users=[{"name": "nosetest1", "pwd": "Nbv-12345", "priv": "read-only", "account_status": "active"}, {
                                "name": "nosetest2", "pwd": "Nbv-12345", "priv": "user", "account_status": "active"}])
    assert_equal(create["changed"], False)


def test_local_users_update_priv():
    update = local_users_update(handle, users=[{"name": "nosetest1", "pwd": "Nbv-12345", "priv": "user", "account_status": "active"}, {
                                "name": "nosetest2", "pwd": "Nbv-12345", "priv": "user", "account_status": "active"}])
    assert_equal(update["changed"], True)


def test_local_users_update_priv_no_change():
    update = local_users_update(handle, users=[{"name": "nosetest1", "pwd": "Nbv-12345", "priv": "user", "account_status": "active"}, {
                                "name": "nosetest2", "pwd": "Nbv-12345", "priv": "user", "account_status": "active"}])
    assert_equal(update["changed"], False)


def test_local_users_update_pwd():
    update = local_users_update(handle, users=[{"name": "nosetest1", "pwd": "Nbv123456", "priv": "read-only", "account_status": "active", "change_password": True}, {
                                "name": "nosetest2", "pwd": "Nbv12345", "priv": "user", "account_status": "active", "change_password": True}])
    assert_equal(update["changed"], True)


def test_local_users_update_pwd_no_change():
    update = local_users_update(handle, users=[{"name": "nosetest1", "pwd": "Nbv12345", "priv": "read-only", "account_status": "active", "change_password": False}, {
                                "name": "nosetest2", "pwd": "Nbv12345", "priv": "user", "account_status": "active", "change_password": False}])
    assert_equal(update["changed"], False)


def test_local_users_update_account_status():
    update = local_users_update(handle, users=[{"name": "nosetest1", "pwd": "Nbv12345", "priv": "read-only", "account_status": "inactive"}, {
                                "name": "nosetest2", "pwd": "Nbv12345", "priv": "user", "account_status": "inactive", }])
    assert_equal(update["changed"], True)


def test_local_users_update_account_status_no_change():
    update = local_users_update(handle, users=[{"name": "nosetest1", "pwd": "Nbv12345", "priv": "read-only", "account_status": "inactive"}, {
                                "name": "nosetest2", "pwd": "Nbv12345", "priv": "user", "account_status": "inactive", }])
    assert_equal(update["changed"], False)


def test_local_users_delete():
    delete = local_users_update(handle, users=[
                                {"name": "nosetest1", "pwd": "Nbv12345", "priv": "read-only", "account_status": "inactive"}])
    assert_equal(delete["changed"], True)


def test_local_users_delete_no_change():
    delete = local_users_update(handle, users=[
                                {"name": "nosetest1", "pwd": "Nbv12345", "priv": "read-only", "account_status": "inactive"}])
    assert_equal(delete["changed"], False)

# scale tests, MAX_USERS=15


def test_local_users_create_max_users_without_admin():
    try:
        local_users_update(handle,
                           users=[{
                               "name": "dummy1",
                               "pwd": "Nbv123456",
                               "priv": "admin",
                               "account_status": "active",
                               "change_password": True
                           },
                               {"name": "dummy2",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy3",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy4",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy5",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy6",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy7",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy8",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy9",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy10",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy11",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy12",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy13",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy14",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy15",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                }])
    except:
        print("Max users already configured")


def test_local_users_create_max_users_with_admin():
    create = local_users_update(handle,
                                users=[
                                    {"name": "dummy2",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy3",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy4",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy5",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy6",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy7",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy8",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy9",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy10",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy11",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy12",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy13",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy14",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy15",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     }])

    assert_equal(create["changed"], True)


def test_local_users_update_max_users_without_admin():
    try:
        local_users_update(handle,
                           users=[{
                               "name": "dummy1",
                               "pwd": "Nbv123456",
                               "priv": "admin",
                               "account_status": "active",
                               "change_password": True
                           },
                               {"name": "dummy2",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy3",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy4",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy5",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy6",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy7",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy8",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy9",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy10",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy11",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy12",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy13",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy14",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy15",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                }])
    except:
        print("Max users already configured")


def test_local_users_update_max_users_with_admin():
    update = local_users_update(handle,
                                users=[{
                                    "name": "admin",
                                    "pwd": "Nbv12345",
                                    "priv": "admin",
                                    "account_status": "active",
                                    "change_password": True
                                },
                                    {"name": "dummy2",
                                     "pwd": "Nbv1234567",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy3",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy4",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy5",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy6",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy7",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy8",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy9",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy10",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy11",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy12",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy13",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy14",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     },
                                    {"name": "dummy15",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     "change_password": True
                                     }])

    assert_equal(update["changed"], True)


def test_local_users_update_max_users_with_admin_no_change():
    update = local_users_update(handle,
                                users=[{
                                    "name": "admin",
                                    "pwd": "Nbv12345",
                                    "priv": "admin",
                                    "account_status": "active",
                                },
                                    {"name": "dummy2",
                                     "pwd": "Nbv1234567",
                                     "priv": "admin",
                                     "account_status": "active",
                                     },
                                    {"name": "dummy3",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     },
                                    {"name": "dummy4",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     },
                                    {"name": "dummy5",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     },
                                    {"name": "dummy6",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     },
                                    {"name": "dummy7",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     },
                                    {"name": "dummy8",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     },
                                    {"name": "dummy9",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     },
                                    {"name": "dummy10",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     },
                                    {"name": "dummy11",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     },
                                    {"name": "dummy12",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     },
                                    {"name": "dummy13",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     },
                                    {"name": "dummy14",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     },
                                    {"name": "dummy15",
                                     "pwd": "Nbv123456",
                                     "priv": "admin",
                                     "account_status": "active",
                                     }])

    assert_equal(update["changed"], False)


def test_local_users_update_with_16_users():
    try:
        local_users_update(handle,
                           users=[{
                               "name": "dummy1",
                               "pwd": "Nbv123456",
                               "priv": "admin",
                               "account_status": "active",
                               "change_password": True
                           },
                               {"name": "dummy2",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy3",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy4",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy5",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy6",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy7",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy8",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy9",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy10",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy11",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy12",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy13",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy14",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy15",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                },
                               {"name": "dummy16",
                                   "pwd": "Nbv123456",
                                "priv": "admin",
                                "account_status": "active",
                                "change_password": True
                                }])
    except:
        print("Number of users exceeded max allowed limit on IMC")


def test_local_users_delete_all():
    update = local_users_update(handle, users=[])
    assert_equal(update["changed"], True)

def test_password_properties_enable():
   password_properties_set(handle, password_expiry_duration = 100,
                                                     password_notification_period = 5,
                                                    password_grace_period = 5,
                                                    password_history = 3) 
   match, mo = password_properties_exists(handle) 
   assert_equal(match, True)


def test_password_properties_disable():
   password_properties_set(handle, password_expiry_duration = 0,
                                                     password_notification_period = 15,
                                                    password_grace_period = 5,
                                                    password_history = 4) 
   match, mo = password_properties_exists(handle) 
   assert_equal(match, True)

