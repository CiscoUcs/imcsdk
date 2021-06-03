"""This module contains the general information for BiosVfPcieARISupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPcieARISupportConsts:
    VP_PCIE_ARISUPPORT_AUTO = "Auto"
    VP_PCIE_ARISUPPORT_DISABLED = "Disabled"
    VP_PCIE_ARISUPPORT_ENABLED = "Enabled"
    _VP_PCIE_ARISUPPORT_DISABLED = "disabled"
    _VP_PCIE_ARISUPPORT_ENABLED = "enabled"
    VP_PCIE_ARISUPPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfPcieARISupport(ManagedObject):
    """This is BiosVfPcieARISupport class."""

    consts = BiosVfPcieARISupportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPcieARISupport", "biosVfPcieARISupport", "PCIe-ARI-Support", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pcie_ari_support": MoPropertyMeta("vp_pcie_ari_support", "vpPcieARISupport", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPcieARISupport": "vp_pcie_ari_support", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_pcie_ari_support = None

        ManagedObject.__init__(self, "BiosVfPcieARISupport", parent_mo_or_dn, **kwargs)

