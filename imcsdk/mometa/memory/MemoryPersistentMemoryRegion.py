"""This module contains the general information for MemoryPersistentMemoryRegion ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MemoryPersistentMemoryRegionConsts:
    HEALTH_STATE_CRITICAL_FAILURE = "CriticalFailure"
    HEALTH_STATE_HEALTHY = "Healthy"
    HEALTH_STATE_MINOR_FAILURE = "MinorFailure"
    HEALTH_STATE_NON_FUNCTIONAL = "NonFunctional"
    HEALTH_STATE_UNKNOWN = "Unknown"
    HEALTH_STATE_UNMANAGABLE = "Unmanagable"
    HEALTH_STATE_UNRECOVERABLE_ERROR = "UnrecoverableError"
    ID_UNSPECIFIED = "unspecified"
    SOCKET_ID_1 = "1"
    SOCKET_ID_2 = "2"
    SOCKET_ID_3 = "3"
    SOCKET_ID_4 = "4"
    SOCKET_LOCAL_DIMM_NUMBER_10 = "10"
    SOCKET_LOCAL_DIMM_NUMBER_11 = "11"
    SOCKET_LOCAL_DIMM_NUMBER_12 = "12"
    SOCKET_LOCAL_DIMM_NUMBER_14 = "14"
    SOCKET_LOCAL_DIMM_NUMBER_15 = "15"
    SOCKET_LOCAL_DIMM_NUMBER_16 = "16"
    SOCKET_LOCAL_DIMM_NUMBER_2 = "2"
    SOCKET_LOCAL_DIMM_NUMBER_3 = "3"
    SOCKET_LOCAL_DIMM_NUMBER_4 = "4"
    SOCKET_LOCAL_DIMM_NUMBER_6 = "6"
    SOCKET_LOCAL_DIMM_NUMBER_7 = "7"
    SOCKET_LOCAL_DIMM_NUMBER_8 = "8"
    SOCKET_LOCAL_DIMM_NUMBER_NOT_APPLICABLE = "Not applicable"


class MemoryPersistentMemoryRegion(ManagedObject):
    """This is MemoryPersistentMemoryRegion class."""

    consts = MemoryPersistentMemoryRegionConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("MemoryPersistentMemoryRegion", "memoryPersistentMemoryRegion", "region-[id]", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryConfiguration'], ['memoryPersistentMemoryNamespace'], [None]),
        "modular": MoMeta("MemoryPersistentMemoryRegion", "memoryPersistentMemoryRegion", "region-[id]", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryConfiguration'], ['memoryPersistentMemoryNamespace'], [None])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dimm_locator_ids": MoPropertyMeta("dimm_locator_ids", "dimmLocatorIds", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "free_capacity": MoPropertyMeta("free_capacity", "freeCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "health_state": MoPropertyMeta("health_state", "healthState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["CriticalFailure", "Healthy", "MinorFailure", "NonFunctional", "Unknown", "Unmanagable", "UnrecoverableError"], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version404b, MoPropertyMeta.NAMING, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "interleaved_set_id": MoPropertyMeta("interleaved_set_id", "interleavedSetId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "persistent_memory_type": MoPropertyMeta("persistent_memory_type", "persistentMemoryType", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "3", "4"], []),
            "socket_local_dimm_number": MoPropertyMeta("socket_local_dimm_number", "socketLocalDimmNumber", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["10", "11", "12", "14", "15", "16", "2", "3", "4", "6", "7", "8", "Not applicable"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "total_capacity": MoPropertyMeta("total_capacity", "totalCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dimm_locator_ids": MoPropertyMeta("dimm_locator_ids", "dimmLocatorIds", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "free_capacity": MoPropertyMeta("free_capacity", "freeCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "health_state": MoPropertyMeta("health_state", "healthState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["CriticalFailure", "Healthy", "MinorFailure", "NonFunctional", "Unknown", "Unmanagable", "UnrecoverableError"], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version404b, MoPropertyMeta.NAMING, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "interleaved_set_id": MoPropertyMeta("interleaved_set_id", "interleavedSetId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "persistent_memory_type": MoPropertyMeta("persistent_memory_type", "persistentMemoryType", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "3", "4"], []),
            "socket_local_dimm_number": MoPropertyMeta("socket_local_dimm_number", "socketLocalDimmNumber", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["10", "12", "2", "4", "6", "8", "Not applicable"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "total_capacity": MoPropertyMeta("total_capacity", "totalCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dimmLocatorIds": "dimm_locator_ids", 
            "dn": "dn", 
            "freeCapacity": "free_capacity", 
            "healthState": "health_state", 
            "id": "id", 
            "interleavedSetId": "interleaved_set_id", 
            "persistentMemoryType": "persistent_memory_type", 
            "rn": "rn", 
            "socketId": "socket_id", 
            "socketLocalDimmNumber": "socket_local_dimm_number", 
            "status": "status", 
            "totalCapacity": "total_capacity", 
        },

        "modular": {
            "childAction": "child_action", 
            "dimmLocatorIds": "dimm_locator_ids", 
            "dn": "dn", 
            "freeCapacity": "free_capacity", 
            "healthState": "health_state", 
            "id": "id", 
            "interleavedSetId": "interleaved_set_id", 
            "persistentMemoryType": "persistent_memory_type", 
            "rn": "rn", 
            "socketId": "socket_id", 
            "socketLocalDimmNumber": "socket_local_dimm_number", 
            "status": "status", 
            "totalCapacity": "total_capacity", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.dimm_locator_ids = None
        self.free_capacity = None
        self.health_state = None
        self.interleaved_set_id = None
        self.persistent_memory_type = None
        self.socket_id = None
        self.socket_local_dimm_number = None
        self.status = None
        self.total_capacity = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryRegion", parent_mo_or_dn, **kwargs)

