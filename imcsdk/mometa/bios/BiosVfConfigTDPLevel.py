"""This module contains the general information for BiosVfConfigTDPLevel ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfConfigTDPLevelConsts:
    VP_CONFIG_TDPLEVEL_LEVEL_1 = "Level 1"
    VP_CONFIG_TDPLEVEL_LEVEL_2 = "Level 2"
    VP_CONFIG_TDPLEVEL_NORMAL = "Normal"
    VP_CONFIG_TDPLEVEL_PLATFORM_DEFAULT = "platform-default"


class BiosVfConfigTDPLevel(ManagedObject):
    """This is BiosVfConfigTDPLevel class."""

    consts = BiosVfConfigTDPLevelConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfConfigTDPLevel", "biosVfConfigTDPLevel", "Configurable-TDP-Level", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfConfigTDPLevel", "biosVfConfigTDPLevel", "Configurable-TDP-Level", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_config_tdp_level": MoPropertyMeta("vp_config_tdp_level", "vpConfigTDPLevel", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Level 1", "Level 2", "Normal", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_config_tdp_level": MoPropertyMeta("vp_config_tdp_level", "vpConfigTDPLevel", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Level 1", "Level 2", "Normal", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpConfigTDPLevel": "vp_config_tdp_level", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpConfigTDPLevel": "vp_config_tdp_level", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_config_tdp_level = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfConfigTDPLevel", parent_mo_or_dn, **kwargs)

