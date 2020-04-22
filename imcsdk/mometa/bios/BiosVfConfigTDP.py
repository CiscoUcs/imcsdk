"""This module contains the general information for BiosVfConfigTDP ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfConfigTDPConsts:
    VP_CONFIG_TDP_DISABLED = "Disabled"
    VP_CONFIG_TDP_ENABLED = "Enabled"
    _VP_CONFIG_TDP_DISABLED = "disabled"
    _VP_CONFIG_TDP_ENABLED = "enabled"
    VP_CONFIG_TDP_PLATFORM_DEFAULT = "platform-default"


class BiosVfConfigTDP(ManagedObject):
    """This is BiosVfConfigTDP class."""

    consts = BiosVfConfigTDPConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfConfigTDP", "biosVfConfigTDP", "Config-TDP", VersionMeta.Version303a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_config_tdp": MoPropertyMeta("vp_config_tdp", "vpConfigTDP", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpConfigTDP": "vp_config_tdp", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_config_tdp = None

        ManagedObject.__init__(self, "BiosVfConfigTDP", parent_mo_or_dn, **kwargs)

