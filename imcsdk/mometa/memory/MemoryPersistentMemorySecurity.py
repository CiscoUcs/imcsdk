"""This module contains the general information for MemoryPersistentMemorySecurity ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MemoryPersistentMemorySecurityConsts:
    pass


class MemoryPersistentMemorySecurity(ManagedObject):
    """This is MemoryPersistentMemorySecurity class."""

    consts = MemoryPersistentMemorySecurityConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("MemoryPersistentMemorySecurity", "memoryPersistentMemorySecurity", "pmemory-security", VersionMeta.Version404b, "InputOutput", 0xf, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryLogicalConfiguration'], ['memoryPersistentMemoryLocalSecurity'], [None]),
        "modular": MoMeta("MemoryPersistentMemorySecurity", "memoryPersistentMemorySecurity", "pmemory-security", VersionMeta.Version404b, "InputOutput", 0xf, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryLogicalConfiguration'], ['memoryPersistentMemoryLocalSecurity'], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "MemoryPersistentMemorySecurity", parent_mo_or_dn, **kwargs)

