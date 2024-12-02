"""This module contains the general information for BiosVfCbsDfCmnDramScrubTime ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsDfCmnDramScrubTimeConsts:
    VP_CBS_DF_CMN_DRAM_SCRUB_TIME_1_HOUR = "1 hour"
    VP_CBS_DF_CMN_DRAM_SCRUB_TIME_12_HOURS = "12 hours"
    VP_CBS_DF_CMN_DRAM_SCRUB_TIME_16_HOURS = "16 hours"
    VP_CBS_DF_CMN_DRAM_SCRUB_TIME_24_HOURS = "24 hours"
    VP_CBS_DF_CMN_DRAM_SCRUB_TIME_4_HOURS = "4 hours"
    VP_CBS_DF_CMN_DRAM_SCRUB_TIME_48_HOURS = "48 hours"
    VP_CBS_DF_CMN_DRAM_SCRUB_TIME_6_HOURS = "6 hours"
    VP_CBS_DF_CMN_DRAM_SCRUB_TIME_8_HOURS = "8 hours"
    VP_CBS_DF_CMN_DRAM_SCRUB_TIME_AUTO = "Auto"
    VP_CBS_DF_CMN_DRAM_SCRUB_TIME_DISABLED = "Disabled"
    VP_CBS_DF_CMN_DRAM_SCRUB_TIME_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsDfCmnDramScrubTime(ManagedObject):
    """This is BiosVfCbsDfCmnDramScrubTime class."""

    consts = BiosVfCbsDfCmnDramScrubTimeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsDfCmnDramScrubTime", "biosVfCbsDfCmnDramScrubTime", "dram-scrub-time", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_df_cmn_dram_scrub_time": MoPropertyMeta("vp_cbs_df_cmn_dram_scrub_time", "vpCbsDfCmnDramScrubTime", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1 hour", "12 hours", "16 hours", "24 hours", "4 hours", "48 hours", "6 hours", "8 hours", "Auto", "Disabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsDfCmnDramScrubTime": "vp_cbs_df_cmn_dram_scrub_time", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_df_cmn_dram_scrub_time = None

        ManagedObject.__init__(self, "BiosVfCbsDfCmnDramScrubTime", parent_mo_or_dn, **kwargs)

