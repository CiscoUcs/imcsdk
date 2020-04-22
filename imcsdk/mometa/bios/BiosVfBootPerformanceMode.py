"""This module contains the general information for BiosVfBootPerformanceMode ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfBootPerformanceModeConsts:
    VP_BOOT_PERFORMANCE_MODE_MAX_EFFICIENT = "Max Efficient"
    VP_BOOT_PERFORMANCE_MODE_MAX_PERFORMANCE = "Max Performance"
    VP_BOOT_PERFORMANCE_MODE_SET_BY_INTEL_NM = "Set by Intel NM"
    VP_BOOT_PERFORMANCE_MODE_PLATFORM_DEFAULT = "platform-default"


class BiosVfBootPerformanceMode(ManagedObject):
    """This is BiosVfBootPerformanceMode class."""

    consts = BiosVfBootPerformanceModeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfBootPerformanceMode", "biosVfBootPerformanceMode", "Boot-Performance-Mode", VersionMeta.Version303a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfBootPerformanceMode", "biosVfBootPerformanceMode", "Boot-Performance-Mode", VersionMeta.Version303a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_boot_performance_mode": MoPropertyMeta("vp_boot_performance_mode", "vpBootPerformanceMode", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Max Efficient", "Max Performance", "Set by Intel NM", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_boot_performance_mode": MoPropertyMeta("vp_boot_performance_mode", "vpBootPerformanceMode", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Max Efficient", "Max Performance", "Set by Intel NM", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpBootPerformanceMode": "vp_boot_performance_mode", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpBootPerformanceMode": "vp_boot_performance_mode", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_boot_performance_mode = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfBootPerformanceMode", parent_mo_or_dn, **kwargs)

