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


"""
This module provides apis to setup cisco vic adaptor properties \
and create vnics and vhbas
"""

from imcsdk.imccoreutils import get_server_dn
from imcsdk.apis.utils import _get_mo


def _get_adaptor_dn(handle, adaptor_slot, server_id=1):
    server_dn = get_server_dn(handle, server_id)
    return(server_dn + "/adaptor-" + str(adaptor_slot))


def adaptor_unit_get(handle, adaptor_slot, server_id=1, **kwargs):
    """
    This method fetches the adaptorUnit Managed Object for the specified
    adaptor Slot on a server.

    Args:
        handle (ImcHandle)
        adaptor_slot (string): PCI slot number of the adaptor
        server_id (int): Server Id for C3260 platforms
        kwargs: key=value paired arguments

    Returns:
        AdaptorUnit object

    Examples:
        adaptor_unit_get(handle, adaptor_slot=1, server_id=1)
    """
    return _get_mo(handle, dn=_get_adaptor_dn(handle, adaptor_slot, server_id))


def adaptor_properties_get(handle, adaptor_slot, server_id=1, **kwargs):
    """
    This method is used to get the vic adaptor properties
    Args:
        handle (ImcHandle)
        adaptor_slot (string): PCI slot of the vic adaptor
        server_id (int): Server Id to be specified for C3260 platforms
        kwargs: key=value paired arguments

    Examples:
        For non-3x60 platforms:-
        adaptor_properties_get(handle, adaptor_slot="1")

        For 3x60 platforms:-
        adaptor_properties_get(handle, adaptor_slot="1", server_id=1)

    Returns:
        AdaptorGenProfile object
    """

    dn = _get_adaptor_dn(handle, adaptor_slot, server_id) + "/general"
    return _get_mo(handle, dn=dn)


def adaptor_properties_set(handle, adaptor_slot, lldp=None, fip_mode=None,
                                 vntag_mode=None, num_vmfex_ifs=None,
                                 server_id=1, **kwargs):
    """
    This method setups the vic adaptor properties.
    A reboot will be required when these properties are changed
    Args:
        handle (ImcHandle)
        adaptor_slot (string): PCI slot number of the adaptor
        fip_mode (bool): Enable fip mode
        vntag_mode (bool): Enable vntag mode
        num_vmfex_ifs (int): Number of vmfex interfaces to be configured when \
                             adaptor is in vntag mode
                             When the vntag mode is being disabled,
                             this property will be set to 0
        server_id (int): Server Id to be specified for C3260 platforms
        kwargs: key=value paired arguments

    Examples:
        For non-C3260 platforms:-
        adaptor_properties_set(handle, adaptor_slot="1",
                                     fip_mode=True)

        For C3260 platforms:-
        adaptor_properties_set(handle, adaptor_slot="1",
                                     vntag_mode=True, num_of_vm_fex_ifs=5,
                                     server_id=2)
        adaptor_properties_set(handle, adaptor_slot="1",
                                     fip_mode=False, server_id=1)

    Returns:
        AdaptorGenProfile object
    """

    from imcsdk.mometa.adaptor.AdaptorGenProfile import AdaptorGenProfile
    adaptor = adaptor_unit_get(handle, adaptor_slot, server_id, **kwargs)
    mo = AdaptorGenProfile(parent_mo_or_dn=adaptor.dn)
    # VMFEX feature support is discontinued since 3.0(1c) release

    values = {
        True: "enabled",
        False: "disabled"
    }

    mo.fip_mode = values.get(fip_mode)
    mo.vntag_mode = values.get(vntag_mode)
    mo.lldp = values.get(lldp)

    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def adaptor_reset(handle, adaptor_slot, server_id=1, **kwargs):
    """

    Args:
        handle (ImcHandle)
        adaptor_slot (string): PCI slot number of the adaptor
        server_id (int): Server Id to be specified for C3260 platforms
        kwargs: key=value paired arguments

    Returns:
        AdaptorUnit object

    """
    from imcsdk.mometa.adaptor.AdaptorUnit import AdaptorUnitConsts
    mo = adaptor_unit_get(handle, adaptor_slot, server_id, **kwargs)
    mo.admin_state = AdaptorUnitConsts.ADMIN_STATE_ADAPTOR_RESET
    handle.set_mo(mo)
    return mo


def vnic_get(handle, adaptor_slot, name, server_id=1, **kwargs):
    """
    This method is used to get a vnic
    Args:
        handle (ImcHandle)
        adaptor_slot (string): PCI slot number of the adaptor
        name (string): Name for the vnic to be deleted
        server_id (int): Server Id for C3260 platforms
        kwargs: key=value paired arguments

    Returns:
        AdaptorHostEthIf object
    """

    from imcsdk.mometa.adaptor.AdaptorHostEthIf import AdaptorHostEthIf

    mo = adaptor_unit_get(handle, adaptor_slot, server_id, **kwargs)
    vnic_mo = AdaptorHostEthIf(parent_mo_or_dn=mo.dn, name=name)
    return handle.query_dn(vnic_mo.dn)


