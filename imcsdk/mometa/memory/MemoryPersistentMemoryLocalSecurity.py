"""This module contains the general information for MemoryPersistentMemoryLocalSecurity ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MemoryPersistentMemoryLocalSecurityConsts:
    pass


class MemoryPersistentMemoryLocalSecurity(ManagedObject):
    """This is MemoryPersistentMemoryLocalSecurity class."""

    consts = MemoryPersistentMemoryLocalSecurityConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("MemoryPersistentMemoryLocalSecurity", "memoryPersistentMemoryLocalSecurity", "local", VersionMeta.Version404b, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['memoryPersistentMemorySecurity'], [], [None]),
        "modular": MoMeta("MemoryPersistentMemoryLocalSecurity", "memoryPersistentMemoryLocalSecurity", "local", VersionMeta.Version404b, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['memoryPersistentMemorySecurity'], [], [None])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, 0x2, None, None, None, [], []),
            "deployed_secure_passphrase": MoPropertyMeta("deployed_secure_passphrase", "deployedSecurePassphrase", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 1, 32, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "secure_passphrase": MoPropertyMeta("secure_passphrase", "securePassphrase", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x20, 1, 32, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, 0x2, None, None, None, [], []),
            "deployed_secure_passphrase": MoPropertyMeta("deployed_secure_passphrase", "deployedSecurePassphrase", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 1, 32, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "secure_passphrase": MoPropertyMeta("secure_passphrase", "securePassphrase", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x20, 1, 32, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "deployedSecurePassphrase": "deployed_secure_passphrase", 
            "dn": "dn", 
            "rn": "rn", 
            "securePassphrase": "secure_passphrase", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "deployedSecurePassphrase": "deployed_secure_passphrase", 
            "dn": "dn", 
            "rn": "rn", 
            "securePassphrase": "secure_passphrase", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.deployed_secure_passphrase = None
        self.secure_passphrase = None
        self.status = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryLocalSecurity", parent_mo_or_dn, **kwargs)

