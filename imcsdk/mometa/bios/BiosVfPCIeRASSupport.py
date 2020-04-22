"""This module contains the general information for BiosVfPCIeRASSupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPCIeRASSupportConsts:
    VP_PCIE_RASSUPPORT_DISABLED = "Disabled"
    VP_PCIE_RASSUPPORT_ENABLED = "Enabled"
    _VP_PCIE_RASSUPPORT_DISABLED = "disabled"
    _VP_PCIE_RASSUPPORT_ENABLED = "enabled"
    VP_PCIE_RASSUPPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfPCIeRASSupport(ManagedObject):
    """This is BiosVfPCIeRASSupport class."""

    consts = BiosVfPCIeRASSupportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPCIeRASSupport", "biosVfPCIeRASSupport", "PCIe-RAS-Support", VersionMeta.Version411c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfPCIeRASSupport", "biosVfPCIeRASSupport", "PCIe-RAS-Support", VersionMeta.Version411c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pc_ie_ras_support": MoPropertyMeta("vp_pc_ie_ras_support", "vpPCIeRASSupport", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pc_ie_ras_support": MoPropertyMeta("vp_pc_ie_ras_support", "vpPCIeRASSupport", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPCIeRASSupport": "vp_pc_ie_ras_support", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPCIeRASSupport": "vp_pc_ie_ras_support", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_pc_ie_ras_support = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfPCIeRASSupport", parent_mo_or_dn, **kwargs)

