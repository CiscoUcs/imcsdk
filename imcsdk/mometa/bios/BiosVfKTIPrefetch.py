"""This module contains the general information for BiosVfKTIPrefetch ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfKTIPrefetchConsts:
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
        "classic": MoMeta("BiosVfKTIPrefetch", "biosVfKTIPrefetch", "kti-prefetch", VersionMeta.Version311d, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_kti_prefetch": MoPropertyMeta("vp_kti_prefetch", "vpKTIPrefetch", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
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

        ManagedObject.__init__(self, "BiosVfKTIPrefetch", parent_mo_or_dn, **kwargs)

