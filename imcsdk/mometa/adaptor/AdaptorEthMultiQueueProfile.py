"""This module contains the general information for AdaptorEthMultiQueueProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorEthMultiQueueProfileConsts:
    MULTI_QUEUE_CLASS_OF_SERVICE_0 = "0"
    MULTI_QUEUE_CLASS_OF_SERVICE_1 = "1"
    MULTI_QUEUE_CLASS_OF_SERVICE_2 = "2"
    MULTI_QUEUE_CLASS_OF_SERVICE_4 = "4"
    MULTI_QUEUE_CLASS_OF_SERVICE_5 = "5"
    MULTI_QUEUE_CLASS_OF_SERVICE_6 = "6"


class AdaptorEthMultiQueueProfile(ManagedObject):
    """This is AdaptorEthMultiQueueProfile class."""

    consts = AdaptorEthMultiQueueProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorEthMultiQueueProfile", "adaptorEthMultiQueueProfile", "eth-multi-q", VersionMeta.Version402c, "InputOutput", 0x7ff, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], [None]),
        "modular": MoMeta("AdaptorEthMultiQueueProfile", "adaptorEthMultiQueueProfile", "eth-multi-q", VersionMeta.Version404b, "InputOutput", 0x7ff, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], [None])
    }


    prop_meta = {

        "classic": {
            "completion_count": MoPropertyMeta("completion_count", "completionCount", "uint", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-2000", "1-2000"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "multi_queue_memory_regions": MoPropertyMeta("multi_queue_memory_regions", "multiQueueMemoryRegions", "uint", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-524288"]),
            "multi_queue_pairs": MoPropertyMeta("multi_queue_pairs", "multiQueuePairs", "uint", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-8192"]),
            "multi_queue_resource_groups": MoPropertyMeta("multi_queue_resource_groups", "multiQueueResourceGroups", "uint", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-128"]),
            "multi_queue_roce_version2": MoPropertyMeta("multi_queue_roce_version2", "multiQueueRoceVersion2", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "receive_count": MoPropertyMeta("receive_count", "receiveCount", "uint", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["0-1000", "1-1000"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "transmit_count": MoPropertyMeta("transmit_count", "transmitCount", "uint", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], ["0-1000", "1-1000"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version402c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "multi_queue_class_of_service": MoPropertyMeta("multi_queue_class_of_service", "multiQueueClassOfService", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["0", "1", "2", "4", "5", "6"], []),
            "multi_queue_roce_version1": MoPropertyMeta("multi_queue_roce_version1", "multiQueueRoceVersion1", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
        },

        "modular": {
            "completion_count": MoPropertyMeta("completion_count", "completionCount", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-2000", "1-2000"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "multi_queue_memory_regions": MoPropertyMeta("multi_queue_memory_regions", "multiQueueMemoryRegions", "uint", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-524288"]),
            "multi_queue_pairs": MoPropertyMeta("multi_queue_pairs", "multiQueuePairs", "uint", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-8192"]),
            "multi_queue_resource_groups": MoPropertyMeta("multi_queue_resource_groups", "multiQueueResourceGroups", "uint", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-128"]),
            "multi_queue_roce_version2": MoPropertyMeta("multi_queue_roce_version2", "multiQueueRoceVersion2", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "receive_count": MoPropertyMeta("receive_count", "receiveCount", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["0-1000", "1-1000"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "transmit_count": MoPropertyMeta("transmit_count", "transmitCount", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], ["0-1000", "1-1000"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "multi_queue_class_of_service": MoPropertyMeta("multi_queue_class_of_service", "multiQueueClassOfService", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["0", "1", "2", "4", "5", "6"], []),
            "multi_queue_roce_version1": MoPropertyMeta("multi_queue_roce_version1", "multiQueueRoceVersion1", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
        },

    }

    prop_map = {

        "classic": {
            "completionCount": "completion_count", 
            "dn": "dn", 
            "multiQueueMemoryRegions": "multi_queue_memory_regions", 
            "multiQueuePairs": "multi_queue_pairs", 
            "multiQueueResourceGroups": "multi_queue_resource_groups", 
            "multiQueueRoceVersion2": "multi_queue_roce_version2", 
            "receiveCount": "receive_count", 
            "rn": "rn", 
            "status": "status", 
            "transmitCount": "transmit_count", 
            "childAction": "child_action", 
            "multiQueueClassOfService": "multi_queue_class_of_service", 
            "multiQueueRoceVersion1": "multi_queue_roce_version1", 
        },

        "modular": {
            "completionCount": "completion_count", 
            "dn": "dn", 
            "multiQueueMemoryRegions": "multi_queue_memory_regions", 
            "multiQueuePairs": "multi_queue_pairs", 
            "multiQueueResourceGroups": "multi_queue_resource_groups", 
            "multiQueueRoceVersion2": "multi_queue_roce_version2", 
            "receiveCount": "receive_count", 
            "rn": "rn", 
            "status": "status", 
            "transmitCount": "transmit_count", 
            "childAction": "child_action", 
            "multiQueueClassOfService": "multi_queue_class_of_service", 
            "multiQueueRoceVersion1": "multi_queue_roce_version1", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.completion_count = None
        self.multi_queue_memory_regions = None
        self.multi_queue_pairs = None
        self.multi_queue_resource_groups = None
        self.multi_queue_roce_version2 = None
        self.receive_count = None
        self.status = None
        self.transmit_count = None
        self.child_action = None
        self.multi_queue_class_of_service = None
        self.multi_queue_roce_version1 = None

        ManagedObject.__init__(self, "AdaptorEthMultiQueueProfile", parent_mo_or_dn, **kwargs)

