"""This module contains the general information for BiosVfCDNSupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCDNSupportConsts:
    VP_CDNSUPPORT_DISABLED = "Disabled"
    VP_CDNSUPPORT_ENABLED = "Enabled"
    VP_CDNSUPPORT_LOMS_ONLY = "LOMs Only"
    _VP_CDNSUPPORT_DISABLED = "disabled"
    _VP_CDNSUPPORT_ENABLED = "enabled"
    VP_CDNSUPPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfCDNSupport(ManagedObject):
    """This is BiosVfCDNSupport class."""

    consts = BiosVfCDNSupportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCDNSupport", "biosVfCDNSupport", "CDN-Support", VersionMeta.Version201a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfCDNSupport", "biosVfCDNSupport", "CDN-Support", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cdn_support": MoPropertyMeta("vp_cdn_support", "vpCDNSupport", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "LOMs Only", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cdn_support": MoPropertyMeta("vp_cdn_support", "vpCDNSupport", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "LOMs Only", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCDNSupport": "vp_cdn_support", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCDNSupport": "vp_cdn_support", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_cdn_support = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfCDNSupport", parent_mo_or_dn, **kwargs)

