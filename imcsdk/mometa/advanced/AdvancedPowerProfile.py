"""This module contains the general information for AdvancedPowerProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdvancedPowerProfileConsts:
    CORR_ACTION_ALERT = "alert"
    CORR_ACTION_ALERT_SHUTDOWN = "alert,shutdown"
    CORR_ACTION_NONE = "none"
    CORR_ACTION_SHUTDOWN = "shutdown"


class AdvancedPowerProfile(ManagedObject):
    """This is AdvancedPowerProfile class."""

    consts = AdvancedPowerProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdvancedPowerProfile", "advancedPowerProfile", "advpwrprof", VersionMeta.Version202c, "InputOutput", 0x7ffff, [], ["admin", "read-only", "user"], ['powerBudget'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "allow_throttle": MoPropertyMeta("allow_throttle", "allowThrottle", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "corr_action": MoPropertyMeta("corr_action", "corrAction", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["alert", "alert,shutdown", "none", "shutdown"], []),
            "corr_time": MoPropertyMeta("corr_time", "corrTime", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], ["0-4294967295"]),
            "cpu_power_limit": MoPropertyMeta("cpu_power_limit", "cpuPowerLimit", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], ["0-4294967295"]),
            "cpu_safe_throt_lvl": MoPropertyMeta("cpu_safe_throt_lvl", "cpuSafeThrotLvl", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], ["0-100"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "hard_cap": MoPropertyMeta("hard_cap", "hardCap", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "mem_safe_throt_lvl": MoPropertyMeta("mem_safe_throt_lvl", "memSafeThrotLvl", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, [], ["0-100"]),
            "memory_power_limit": MoPropertyMeta("memory_power_limit", "memoryPowerLimit", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x200, 0, 510, None, [], ["0-4294967295"]),
            "miss_rdg_timeout": MoPropertyMeta("miss_rdg_timeout", "missRdgTimeout", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, None, [], ["0-4294967295"]),
            "plat_safe_throt_lvl": MoPropertyMeta("plat_safe_throt_lvl", "platSafeThrotLvl", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x800, 0, 510, None, [], ["0-100"]),
            "platform_thermal": MoPropertyMeta("platform_thermal", "platformThermal", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x1000, 0, 510, None, [], ["0-4294967295"]),
            "power_limit": MoPropertyMeta("power_limit", "powerLimit", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2000, 0, 510, None, [], ["0-4294967295"]),
            "profile_enabled": MoPropertyMeta("profile_enabled", "profileEnabled", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "profile_type": MoPropertyMeta("profile_type", "profileType", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x8000, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "suspend_period": MoPropertyMeta("suspend_period", "suspendPeriod", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x20000, 0, 510, None, [], []),
            "thermal_pow_limit": MoPropertyMeta("thermal_pow_limit", "thermalPowLimit", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x40000, 0, 510, None, [], ["0-4294967295"]),
        },

    }

    prop_map = {

        "classic": {
            "allowThrottle": "allow_throttle", 
            "childAction": "child_action", 
            "corrAction": "corr_action", 
            "corrTime": "corr_time", 
            "cpuPowerLimit": "cpu_power_limit", 
            "cpuSafeThrotLvl": "cpu_safe_throt_lvl", 
            "dn": "dn", 
            "hardCap": "hard_cap", 
            "memSafeThrotLvl": "mem_safe_throt_lvl", 
            "memoryPowerLimit": "memory_power_limit", 
            "missRdgTimeout": "miss_rdg_timeout", 
            "platSafeThrotLvl": "plat_safe_throt_lvl", 
            "platformThermal": "platform_thermal", 
            "powerLimit": "power_limit", 
            "profileEnabled": "profile_enabled", 
            "profileType": "profile_type", 
            "rn": "rn", 
            "status": "status", 
            "suspendPeriod": "suspend_period", 
            "thermalPowLimit": "thermal_pow_limit", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.allow_throttle = None
        self.child_action = None
        self.corr_action = None
        self.corr_time = None
        self.cpu_power_limit = None
        self.cpu_safe_throt_lvl = None
        self.hard_cap = None
        self.mem_safe_throt_lvl = None
        self.memory_power_limit = None
        self.miss_rdg_timeout = None
        self.plat_safe_throt_lvl = None
        self.platform_thermal = None
        self.power_limit = None
        self.profile_enabled = None
        self.profile_type = None
        self.status = None
        self.suspend_period = None
        self.thermal_pow_limit = None

        ManagedObject.__init__(self, "AdvancedPowerProfile", parent_mo_or_dn, **kwargs)

