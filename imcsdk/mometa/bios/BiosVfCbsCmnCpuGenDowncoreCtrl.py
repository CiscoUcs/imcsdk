"""This module contains the general information for BiosVfCbsCmnCpuGenDowncoreCtrl ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnCpuGenDowncoreCtrlConsts:
    VP_CBS_CMN_CPU_GEN_DOWNCORE_CTRL_AUTO = "Auto"
    VP_CBS_CMN_CPU_GEN_DOWNCORE_CTRL_FOUR_2_2 = "FOUR (2 + 2)"
    VP_CBS_CMN_CPU_GEN_DOWNCORE_CTRL_FOUR_4_0 = "FOUR (4 + 0)"
    VP_CBS_CMN_CPU_GEN_DOWNCORE_CTRL_SIX_3_3 = "SIX (3 + 3)"
    VP_CBS_CMN_CPU_GEN_DOWNCORE_CTRL_THREE_3_0 = "THREE (3 + 0)"
    VP_CBS_CMN_CPU_GEN_DOWNCORE_CTRL_TWO_1_1 = "TWO (1 + 1)"
    VP_CBS_CMN_CPU_GEN_DOWNCORE_CTRL_TWO_2_0 = "TWO (2 + 0)"
    VP_CBS_CMN_CPU_GEN_DOWNCORE_CTRL_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnCpuGenDowncoreCtrl(ManagedObject):
    """This is BiosVfCbsCmnCpuGenDowncoreCtrl class."""

    consts = BiosVfCbsCmnCpuGenDowncoreCtrlConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnCpuGenDowncoreCtrl", "biosVfCbsCmnCpuGenDowncoreCtrl", "downcore-ctrl", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_cpu_gen_downcore_ctrl": MoPropertyMeta("vp_cbs_cmn_cpu_gen_downcore_ctrl", "vpCbsCmnCpuGenDowncoreCtrl", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "FOUR (2 + 2)", "FOUR (4 + 0)", "SIX (3 + 3)", "THREE (3 + 0)", "TWO (1 + 1)", "TWO (2 + 0)", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnCpuGenDowncoreCtrl": "vp_cbs_cmn_cpu_gen_downcore_ctrl", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_cpu_gen_downcore_ctrl = None

        ManagedObject.__init__(self, "BiosVfCbsCmnCpuGenDowncoreCtrl", parent_mo_or_dn, **kwargs)

