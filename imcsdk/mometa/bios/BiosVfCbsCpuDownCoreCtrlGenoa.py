"""This module contains the general information for BiosVfCbsCpuDownCoreCtrlGenoa ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCpuDownCoreCtrlGenoaConsts:
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_AUTO = "Auto"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_EIGHT_8_0 = "EIGHT (8 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_ELEVEN_11_0 = "ELEVEN (11 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_FIFTEEN_15_0 = "FIFTEEN (15 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_FIVE_5_0 = "FIVE (5 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_FOUR_4_0 = "FOUR (4 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_FOURTEEN_14_0 = "FOURTEEN (14 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_NINE_9_0 = "NINE (9 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_ONE_1_0 = "ONE (1 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_SEVEN_7_0 = "SEVEN (7 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_SIX_6_0 = "SIX (6 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_TEN_10_0 = "TEN (10 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_THIRTEEN_13_0 = "THIRTEEN (13 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_THREE_3_0 = "THREE (3 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_TWELVE_12_0 = "TWELVE (12 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_TWO_2_0 = "TWO (2 + 0)"
    VP_CBS_CPU_DOWN_CORE_CTRL_GENOA_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCpuDownCoreCtrlGenoa(ManagedObject):
    """This is BiosVfCbsCpuDownCoreCtrlGenoa class."""

    consts = BiosVfCbsCpuDownCoreCtrlGenoaConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCpuDownCoreCtrlGenoa", "biosVfCbsCpuDownCoreCtrlGenoa", "downcore-control", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cpu_down_core_ctrl_genoa": MoPropertyMeta("vp_cbs_cpu_down_core_ctrl_genoa", "vpCbsCpuDownCoreCtrlGenoa", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "EIGHT (8 + 0)", "ELEVEN (11 + 0)", "FIFTEEN (15 + 0)", "FIVE (5 + 0)", "FOUR (4 + 0)", "FOURTEEN (14 + 0)", "NINE (9 + 0)", "ONE (1 + 0)", "SEVEN (7 + 0)", "SIX (6 + 0)", "TEN (10 + 0)", "THIRTEEN (13 + 0)", "THREE (3 + 0)", "TWELVE (12 + 0)", "TWO (2 + 0)", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCpuDownCoreCtrlGenoa": "vp_cbs_cpu_down_core_ctrl_genoa", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cpu_down_core_ctrl_genoa = None

        ManagedObject.__init__(self, "BiosVfCbsCpuDownCoreCtrlGenoa", parent_mo_or_dn, **kwargs)

