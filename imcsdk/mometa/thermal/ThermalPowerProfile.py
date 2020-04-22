"""This module contains the general information for ThermalPowerProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class ThermalPowerProfileConsts:
    pass


class ThermalPowerProfile(ManagedObject):
    """This is ThermalPowerProfile class."""

    consts = ThermalPowerProfileConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("ThermalPowerProfile", "thermalPowerProfile", "thermal-prof", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['powerBudget'], [], ["Get", "Set"])
    }


    prop_meta = {

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "power_limit": MoPropertyMeta("power_limit", "powerLimit", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "profile_enabled": MoPropertyMeta("profile_enabled", "profileEnabled", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "no", "yes"], []),
            "profile_type": MoPropertyMeta("profile_type", "profileType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "temperature": MoPropertyMeta("temperature", "temperature", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], ["0-4294967295"]),
        },

    }

    prop_map = {

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "powerLimit": "power_limit", 
            "profileEnabled": "profile_enabled", 
            "profileType": "profile_type", 
            "rn": "rn", 
            "status": "status", 
            "temperature": "temperature", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.power_limit = None
        self.profile_enabled = None
        self.profile_type = None
        self.status = None
        self.temperature = None

        ManagedObject.__init__(self, "ThermalPowerProfile", parent_mo_or_dn, **kwargs)

