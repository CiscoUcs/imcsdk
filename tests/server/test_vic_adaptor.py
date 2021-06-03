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

import logging

from nose.tools import raises
from ..connection.info import custom_setup, custom_teardown

from imcsdk.imcexception import ImcOperationError, ImcException
from imcsdk.apis.server.vic import adaptor_set_all, vnic_get, vhba_get,\
        _vic_get_all, adaptor_unit_get, _ext_ethif_get_all
from imcsdk.apis.server.serveractions import server_power_down, server_power_up
from imcsdk.apis.server.adaptor import adaptor_properties_get
from imcsdk.apis.utils import _get_mo

log = logging.getLogger('imc')

handle = None
ADAPTOR_ID = "1"
# ADAPTOR_ID = "MLOM"
# ADAPTOR_ID = "SIOC1"


def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    server_power_up(handle)
    custom_teardown(handle)


def test_adaptor_set_all_default():
    adaptor_set_all(handle)


def test_adaptor_set_all_empty_list():
    adaptors = []
    adaptor_set_all(handle, adaptors)


def test_adaptor_set_all_disabled():
    state = "disabled"
    adaptors = [
        {
            "id": ADAPTOR_ID,
            "lldp": state,
            "fip_mode": state,
            "vntag_mode": state
        }
    ]
    adaptor_set_all(handle, adaptors)



def test_adaptor_set_all_enabled():
    state = "enabled"
    adaptors = [
        {
            "id": ADAPTOR_ID,
            "lldp": state,
            "fip_mode": state,
            "vntag_mode": state,
            "port_channel_enable": "enabled"
        }
    ]
    adaptor_set_all(handle, adaptors)

def test_adaptor_port_channel_disabled():

    state = "enabled"
    adaptors = [
        {
            "id": ADAPTOR_ID,
            "lldp": state,
            "fip_mode": state,
            "vntag_mode": state,
            "port_channel_enable": "disabled"
        }
    ]
    adaptor_set_all(handle, adaptors)
    mos = _vic_get_all(handle, ADAPTOR_ID, "vnic")
    assert len(mos) == 4
    mos = _vic_get_all(handle, ADAPTOR_ID, "vhba")
    assert len(mos) == 4

def test_adaptor_port_channel_enabled():
    state = "enabled"
    adaptors = [
        {
            "id": ADAPTOR_ID,
            "lldp": state,
            "fip_mode": state,
            "vntag_mode": state,
            "port_channel_enable": state
        }
    ]
    adaptor_properties = adaptor_properties_get(handle, ADAPTOR_ID, server_id=1)

    if adaptor_properties.port_channel_enable == "Disabled":
        adaptor_set_all(handle, adaptors)
        vnics = _vic_get_all(handle, ADAPTOR_ID, "vnic")
        vhbas = _vic_get_all(handle, ADAPTOR_ID, "vhba")
        assert len(vnics) == 2
        assert len(vhbas) == 2
    else:
        old_vnics = _vic_get_all(handle, ADAPTOR_ID, "vnic")
        old_vhbas = _vic_get_all(handle, ADAPTOR_ID, "vhba")
        adaptor_set_all(handle, adaptors)
        new_vnics = _vic_get_all(handle, ADAPTOR_ID, "vnic")
        new_vhbas = _vic_get_all(handle, ADAPTOR_ID, "vhba")
        assert len(old_vnics) == len(new_vnics)
        assert len(old_vhbas) == len(new_vhbas)

@raises(ImcOperationError)
def test_adaptor_set_all_unknow_adaptor():
    state = "enabled"
    adaptors = [
        {
            "id": "3",
            "lldp": state,
            "fip_mode": state,
            "vntag_mode": state
        }
    ]
    adaptor_set_all(handle, adaptors)

def test_adaptor_set_ext_ethifs():
    state = "enabled"
    ext_ethifs = [{"port_id": "0", "fec_mode" :"cl91"},
                  {"port_id": "1", "fec_mode": "cl74" },
                  {"port_id": "2", "fec_mode": "Off"},
                  {"port_id": "3", "fec_mode": "Auto"}]
    adaptors = [
        {
            "id": ADAPTOR_ID,
            "lldp": state,
            "fip_mode": state,
            "vntag_mode": state,
            "ext_ethifs": ext_ethifs,
            "port_channel_enable": "enabled"
        }
    ]
    adaptor_set_all(handle, adaptors)
    adaptor_mo = adaptor_unit_get(handle, ADAPTOR_ID, 1)
    ext_ethifs = _ext_ethif_get_all(handle, adaptor_mo)
    assert ext_ethifs['0'].admin_fec_mode == "cl91"
    assert ext_ethifs['1'].admin_fec_mode == "cl74"
    assert ext_ethifs['2'].admin_fec_mode == "Off"
    assert ext_ethifs['3'].admin_fec_mode == "Auto"

# Server must be powered off for the following test to pass
@raises(ImcOperationError)
def test_adaptor_set_all_server_powered_off():
    state = "enabled"
    adaptors = [
        {
            "id": "1",
            "lldp": state,
            "fip_mode": state,
            "vntag_mode": state
        }
    ]
    server_power_down(handle)
    adaptor_set_all(handle, adaptors)
