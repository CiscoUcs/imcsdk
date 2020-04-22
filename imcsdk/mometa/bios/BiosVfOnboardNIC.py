"""This module contains the general information for BiosVfOnboardNIC ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfOnboardNICConsts:
    VP_ONBOARD10_GBIT_LOM_DISABLED = "Disabled"
    VP_ONBOARD10_GBIT_LOM_ENABLED = "Enabled"
    _VP_ONBOARD10_GBIT_LOM_DISABLED = "disabled"
    _VP_ONBOARD10_GBIT_LOM_ENABLED = "enabled"
    VP_ONBOARD10_GBIT_LOM_PLATFORM_DEFAULT = "platform-default"
    VP_ONBOARD_GBIT_LOM_DISABLED = "Disabled"
    VP_ONBOARD_GBIT_LOM_ENABLED = "Enabled"
    _VP_ONBOARD_GBIT_LOM_DISABLED = "disabled"
    _VP_ONBOARD_GBIT_LOM_ENABLED = "enabled"
    VP_ONBOARD_GBIT_LOM_PLATFORM_DEFAULT = "platform-default"


class BiosVfOnboardNIC(ManagedObject):
    """This is BiosVfOnboardNIC class."""

    consts = BiosVfOnboardNICConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfOnboardNIC", "biosVfOnboardNIC", "Onboard-NIC", VersionMeta.Version151f, "InputOutput", 0x3f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfOnboardNIC", "biosVfOnboardNIC", "Onboard-NIC", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_onboard10_gbit_lom": MoPropertyMeta("vp_onboard10_gbit_lom", "vpOnboard10GbitLOM", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_onboard_gbit_lom": MoPropertyMeta("vp_onboard_gbit_lom", "vpOnboardGbitLOM", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_onboard10_gbit_lom": MoPropertyMeta("vp_onboard10_gbit_lom", "vpOnboard10GbitLOM", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_onboard_gbit_lom": MoPropertyMeta("vp_onboard_gbit_lom", "vpOnboardGbitLOM", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpOnboard10GbitLOM": "vp_onboard10_gbit_lom", 
            "vpOnboardGbitLOM": "vp_onboard_gbit_lom", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpOnboard10GbitLOM": "vp_onboard10_gbit_lom", 
            "vpOnboardGbitLOM": "vp_onboard_gbit_lom", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_onboard10_gbit_lom = None
        self.vp_onboard_gbit_lom = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfOnboardNIC", parent_mo_or_dn, **kwargs)

