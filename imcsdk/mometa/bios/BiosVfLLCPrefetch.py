"""This module contains the general information for BiosVfLLCPrefetch ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfLLCPrefetchConsts:
    VP_LLCPREFETCH_DISABLED = "Disabled"
    VP_LLCPREFETCH_ENABLED = "Enabled"
    _VP_LLCPREFETCH_DISABLED = "disabled"
    _VP_LLCPREFETCH_ENABLED = "enabled"
    VP_LLCPREFETCH_PLATFORM_DEFAULT = "platform-default"


class BiosVfLLCPrefetch(ManagedObject):
    """This is BiosVfLLCPrefetch class."""

    consts = BiosVfLLCPrefetchConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfLLCPrefetch", "biosVfLLCPrefetch", "LLC-Prefetch", VersionMeta.Version311d, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version311d, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_llc_prefetch": MoPropertyMeta("vp_llc_prefetch", "vpLLCPrefetch", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpLLCPrefetch": "vp_llc_prefetch", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_llc_prefetch = None

        ManagedObject.__init__(self, "BiosVfLLCPrefetch", parent_mo_or_dn, **kwargs)

