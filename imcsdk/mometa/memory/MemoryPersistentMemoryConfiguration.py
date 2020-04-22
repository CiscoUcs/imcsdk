"""This module contains the general information for MemoryPersistentMemoryConfiguration ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MemoryPersistentMemoryConfigurationConsts:
    NUM_OF_DIMMS_UNSPECIFIED = "unspecified"
    NUM_OF_REGIONS_UNSPECIFIED = "unspecified"


class MemoryPersistentMemoryConfiguration(ManagedObject):
    """This is MemoryPersistentMemoryConfiguration class."""

    consts = MemoryPersistentMemoryConfigurationConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("MemoryPersistentMemoryConfiguration", "memoryPersistentMemoryConfiguration", "pmemory-config", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['computeBoard'], ['memoryPersistentMemoryBackup', 'memoryPersistentMemoryConfigResult', 'memoryPersistentMemoryImporter', 'memoryPersistentMemoryRegion'], [None]),
        "modular": MoMeta("MemoryPersistentMemoryConfiguration", "memoryPersistentMemoryConfiguration", "pmemory-config", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['computeBoard'], ['memoryPersistentMemoryBackup', 'memoryPersistentMemoryConfigResult', 'memoryPersistentMemoryImporter', 'memoryPersistentMemoryRegion'], [None])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "memory_capacity": MoPropertyMeta("memory_capacity", "memoryCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_dimms": MoPropertyMeta("num_of_dimms", "numOfDimms", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "num_of_regions": MoPropertyMeta("num_of_regions", "numOfRegions", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "persistent_memory_capacity": MoPropertyMeta("persistent_memory_capacity", "persistentMemoryCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "reserved_capacity": MoPropertyMeta("reserved_capacity", "reservedCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "security_state": MoPropertyMeta("security_state", "securityState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "total_capacity": MoPropertyMeta("total_capacity", "totalCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "memory_capacity": MoPropertyMeta("memory_capacity", "memoryCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_dimms": MoPropertyMeta("num_of_dimms", "numOfDimms", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "num_of_regions": MoPropertyMeta("num_of_regions", "numOfRegions", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "persistent_memory_capacity": MoPropertyMeta("persistent_memory_capacity", "persistentMemoryCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "reserved_capacity": MoPropertyMeta("reserved_capacity", "reservedCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "security_state": MoPropertyMeta("security_state", "securityState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "total_capacity": MoPropertyMeta("total_capacity", "totalCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "configState": "config_state", 
            "dn": "dn", 
            "memoryCapacity": "memory_capacity", 
            "numOfDimms": "num_of_dimms", 
            "numOfRegions": "num_of_regions", 
            "persistentMemoryCapacity": "persistent_memory_capacity", 
            "reservedCapacity": "reserved_capacity", 
            "rn": "rn", 
            "securityState": "security_state", 
            "status": "status", 
            "totalCapacity": "total_capacity", 
        },

        "modular": {
            "childAction": "child_action", 
            "configState": "config_state", 
            "dn": "dn", 
            "memoryCapacity": "memory_capacity", 
            "numOfDimms": "num_of_dimms", 
            "numOfRegions": "num_of_regions", 
            "persistentMemoryCapacity": "persistent_memory_capacity", 
            "reservedCapacity": "reserved_capacity", 
            "rn": "rn", 
            "securityState": "security_state", 
            "status": "status", 
            "totalCapacity": "total_capacity", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_state = None
        self.memory_capacity = None
        self.num_of_dimms = None
        self.num_of_regions = None
        self.persistent_memory_capacity = None
        self.reserved_capacity = None
        self.security_state = None
        self.status = None
        self.total_capacity = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryConfiguration", parent_mo_or_dn, **kwargs)

