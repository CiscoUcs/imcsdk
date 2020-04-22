"""This module contains the general information for ComputeMbPowerStats ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class ComputeMbPowerStatsConsts:
    pass


class ComputeMbPowerStats(ManagedObject):
    """This is ComputeMbPowerStats class."""

    consts = ComputeMbPowerStatsConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("ComputeMbPowerStats", "computeMbPowerStats", "power-stats", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['computeBoard'], [], ["Get"]),
        "modular": MoMeta("ComputeMbPowerStats", "computeMbPowerStats", "power-stats", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['computeBoard'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "consumed_power": MoPropertyMeta("consumed_power", "consumedPower", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "input_current": MoPropertyMeta("input_current", "inputCurrent", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "input_voltage": MoPropertyMeta("input_voltage", "inputVoltage", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "consumed_power": MoPropertyMeta("consumed_power", "consumedPower", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "input_current": MoPropertyMeta("input_current", "inputCurrent", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "input_voltage": MoPropertyMeta("input_voltage", "inputVoltage", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "consumedPower": "consumed_power", 
            "dn": "dn", 
            "inputCurrent": "input_current", 
            "inputVoltage": "input_voltage", 
            "rn": "rn", 
            "status": "status", 
            "timeCollected": "time_collected", 
        },

        "modular": {
            "childAction": "child_action", 
            "consumedPower": "consumed_power", 
            "dn": "dn", 
            "inputCurrent": "input_current", 
            "inputVoltage": "input_voltage", 
            "rn": "rn", 
            "status": "status", 
            "timeCollected": "time_collected", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.consumed_power = None
        self.input_current = None
        self.input_voltage = None
        self.status = None
        self.time_collected = None

        ManagedObject.__init__(self, "ComputeMbPowerStats", parent_mo_or_dn, **kwargs)

