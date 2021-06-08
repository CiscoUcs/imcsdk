"""This module contains the general information for BiosVfCbsCmnCpuL2StreamHwPrefetcher ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnCpuL2StreamHwPrefetcherConsts:
    VP_CBS_CMN_CPU_L2_STREAM_HW_PREFETCHER_AUTO = "Auto"
    VP_CBS_CMN_CPU_L2_STREAM_HW_PREFETCHER_DISABLED = "Disabled"
    VP_CBS_CMN_CPU_L2_STREAM_HW_PREFETCHER_ENABLED = "Enabled"
    _VP_CBS_CMN_CPU_L2_STREAM_HW_PREFETCHER_DISABLED = "disabled"
    _VP_CBS_CMN_CPU_L2_STREAM_HW_PREFETCHER_ENABLED = "enabled"
    VP_CBS_CMN_CPU_L2_STREAM_HW_PREFETCHER_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnCpuL2StreamHwPrefetcher(ManagedObject):
    """This is BiosVfCbsCmnCpuL2StreamHwPrefetcher class."""

    consts = BiosVfCbsCmnCpuL2StreamHwPrefetcherConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnCpuL2StreamHwPrefetcher", "biosVfCbsCmnCpuL2StreamHwPrefetcher", "cpu-l2-prefetch", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_cpu_l2_stream_hw_prefetcher": MoPropertyMeta("vp_cbs_cmn_cpu_l2_stream_hw_prefetcher", "vpCbsCmnCpuL2StreamHwPrefetcher", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnCpuL2StreamHwPrefetcher": "vp_cbs_cmn_cpu_l2_stream_hw_prefetcher", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_cpu_l2_stream_hw_prefetcher = None

        ManagedObject.__init__(self, "BiosVfCbsCmnCpuL2StreamHwPrefetcher", parent_mo_or_dn, **kwargs)

