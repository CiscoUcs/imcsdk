"""This module contains the general information for MemoryPersistentMemoryDimms ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MemoryPersistentMemoryDimmsConsts:
    SOCKET_ID_1 = "1"
    SOCKET_ID_2 = "2"
    SOCKET_ID_3 = "3"
    SOCKET_ID_4 = "4"
    SOCKET_ID_ALL = "ALL"


class MemoryPersistentMemoryDimms(ManagedObject):
    """This is MemoryPersistentMemoryDimms class."""

    consts = MemoryPersistentMemoryDimmsConsts()
    naming_props = set(['socketId'])

    mo_meta = {
        "classic": MoMeta("MemoryPersistentMemoryDimms", "memoryPersistentMemoryDimms", "pmemory-dimms-[socket_id]", VersionMeta.Version404b, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryLogicalConfiguration'], [], [None]),
        "modular": MoMeta("MemoryPersistentMemoryDimms", "memoryPersistentMemoryDimms", "pmemory-dimms-[socket_id]", VersionMeta.Version404b, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryLogicalConfiguration'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404b, MoPropertyMeta.NAMING, 0x8, 0, 510, None, ["1", "2", "3", "4", "ALL"], []),
            "socket_local_dimm_numbers": MoPropertyMeta("socket_local_dimm_numbers", "socketLocalDimmNumbers", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404b, MoPropertyMeta.NAMING, 0x8, 0, 510, None, ["1", "2", "3", "4", "ALL"], []),
            "socket_local_dimm_numbers": MoPropertyMeta("socket_local_dimm_numbers", "socketLocalDimmNumbers", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "socketId": "socket_id", 
            "socketLocalDimmNumbers": "socket_local_dimm_numbers", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "socketId": "socket_id", 
            "socketLocalDimmNumbers": "socket_local_dimm_numbers", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, socket_id, **kwargs):
        self._dirty_mask = 0
        self.socket_id = socket_id
        self.socket_local_dimm_numbers = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryDimms", parent_mo_or_dn, **kwargs)

