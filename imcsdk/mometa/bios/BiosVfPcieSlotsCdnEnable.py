"""This module contains the general information for BiosVfPcieSlotsCdnEnable ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPcieSlotsCdnEnableConsts:
    VP_PCIE_SLOTS_CDN_ENABLE_DISABLED = "Disabled"
    VP_PCIE_SLOTS_CDN_ENABLE_ENABLED = "Enabled"
    _VP_PCIE_SLOTS_CDN_ENABLE_DISABLED = "disabled"
    _VP_PCIE_SLOTS_CDN_ENABLE_ENABLED = "enabled"
    VP_PCIE_SLOTS_CDN_ENABLE_PLATFORM_DEFAULT = "platform-default"


class BiosVfPcieSlotsCdnEnable(ManagedObject):
    """This is BiosVfPcieSlotsCdnEnable class."""

    consts = BiosVfPcieSlotsCdnEnableConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPcieSlotsCdnEnable", "biosVfPcieSlotsCdnEnable", "PCIe-Slots-CDN-Control", VersionMeta.Version413h, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413h, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413h, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413h, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pcie_slots_cdn_enable": MoPropertyMeta("vp_pcie_slots_cdn_enable", "vpPcieSlotsCdnEnable", "string", VersionMeta.Version413h, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPcieSlotsCdnEnable": "vp_pcie_slots_cdn_enable", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_pcie_slots_cdn_enable = None

        ManagedObject.__init__(self, "BiosVfPcieSlotsCdnEnable", parent_mo_or_dn, **kwargs)

