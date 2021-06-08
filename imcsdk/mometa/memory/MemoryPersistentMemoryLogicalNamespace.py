"""This module contains the general information for MemoryPersistentMemoryLogicalNamespace ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MemoryPersistentMemoryLogicalNamespaceConsts:
    CAPACITY_REMAINING_CAPACITY = "remaining-capacity"
    MODE_BLOCK = "block"
    MODE_RAW = "raw"
    SOCKET_ID_1 = "1"
    SOCKET_ID_2 = "2"
    SOCKET_ID_3 = "3"
    SOCKET_ID_4 = "4"
    SOCKET_LOCAL_DIMM_NUMBER_0 = "0"
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


class MemoryPersistentMemoryLogicalNamespace(ManagedObject):
    """This is MemoryPersistentMemoryLogicalNamespace class."""

    consts = MemoryPersistentMemoryLogicalNamespaceConsts()
    naming_props = set(['name'])

    mo_meta = {
        "classic": MoMeta("MemoryPersistentMemoryLogicalNamespace", "memoryPersistentMemoryLogicalNamespace", "lns-[name]", VersionMeta.Version404b, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryLogicalConfiguration'], [], [None]),
        "modular": MoMeta("MemoryPersistentMemoryLogicalNamespace", "memoryPersistentMemoryLogicalNamespace", "lns-[name]", VersionMeta.Version404b, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryLogicalConfiguration'], [], [None])
    }


    prop_meta = {

        "classic": {
            "capacity": MoPropertyMeta("capacity", "capacity", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["remaining-capacity"], ["1-49152"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["block", "raw"], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version404b, MoPropertyMeta.NAMING, 0x10, None, None, r"""(([a-zA-Z0-9_\-#]{1})|([a-zA-Z0-9_\-#]{1}[a-zA-Z0-9 _\-#]{0,61}[a-zA-Z0-9_\-#]{1})|([a-zA-Z0-9_\-#]{2}))""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["1", "2", "3", "4"], []),
            "socket_local_dimm_number": MoPropertyMeta("socket_local_dimm_number", "socketLocalDimmNumber", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["0", "10", "11", "12", "14", "15", "16", "2", "3", "4", "6", "7", "8", "Not applicable"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "capacity": MoPropertyMeta("capacity", "capacity", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["remaining-capacity"], ["1-49152"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["block", "raw"], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version404b, MoPropertyMeta.NAMING, 0x10, None, None, r"""(([a-zA-Z0-9_\-#]{1})|([a-zA-Z0-9_\-#]{1}[a-zA-Z0-9 _\-#]{0,61}[a-zA-Z0-9_\-#]{1})|([a-zA-Z0-9_\-#]{2}))""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["1", "2", "3", "4"], []),
            "socket_local_dimm_number": MoPropertyMeta("socket_local_dimm_number", "socketLocalDimmNumber", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["0", "10", "12", "2", "4", "6", "8", "Not applicable"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "capacity": "capacity", 
            "dn": "dn", 
            "mode": "mode", 
            "name": "name", 
            "rn": "rn", 
            "socketId": "socket_id", 
            "socketLocalDimmNumber": "socket_local_dimm_number", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "capacity": "capacity", 
            "dn": "dn", 
            "mode": "mode", 
            "name": "name", 
            "rn": "rn", 
            "socketId": "socket_id", 
            "socketLocalDimmNumber": "socket_local_dimm_number", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.capacity = None
        self.mode = None
        self.socket_id = None
        self.socket_local_dimm_number = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryLogicalNamespace", parent_mo_or_dn, **kwargs)

