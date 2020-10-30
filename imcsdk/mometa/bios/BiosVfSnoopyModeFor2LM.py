"""This module contains the general information for BiosVfSnoopyModeFor2LM ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSnoopyModeFor2LMConsts:
    VP_SNOOPY_MODE_FOR2_LM_DISABLED = "Disabled"
    VP_SNOOPY_MODE_FOR2_LM_ENABLED = "Enabled"
    _VP_SNOOPY_MODE_FOR2_LM_DISABLED = "disabled"
    _VP_SNOOPY_MODE_FOR2_LM_ENABLED = "enabled"
    VP_SNOOPY_MODE_FOR2_LM_PLATFORM_DEFAULT = "platform-default"


class BiosVfSnoopyModeFor2LM(ManagedObject):
    """This is BiosVfSnoopyModeFor2LM class."""

    consts = BiosVfSnoopyModeFor2LMConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSnoopyModeFor2LM", "biosVfSnoopyModeFor2LM", "Snoopy-mode-for-2LM", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfSnoopyModeFor2LM", "biosVfSnoopyModeFor2LM", "Snoopy-mode-for-2LM", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_snoopy_mode_for2_lm": MoPropertyMeta("vp_snoopy_mode_for2_lm", "vpSnoopyModeFor2LM", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_snoopy_mode_for2_lm": MoPropertyMeta("vp_snoopy_mode_for2_lm", "vpSnoopyModeFor2LM", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSnoopyModeFor2LM": "vp_snoopy_mode_for2_lm", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSnoopyModeFor2LM": "vp_snoopy_mode_for2_lm", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_snoopy_mode_for2_lm = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfSnoopyModeFor2LM", parent_mo_or_dn, **kwargs)

