"""This module contains the general information for BiosVfLatencyOptimizedMode ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfLatencyOptimizedModeConsts:
    VP_LATENCY_OPTIMIZED_MODE_DISABLED = "Disabled"
    VP_LATENCY_OPTIMIZED_MODE_ENABLED = "Enabled"
    _VP_LATENCY_OPTIMIZED_MODE_DISABLED = "disabled"
    _VP_LATENCY_OPTIMIZED_MODE_ENABLED = "enabled"
    VP_LATENCY_OPTIMIZED_MODE_PLATFORM_DEFAULT = "platform-default"


class BiosVfLatencyOptimizedMode(ManagedObject):
    """This is BiosVfLatencyOptimizedMode class."""

    consts = BiosVfLatencyOptimizedModeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfLatencyOptimizedMode", "biosVfLatencyOptimizedMode", "Latency-Optimized-Mode", VersionMeta.Version435_240045, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version435_240045, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version435_240045, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version435_240045, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version435_240045, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_latency_optimized_mode": MoPropertyMeta("vp_latency_optimized_mode", "vpLatencyOptimizedMode", "string", VersionMeta.Version435_240045, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpLatencyOptimizedMode": "vp_latency_optimized_mode", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_latency_optimized_mode = None

        ManagedObject.__init__(self, "BiosVfLatencyOptimizedMode", parent_mo_or_dn, **kwargs)

