"""This module contains the general information for CustomPowerProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CustomPowerProfileConsts:
    CORR_ACTION_ALERT = "alert"
    CORR_ACTION_ALERT_SHUTDOWN = "alert,shutdown"
    CORR_ACTION_NONE = "none"


class CustomPowerProfile(ManagedObject):
    """This is CustomPowerProfile class."""

    consts = CustomPowerProfileConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("CustomPowerProfile", "customPowerProfile", "cust-prof", VersionMeta.Version2013e, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['powerBudget'], [], ["Get", "Set"])
    }


    prop_meta = {

        "modular": {
            "allow_throttle": MoPropertyMeta("allow_throttle", "allowThrottle", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["No", "Yes", "no", "yes"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "corr_action": MoPropertyMeta("corr_action", "corrAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["alert", "alert,shutdown", "none"], []),
            "corr_time": MoPropertyMeta("corr_time", "corrTime", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], ["0-4294967295"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "power_limit": MoPropertyMeta("power_limit", "powerLimit", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], ["0-4294967295"]),
            "profile_enabled": MoPropertyMeta("profile_enabled", "profileEnabled", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["No", "Yes", "no", "yes"], []),
            "profile_type": MoPropertyMeta("profile_type", "profileType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "suspend_period": MoPropertyMeta("suspend_period", "suspendPeriod", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "modular": {
            "allowThrottle": "allow_throttle", 
            "childAction": "child_action", 
            "corrAction": "corr_action", 
            "corrTime": "corr_time", 
            "dn": "dn", 
            "powerLimit": "power_limit", 
            "profileEnabled": "profile_enabled", 
            "profileType": "profile_type", 
            "rn": "rn", 
            "status": "status", 
            "suspendPeriod": "suspend_period", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.allow_throttle = None
        self.child_action = None
        self.corr_action = None
        self.corr_time = None
        self.power_limit = None
        self.profile_enabled = None
        self.profile_type = None
        self.status = None
        self.suspend_period = None

        ManagedObject.__init__(self, "CustomPowerProfile", parent_mo_or_dn, **kwargs)

