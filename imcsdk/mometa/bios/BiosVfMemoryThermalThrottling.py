"""This module contains the general information for BiosVfMemoryThermalThrottling ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfMemoryThermalThrottlingConsts:
    VP_MEMORY_THERMAL_THROTTLING_CLTT_WITH_PECI = "CLTT with PECI"
    VP_MEMORY_THERMAL_THROTTLING_DISABLED = "Disabled"
    VP_MEMORY_THERMAL_THROTTLING_PLATFORM_DEFAULT = "platform-default"


class BiosVfMemoryThermalThrottling(ManagedObject):
    """This is BiosVfMemoryThermalThrottling class."""

    consts = BiosVfMemoryThermalThrottlingConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfMemoryThermalThrottling", "biosVfMemoryThermalThrottling", "Memory-Thermal-Throttling-Mode", VersionMeta.Version413a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfMemoryThermalThrottling", "biosVfMemoryThermalThrottling", "Memory-Thermal-Throttling-Mode", VersionMeta.Version413a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_memory_thermal_throttling": MoPropertyMeta("vp_memory_thermal_throttling", "vpMemoryThermalThrottling", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["CLTT with PECI", "Disabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_memory_thermal_throttling": MoPropertyMeta("vp_memory_thermal_throttling", "vpMemoryThermalThrottling", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["CLTT with PECI", "Disabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpMemoryThermalThrottling": "vp_memory_thermal_throttling", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpMemoryThermalThrottling": "vp_memory_thermal_throttling", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_memory_thermal_throttling = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfMemoryThermalThrottling", parent_mo_or_dn, **kwargs)

