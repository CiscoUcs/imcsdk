"""This module contains the general information for MemoryPersistentMemoryLogicalConfiguration ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MemoryPersistentMemoryLogicalConfigurationConsts:
    ADMIN_ACTION_DISABLE_SECURITY = "disable-security"
    ADMIN_ACTION_ENABLE_SECURITY = "enable-security"
    ADMIN_ACTION_MODIFY_PASSPHRASE = "modify-passphrase"
    ADMIN_ACTION_RESET_FACTORY_DEFAULT = "reset-factory-default"
    ADMIN_ACTION_SECURE_ERASE = "secure-erase"
    ADMIN_ACTION_UNLOCK_DIMMS = "unlock-dimms"
    FORCE_CONFIG_FALSE = "false"
    FORCE_CONFIG_NO = "no"
    FORCE_CONFIG_TRUE = "true"
    FORCE_CONFIG_YES = "yes"
    MGMT_MODE_HOST_MANAGED = "host-managed"
    MGMT_MODE_IMC_MANAGED = "imc-managed"
    REBOOT_ON_UPDATE_FALSE = "false"
    REBOOT_ON_UPDATE_NO = "no"
    REBOOT_ON_UPDATE_TRUE = "true"
    REBOOT_ON_UPDATE_YES = "yes"


class MemoryPersistentMemoryLogicalConfiguration(ManagedObject):
    """This is MemoryPersistentMemoryLogicalConfiguration class."""

    consts = MemoryPersistentMemoryLogicalConfigurationConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("MemoryPersistentMemoryLogicalConfiguration", "memoryPersistentMemoryLogicalConfiguration", "pmemory-lconfig", VersionMeta.Version404b, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['computeBoard'], ['memoryPersistentMemoryDimms', 'memoryPersistentMemoryGoal', 'memoryPersistentMemoryLogicalNamespace', 'memoryPersistentMemorySecurity'], [None]),
        "modular": MoMeta("MemoryPersistentMemoryLogicalConfiguration", "memoryPersistentMemoryLogicalConfiguration", "pmemory-lconfig", VersionMeta.Version404b, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['computeBoard'], ['memoryPersistentMemoryDimms', 'memoryPersistentMemoryGoal', 'memoryPersistentMemoryLogicalNamespace', 'memoryPersistentMemorySecurity'], [None])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["disable-security", "enable-security", "modify-passphrase", "reset-factory-default", "secure-erase", "unlock-dimms"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "force_config": MoPropertyMeta("force_config", "forceConfig", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "mgmt_mode": MoPropertyMeta("mgmt_mode", "mgmtMode", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["host-managed", "imc-managed"], []),
            "reboot_on_update": MoPropertyMeta("reboot_on_update", "rebootOnUpdate", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["disable-security", "enable-security", "modify-passphrase", "reset-factory-default", "secure-erase", "unlock-dimms"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "force_config": MoPropertyMeta("force_config", "forceConfig", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["No", "Yes", "no", "yes"], []),
            "mgmt_mode": MoPropertyMeta("mgmt_mode", "mgmtMode", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["host-managed", "imc-managed"], []),
            "reboot_on_update": MoPropertyMeta("reboot_on_update", "rebootOnUpdate", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["No", "Yes", "no", "yes"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "forceConfig": "force_config", 
            "mgmtMode": "mgmt_mode", 
            "rebootOnUpdate": "reboot_on_update", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "forceConfig": "force_config", 
            "mgmtMode": "mgmt_mode", 
            "rebootOnUpdate": "reboot_on_update", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.force_config = None
        self.mgmt_mode = None
        self.reboot_on_update = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryLogicalConfiguration", parent_mo_or_dn, **kwargs)

