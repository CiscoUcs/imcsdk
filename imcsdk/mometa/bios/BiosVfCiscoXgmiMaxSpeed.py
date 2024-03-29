"""This module contains the general information for BiosVfCiscoXgmiMaxSpeed ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCiscoXgmiMaxSpeedConsts:
    VP_CISCO_XGMI_MAX_SPEED_DISABLED = "Disabled"
    VP_CISCO_XGMI_MAX_SPEED_ENABLED = "Enabled"
    _VP_CISCO_XGMI_MAX_SPEED_DISABLED = "disabled"
    _VP_CISCO_XGMI_MAX_SPEED_ENABLED = "enabled"
    VP_CISCO_XGMI_MAX_SPEED_PLATFORM_DEFAULT = "platform-default"


class BiosVfCiscoXgmiMaxSpeed(ManagedObject):
    """This is BiosVfCiscoXgmiMaxSpeed class."""

    consts = BiosVfCiscoXgmiMaxSpeedConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCiscoXgmiMaxSpeed", "biosVfCiscoXgmiMaxSpeed", "xgmi-max-speed", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cisco_xgmi_max_speed": MoPropertyMeta("vp_cisco_xgmi_max_speed", "vpCiscoXgmiMaxSpeed", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCiscoXgmiMaxSpeed": "vp_cisco_xgmi_max_speed", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cisco_xgmi_max_speed = None

        ManagedObject.__init__(self, "BiosVfCiscoXgmiMaxSpeed", parent_mo_or_dn, **kwargs)

