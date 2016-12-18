"""This module contains the general information for BiosVfCPUPerformance ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCPUPerformanceConsts:
    VP_CPUPERFORMANCE_CUSTOM = "custom"
    VP_CPUPERFORMANCE_ENTERPRISE = "enterprise"
    VP_CPUPERFORMANCE_HIGH_THROUGHPUT = "high-throughput"
    VP_CPUPERFORMANCE_HPC = "hpc"
    VP_CPUPERFORMANCE_PLATFORM_DEFAULT = "platform-default"


class BiosVfCPUPerformance(ManagedObject):
    """This is BiosVfCPUPerformance class."""

    consts = BiosVfCPUPerformanceConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCPUPerformance", "biosVfCPUPerformance", "CPU-Performance", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfCPUPerformance", "biosVfCPUPerformance", "CPU-Performance", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_cpu_performance": MoPropertyMeta("vp_cpu_performance", "vpCPUPerformance", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["custom", "enterprise", "high-throughput", "hpc", "platform-default"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_cpu_performance": MoPropertyMeta("vp_cpu_performance", "vpCPUPerformance", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["custom", "enterprise", "high-throughput", "hpc", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCPUPerformance": "vp_cpu_performance", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCPUPerformance": "vp_cpu_performance", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cpu_performance = None

        ManagedObject.__init__(self, "BiosVfCPUPerformance", parent_mo_or_dn, **kwargs)

