"""This module contains the general information for BiosVfDCUPrefetch ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfDCUPrefetchConsts:
    VP_IPPREFETCH_DISABLED = "Disabled"
    VP_IPPREFETCH_ENABLED = "Enabled"
    _VP_IPPREFETCH_DISABLED = "disabled"
    _VP_IPPREFETCH_ENABLED = "enabled"
    VP_IPPREFETCH_PLATFORM_DEFAULT = "platform-default"
    VP_STREAMER_PREFETCH_DISABLED = "Disabled"
    VP_STREAMER_PREFETCH_ENABLED = "Enabled"
    _VP_STREAMER_PREFETCH_DISABLED = "disabled"
    _VP_STREAMER_PREFETCH_ENABLED = "enabled"
    VP_STREAMER_PREFETCH_PLATFORM_DEFAULT = "platform-default"


class BiosVfDCUPrefetch(ManagedObject):
    """This is BiosVfDCUPrefetch class."""

    consts = BiosVfDCUPrefetchConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfDCUPrefetch", "biosVfDCUPrefetch", "DCU-Prefetch", VersionMeta.Version151f, "InputOutput", 0x3f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfDCUPrefetch", "biosVfDCUPrefetch", "DCU-Prefetch", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_ip_prefetch": MoPropertyMeta("vp_ip_prefetch", "vpIPPrefetch", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_streamer_prefetch": MoPropertyMeta("vp_streamer_prefetch", "vpStreamerPrefetch", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_ip_prefetch": MoPropertyMeta("vp_ip_prefetch", "vpIPPrefetch", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_streamer_prefetch": MoPropertyMeta("vp_streamer_prefetch", "vpStreamerPrefetch", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIPPrefetch": "vp_ip_prefetch", 
            "vpStreamerPrefetch": "vp_streamer_prefetch", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIPPrefetch": "vp_ip_prefetch", 
            "vpStreamerPrefetch": "vp_streamer_prefetch", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_ip_prefetch = None
        self.vp_streamer_prefetch = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfDCUPrefetch", parent_mo_or_dn, **kwargs)

