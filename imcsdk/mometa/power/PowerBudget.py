"""This module contains the general information for PowerBudget ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PowerBudgetConsts:
    ADMIN_ACTION_RESET_POWER_PROFILE_DEFAULT = "reset-power-profile-default"
    ADMIN_ACTION_START_POWER_CHAR = "start-power-char"


class PowerBudget(ManagedObject):
    """This is PowerBudget class."""

    consts = PowerBudgetConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("PowerBudget", "powerBudget", "budget", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['computeRackUnit'], ['advancedPowerProfile', 'faultInst', 'standardPowerProfile'], ["Get", "Set"]),
        "modular": MoMeta("PowerBudget", "powerBudget", "budget", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['computeServerNode'], ['customPowerProfile', 'faultInst', 'thermalPowerProfile'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["reset-power-profile-default", "start-power-char"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "eff_cpu_power": MoPropertyMeta("eff_cpu_power", "effCpuPower", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "eff_power": MoPropertyMeta("eff_power", "effPower", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "max_cpu_power": MoPropertyMeta("max_cpu_power", "maxCpuPower", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "max_memory_power": MoPropertyMeta("max_memory_power", "maxMemoryPower", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "max_power": MoPropertyMeta("max_power", "maxPower", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "min_cpu_power": MoPropertyMeta("min_cpu_power", "minCpuPower", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "min_memory_power": MoPropertyMeta("min_memory_power", "minMemoryPower", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "min_power": MoPropertyMeta("min_power", "minPower", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pow_char_enable": MoPropertyMeta("pow_char_enable", "powCharEnable", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "power_char_status": MoPropertyMeta("power_char_status", "powerCharStatus", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "eff_power": MoPropertyMeta("eff_power", "effPower", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "max_cpu_power": MoPropertyMeta("max_cpu_power", "maxCpuPower", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "max_memory_power": MoPropertyMeta("max_memory_power", "maxMemoryPower", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "max_power": MoPropertyMeta("max_power", "maxPower", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "min_cpu_power": MoPropertyMeta("min_cpu_power", "minCpuPower", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "min_memory_power": MoPropertyMeta("min_memory_power", "minMemoryPower", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "min_power": MoPropertyMeta("min_power", "minPower", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "power_char_status": MoPropertyMeta("power_char_status", "powerCharStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "effCpuPower": "eff_cpu_power", 
            "effPower": "eff_power", 
            "maxCpuPower": "max_cpu_power", 
            "maxMemoryPower": "max_memory_power", 
            "maxPower": "max_power", 
            "minCpuPower": "min_cpu_power", 
            "minMemoryPower": "min_memory_power", 
            "minPower": "min_power", 
            "powCharEnable": "pow_char_enable", 
            "powerCharStatus": "power_char_status", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "description": "description", 
            "dn": "dn", 
            "effPower": "eff_power", 
            "maxCpuPower": "max_cpu_power", 
            "maxMemoryPower": "max_memory_power", 
            "maxPower": "max_power", 
            "minCpuPower": "min_cpu_power", 
            "minMemoryPower": "min_memory_power", 
            "minPower": "min_power", 
            "powerCharStatus": "power_char_status", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.admin_state = None
        self.child_action = None
        self.eff_cpu_power = None
        self.eff_power = None
        self.max_cpu_power = None
        self.max_memory_power = None
        self.max_power = None
        self.min_cpu_power = None
        self.min_memory_power = None
        self.min_power = None
        self.pow_char_enable = None
        self.power_char_status = None
        self.status = None
        self.description = None

        ManagedObject.__init__(self, "PowerBudget", parent_mo_or_dn, **kwargs)

