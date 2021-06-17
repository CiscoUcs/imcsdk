"""This module contains the general information for BiosVfCbsDfCmnDramNps ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsDfCmnDramNpsConsts:
    VP_CBS_DF_CMN_DRAM_NPS_AUTO = "Auto"
    VP_CBS_DF_CMN_DRAM_NPS_NPS0 = "NPS0"
    VP_CBS_DF_CMN_DRAM_NPS_NPS1 = "NPS1"
    VP_CBS_DF_CMN_DRAM_NPS_NPS2 = "NPS2"
    VP_CBS_DF_CMN_DRAM_NPS_NPS4 = "NPS4"
    VP_CBS_DF_CMN_DRAM_NPS_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsDfCmnDramNps(ManagedObject):
    """This is BiosVfCbsDfCmnDramNps class."""

    consts = BiosVfCbsDfCmnDramNpsConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsDfCmnDramNps", "biosVfCbsDfCmnDramNps", "nodes-per-socket", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_df_cmn_dram_nps": MoPropertyMeta("vp_cbs_df_cmn_dram_nps", "vpCbsDfCmnDramNps", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "NPS0", "NPS1", "NPS2", "NPS4", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsDfCmnDramNps": "vp_cbs_df_cmn_dram_nps", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_df_cmn_dram_nps = None

        ManagedObject.__init__(self, "BiosVfCbsDfCmnDramNps", parent_mo_or_dn, **kwargs)

