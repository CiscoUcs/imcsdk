"""This module contains the general information for BiosVfCPUPowerManagement ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCPUPowerManagementConsts:
    VP_CPUPOWER_MANAGEMENT_CUSTOM = "custom"
    VP_CPUPOWER_MANAGEMENT_DISABLED = "disabled"
    VP_CPUPOWER_MANAGEMENT_ENERGY_EFFICIENT = "energy-efficient"
    VP_CPUPOWER_MANAGEMENT_PERFORMANCE = "performance"
    VP_CPUPOWER_MANAGEMENT_PLATFORM_DEFAULT = "platform-default"


class BiosVfCPUPowerManagement(ManagedObject):
    """This is BiosVfCPUPowerManagement class."""

    consts = BiosVfCPUPowerManagementConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCPUPowerManagement", "biosVfCPUPowerManagement", "CPU-PowerManagement", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfCPUPowerManagement", "biosVfCPUPowerManagement", "CPU-PowerManagement", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cpu_power_management": MoPropertyMeta("vp_cpu_power_management", "vpCPUPowerManagement", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["custom", "disabled", "energy-efficient", "performance", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cpu_power_management": MoPropertyMeta("vp_cpu_power_management", "vpCPUPowerManagement", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["custom", "disabled", "energy-efficient", "performance", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCPUPowerManagement": "vp_cpu_power_management", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCPUPowerManagement": "vp_cpu_power_management", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_cpu_power_management = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfCPUPowerManagement", parent_mo_or_dn, **kwargs)

