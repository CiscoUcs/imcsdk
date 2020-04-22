"""This module contains the general information for ServerUtilization ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class ServerUtilizationConsts:
    pass


class ServerUtilization(ManagedObject):
    """This is ServerUtilization class."""

    consts = ServerUtilizationConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("ServerUtilization", "serverUtilization", "utilization", VersionMeta.Version202c, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['computeRackUnit'], [], ["Get"]),
        "modular": MoMeta("ServerUtilization", "serverUtilization", "utilization", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['computeServerNode'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "cpu_utilization": MoPropertyMeta("cpu_utilization", "cpuUtilization", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "io_utilization": MoPropertyMeta("io_utilization", "ioUtilization", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "memory_utilization": MoPropertyMeta("memory_utilization", "memoryUtilization", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "overall_utilization": MoPropertyMeta("overall_utilization", "overallUtilization", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "cpu_utilization": MoPropertyMeta("cpu_utilization", "cpuUtilization", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "io_utilization": MoPropertyMeta("io_utilization", "ioUtilization", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "memory_utilization": MoPropertyMeta("memory_utilization", "memoryUtilization", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "overall_utilization": MoPropertyMeta("overall_utilization", "overallUtilization", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "cpuUtilization": "cpu_utilization", 
            "dn": "dn", 
            "ioUtilization": "io_utilization", 
            "memoryUtilization": "memory_utilization", 
            "overallUtilization": "overall_utilization", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "cpuUtilization": "cpu_utilization", 
            "dn": "dn", 
            "ioUtilization": "io_utilization", 
            "memoryUtilization": "memory_utilization", 
            "overallUtilization": "overall_utilization", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.cpu_utilization = None
        self.io_utilization = None
        self.memory_utilization = None
        self.overall_utilization = None
        self.status = None

        ManagedObject.__init__(self, "ServerUtilization", parent_mo_or_dn, **kwargs)

