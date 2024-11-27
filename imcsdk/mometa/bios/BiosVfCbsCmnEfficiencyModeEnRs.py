"""This module contains the general information for BiosVfCbsCmnEfficiencyModeEnRs ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnEfficiencyModeEnRsConsts:
    VP_CBS_CMN_EFFICIENCY_MODE_EN_RS_AUTO = "Auto"
    VP_CBS_CMN_EFFICIENCY_MODE_EN_RS_BALANCED_CORE_MEMORY_PERFORMANCE_MODE = "Balanced Core Memory Performance Mode"
    VP_CBS_CMN_EFFICIENCY_MODE_EN_RS_BALANCED_CORE_PERFORMANCE_MODE = "Balanced Core Performance Mode"
    VP_CBS_CMN_EFFICIENCY_MODE_EN_RS_BALANCED_MEMORY_PERFORMANCE_MODE = "Balanced Memory Performance Mode"
    VP_CBS_CMN_EFFICIENCY_MODE_EN_RS_EFFICIENCY_MODE = "Efficiency Mode"
    VP_CBS_CMN_EFFICIENCY_MODE_EN_RS_HIGH_PERFORMANCE_MODE = "High Performance Mode"
    VP_CBS_CMN_EFFICIENCY_MODE_EN_RS_MAXIMUM_IO_PERFORMANCE_MODE = "Maximum IO Performance Mode"
    VP_CBS_CMN_EFFICIENCY_MODE_EN_RS_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnEfficiencyModeEnRs(ManagedObject):
    """This is BiosVfCbsCmnEfficiencyModeEnRs class."""

    consts = BiosVfCbsCmnEfficiencyModeEnRsConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnEfficiencyModeEnRs", "biosVfCbsCmnEfficiencyModeEnRs", "Efficiency-Mode-En-F19h", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_efficiency_mode_en_rs": MoPropertyMeta("vp_cbs_cmn_efficiency_mode_en_rs", "vpCbsCmnEfficiencyModeEnRs", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Balanced Core Memory Performance Mode", "Balanced Core Performance Mode", "Balanced Memory Performance Mode", "Efficiency Mode", "High Performance Mode", "Maximum IO Performance Mode", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnEfficiencyModeEnRs": "vp_cbs_cmn_efficiency_mode_en_rs", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_efficiency_mode_en_rs = None

        ManagedObject.__init__(self, "BiosVfCbsCmnEfficiencyModeEnRs", parent_mo_or_dn, **kwargs)

