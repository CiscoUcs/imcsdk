"""This module contains the general information for BiosVfAutonumousCstateEnable ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfAutonumousCstateEnableConsts:
    VP_AUTONUMOUS_CSTATE_ENABLE_DISABLED = "Disabled"
    VP_AUTONUMOUS_CSTATE_ENABLE_ENABLED = "Enabled"
    _VP_AUTONUMOUS_CSTATE_ENABLE_DISABLED = "disabled"
    _VP_AUTONUMOUS_CSTATE_ENABLE_ENABLED = "enabled"
    VP_AUTONUMOUS_CSTATE_ENABLE_PLATFORM_DEFAULT = "platform-default"


class BiosVfAutonumousCstateEnable(ManagedObject):
    """This is BiosVfAutonumousCstateEnable class."""

    consts = BiosVfAutonumousCstateEnableConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfAutonumousCstateEnable", "biosVfAutonumousCstateEnable", "Autonumous-Cstate-Enable", VersionMeta.Version2010b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfAutonumousCstateEnable", "biosVfAutonumousCstateEnable", "Autonumous-Cstate-Enable", VersionMeta.Version303a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_autonumous_cstate_enable": MoPropertyMeta("vp_autonumous_cstate_enable", "vpAutonumousCstateEnable", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2010b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_autonumous_cstate_enable": MoPropertyMeta("vp_autonumous_cstate_enable", "vpAutonumousCstateEnable", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpAutonumousCstateEnable": "vp_autonumous_cstate_enable", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpAutonumousCstateEnable": "vp_autonumous_cstate_enable", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_autonumous_cstate_enable = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfAutonumousCstateEnable", parent_mo_or_dn, **kwargs)

