"""This module contains the general information for BiosVfPciePllSsc ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPciePllSscConsts:
    VP_PCIE_PLL_SSC_AUTO = "Auto"
    VP_PCIE_PLL_SSC_DISABLED = "Disabled"
    VP_PCIE_PLL_SSC_ZERO_POINT_FIVE = "ZeroPointFive"
    VP_PCIE_PLL_SSC_PLATFORM_DEFAULT = "platform-default"


class BiosVfPciePllSsc(ManagedObject):
    """This is BiosVfPciePllSsc class."""

    consts = BiosVfPciePllSscConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPciePllSsc", "biosVfPciePllSsc", "PCIe-PLL-SSC", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfPciePllSsc", "biosVfPciePllSsc", "PCIe-PLL-SSC", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pcie_pll_ssc": MoPropertyMeta("vp_pcie_pll_ssc", "vpPciePllSsc", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "ZeroPointFive", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pcie_pll_ssc": MoPropertyMeta("vp_pcie_pll_ssc", "vpPciePllSsc", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "ZeroPointFive", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPciePllSsc": "vp_pcie_pll_ssc", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPciePllSsc": "vp_pcie_pll_ssc", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_pcie_pll_ssc = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfPciePllSsc", parent_mo_or_dn, **kwargs)

