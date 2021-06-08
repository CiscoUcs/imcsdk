"""This module contains the general information for BiosVfCbsCmnCpuStreamingStoresCtrl ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnCpuStreamingStoresCtrlConsts:
    VP_CBS_CMN_CPU_STREAMING_STORES_CTRL_AUTO = "Auto"
    VP_CBS_CMN_CPU_STREAMING_STORES_CTRL_DISABLED = "Disabled"
    VP_CBS_CMN_CPU_STREAMING_STORES_CTRL_ENABLED = "Enabled"
    _VP_CBS_CMN_CPU_STREAMING_STORES_CTRL_DISABLED = "disabled"
    _VP_CBS_CMN_CPU_STREAMING_STORES_CTRL_ENABLED = "enabled"
    VP_CBS_CMN_CPU_STREAMING_STORES_CTRL_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnCpuStreamingStoresCtrl(ManagedObject):
    """This is BiosVfCbsCmnCpuStreamingStoresCtrl class."""

    consts = BiosVfCbsCmnCpuStreamingStoresCtrlConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnCpuStreamingStoresCtrl", "biosVfCbsCmnCpuStreamingStoresCtrl", "streaming-stores-control", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_cpu_streaming_stores_ctrl": MoPropertyMeta("vp_cbs_cmn_cpu_streaming_stores_ctrl", "vpCbsCmnCpuStreamingStoresCtrl", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnCpuStreamingStoresCtrl": "vp_cbs_cmn_cpu_streaming_stores_ctrl", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_cpu_streaming_stores_ctrl = None

        ManagedObject.__init__(self, "BiosVfCbsCmnCpuStreamingStoresCtrl", parent_mo_or_dn, **kwargs)

