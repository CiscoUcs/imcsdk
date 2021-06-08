"""This module contains the general information for BiosVfCbsCpuCoreCtrl ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCpuCoreCtrlConsts:
    VP_CBS_CPU_CORE_CTRL_AUTO = "Auto"
    VP_CBS_CPU_CORE_CTRL_FIVE_5_0 = "FIVE (5 + 0)"
    VP_CBS_CPU_CORE_CTRL_FOUR_4_0 = "FOUR (4 + 0)"
    VP_CBS_CPU_CORE_CTRL_ONE_1_0 = "ONE (1 + 0)"
    VP_CBS_CPU_CORE_CTRL_SEVEN_7_0 = "SEVEN (7 + 0)"
    VP_CBS_CPU_CORE_CTRL_SIX_6_0 = "SIX (6 + 0)"
    VP_CBS_CPU_CORE_CTRL_THREE_3_0 = "THREE (3 + 0)"
    VP_CBS_CPU_CORE_CTRL_TWO_2_0 = "TWO (2 + 0)"
    VP_CBS_CPU_CORE_CTRL_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCpuCoreCtrl(ManagedObject):
    """This is BiosVfCbsCpuCoreCtrl class."""

    consts = BiosVfCbsCpuCoreCtrlConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCpuCoreCtrl", "biosVfCbsCpuCoreCtrl", "downcore-control", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cpu_core_ctrl": MoPropertyMeta("vp_cbs_cpu_core_ctrl", "vpCbsCpuCoreCtrl", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "FIVE (5 + 0)", "FOUR (4 + 0)", "ONE (1 + 0)", "SEVEN (7 + 0)", "SIX (6 + 0)", "THREE (3 + 0)", "TWO (2 + 0)", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCpuCoreCtrl": "vp_cbs_cpu_core_ctrl", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cpu_core_ctrl = None

        ManagedObject.__init__(self, "BiosVfCbsCpuCoreCtrl", parent_mo_or_dn, **kwargs)

