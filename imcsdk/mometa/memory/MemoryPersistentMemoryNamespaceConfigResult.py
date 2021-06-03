"""This module contains the general information for MemoryPersistentMemoryNamespaceConfigResult ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MemoryPersistentMemoryNamespaceConfigResultConsts:
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


class MemoryPersistentMemoryNamespaceConfigResult(ManagedObject):
    """This is MemoryPersistentMemoryNamespaceConfigResult class."""

    consts = MemoryPersistentMemoryNamespaceConfigResultConsts()
    naming_props = set(['name'])

    mo_meta = {
        "classic": MoMeta("MemoryPersistentMemoryNamespaceConfigResult", "memoryPersistentMemoryNamespaceConfigResult", "nscr-[name]", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryConfigResult'], [], [None]),
        "modular": MoMeta("MemoryPersistentMemoryNamespaceConfigResult", "memoryPersistentMemoryNamespaceConfigResult", "nscr-[name]", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryConfigResult'], [], [None])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "config_status": MoPropertyMeta("config_status", "configStatus", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version404b, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "3", "4"], []),
            "socket_local_dimm_number": MoPropertyMeta("socket_local_dimm_number", "socketLocalDimmNumber", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["10", "11", "12", "14", "15", "16", "2", "3", "4", "6", "7", "8", "Not applicable"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "config_status": MoPropertyMeta("config_status", "configStatus", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version404b, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "3", "4"], []),
            "socket_local_dimm_number": MoPropertyMeta("socket_local_dimm_number", "socketLocalDimmNumber", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["10", "12", "2", "4", "6", "8", "Not applicable"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "configStatus": "config_status", 
            "dn": "dn", 
            "name": "name", 
            "rn": "rn", 
            "socketId": "socket_id", 
            "socketLocalDimmNumber": "socket_local_dimm_number", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "configStatus": "config_status", 
            "dn": "dn", 
            "name": "name", 
            "rn": "rn", 
            "socketId": "socket_id", 
            "socketLocalDimmNumber": "socket_local_dimm_number", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.config_status = None
        self.socket_id = None
        self.socket_local_dimm_number = None
        self.status = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryNamespaceConfigResult", parent_mo_or_dn, **kwargs)

