"""This module contains the general information for StorageController ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageControllerConsts:
    ADMIN_ACTION_CLEAR_ALL_CONFIG = "clear-all-config"
    ADMIN_ACTION_CLEAR_BOOT_DRIVE = "clear-boot-drive"
    ADMIN_ACTION_CLEAR_CACHE = "clear-cache"
    ADMIN_ACTION_CLEAR_FOREIGN_CONFIG = "clear-foreign-config"
    ADMIN_ACTION_DELETE_ALL_VDS_RESET_PDS = "delete-all-vds-reset-pds"
    ADMIN_ACTION_DISABLE_JBOD = "disable-jbod"
    ADMIN_ACTION_ENABLE_JBOD = "enable-jbod"
    ADMIN_ACTION_GET_TTY_LOG = "get-tty-log"
    ADMIN_ACTION_IMPORT_FOREIGN_CONFIG = "import-foreign-config"
    ADMIN_ACTION_RESET_DEFAULT_CONFIG = "reset-default-config"
    ADMIN_ACTION_SET_PHYSICAL_DRIVE_STATUS_AUTO_CONFIG_MODE = "set-physical-drive-status-auto-config-mode"
    PHYSICAL_DRIVE_STATUS_AUTO_CONFIG_CAPABLE_NO = "no"
    PHYSICAL_DRIVE_STATUS_AUTO_CONFIG_CAPABLE_YES = "yes"
    PHYSICAL_DRIVE_STATUS_AUTO_CONFIG_MODE_JBOD = "jbod"
    PHYSICAL_DRIVE_STATUS_AUTO_CONFIG_MODE_RAID0_WRITEBACK = "raid0-writeback"
    PHYSICAL_DRIVE_STATUS_AUTO_CONFIG_MODE_UNCONFIGURED_GOOD = "unconfigured-good"
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
    naming_props = set(['type', 'id'])

    mo_meta = {
        "classic": MoMeta("StorageController", "storageController", "storage-[type]-[id]", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['computeBoard'], ['faultInst', 'firmwareBootDefinition', 'firmwareRunning', 'generatedStorageControllerKeyId', 'selfEncryptStorageController', 'storageControllerHealth', 'storageControllerNextConsistencyCheckSchedule', 'storageControllerNextPatrolReadSchedule', 'storageControllerProps', 'storageControllerSettings', 'storageLocalDisk', 'storageLocalDiskProps', 'storageRaidBattery', 'storageVirtualDrive', 'storageVirtualDriveCreatorUsingUnusedPhysicalDrive', 'storageVirtualDriveCreatorUsingVirtualDriveGroup', 'suggestedStorageControllerSecurityKey'], ["Get", "Set"]),
        "modular": MoMeta("StorageController", "storageController", "storage-[type]-[id]", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['computeBoard'], ['faultInst', 'firmwareBootDefinition', 'firmwareRunning', 'generatedStorageControllerKeyId', 'selfEncryptStorageController', 'storageControllerHealth', 'storageControllerNextConsistencyCheckSchedule', 'storageControllerNextPatrolReadSchedule', 'storageControllerProps', 'storageControllerSettings', 'storageLocalDisk', 'storageLocalDiskEp', 'storageLocalDiskProps', 'storageRaidBattery', 'storageVirtualDrive', 'storageVirtualDriveCreatorUsingUnusedPhysicalDrive', 'storageVirtualDriveCreatorUsingVirtualDriveGroup', 'suggestedStorageControllerSecurityKey'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear-all-config", "clear-boot-drive", "clear-cache", "clear-foreign-config", "delete-all-vds-reset-pds", "disable-jbod", "enable-jbod", "get-tty-log", "import-foreign-config", "reset-default-config", "set-physical-drive-status-auto-config-mode"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x8, None, None, r"""[a-zA-Z0-9_\-]{1,30}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "controller_type": MoPropertyMeta("controller_type", "controllerType", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "foreign_config_physical_drive_count": MoPropertyMeta("foreign_config_physical_drive_count", "foreignConfigPhysicalDriveCount", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "physical_drive_status_auto_config_capable": MoPropertyMeta("physical_drive_status_auto_config_capable", "physicalDriveStatusAutoConfigCapable", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
            "physical_drive_status_auto_config_mode": MoPropertyMeta("physical_drive_status_auto_config_mode", "physicalDriveStatusAutoConfigMode", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, ["jbod", "raid0-writeback", "unconfigured-good"], []),
            "pid": MoPropertyMeta("pid", "pid", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], []),
            "product_pid": MoPropertyMeta("product_pid", "productPID", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "raid_support": MoPropertyMeta("raid_support", "raidSupport", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "self_encrypt_enabled": MoPropertyMeta("self_encrypt_enabled", "selfEncryptEnabled", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "type_plus_slot_id": MoPropertyMeta("type_plus_slot_id", "typePlusSlotId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear-all-config", "clear-boot-drive", "clear-cache", "clear-foreign-config", "delete-all-vds-reset-pds", "disable-jbod", "enable-jbod", "get-tty-log", "import-foreign-config", "reset-default-config"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x8, None, None, r"""[a-zA-Z0-9_\-]{1,30}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "controller_type": MoPropertyMeta("controller_type", "controllerType", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pid": MoPropertyMeta("pid", "pid", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], []),
            "product_pid": MoPropertyMeta("product_pid", "productPID", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "raid_support": MoPropertyMeta("raid_support", "raidSupport", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "self_encrypt_enabled": MoPropertyMeta("self_encrypt_enabled", "selfEncryptEnabled", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "no", "yes"], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "type_plus_slot_id": MoPropertyMeta("type_plus_slot_id", "typePlusSlotId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "controllerType": "controller_type", 
            "foreignConfigPhysicalDriveCount": "foreign_config_physical_drive_count", 
            "model": "model", 
            "pciSlot": "pci_slot", 
            "physicalDriveStatusAutoConfigCapable": "physical_drive_status_auto_config_capable", 
            "physicalDriveStatusAutoConfigMode": "physical_drive_status_auto_config_mode", 
            "pid": "pid", 
            "presence": "presence", 
            "productPID": "product_pid", 
            "raidSupport": "raid_support", 
            "selfEncryptEnabled": "self_encrypt_enabled", 
            "serial": "serial", 
            "type": "type", 
            "typePlusSlotId": "type_plus_slot_id", 
            "vendor": "vendor", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "controllerType": "controller_type", 
            "model": "model", 
            "pciSlot": "pci_slot", 
            "pid": "pid", 
            "presence": "presence", 
            "productPID": "product_pid", 
            "raidSupport": "raid_support", 
            "selfEncryptEnabled": "self_encrypt_enabled", 
            "serial": "serial", 
            "type": "type", 
            "typePlusSlotId": "type_plus_slot_id", 
            "vendor": "vendor", 
        },

    }

    def __init__(self, parent_mo_or_dn, type, id, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.id = id
        self.admin_action = None
        self.status = None
        self.child_action = None
        self.controller_type = None
        self.foreign_config_physical_drive_count = None
        self.model = None
        self.pci_slot = None
        self.physical_drive_status_auto_config_capable = None
        self.physical_drive_status_auto_config_mode = None
        self.pid = None
        self.presence = None
        self.product_pid = None
        self.raid_support = None
        self.self_encrypt_enabled = None
        self.serial = None
        self.type_plus_slot_id = None
        self.vendor = None

        ManagedObject.__init__(self, "StorageController", parent_mo_or_dn, **kwargs)

