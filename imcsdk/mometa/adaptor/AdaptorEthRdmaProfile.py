"""This module contains the general information for AdaptorEthRdmaProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorEthRdmaProfileConsts:
    RDMA_CLASS_OF_SERVICE_0 = "0"
    RDMA_CLASS_OF_SERVICE_1 = "1"
    RDMA_CLASS_OF_SERVICE_2 = "2"
    RDMA_CLASS_OF_SERVICE_4 = "4"
    RDMA_CLASS_OF_SERVICE_5 = "5"
    RDMA_CLASS_OF_SERVICE_6 = "6"


class AdaptorEthRdmaProfile(ManagedObject):
    """This is AdaptorEthRdmaProfile class."""

    consts = AdaptorEthRdmaProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorEthRdmaProfile", "adaptorEthRdmaProfile", "rdmaprofile", VersionMeta.Version2013e, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorEthRdmaProfile", "adaptorEthRdmaProfile", "rdmaprofile", VersionMeta.Version2013e, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "memory_regions": MoPropertyMeta("memory_regions", "memoryRegions", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["0-524288"]),
            "queue_pairs": MoPropertyMeta("queue_pairs", "queuePairs", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-8192"]),
            "rdma_class_of_service": MoPropertyMeta("rdma_class_of_service", "rdmaClassOfService", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["0", "1", "2", "4", "5", "6"], []),
            "resource_groups": MoPropertyMeta("resource_groups", "resourceGroups", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-128"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "roce_version2": MoPropertyMeta("roce_version2", "roceVersion2", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "roce_version1": MoPropertyMeta("roce_version1", "roceVersion1", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "memory_regions": MoPropertyMeta("memory_regions", "memoryRegions", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["0-524288"]),
            "queue_pairs": MoPropertyMeta("queue_pairs", "queuePairs", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-8192"]),
            "rdma_class_of_service": MoPropertyMeta("rdma_class_of_service", "rdmaClassOfService", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["0", "1", "2", "4", "5", "6"], []),
            "resource_groups": MoPropertyMeta("resource_groups", "resourceGroups", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-128"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "roce_version2": MoPropertyMeta("roce_version2", "roceVersion2", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "roce_version1": MoPropertyMeta("roce_version1", "roceVersion1", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "memoryRegions": "memory_regions", 
            "queuePairs": "queue_pairs", 
            "rdmaClassOfService": "rdma_class_of_service", 
            "resourceGroups": "resource_groups", 
            "rn": "rn", 
            "roceVersion2": "roce_version2", 
            "status": "status", 
            "childAction": "child_action", 
            "roceVersion1": "roce_version1", 
        },

        "modular": {
            "dn": "dn", 
            "memoryRegions": "memory_regions", 
            "queuePairs": "queue_pairs", 
            "rdmaClassOfService": "rdma_class_of_service", 
            "resourceGroups": "resource_groups", 
            "rn": "rn", 
            "roceVersion2": "roce_version2", 
            "status": "status", 
            "childAction": "child_action", 
            "roceVersion1": "roce_version1", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.memory_regions = None
        self.queue_pairs = None
        self.rdma_class_of_service = None
        self.resource_groups = None
        self.roce_version2 = None
        self.status = None
        self.child_action = None
        self.roce_version1 = None

        ManagedObject.__init__(self, "AdaptorEthRdmaProfile", parent_mo_or_dn, **kwargs)

