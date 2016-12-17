"""This module contains the general information for BiosVfAdjacentCacheLinePrefetch ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfAdjacentCacheLinePrefetchConsts:
    VP_ADJACENT_CACHE_LINE_PREFETCH_DISABLED = "Disabled"
    VP_ADJACENT_CACHE_LINE_PREFETCH_ENABLED = "Enabled"
    _VP_ADJACENT_CACHE_LINE_PREFETCH_DISABLED = "disabled"
    _VP_ADJACENT_CACHE_LINE_PREFETCH_ENABLED = "enabled"
    VP_ADJACENT_CACHE_LINE_PREFETCH_PLATFORM_DEFAULT = "platform-default"


class BiosVfAdjacentCacheLinePrefetch(ManagedObject):
    """This is BiosVfAdjacentCacheLinePrefetch class."""

    consts = BiosVfAdjacentCacheLinePrefetchConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfAdjacentCacheLinePrefetch", "biosVfAdjacentCacheLinePrefetch", "Adjacent-Cache-Line-Prefetch", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfAdjacentCacheLinePrefetch", "biosVfAdjacentCacheLinePrefetch", "Adjacent-Cache-Line-Prefetch", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_adjacent_cache_line_prefetch": MoPropertyMeta("vp_adjacent_cache_line_prefetch", "vpAdjacentCacheLinePrefetch", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_adjacent_cache_line_prefetch": MoPropertyMeta("vp_adjacent_cache_line_prefetch", "vpAdjacentCacheLinePrefetch", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpAdjacentCacheLinePrefetch": "vp_adjacent_cache_line_prefetch", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpAdjacentCacheLinePrefetch": "vp_adjacent_cache_line_prefetch", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_adjacent_cache_line_prefetch = None

        ManagedObject.__init__(self, "BiosVfAdjacentCacheLinePrefetch", parent_mo_or_dn, **kwargs)

