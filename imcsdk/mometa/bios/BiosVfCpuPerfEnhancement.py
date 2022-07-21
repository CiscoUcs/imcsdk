"""This module contains the general information for BiosVfCpuPerfEnhancement ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCpuPerfEnhancementConsts:
    VP_CPU_PERF_ENHANCEMENT_AUTO = "Auto"
    VP_CPU_PERF_ENHANCEMENT_DISABLED = "Disabled"
    VP_CPU_PERF_ENHANCEMENT_PLATFORM_DEFAULT = "platform-default"


class BiosVfCpuPerfEnhancement(ManagedObject):
    """This is BiosVfCpuPerfEnhancement class."""

    consts = BiosVfCpuPerfEnhancementConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCpuPerfEnhancement", "biosVfCpuPerfEnhancement", "Cpu-Perf-Enhancement", VersionMeta.Version421b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cpu_perf_enhancement": MoPropertyMeta("vp_cpu_perf_enhancement", "vpCpuPerfEnhancement", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCpuPerfEnhancement": "vp_cpu_perf_enhancement", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cpu_perf_enhancement = None

        ManagedObject.__init__(self, "BiosVfCpuPerfEnhancement", parent_mo_or_dn, **kwargs)

