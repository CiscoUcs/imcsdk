"""This module contains the general information for BiosVfSnoopyModeForAD ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSnoopyModeForADConsts:
    VP_SNOOPY_MODE_FOR_AD_DISABLED = "Disabled"
    VP_SNOOPY_MODE_FOR_AD_ENABLED = "Enabled"
    _VP_SNOOPY_MODE_FOR_AD_DISABLED = "disabled"
    _VP_SNOOPY_MODE_FOR_AD_ENABLED = "enabled"
    VP_SNOOPY_MODE_FOR_AD_PLATFORM_DEFAULT = "platform-default"


class BiosVfSnoopyModeForAD(ManagedObject):
    """This is BiosVfSnoopyModeForAD class."""

    consts = BiosVfSnoopyModeForADConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSnoopyModeForAD", "biosVfSnoopyModeForAD", "Snoopy-mode-for-AD", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfSnoopyModeForAD", "biosVfSnoopyModeForAD", "Snoopy-mode-for-AD", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_snoopy_mode_for_ad": MoPropertyMeta("vp_snoopy_mode_for_ad", "vpSnoopyModeForAD", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_snoopy_mode_for_ad": MoPropertyMeta("vp_snoopy_mode_for_ad", "vpSnoopyModeForAD", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSnoopyModeForAD": "vp_snoopy_mode_for_ad", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSnoopyModeForAD": "vp_snoopy_mode_for_ad", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_snoopy_mode_for_ad = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfSnoopyModeForAD", parent_mo_or_dn, **kwargs)