def vnic_create(handle,
                name,
                adaptor_slot=1,
                channel_number=None,
                mac="AUTO",
                mtu=1500,
                class_of_service=None,
                port_profile=None,
                pxe_boot=False,
                uplink_port=0,
                server_id=1,
                **kwargs):
    """
    This method is used to create a new vnic
    Args:
        handle (ImcHandle)
        name (string): Name for the vnic
        adaptor_slot (string): PCI slot number of the adaptor
        channel_number (int): channel number for the vnic
        class_of_service (int): class of service. 0-6
        mac (string): mac address for the vnic
        mtu (int): mtu size for the vnic
        port_profile (string): port-profile name
        pxe_boot (bool): enable pxe_boot. True/False
        uplink_port (int): uplink port for binding the vnic. 0/1
        server_id (int): Server Id for C3260 platforms
        kwargs: key=value paired arguments

    Examples:
        For non-C3260 platforms:-
        vnic_create(handle, adaptor_slot="1", name="test-vnic",
                    channel_number=10, mac="00:11:22:33:44:55",
                    mtu=1500, pxe_boot=True, uplink_port=0)

        For C3260 platforms:
        vnic_create(handle, adaptor_slot="1", name="test-vnic",
                    channel_number=10, mac="00:11:22:33:44:55",
                    mtu=1500, pxe_boot=True, uplink_port=0, server_id=1)

    Returns:
        AdaptorHostEthIf object
    """

    from imcsdk.mometa.adaptor.AdaptorHostEthIf import AdaptorHostEthIf

    mo = adaptor_unit_get(handle, adaptor_slot, server_id, **kwargs)
    vnic = AdaptorHostEthIf(parent_mo_or_dn=mo.dn, name=name)

    params = {
        "mac": mac,
        "mtu": str(mtu),
        "pxe_boot": ("disabled", "enabled")[pxe_boot],
        "uplink_port": str(uplink_port),
        "class_of_service": (None, str(class_of_service))[class_of_service is not None],
        "channel_number": (None, str(channel_number))[channel_number is not None],
        "port_profile": port_profile,
    }

    vnic.set_prop_multiple(**params)
    vnic.set_prop_multiple(**kwargs)
    handle.add_mo(vnic, modify_present=True)
    return handle.query_dn(vnic.dn)


def vnic_delete(handle, name, adaptor_slot=1, server_id=1, **kwargs):
    """
    This method is used to delete a vnic
    Args:
        handle (ImcHandle)
        name (string): Name for the vnic to be deleted
        adaptor_slot (string): PCI slot number of the adaptor
        server_id (int): Server Id for C3260 platforms
        kwargs: key=value paired arguments

    Returns:
        None
    """

    vnic_mo = vnic_get(handle, adaptor_slot, name, server_id, **kwargs)
    if vnic_mo:
        handle.remove_mo(vnic_mo)


def vhba_get(handle, adaptor_slot, name, server_id=1, **kwargs):
    """
    This method is used to get a vhba
    Args:
        handle (ImcHandle)
        adaptor_slot (string): PCI slot number of the adaptor
        name (string): Name for the vhba to be deleted
        server_id (int): Server Id for C3260 platforms
        kwargs: key=value paired arguments

    Returns:
        AdaptorHostEthIf object
    """

    from imcsdk.mometa.adaptor.AdaptorHostFcIf import AdaptorHostFcIf

    mo = adaptor_unit_get(handle, adaptor_slot, server_id, **kwargs)
    vhba_mo = AdaptorHostFcIf(parent_mo_or_dn=mo.dn, name=name)
    return handle.query_dn(vhba_mo.dn)


def vhba_create(handle, adaptor_slot, name, channel_number, wwnn, wwpn,
                port_profile=None, san_boot=False, uplink_port=0,
                server_id=1, **kwargs):
    """
    This method is used to create a new vhba
    Args:
        handle (ImcHandle)
        adaptor_slot (string): PCI slot number of the adaptor
        name (string): Name for the vhba to be deleted
        channel_number (int): channel number for the vnic
        wwnn (string): wwnn
        wwpn (string): wwpn
        port_profile (string): port-profile name
        san_boot (bool): san-boot
        uplink_port (int): uplink port for binding the vhba. "0", "1"
        server_id (int): Server Id for C3260 platforms
        kwargs: key=value paired arguments
    Returns:
        AdaptorHostFcIf object
    Examples:
        For non-3x60 platforms:
        vhba_create(handle, adaptor_slot="1", name="test-vhba",
                    channel_number=101, wwnn="10:00:11:3A:7D:D0:9A:43",
                    wwpn="20:00:11:3A:7D:D0:9A:43",
                    san_boot=True, uplink_port=0)
        For 3x60 platforms:
        vhba_create(handle, adaptor_slot="2", name="test-vhba",
                    channel_number=100, wwnn="10:00:11:3A:7D:D0:9A:43",
                    wwpn="20:00:11:3A:7D:D0:9A:43",
                    san_boot=True, uplink_port=0, server_id=2)
    """

    from imcsdk.mometa.adaptor.AdaptorHostFcIf import AdaptorHostFcIf

    mo = adaptor_unit_get(handle, adaptor_slot, server_id, **kwargs)
    vhba_mo = AdaptorHostFcIf(parent_mo_or_dn=mo.dn, name=name)

    params = {
        "channel_number": (None, str(channel_number))[channel_number is not None],
        "wwnn": wwnn,
        "wwpn": wwpn,
        "port_profile": port_profile,
        "san_boot": ("disabled", "enabled")[san_boot],
        "uplink_port": str(uplink_port)
    }

    vhba_mo.set_prop_multiple(**params)
    vhba_mo.set_prop_multiple(**kwargs)
    handle.add_mo(vhba_mo, modify_present=True)
    return handle.query_dn(vhba_mo.dn)


def vhba_delete(handle, adaptor_slot, name, server_id=1, **kwargs):
    """
    This method is used to delete a vnic
    Args:
        handle (ImcHandle)
        adaptor_slot (string): PCI slot number of the adaptor
        name (string): Name for the vhba to be deleted
        server_id (int): Server Id for C3260 platforms
        kwargs: key=value paired arguments

    Returns:
        None
    """

    vhba_mo = vhba_get(handle, adaptor_slot, name, server_id, **kwargs)
    if vhba_mo:
        handle.remove_mo(vhba_mo)
