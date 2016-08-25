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
This module provides apis to setup cisco vic adaptor properties and create vnics
and vhbas
"""


def get_vic_adaptor_properties(handle, adaptor_slot):
    """
    This method is used to get the vic adaptor properties
    Args:
        handle (ImcHandle)
        adaptor_slot (int): PCI slot of the vic adaptor

    Returns:
        AdaptorGenProfile object
    """

    from imcsdk.imcexception import ImcOperationError

    dn = "sys/rack-unit-1/adaptor-" + str(adaptor_slot) + "/general"
    mo = handle.query_dn(dn)

    if mo is None:
        raise ImcOperationError("Set Adaptor properties",
                                "Adaptor is not available")

    return mo


def setup_vic_adaptor_properties(handle, adaptor_slot=1, fip_mode=None,
                                 vntag_mode=None, num_vmfex_ifs=0):
    """
    This method setups the vic adaptor properties.
    A reboot will be required when
    Args:
        handle (ImcHandle)
        adaptor_slot (int): PCI slot number of the adaptor
        fip_mode (bool): Enable fip mode
        vntag_mode (bool): Enable vntag mode
        num_vmfex_ifs (int): Number of vmfex interfaces to be configured when \
            adaptor is in vntag mode
            When the vntag mode is being disabled, this property will be set to 0

    Returns:
        AdaptorGenProfile object
    """

    from imcsdk.imcexception import ImcOperationError

    dn = "sys/rack-unit-1/adaptor-" + str(adaptor_slot) + "/general"
    mo = handle.query_dn(dn)

    if mo is None:
        raise ImcOperationError("Set Adaptor properties",
                                    "Adaptor is not available")

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


def get_vnic(handle, adaptor_slot, name):
    """
    This method is used to get a vnic
    Args:
        handle (ImcHandle)
        adaptor_slot (int): PCI slot number of the adaptor
        name (string): Name for the vnic to be deleted

    Returns:
        AdaptorHostEthIf object
    """

    from imcsdk.imcexception import ImcOperationError
    from imcsdk.mometa.adaptor.AdaptorHostEthIf import AdaptorHostEthIf

    dn = "sys/rack-unit-1/adaptor-" + str(adaptor_slot)
    mo = handle.query_dn(dn)

    if mo is None:
        raise ImcOperationError("Get Vnic",
                                "Adaptor is not available")

    vnic_mo = AdaptorHostEthIf(parent_mo_or_dn=dn, name=name)
    vnic_mo = handle.query_dn(vnic_mo.dn)

    return vnic_mo


def create_vnic(handle, adaptor_slot, name, channel_number, mac, mtu, cos="",
                port_profile="", pxe_boot=False, uplink_port=0):
    """
    This method is used to create vnic on
    Args:
        handle (ImcHandle)
        adaptor_slot (int): PCI slot number of the adaptor
        name (string): Name for the vnic
        channel_number (int): channel number for the vnic
        cos (string): class of service
        mac (string): mac address for the vnic
        mtu (int): mtu size for the vnic
        port_profile (string): port-profile name
        pxe_boot (bool): enable pxe_boot
        uplink_port (int): uplink port for binding the vnic. "0", "1"

    Returns:
        AdaptorHostEthIf object
    """

    from imcsdk.imcexception import ImcOperationError
    from imcsdk.mometa.adaptor.AdaptorHostEthIf import AdaptorHostEthIf, \
        AdaptorHostEthIfConsts

    dn = "sys/rack-unit-1/adaptor-" + str(adaptor_slot)
    mo = handle.query_dn(dn)

    if mo is None:
        raise ImcOperationError("Create Vnic",
                                "Adaptor is not available")

    vnic_mo = AdaptorHostEthIf(parent_mo_or_dn=dn, name=name)
    vnic_mo.channel_number = str(channel_number)
    if cos is not "":
        vnic_mo.class_of_service = cos
    vnic_mo.mac = mac
    vnic_mo.mtu = str(mtu)
    if port_profile is not "":
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


def delete_vnic(handle, adaptor_slot, name):
    """
    This method is used to delete a vnic
    Args:
        handle (ImcHandle)
        adaptor_slot (int): PCI slot number of the adaptor
        name (string): Name for the vnic to be deleted

    Returns:
        None
    """

    vnic_mo = get_vnic(handle, adaptor_slot, name)
    if vnic_mo is not None:
        handle.remove_mo(vnic_mo)


def get_vhba(handle, adaptor_slot, name):
    """
        This method is used to get a vnic
        Args:
            handle (ImcHandle)
            adaptor_slot (int): PCI slot number of the adaptor
            name (string): Name for the vnic to be deleted

        Returns:
            AdaptorHostEthIf object
        """

    from imcsdk.imcexception import ImcOperationError
    from imcsdk.mometa.adaptor.AdaptorHostFcIf import AdaptorHostFcIf

    dn = "sys/rack-unit-1/adaptor-" + str(adaptor_slot)
    mo = handle.query_dn(dn)

    if mo is None:
        raise ImcOperationError("Get Vhba",
                                "Adaptor is not available")

    vhba_mo = AdaptorHostFcIf(parent_mo_or_dn=dn, name=name)
    vhba_mo = handle.query_dn(vhba_mo.dn)

    return vhba_mo


def create_vhba(handle, adaptor_slot, name, channel_number, wwnn, wwpn,
                port_profile="", san_boot=False, uplink_port=0):
    """
    This method is used to create a new vhba
    Args:
        handle (ImcHandle)
        adaptor_slot (int): PCI slot number of the adaptor
        name (string): Name for the vnic
        channel_number (int): channel number for the vnic
        wwnn (string): wwnn
        wwpn (string): wwpn
        port_profile (string): port-profile name
        san_boot (bool): san-boot
        uplink_port (int): uplink port for binding the vnic. "0", "1"

    Returns:
        AdaptorHostFcIf object
    """

    from imcsdk.imcexception import ImcOperationError
    from imcsdk.mometa.adaptor.AdaptorHostFcIf import AdaptorHostFcIf

    dn = "sys/rack-unit-1/adaptor-" + str(adaptor_slot)
    mo = handle.query_dn(dn)

    if mo is None:
        raise ImcOperationError("Get Vhba",
                                "Adaptor is not available")

    vhba_mo = AdaptorHostFcIf(parent_mo_or_dn=dn, name=name)
    vhba_mo.channel_number = str(channel_number)
    vhba_mo.wwnn = wwnn
    vhba_mo.wwpn = wwpn
    if port_profile is not "":
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


def delete_vhba(handle, adaptor_slot, name):
    """
    This method is used to delete a vnic
    Args:
        handle (ImcHandle)
        adaptor_slot (int): PCI slot number of the adaptor
        name (string): Name for the vhba to be deleted

    Returns:
        None
    """

    vhba_mo = get_vhba(handle, adaptor_slot, name)
    if vhba_mo is not None:
        handle.remove_mo(vhba_mo)

