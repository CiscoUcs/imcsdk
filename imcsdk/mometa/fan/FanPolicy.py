"""This module contains the general information for FanPolicy ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class FanPolicyConsts:
    CONFIGURED_FAN_POLICY_ACOUSTIC = "Acoustic"
    CONFIGURED_FAN_POLICY_BALANCED = "Balanced"
    CONFIGURED_FAN_POLICY_HIGH_POWER = "High Power"
    CONFIGURED_FAN_POLICY_LOW_POWER = "Low Power"
    CONFIGURED_FAN_POLICY_MAXIMUM_POWER = "Maximum Power"
    CONFIGURED_FAN_POLICY_PERFORMANCE = "Performance"


class FanPolicy(ManagedObject):
    """This is FanPolicy class."""

    consts = FanPolicyConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("FanPolicy", "fanPolicy", "fan-policy", VersionMeta.Version301c, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['computeBoard'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "aggressive_cooling_enable": MoPropertyMeta("aggressive_cooling_enable", "aggressiveCoolingEnable", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "applied_fan_policy": MoPropertyMeta("applied_fan_policy", "appliedFanPolicy", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "configuration_status": MoPropertyMeta("configuration_status", "configurationStatus", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "configured_fan_policy": MoPropertyMeta("configured_fan_policy", "configuredFanPolicy", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Acoustic", "Balanced", "High Power", "Low Power", "Maximum Power", "Performance"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "aggressiveCoolingEnable": "aggressive_cooling_enable", 
            "appliedFanPolicy": "applied_fan_policy", 
            "childAction": "child_action", 
            "configurationStatus": "configuration_status", 
            "configuredFanPolicy": "configured_fan_policy", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.aggressive_cooling_enable = None
        self.applied_fan_policy = None
        self.child_action = None
        self.configuration_status = None
        self.configured_fan_policy = None
        self.status = None

        ManagedObject.__init__(self, "FanPolicy", parent_mo_or_dn, **kwargs)

