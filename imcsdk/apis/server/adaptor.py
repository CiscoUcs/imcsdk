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
from imcsdk.imcexception import ImcOperationError


def _get_adaptor(handle, adaptor_slot, server_id=1, **kwargs):

    server_dn = get_server_dn(handle, server_id)
    dn = server_dn + "/adaptor-" + str(adaptor_slot)
    mo = handle.query_dn(dn)

    if mo is None:
        raise ImcOperationError("Get Adaptor",
                                "Adaptor is not available")

    return mo


def get_vic_adaptor_properties(handle, adaptor_slot, server_id=1, **kwargs):
    """
    This method is used to get the vic adaptor properties
    Args:
        handle (ImcHandle)
        adaptor_slot (string): PCI slot of the vic adaptor
        server_id (int): Server Id to be specified for C3260 platforms
        kwargs: key=value paired arguments

    Examples:
        For non-3x60 platforms:-
        get_vic_adaptor_properties(handle, adaptor_slot="1")

        For 3x60 platforms:-
        get_vic_adaptor_properties(handle, adaptor_slot="1", server_id=1)

    Returns:
        AdaptorGenProfile object
    """

    server_dn = get_server_dn(handle, server_id)
    dn = server_dn + "/adaptor-" + str(adaptor_slot) + "/general"
    mo = handle.query_dn(dn)

    if mo is None:
        raise ImcOperationError("Get Adaptor",
                                "Adaptor is not available")

    return mo


