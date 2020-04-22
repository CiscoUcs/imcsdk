"""This module contains the general information for MemoryPersistentMemoryNamespace ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MemoryPersistentMemoryNamespaceConsts:
    HEALTH_STATE_CRITICAL_FAILURE = "CriticalFailure"
    HEALTH_STATE_HEALTHY = "Healthy"
    HEALTH_STATE_MINOR_FAILURE = "MinorFailure"
    HEALTH_STATE_NON_FUNCTIONAL = "NonFunctional"
    HEALTH_STATE_UNKNOWN = "Unknown"
    HEALTH_STATE_UNMANAGABLE = "Unmanagable"
    HEALTH_STATE_UNRECOVERABLE_ERROR = "UnrecoverableError"
    OPER_MODE_BLOCK = "block"
    OPER_MODE_RAW = "raw"


class MemoryPersistentMemoryNamespace(ManagedObject):
    """This is MemoryPersistentMemoryNamespace class."""

    consts = MemoryPersistentMemoryNamespaceConsts()
    naming_props = set(['uuid'])

    mo_meta = {
        "classic": MoMeta("MemoryPersistentMemoryNamespace", "memoryPersistentMemoryNamespace", "ns-[uuid]", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryRegion'], [], [None]),
        "modular": MoMeta("MemoryPersistentMemoryNamespace", "memoryPersistentMemoryNamespace", "ns-[uuid]", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryRegion'], [], [None])
    }


    prop_meta = {

        "classic": {
            "capacity": MoPropertyMeta("capacity", "capacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "health_state": MoPropertyMeta("health_state", "healthState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["CriticalFailure", "Healthy", "MinorFailure", "NonFunctional", "Unknown", "Unmanagable", "UnrecoverableError"], []),
            "label_version": MoPropertyMeta("label_version", "labelVersion", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "oper_mode": MoPropertyMeta("oper_mode", "operMode", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["block", "raw"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version404b, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
        },

        "modular": {
            "capacity": MoPropertyMeta("capacity", "capacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "health_state": MoPropertyMeta("health_state", "healthState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["CriticalFailure", "Healthy", "MinorFailure", "NonFunctional", "Unknown", "Unmanagable", "UnrecoverableError"], []),
            "label_version": MoPropertyMeta("label_version", "labelVersion", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "oper_mode": MoPropertyMeta("oper_mode", "operMode", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["block", "raw"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version404b, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "capacity": "capacity", 
            "childAction": "child_action", 
            "dn": "dn", 
            "healthState": "health_state", 
            "labelVersion": "label_version", 
            "name": "name", 
            "operMode": "oper_mode", 
            "rn": "rn", 
            "status": "status", 
            "uuid": "uuid", 
        },

        "modular": {
            "capacity": "capacity", 
            "childAction": "child_action", 
            "dn": "dn", 
            "healthState": "health_state", 
            "labelVersion": "label_version", 
            "name": "name", 
            "operMode": "oper_mode", 
            "rn": "rn", 
            "status": "status", 
            "uuid": "uuid", 
        },

    }

    def __init__(self, parent_mo_or_dn, uuid, **kwargs):
        self._dirty_mask = 0
        self.uuid = uuid
        self.capacity = None
        self.child_action = None
        self.health_state = None
        self.label_version = None
        self.name = None
        self.oper_mode = None
        self.status = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryNamespace", parent_mo_or_dn, **kwargs)

