"""This module contains the general information for BiosVfXPTPrefetch ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfXPTPrefetchConsts:
    VP_XPTPREFETCH_DISABLED = "Disabled"
    VP_XPTPREFETCH_ENABLED = "Enabled"
    _VP_XPTPREFETCH_DISABLED = "disabled"
    _VP_XPTPREFETCH_ENABLED = "enabled"
    VP_XPTPREFETCH_PLATFORM_DEFAULT = "platform-default"


class BiosVfXPTPrefetch(ManagedObject):
    """This is BiosVfXPTPrefetch class."""

    consts = BiosVfXPTPrefetchConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfXPTPrefetch", "biosVfXPTPrefetch", "xpt-prefetch", VersionMeta.Version311d, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_xpt_prefetch": MoPropertyMeta("vp_xpt_prefetch", "vpXPTPrefetch", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpXPTPrefetch": "vp_xpt_prefetch", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_xpt_prefetch = None

        ManagedObject.__init__(self, "BiosVfXPTPrefetch", parent_mo_or_dn, **kwargs)

