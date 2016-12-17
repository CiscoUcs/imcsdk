"""This module contains the general information for BiosVfCDNEnable ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCDNEnableConsts:
    VP_CDNENABLE_DISABLED = "Disabled"
    VP_CDNENABLE_ENABLED = "Enabled"
    _VP_CDNENABLE_DISABLED = "disabled"
    _VP_CDNENABLE_ENABLED = "enabled"
    VP_CDNENABLE_PLATFORM_DEFAULT = "platform-default"


class BiosVfCDNEnable(ManagedObject):
    """This is BiosVfCDNEnable class."""

    consts = BiosVfCDNEnableConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCDNEnable", "biosVfCDNEnable", "CDN-Enable", VersionMeta.Version204c, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfCDNEnable", "biosVfCDNEnable", "CDN-Enable", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_cdn_enable": MoPropertyMeta("vp_cdn_enable", "vpCDNEnable", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_cdn_enable": MoPropertyMeta("vp_cdn_enable", "vpCDNEnable", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCDNEnable": "vp_cdn_enable", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCDNEnable": "vp_cdn_enable", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_cdn_enable = None

        ManagedObject.__init__(self, "BiosVfCDNEnable", parent_mo_or_dn, **kwargs)

