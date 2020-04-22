"""This module contains the general information for BiosVfCPUEnergyPerformance ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCPUEnergyPerformanceConsts:
    VP_CPUENERGY_PERFORMANCE_BALANCED_ENERGY = "balanced-energy"
    VP_CPUENERGY_PERFORMANCE_BALANCED_PERFORMANCE = "balanced-performance"
    VP_CPUENERGY_PERFORMANCE_BALANCED_POWER = "balanced-power"
    VP_CPUENERGY_PERFORMANCE_ENERGY_EFFICIENT = "energy-efficient"
    VP_CPUENERGY_PERFORMANCE_PERFORMANCE = "performance"
    VP_CPUENERGY_PERFORMANCE_PLATFORM_DEFAULT = "platform-default"
    VP_CPUENERGY_PERFORMANCE_POWER = "power"


class BiosVfCPUEnergyPerformance(ManagedObject):
    """This is BiosVfCPUEnergyPerformance class."""

    consts = BiosVfCPUEnergyPerformanceConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCPUEnergyPerformance", "biosVfCPUEnergyPerformance", "CPU-EngPerfBias", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfCPUEnergyPerformance", "biosVfCPUEnergyPerformance", "CPU-EngPerfBias", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cpu_energy_performance": MoPropertyMeta("vp_cpu_energy_performance", "vpCPUEnergyPerformance", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["balanced-energy", "balanced-performance", "balanced-power", "energy-efficient", "performance", "platform-default", "power"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cpu_energy_performance": MoPropertyMeta("vp_cpu_energy_performance", "vpCPUEnergyPerformance", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["balanced-energy", "balanced-performance", "balanced-power", "energy-efficient", "performance", "platform-default", "power"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCPUEnergyPerformance": "vp_cpu_energy_performance", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCPUEnergyPerformance": "vp_cpu_energy_performance", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_cpu_energy_performance = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfCPUEnergyPerformance", parent_mo_or_dn, **kwargs)

