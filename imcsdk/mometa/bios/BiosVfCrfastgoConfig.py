"""This module contains the general information for BiosVfCrfastgoConfig ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCrfastgoConfigConsts:
    VP_CRFASTGO_CONFIG_AUTO = "Auto"
    VP_CRFASTGO_CONFIG_DEFAULT = "Default"
    VP_CRFASTGO_CONFIG_DISABLE_OPTIMIZATION = "Disable optimization"
    VP_CRFASTGO_CONFIG_ENABLE_OPTIMIZATION = "Enable optimization"
    VP_CRFASTGO_CONFIG_OPTION_1 = "Option 1"
    VP_CRFASTGO_CONFIG_OPTION_2 = "Option 2"
    VP_CRFASTGO_CONFIG_OPTION_3 = "Option 3"
    VP_CRFASTGO_CONFIG_OPTION_4 = "Option 4"
    VP_CRFASTGO_CONFIG_OPTION_5 = "Option 5"
    VP_CRFASTGO_CONFIG_PLATFORM_DEFAULT = "platform-default"


class BiosVfCrfastgoConfig(ManagedObject):
    """This is BiosVfCrfastgoConfig class."""

    consts = BiosVfCrfastgoConfigConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCrfastgoConfig", "biosVfCrfastgoConfig", "CR-FastGo-Config", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfCrfastgoConfig", "biosVfCrfastgoConfig", "CR-FastGo-Config", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_crfastgo_config": MoPropertyMeta("vp_crfastgo_config", "vpCrfastgoConfig", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Default", "Disable optimization", "Enable optimization", "Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_crfastgo_config": MoPropertyMeta("vp_crfastgo_config", "vpCrfastgoConfig", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Default", "Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCrfastgoConfig": "vp_crfastgo_config", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCrfastgoConfig": "vp_crfastgo_config", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_crfastgo_config = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfCrfastgoConfig", parent_mo_or_dn, **kwargs)

