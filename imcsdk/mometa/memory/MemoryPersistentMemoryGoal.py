"""This module contains the general information for MemoryPersistentMemoryGoal ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MemoryPersistentMemoryGoalConsts:
    PERSISTENT_MEMORY_TYPE_APP_DIRECT = "app-direct"
    PERSISTENT_MEMORY_TYPE_APP_DIRECT_NON_INTERLEAVED = "app-direct-non-interleaved"
    SOCKET_ID_ALL = "ALL"


class MemoryPersistentMemoryGoal(ManagedObject):
    """This is MemoryPersistentMemoryGoal class."""

    consts = MemoryPersistentMemoryGoalConsts()
    naming_props = set(['socketId'])

    mo_meta = {
        "classic": MoMeta("MemoryPersistentMemoryGoal", "memoryPersistentMemoryGoal", "goal-[socket_id]", VersionMeta.Version404b, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryLogicalConfiguration'], [], [None]),
        "modular": MoMeta("MemoryPersistentMemoryGoal", "memoryPersistentMemoryGoal", "goal-[socket_id]", VersionMeta.Version404b, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryLogicalConfiguration'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "memory_mode_percentage": MoPropertyMeta("memory_mode_percentage", "memoryModePercentage", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["0-100"]),
            "persistent_memory_type": MoPropertyMeta("persistent_memory_type", "persistentMemoryType", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["app-direct", "app-direct-non-interleaved"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404b, MoPropertyMeta.NAMING, 0x20, None, None, None, ["ALL"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "memory_mode_percentage": MoPropertyMeta("memory_mode_percentage", "memoryModePercentage", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["0-100"]),
            "persistent_memory_type": MoPropertyMeta("persistent_memory_type", "persistentMemoryType", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["app-direct", "app-direct-non-interleaved"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404b, MoPropertyMeta.NAMING, 0x20, None, None, None, ["ALL"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "memoryModePercentage": "memory_mode_percentage", 
            "persistentMemoryType": "persistent_memory_type", 
            "rn": "rn", 
            "socketId": "socket_id", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "memoryModePercentage": "memory_mode_percentage", 
            "persistentMemoryType": "persistent_memory_type", 
            "rn": "rn", 
            "socketId": "socket_id", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, socket_id, **kwargs):
        self._dirty_mask = 0
        self.socket_id = socket_id
        self.memory_mode_percentage = None
        self.persistent_memory_type = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryGoal", parent_mo_or_dn, **kwargs)

