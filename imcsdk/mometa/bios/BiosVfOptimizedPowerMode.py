"""This module contains the general information for BiosVfOptimizedPowerMode ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfOptimizedPowerModeConsts:
    VP_OPTIMIZED_POWER_MODE_DISABLED = "Disabled"
    VP_OPTIMIZED_POWER_MODE_ENABLED = "Enabled"
    _VP_OPTIMIZED_POWER_MODE_DISABLED = "disabled"
    _VP_OPTIMIZED_POWER_MODE_ENABLED = "enabled"
    VP_OPTIMIZED_POWER_MODE_PLATFORM_DEFAULT = "platform-default"


class BiosVfOptimizedPowerMode(ManagedObject):
    """This is BiosVfOptimizedPowerMode class."""

    consts = BiosVfOptimizedPowerModeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfOptimizedPowerMode", "biosVfOptimizedPowerMode", "Optimized-Power-Mode", VersionMeta.Version432_230190, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version432_230190, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_optimized_power_mode": MoPropertyMeta("vp_optimized_power_mode", "vpOptimizedPowerMode", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpOptimizedPowerMode": "vp_optimized_power_mode", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_optimized_power_mode = None

        ManagedObject.__init__(self, "BiosVfOptimizedPowerMode", parent_mo_or_dn, **kwargs)

