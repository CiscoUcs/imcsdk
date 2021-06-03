"""This module contains the general information for BiosVfCbsCpuCcdCtrlSsp ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCpuCcdCtrlSspConsts:
    VP_CBS_CPU_CCD_CTRL_SSP_2_CCDS = "2 CCDs"
    VP_CBS_CPU_CCD_CTRL_SSP_3_CCDS = "3 CCDs"
    VP_CBS_CPU_CCD_CTRL_SSP_4_CCDS = "4 CCDs"
    VP_CBS_CPU_CCD_CTRL_SSP_6_CCDS = "6 CCDs"
    VP_CBS_CPU_CCD_CTRL_SSP_AUTO = "Auto"
    VP_CBS_CPU_CCD_CTRL_SSP_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCpuCcdCtrlSsp(ManagedObject):
    """This is BiosVfCbsCpuCcdCtrlSsp class."""

    consts = BiosVfCbsCpuCcdCtrlSspConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCpuCcdCtrlSsp", "biosVfCbsCpuCcdCtrlSsp", "ccd-control", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cpu_ccd_ctrl_ssp": MoPropertyMeta("vp_cbs_cpu_ccd_ctrl_ssp", "vpCbsCpuCcdCtrlSsp", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["2 CCDs", "3 CCDs", "4 CCDs", "6 CCDs", "Auto", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCpuCcdCtrlSsp": "vp_cbs_cpu_ccd_ctrl_ssp", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cpu_ccd_ctrl_ssp = None

        ManagedObject.__init__(self, "BiosVfCbsCpuCcdCtrlSsp", parent_mo_or_dn, **kwargs)

