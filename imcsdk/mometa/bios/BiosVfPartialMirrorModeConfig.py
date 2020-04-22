"""This module contains the general information for BiosVfPartialMirrorModeConfig ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPartialMirrorModeConfigConsts:
    VP_PARTIAL_MIRROR_MODE_CONFIG_DISABLED = "Disabled"
    VP_PARTIAL_MIRROR_MODE_CONFIG_PERCENTAGE = "Percentage"
    VP_PARTIAL_MIRROR_MODE_CONFIG_VALUE_IN_GB = "Value in GB"
    _VP_PARTIAL_MIRROR_MODE_CONFIG_DISABLED = "disabled"
    VP_PARTIAL_MIRROR_MODE_CONFIG_PLATFORM_DEFAULT = "platform-default"


class BiosVfPartialMirrorModeConfig(ManagedObject):
    """This is BiosVfPartialMirrorModeConfig class."""

    consts = BiosVfPartialMirrorModeConfigConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPartialMirrorModeConfig", "biosVfPartialMirrorModeConfig", "Partial-Mirror-Mode", VersionMeta.Version411c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfPartialMirrorModeConfig", "biosVfPartialMirrorModeConfig", "Partial-Mirror-Mode", VersionMeta.Version411c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_partial_mirror_mode_config": MoPropertyMeta("vp_partial_mirror_mode_config", "vpPartialMirrorModeConfig", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Percentage", "Value in GB", "disabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_partial_mirror_mode_config": MoPropertyMeta("vp_partial_mirror_mode_config", "vpPartialMirrorModeConfig", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Percentage", "Value in GB", "disabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPartialMirrorModeConfig": "vp_partial_mirror_mode_config", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPartialMirrorModeConfig": "vp_partial_mirror_mode_config", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_partial_mirror_mode_config = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfPartialMirrorModeConfig", parent_mo_or_dn, **kwargs)

