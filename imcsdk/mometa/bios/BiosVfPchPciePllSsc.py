"""This module contains the general information for BiosVfPchPciePllSsc ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPchPciePllSscConsts:
    VP_PCH_PCIE_PLL_SSC_PLATFORM_DEFAULT = "platform-default"


class BiosVfPchPciePllSsc(ManagedObject):
    """This is BiosVfPchPciePllSsc class."""

    consts = BiosVfPchPciePllSscConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPchPciePllSsc", "biosVfPchPciePllSsc", "Pch-PCIe-PLL-SSC", VersionMeta.Version431a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version431a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pch_pcie_pll_ssc": MoPropertyMeta("vp_pch_pcie_pll_ssc", "vpPchPciePllSsc", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["platform-default"], ["0-255"]),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPchPciePllSsc": "vp_pch_pcie_pll_ssc", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_pch_pcie_pll_ssc = None

        ManagedObject.__init__(self, "BiosVfPchPciePllSsc", parent_mo_or_dn, **kwargs)

