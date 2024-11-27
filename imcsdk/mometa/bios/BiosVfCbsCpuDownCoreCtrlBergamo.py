"""This module contains the general information for BiosVfCbsCpuDownCoreCtrlBergamo ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCpuDownCoreCtrlBergamoConsts:
    VP_CBS_CPU_DOWN_CORE_CTRL_BERGAMO_AUTO = "Auto"
    VP_CBS_CPU_DOWN_CORE_CTRL_BERGAMO_EIGHT_4_4 = "EIGHT (4 + 4)"
    VP_CBS_CPU_DOWN_CORE_CTRL_BERGAMO_FOUR_2_2 = "FOUR (2 + 2)"
    VP_CBS_CPU_DOWN_CORE_CTRL_BERGAMO_FOURTEEN_7_7 = "FOURTEEN (7 + 7)"
    VP_CBS_CPU_DOWN_CORE_CTRL_BERGAMO_SIX_3_3 = "SIX (3 + 3)"
    VP_CBS_CPU_DOWN_CORE_CTRL_BERGAMO_TEN_5_5 = "TEN (5 + 5)"
    VP_CBS_CPU_DOWN_CORE_CTRL_BERGAMO_TWELVE_6_6 = "TWELVE (6 + 6)"
    VP_CBS_CPU_DOWN_CORE_CTRL_BERGAMO_TWO_1_1 = "TWO (1 + 1)"
    VP_CBS_CPU_DOWN_CORE_CTRL_BERGAMO_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCpuDownCoreCtrlBergamo(ManagedObject):
    """This is BiosVfCbsCpuDownCoreCtrlBergamo class."""

    consts = BiosVfCbsCpuDownCoreCtrlBergamoConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCpuDownCoreCtrlBergamo", "biosVfCbsCpuDownCoreCtrlBergamo", "downcore-ctrl", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cpu_down_core_ctrl_bergamo": MoPropertyMeta("vp_cbs_cpu_down_core_ctrl_bergamo", "vpCbsCpuDownCoreCtrlBergamo", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "EIGHT (4 + 4)", "FOUR (2 + 2)", "FOURTEEN (7 + 7)", "SIX (3 + 3)", "TEN (5 + 5)", "TWELVE (6 + 6)", "TWO (1 + 1)", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCpuDownCoreCtrlBergamo": "vp_cbs_cpu_down_core_ctrl_bergamo", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cpu_down_core_ctrl_bergamo = None

        ManagedObject.__init__(self, "BiosVfCbsCpuDownCoreCtrlBergamo", parent_mo_or_dn, **kwargs)

