"""This module contains the general information for StorageController ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageControllerConsts:
    ADMIN_ACTION_CLEAR_BOOT_DRIVE = "clear-boot-drive"
    ADMIN_ACTION_CLEAR_CACHE = "clear-cache"
    ADMIN_ACTION_CLEAR_FOREIGN_CONFIG = "clear-foreign-config"
    ADMIN_ACTION_DELETE_ALL_VDS_RESET_PDS = "delete-all-vds-reset-pds"
    ADMIN_ACTION_DISABLE_JBOD = "disable-jbod"
    ADMIN_ACTION_ENABLE_JBOD = "enable-jbod"
    ADMIN_ACTION_GET_TTY_LOG = "get-tty-log"
    ADMIN_ACTION_IMPORT_FOREIGN_CONFIG = "import-foreign-config"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    PRESENCE_INACCESSIBLE = "inaccessible"
    PRESENCE_MISMATCH = "mismatch"
    PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    PRESENCE_MISSING = "missing"
    PRESENCE_NOT_SUPPORTED = "not-supported"
    PRESENCE_UNAUTHORIZED = "unauthorized"
    PRESENCE_UNKNOWN = "unknown"


class StorageController(ManagedObject):
    """This is StorageController class."""

    consts = StorageControllerConsts()
    naming_props = set([u'type', u'id'])

    mo_meta = {
        "classic": MoMeta("StorageController", "storageController", "storage-[type]-[id]", VersionMeta.Version151f, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], [u'computeBoard'], [u'faultInst', u'firmwareBootDefinition', u'firmwareRunning', u'generatedStorageControllerKeyId', u'selfEncryptStorageController', u'storageControllerHealth', u'storageControllerProps', u'storageControllerSettings', u'storageLocalDisk', u'storageLocalDiskProps', u'storageRaidBattery', u'storageVirtualDrive', u'storageVirtualDriveCreatorUsingUnusedPhysicalDrive', u'storageVirtualDriveCreatorUsingVirtualDriveGroup', u'suggestedStorageControllerSecurityKey'], ["Get", "Set"]),
        "modular": MoMeta("StorageController", "storageController", "storage-[type]-[id]", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], [u'computeBoard'], [u'faultInst', u'firmwareBootDefinition', u'firmwareRunning', u'storageControllerHealth', u'storageControllerProps', u'storageControllerSettings', u'storageLocalDisk', u'storageLocalDiskEp', u'storageLocalDiskProps', u'storageRaidBattery', u'storageVirtualDrive', u'storageVirtualDriveCreatorUsingUnusedPhysicalDrive', u'storageVirtualDriveCreatorUsingVirtualDriveGroup'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear-boot-drive", "clear-cache", "clear-foreign-config", "delete-all-vds-reset-pds", "disable-jbod", "enable-jbod", "get-tty-log", "import-foreign-config"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x8, None, None, r"""[a-zA-Z0-9_\-]{1,30}""", [], []), 
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], []), 
            "raid_support": MoPropertyMeta("raid_support", "raidSupport", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "self_encrypt_enabled": MoPropertyMeta("self_encrypt_enabled", "selfEncryptEnabled", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []), 
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear-boot-drive", "clear-cache", "clear-foreign-config", "delete-all-vds-reset-pds", "disable-jbod", "enable-jbod", "get-tty-log", "import-foreign-config"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x8, None, None, r"""[a-zA-Z0-9_\-]{1,30}""", [], []), 
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], []), 
            "raid_support": MoPropertyMeta("raid_support", "raidSupport", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "dn": "dn", 
            "id": "id", 
            "model": "model", 
            "pciSlot": "pci_slot", 
            "presence": "presence", 
            "raidSupport": "raid_support", 
            "rn": "rn", 
            "serial": "serial", 
            "status": "status", 
            "type": "type", 
            "vendor": "vendor", 
            "selfEncryptEnabled": "self_encrypt_enabled", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "dn": "dn", 
            "id": "id", 
            "model": "model", 
            "pciSlot": "pci_slot", 
            "presence": "presence", 
            "raidSupport": "raid_support", 
            "rn": "rn", 
            "serial": "serial", 
            "status": "status", 
            "type": "type", 
            "vendor": "vendor", 
        },

    }

    def __init__(self, parent_mo_or_dn, type, id, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.id = id
        self.admin_action = None
        self.child_action = None
        self.model = None
        self.pci_slot = None
        self.presence = None
        self.raid_support = None
        self.serial = None
        self.status = None
        self.vendor = None
        self.self_encrypt_enabled = None

        ManagedObject.__init__(self, "StorageController", parent_mo_or_dn, **kwargs)

