"""This module contains the general information for SelfEncryptStorageController ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class SelfEncryptStorageControllerConsts:
    ADMIN_ACTION_DISABLE_SELF_ENCRYPT = "disable-self-encrypt"
    ADMIN_ACTION_ENABLE_SELF_ENCRYPT = "enable-self-encrypt"
    ADMIN_ACTION_MODIFY_SELF_ENCRYPT = "modify-self-encrypt"
    ADMIN_ACTION_SWITCH_LOCAL_TO_REMOTE = "switch-local-to-remote"
    ADMIN_ACTION_SWITCH_REMOTE_TO_LOCAL = "switch-remote-to-local"
    ADMIN_ACTION_UNLOCK_SECURED_DRIVES = "unlock-secured-drives"
    KEY_MANAGEMENT_LOCAL = "local"
    KEY_MANAGEMENT_REMOTE = "remote"


class SelfEncryptStorageController(ManagedObject):
    """This is SelfEncryptStorageController class."""

    consts = SelfEncryptStorageControllerConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("SelfEncryptStorageController", "selfEncryptStorageController", "ctr-self-encrypt", VersionMeta.Version209c, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['storageController'], [], ["Get", "Set"]),
        "modular": MoMeta("SelfEncryptStorageController", "selfEncryptStorageController", "ctr-self-encrypt", VersionMeta.Version303a, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['storageController'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["disable-self-encrypt", "enable-self-encrypt", "modify-self-encrypt", "switch-local-to-remote", "switch-remote-to-local", "unlock-secured-drives"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "existing_security_key": MoPropertyMeta("existing_security_key", "existingSecurityKey", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x8, 1, 33, None, [], []),
            "key_id": MoPropertyMeta("key_id", "keyId", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x10, 1, 256, None, [], []),
            "key_management": MoPropertyMeta("key_management", "keyManagement", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, ["local", "remote"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "security_key": MoPropertyMeta("security_key", "securityKey", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x80, 1, 33, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version209c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["disable-self-encrypt", "enable-self-encrypt", "modify-self-encrypt", "switch-local-to-remote", "switch-remote-to-local", "unlock-secured-drives"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "existing_security_key": MoPropertyMeta("existing_security_key", "existingSecurityKey", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, 1, 33, None, [], []),
            "key_id": MoPropertyMeta("key_id", "keyId", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, 1, 256, None, [], []),
            "key_management": MoPropertyMeta("key_management", "keyManagement", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, ["local", "remote"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "security_key": MoPropertyMeta("security_key", "securityKey", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x80, 1, 33, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "existingSecurityKey": "existing_security_key", 
            "keyId": "key_id", 
            "keyManagement": "key_management", 
            "rn": "rn", 
            "securityKey": "security_key", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "existingSecurityKey": "existing_security_key", 
            "keyId": "key_id", 
            "keyManagement": "key_management", 
            "rn": "rn", 
            "securityKey": "security_key", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.existing_security_key = None
        self.key_id = None
        self.key_management = None
        self.security_key = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "SelfEncryptStorageController", parent_mo_or_dn, **kwargs)

