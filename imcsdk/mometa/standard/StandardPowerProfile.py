"""This module contains the general information for StandardPowerProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StandardPowerProfileConsts:
    CORR_ACTION_ALERT = "alert"
    CORR_ACTION_ALERT_SHUTDOWN = "alert,shutdown"
    CORR_ACTION_NONE = "none"
    CORR_ACTION_SHUTDOWN = "shutdown"


class StandardPowerProfile(ManagedObject):
    """This is StandardPowerProfile class."""

    consts = StandardPowerProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StandardPowerProfile", "standardPowerProfile", "stdpwrprof", VersionMeta.Version202c, "InputOutput", 0x7ff, [], ["admin", "read-only", "user"], ['powerBudget'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "allow_throttle": MoPropertyMeta("allow_throttle", "allowThrottle", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "corr_action": MoPropertyMeta("corr_action", "corrAction", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["alert", "alert,shutdown", "none", "shutdown"], []),
            "corr_time": MoPropertyMeta("corr_time", "corrTime", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], ["0-4294967295"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "hard_cap": MoPropertyMeta("hard_cap", "hardCap", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "power_limit": MoPropertyMeta("power_limit", "powerLimit", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], ["0-4294967295"]),
            "profile_enabled": MoPropertyMeta("profile_enabled", "profileEnabled", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "profile_type": MoPropertyMeta("profile_type", "profileType", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "suspend_period": MoPropertyMeta("suspend_period", "suspendPeriod", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "allowThrottle": "allow_throttle", 
            "childAction": "child_action", 
            "corrAction": "corr_action", 
            "corrTime": "corr_time", 
            "dn": "dn", 
            "hardCap": "hard_cap", 
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
        self.hard_cap = None
        self.power_limit = None
        self.profile_enabled = None
        self.profile_type = None
        self.status = None
        self.suspend_period = None

        ManagedObject.__init__(self, "StandardPowerProfile", parent_mo_or_dn, **kwargs)

