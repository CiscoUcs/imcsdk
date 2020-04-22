"""This module contains the general information for BiosVfPCIeSSDHotPlugSupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPCIeSSDHotPlugSupportConsts:
    VP_PCIE_SSDHOT_PLUG_SUPPORT_DISABLED = "Disabled"
    VP_PCIE_SSDHOT_PLUG_SUPPORT_ENABLED = "Enabled"
    _VP_PCIE_SSDHOT_PLUG_SUPPORT_DISABLED = "disabled"
    _VP_PCIE_SSDHOT_PLUG_SUPPORT_ENABLED = "enabled"
    VP_PCIE_SSDHOT_PLUG_SUPPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfPCIeSSDHotPlugSupport(ManagedObject):
    """This is BiosVfPCIeSSDHotPlugSupport class."""

    consts = BiosVfPCIeSSDHotPlugSupportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPCIeSSDHotPlugSupport", "biosVfPCIeSSDHotPlugSupport", "PCIeSSDHotPlugSupport", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pc_ie_ssd_hot_plug_support": MoPropertyMeta("vp_pc_ie_ssd_hot_plug_support", "vpPCIeSSDHotPlugSupport", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPCIeSSDHotPlugSupport": "vp_pc_ie_ssd_hot_plug_support", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_pc_ie_ssd_hot_plug_support = None

        ManagedObject.__init__(self, "BiosVfPCIeSSDHotPlugSupport", parent_mo_or_dn, **kwargs)

