"""This module contains the general information for MemoryArray ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MemoryArrayConsts:
    CURR_CAPACITY_UNSPECIFIED = "unspecified"
    DIMM_BLACK_LIST_DISABLED = "Disabled"
    DIMM_BLACK_LIST_ENABLED = "Enabled"
    DIMM_BLACK_LIST_DISABLE = "disable"
    _DIMM_BLACK_LIST_DISABLED = "disabled"
    DIMM_BLACK_LIST_ENABLE = "enable"
    _DIMM_BLACK_LIST_ENABLED = "enabled"
    FAILED_MEMORY_UNSPECIFIED = "unspecified"
    IGNORED_MEMORY_UNSPECIFIED = "unspecified"
    MAX_DEVICES_UNSPECIFIED = "unspecified"
    OVERALL_DIMMSTATUS_AMBER = "amber"
    OVERALL_DIMMSTATUS_BLUE = "blue"
    OVERALL_DIMMSTATUS_GREEN = "green"
    OVERALL_DIMMSTATUS_RED = "red"
    OVERALL_DIMMSTATUS_UNKNOWN = "unknown"
    POPULATED_UNSPECIFIED = "unspecified"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    PRESENCE_INACCESSIBLE = "inaccessible"
    PRESENCE_MISMATCH = "mismatch"
    PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    PRESENCE_MISSING = "missing"
    PRESENCE_NOT_SUPPORTED = "not-supported"
    PRESENCE_UNAUTHORIZED = "unauthorized"
    PRESENCE_UNKNOWN = "unknown"
    REDUNDANT_MEMORY_UNSPECIFIED = "unspecified"


class MemoryArray(ManagedObject):
    """This is MemoryArray class."""

    consts = MemoryArrayConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("MemoryArray", "memoryArray", "memarray-[id]", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['computeBoard'], ['faultInst', 'memoryPersistentMemoryUnit', 'memoryUnit'], ["Get", "Set"]),
        "modular": MoMeta("MemoryArray", "memoryArray", "memarray-[id]", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['computeBoard'], ['faultInst', 'memoryPersistentMemoryUnit', 'memoryUnit'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dimm_black_list": MoPropertyMeta("dimm_black_list", "dimmBlackList", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disable", "disabled", "enable", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "curr_capacity": MoPropertyMeta("curr_capacity", "currCapacity", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "failed_memory": MoPropertyMeta("failed_memory", "failedMemory", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["1-8"]),
            "ignored_memory": MoPropertyMeta("ignored_memory", "ignoredMemory", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "max_devices": MoPropertyMeta("max_devices", "maxDevices", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "memory_configuration": MoPropertyMeta("memory_configuration", "memoryConfiguration", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "memory_ras_possible": MoPropertyMeta("memory_ras_possible", "memoryRASPossible", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "num_of_failed_dimms": MoPropertyMeta("num_of_failed_dimms", "numOfFailedDimms", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "num_of_ignored_dimms": MoPropertyMeta("num_of_ignored_dimms", "numOfIgnoredDimms", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "overall_dimm_status": MoPropertyMeta("overall_dimm_status", "overallDIMMStatus", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["amber", "blue", "green", "red", "unknown"], []),
            "populated": MoPropertyMeta("populated", "populated", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], []),
            "redundant_memory": MoPropertyMeta("redundant_memory", "redundantMemory", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
        },

        "modular": {
            "dimm_black_list": MoPropertyMeta("dimm_black_list", "dimmBlackList", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disable", "disabled", "enable", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "curr_capacity": MoPropertyMeta("curr_capacity", "currCapacity", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "failed_memory": MoPropertyMeta("failed_memory", "failedMemory", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], ["1-8"]),
            "ignored_memory": MoPropertyMeta("ignored_memory", "ignoredMemory", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "max_devices": MoPropertyMeta("max_devices", "maxDevices", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "memory_configuration": MoPropertyMeta("memory_configuration", "memoryConfiguration", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "memory_ras_possible": MoPropertyMeta("memory_ras_possible", "memoryRASPossible", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "num_of_failed_dimms": MoPropertyMeta("num_of_failed_dimms", "numOfFailedDimms", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "num_of_ignored_dimms": MoPropertyMeta("num_of_ignored_dimms", "numOfIgnoredDimms", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "overall_dimm_status": MoPropertyMeta("overall_dimm_status", "overallDIMMStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["amber", "blue", "green", "red", "unknown"], []),
            "populated": MoPropertyMeta("populated", "populated", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], []),
            "redundant_memory": MoPropertyMeta("redundant_memory", "redundantMemory", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
        },

    }

    prop_map = {

        "classic": {
            "dimmBlackList": "dimm_black_list", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "currCapacity": "curr_capacity", 
            "failedMemory": "failed_memory", 
            "id": "id", 
            "ignoredMemory": "ignored_memory", 
            "maxDevices": "max_devices", 
            "memoryConfiguration": "memory_configuration", 
            "memoryRASPossible": "memory_ras_possible", 
            "numOfFailedDimms": "num_of_failed_dimms", 
            "numOfIgnoredDimms": "num_of_ignored_dimms", 
            "overallDIMMStatus": "overall_dimm_status", 
            "populated": "populated", 
            "presence": "presence", 
            "redundantMemory": "redundant_memory", 
        },

        "modular": {
            "dimmBlackList": "dimm_black_list", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "currCapacity": "curr_capacity", 
            "failedMemory": "failed_memory", 
            "id": "id", 
            "ignoredMemory": "ignored_memory", 
            "maxDevices": "max_devices", 
            "memoryConfiguration": "memory_configuration", 
            "memoryRASPossible": "memory_ras_possible", 
            "numOfFailedDimms": "num_of_failed_dimms", 
            "numOfIgnoredDimms": "num_of_ignored_dimms", 
            "overallDIMMStatus": "overall_dimm_status", 
            "populated": "populated", 
            "presence": "presence", 
            "redundantMemory": "redundant_memory", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.dimm_black_list = None
        self.status = None
        self.child_action = None
        self.curr_capacity = None
        self.failed_memory = None
        self.ignored_memory = None
        self.max_devices = None
        self.memory_configuration = None
        self.memory_ras_possible = None
        self.num_of_failed_dimms = None
        self.num_of_ignored_dimms = None
        self.overall_dimm_status = None
        self.populated = None
        self.presence = None
        self.redundant_memory = None

        ManagedObject.__init__(self, "MemoryArray", parent_mo_or_dn, **kwargs)

