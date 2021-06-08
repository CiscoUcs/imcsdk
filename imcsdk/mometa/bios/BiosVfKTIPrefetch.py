"""This module contains the general information for BiosVfKTIPrefetch ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfKTIPrefetchConsts:
    VP_KTIPREFETCH_AUTO = "Auto"
    VP_KTIPREFETCH_DISABLED = "Disabled"
    VP_KTIPREFETCH_ENABLED = "Enabled"
    _VP_KTIPREFETCH_DISABLED = "disabled"
    _VP_KTIPREFETCH_ENABLED = "enabled"
    VP_KTIPREFETCH_PLATFORM_DEFAULT = "platform-default"


class BiosVfKTIPrefetch(ManagedObject):
    """This is BiosVfKTIPrefetch class."""

    consts = BiosVfKTIPrefetchConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfKTIPrefetch", "biosVfKTIPrefetch", "kti-prefetch", VersionMeta.Version304a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfKTIPrefetch", "biosVfKTIPrefetch", "kti-prefetch", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_kti_prefetch": MoPropertyMeta("vp_kti_prefetch", "vpKTIPrefetch", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_kti_prefetch": MoPropertyMeta("vp_kti_prefetch", "vpKTIPrefetch", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpKTIPrefetch": "vp_kti_prefetch", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpKTIPrefetch": "vp_kti_prefetch", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_kti_prefetch = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfKTIPrefetch", parent_mo_or_dn, **kwargs)

