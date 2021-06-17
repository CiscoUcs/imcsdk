"""This module contains the general information for BiosVfDirectCacheAccess ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfDirectCacheAccessConsts:
    VP_DIRECT_CACHE_ACCESS_AUTO = "Auto"
    VP_DIRECT_CACHE_ACCESS_DISABLED = "Disabled"
    VP_DIRECT_CACHE_ACCESS_ENABLED = "Enabled"
    _VP_DIRECT_CACHE_ACCESS_AUTO = "auto"
    _VP_DIRECT_CACHE_ACCESS_DISABLED = "disabled"
    _VP_DIRECT_CACHE_ACCESS_ENABLED = "enabled"
    VP_DIRECT_CACHE_ACCESS_PLATFORM_DEFAULT = "platform-default"


class BiosVfDirectCacheAccess(ManagedObject):
    """This is BiosVfDirectCacheAccess class."""

    consts = BiosVfDirectCacheAccessConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfDirectCacheAccess", "biosVfDirectCacheAccess", "Direct-Cache-Access", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfDirectCacheAccess", "biosVfDirectCacheAccess", "Direct-Cache-Access", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_direct_cache_access": MoPropertyMeta("vp_direct_cache_access", "vpDirectCacheAccess", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "auto", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_direct_cache_access": MoPropertyMeta("vp_direct_cache_access", "vpDirectCacheAccess", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "auto", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpDirectCacheAccess": "vp_direct_cache_access", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpDirectCacheAccess": "vp_direct_cache_access", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_direct_cache_access = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfDirectCacheAccess", parent_mo_or_dn, **kwargs)

