"""This module contains the general information for BiosVfEPPProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfEPPProfileConsts:
    VP_EPPPROFILE_BALANCED_PERFORMANCE = "Balanced Performance"
    VP_EPPPROFILE_BALANCED_POWER = "Balanced Power"
    VP_EPPPROFILE_PERFORMANCE = "Performance"
    VP_EPPPROFILE_POWER = "Power"
    VP_EPPPROFILE_PLATFORM_DEFAULT = "platform-default"


class BiosVfEPPProfile(ManagedObject):
    """This is BiosVfEPPProfile class."""

    consts = BiosVfEPPProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfEPPProfile", "biosVfEPPProfile", "epp-profile", VersionMeta.Version304a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfEPPProfile", "biosVfEPPProfile", "epp-profile", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_epp_profile": MoPropertyMeta("vp_epp_profile", "vpEPPProfile", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Balanced Performance", "Balanced Power", "Performance", "Power", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version304a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_epp_profile": MoPropertyMeta("vp_epp_profile", "vpEPPProfile", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Balanced Performance", "Balanced Power", "Performance", "Power", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEPPProfile": "vp_epp_profile", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEPPProfile": "vp_epp_profile", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_epp_profile = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfEPPProfile", parent_mo_or_dn, **kwargs)

