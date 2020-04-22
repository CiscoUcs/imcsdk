"""This module contains the general information for MemoryPersistentMemoryConfigResult ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MemoryPersistentMemoryConfigResultConsts:
    pass


class MemoryPersistentMemoryConfigResult(ManagedObject):
    """This is MemoryPersistentMemoryConfigResult class."""

    consts = MemoryPersistentMemoryConfigResultConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("MemoryPersistentMemoryConfigResult", "memoryPersistentMemoryConfigResult", "cfg-result", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryConfiguration'], ['memoryPersistentMemoryNamespaceConfigResult'], [None]),
        "modular": MoMeta("MemoryPersistentMemoryConfigResult", "memoryPersistentMemoryConfigResult", "cfg-result", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryConfiguration'], ['memoryPersistentMemoryNamespaceConfigResult'], [None])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "config_error": MoPropertyMeta("config_error", "configError", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "config_result": MoPropertyMeta("config_result", "configResult", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "config_error": MoPropertyMeta("config_error", "configError", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "config_result": MoPropertyMeta("config_result", "configResult", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "configError": "config_error", 
            "configResult": "config_result", 
            "configState": "config_state", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "configError": "config_error", 
            "configResult": "config_result", 
            "configState": "config_state", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_error = None
        self.config_result = None
        self.config_state = None
        self.status = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryConfigResult", parent_mo_or_dn, **kwargs)

