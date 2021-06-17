"""This module contains the general information for BiosVfPartialCacheLineSparing ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPartialCacheLineSparingConsts:
    VP_PARTIAL_CACHE_LINE_SPARING_DISABLED = "Disabled"
    VP_PARTIAL_CACHE_LINE_SPARING_ENABLED = "Enabled"
    _VP_PARTIAL_CACHE_LINE_SPARING_DISABLED = "disabled"
    _VP_PARTIAL_CACHE_LINE_SPARING_ENABLED = "enabled"
    VP_PARTIAL_CACHE_LINE_SPARING_PLATFORM_DEFAULT = "platform-default"


class BiosVfPartialCacheLineSparing(ManagedObject):
    """This is BiosVfPartialCacheLineSparing class."""

    consts = BiosVfPartialCacheLineSparingConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPartialCacheLineSparing", "biosVfPartialCacheLineSparing", "Partial-Cache-Line-Sparing", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_partial_cache_line_sparing": MoPropertyMeta("vp_partial_cache_line_sparing", "vpPartialCacheLineSparing", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPartialCacheLineSparing": "vp_partial_cache_line_sparing", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_partial_cache_line_sparing = None

        ManagedObject.__init__(self, "BiosVfPartialCacheLineSparing", parent_mo_or_dn, **kwargs)