def setup_vic_adaptor_properties(handle, adaptor_slot, fip_mode=None,
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
        kwargs: key=value paired arguments

    Examples:
        For non-C3260 platforms:-
        setup_vic_adaptor_properties(handle, adaptor_slot="1",
                                     fip_mode=True)

        For C3260 platforms:-
        setup_vic_adaptor_properties(handle, adaptor_slot="1",
                                     vntag_mode=True, num_of_vm_fex_ifs=5,
                                     server_id=2)
        setup_vic_adaptor_properties(handle, adaptor_slot="1",
                                     fip_mode=False, server_id=1)

    Returns:
        AdaptorGenProfile object
    """

    mo = get_vic_adaptor_properties(handle, adaptor_slot, server_id, **kwargs)
    if num_vmfex_ifs:
        mo.num_of_vm_fex_ifs = str(num_vmfex_ifs)

    if fip_mode is True:
        mo.fip_mode = "enabled"
    elif fip_mode is False:
        mo.fip_mode = "disabled"

    if vntag_mode is True:
        mo.vntag_mode = "enabled"
    elif vntag_mode is False:
        mo.vntag_mode = "disabled"
        mo.num_of_vm_fex_ifs = ""

    handle.set_mo(mo)
    return mo


def get_vnic(handle, adaptor_slot, name, server_id=1, **kwargs):
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

    mo = _get_adaptor(handle, adaptor_slot, server_id, **kwargs)
    vnic_mo = AdaptorHostEthIf(parent_mo_or_dn=mo.dn, name=name)
    vnic_mo = handle.query_dn(vnic_mo.dn)

    return vnic_mo


def create_vnic(handle, adaptor_slot, name, channel_number, mac, mtu=1500,
                cos="", port_profile="", pxe_boot=False, uplink_port=0,
                server_id=1, **kwargs):
    """
    This method is used to create a new vnic
    Args:
        handle (ImcHandle)
        adaptor_slot (string): PCI slot number of the adaptor
        name (string): Name for the vnic
        channel_number (int): channel number for the vnic
        cos (string): class of service
        mac (string): mac address for the vnic
        mtu (int): mtu size for the vnic
        port_profile (string): port-profile name
        pxe_boot (bool): enable pxe_boot
        uplink_port (int): uplink port for binding the vnic. "0", "1"
        server_id (int): Server Id for C3260 platforms
        kwargs: key=value paired arguments

    Examples:
        For non-C3260 platforms:-
        create_vnic(handle, adaptor_slot="1", name="test-vnic",
                    channel_number=10, mac="00:11:22:33:44:55",
                    mtu=1500, pxe_boot=True, uplink_port=0)

        For C3260 platforms:
        create_vnic(handle, adaptor_slot="1", name="test-vnic",
                    channel_number=10, mac="00:11:22:33:44:55",
                    mtu=1500, pxe_boot=True, uplink_port=0, server_id=1)

    Returns:
        AdaptorHostEthIf object
    """

    from imcsdk.mometa.adaptor.AdaptorHostEthIf import AdaptorHostEthIf

    mo = _get_adaptor(handle, adaptor_slot, server_id, **kwargs)
    vnic_mo = AdaptorHostEthIf(parent_mo_or_dn=mo.dn, name=name)
    vnic_mo.channel_number = str(channel_number)
    if cos:
        vnic_mo.class_of_service = cos
    vnic_mo.mac = mac
    vnic_mo.mtu = str(mtu)
    if port_profile:
        vnic_mo.port_profile = port_profile
    if pxe_boot:
        vnic_mo.pxe_boot = "enabled"
    else:
        vnic_mo.pxe_boot = "disabled"

    if uplink_port not in [0, 1]:
        raise ImcOperationError("Create Vnic",
                                "Invalid uplink port")

    vnic_mo.uplink_port = str(uplink_port)
    handle.add_mo(vnic_mo, modify_present=True)

    return handle.query_dn(vnic_mo.dn)


def delete_vnic(handle, adaptor_slot, name, server_id=1, **kwargs):
    """
    This method is used to delete a vnic
    Args:
        handle (ImcHandle)
        adaptor_slot (string): PCI slot number of the adaptor
        name (string): Name for the vnic to be deleted
        server_id (int): Server Id for C3260 platforms
        kwargs: key=value paired arguments

    Returns:
        None
    """

    vnic_mo = get_vnic(handle, adaptor_slot, name, server_id, **kwargs)
    if vnic_mo:
        handle.remove_mo(vnic_mo)


def get_vhba(handle, adaptor_slot, name, server_id=1, **kwargs):
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

    mo = _get_adaptor(handle, adaptor_slot, server_id, **kwargs)
    vhba_mo = AdaptorHostFcIf(parent_mo_or_dn=mo.dn, name=name)
    vhba_mo = handle.query_dn(vhba_mo.dn)

    return vhba_mo


def create_vhba(handle, adaptor_slot, name, channel_number, wwnn, wwpn,
                port_profile="", san_boot=False, uplink_port=0,
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
        create_vhba(handle, adaptor_slot="1", name="test-vhba",
                    channel_number=101, wwnn="10:00:11:3A:7D:D0:9A:43",
                    wwpn="20:00:11:3A:7D:D0:9A:43",
                    san_boot=True, uplink_port=0)
        For 3x60 platforms:
        create_vhba(handle, adaptor_slot="2", name="test-vhba",
                    channel_number=100, wwnn="10:00:11:3A:7D:D0:9A:43",
                    wwpn="20:00:11:3A:7D:D0:9A:43",
                    san_boot=True, uplink_port=0, server_id=2)
    """

    from imcsdk.mometa.adaptor.AdaptorHostFcIf import AdaptorHostFcIf

    mo = _get_adaptor(handle, adaptor_slot, server_id, **kwargs)
    vhba_mo = AdaptorHostFcIf(parent_mo_or_dn=mo.dn, name=name)
    vhba_mo.channel_number = str(channel_number)
    vhba_mo.wwnn = wwnn
    vhba_mo.wwpn = wwpn
    if port_profile:
        vhba_mo.port_profile = port_profile
    if san_boot:
        vhba_mo.san_boot = "enabled"
    else:
        vhba_mo.san_boot = "disabled"

    if uplink_port not in [0, 1]:
        raise ImcOperationError("Create Vhba",
                                "Invalid uplink port")

    vhba_mo.uplink_port = str(uplink_port)
    handle.add_mo(vhba_mo, modify_present=True)

    return handle.query_dn(vhba_mo.dn)


def delete_vhba(handle, adaptor_slot, name, server_id=1, **kwargs):
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

    vhba_mo = get_vhba(handle, adaptor_slot, name, server_id, **kwargs)
    if vhba_mo:
        handle.remove_mo(vhba_mo)
