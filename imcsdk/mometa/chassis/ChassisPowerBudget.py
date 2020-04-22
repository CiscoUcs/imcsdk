"""This module contains the general information for ChassisPowerBudget ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class ChassisPowerBudgetConsts:
    ADMIN_ACTION_RESET_POWER_PROFILE_DEFAULT = "reset-power-profile-default"
    ADMIN_ACTION_START_POWER_CHAR = "start-power-char"


class ChassisPowerBudget(ManagedObject):
    """This is ChassisPowerBudget class."""

    consts = ChassisPowerBudgetConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("ChassisPowerBudget", "chassisPowerBudget", "budget", VersionMeta.Version2013e, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['equipmentChassis'], ['autoPowerProfile'], ["Get"])
    }


    prop_meta = {

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["reset-power-profile-default", "start-power-char"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "auto_eff_budget": MoPropertyMeta("auto_eff_budget", "autoEffBudget", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "auto_min_budget": MoPropertyMeta("auto_min_budget", "autoMinBudget", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "budget": MoPropertyMeta("budget", "budget", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], ["0-4294967295"]),
            "cap_budget": MoPropertyMeta("cap_budget", "capBudget", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "max_power": MoPropertyMeta("max_power", "maxPower", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "min_power": MoPropertyMeta("min_power", "minPower", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pow_char_enable": MoPropertyMeta("pow_char_enable", "powCharEnable", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "power_char_status": MoPropertyMeta("power_char_status", "powerCharStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "modular": {
            "adminAction": "admin_action", 
            "adminState": "admin_state", 
            "autoEffBudget": "auto_eff_budget", 
            "autoMinBudget": "auto_min_budget", 
            "budget": "budget", 
            "capBudget": "cap_budget", 
            "childAction": "child_action", 
            "dn": "dn", 
            "maxPower": "max_power", 
            "minPower": "min_power", 
            "powCharEnable": "pow_char_enable", 
            "powerCharStatus": "power_char_status", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.admin_state = None
        self.auto_eff_budget = None
        self.auto_min_budget = None
        self.budget = None
        self.cap_budget = None
        self.child_action = None
        self.max_power = None
        self.min_power = None
        self.pow_char_enable = None
        self.power_char_status = None
        self.status = None

        ManagedObject.__init__(self, "ChassisPowerBudget", parent_mo_or_dn, **kwargs)

