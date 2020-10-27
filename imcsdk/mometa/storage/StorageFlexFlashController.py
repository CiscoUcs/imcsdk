"""This module contains the general information for StorageFlexFlashController ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexFlashControllerConsts:
    ADMIN_ACTION_CONFIGURE_CARDS = "configure-cards"
    ADMIN_ACTION_CONFIGURE_FIRMWARE_MODE = "configure-firmware-mode"
    ADMIN_ACTION_RESET_FLEXFLASH_CONTROLLER = "reset-flexflash-controller"
    ADMIN_ACTION_RESET_PARTITION_DEFAULT = "reset-partition-default"
    ADMIN_ACTION_SYNC_CARD_CONFIGURATION = "sync-card-configuration"
    CARD_SLOT_NONE = "none"
    CARD_SLOT_SLOT_1 = "slot-1"
    CARD_SLOT_SLOT_2 = "slot-2"
    CONFIGURED_MODE_MIRROR = "mirror"
    CONFIGURED_MODE_UTIL = "util"
    VIRTUAL_DRIVE_NON_REMOVABLE = "Non-Removable"
    VIRTUAL_DRIVE_REMOVABLE = "Removable"
    _VIRTUAL_DRIVE_NON_REMOVABLE = "non-removable"
    _VIRTUAL_DRIVE_REMOVABLE = "removable"


class StorageFlexFlashController(ManagedObject):
    """This is StorageFlexFlashController class."""

    consts = StorageFlexFlashControllerConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("StorageFlexFlashController", "storageFlexFlashController", "storage-flexflash-[id]", VersionMeta.Version202c, "InputOutput", 0x7ff, [], ["admin", "read-only", "user"], ['computeBoard'], ['faultInst', 'storageFlexFlashControllerProps', 'storageFlexFlashOperationalProfile', 'storageFlexFlashPhysicalDrive', 'storageFlexFlashVirtualDrive', 'storageFlexFlashVirtualDriveImageMap'], ["Get", "Set"]),
        "modular": MoMeta("StorageFlexFlashController", "storageFlexFlashController", "storage-flexflash-[id]", VersionMeta.Version2013e, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['computeBoard'], ['faultInst', 'storageFlexFlashControllerProps', 'storageFlexFlashOperationalProfile', 'storageFlexFlashPhysicalDrive', 'storageFlexFlashVirtualDrive', 'storageFlexFlashVirtualDriveImageMap'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["configure-cards", "configure-firmware-mode", "reset-flexflash-controller", "reset-partition-default", "sync-card-configuration"], []),
            "auto_sync": MoPropertyMeta("auto_sync", "autoSync", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "card_slot": MoPropertyMeta("card_slot", "cardSlot", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, ["none", "slot-1", "slot-2"], []),
            "configured_mode": MoPropertyMeta("configured_mode", "configuredMode", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, ["mirror", "util"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "non_util_partition_name": MoPropertyMeta("non_util_partition_name", "nonUtilPartitionName", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x40, 0, 15, None, [], []),
            "partition_name": MoPropertyMeta("partition_name", "partitionName", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x80, 0, 15, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "cards_manageable": MoPropertyMeta("cards_manageable", "cardsManageable", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "controller_status": MoPropertyMeta("controller_status", "controllerStatus", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "fw_version": MoPropertyMeta("fw_version", "fwVersion", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version202c, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "internal_state": MoPropertyMeta("internal_state", "internalState", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "running_fw_version": MoPropertyMeta("running_fw_version", "runningFwVersion", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "startup_fw_version": MoPropertyMeta("startup_fw_version", "startupFwVersion", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "virtual_drive": MoPropertyMeta("virtual_drive", "virtualDrive", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, None, ["Non-Removable", "Removable", "non-removable", "removable"], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["configure-cards", "configure-firmware-mode", "reset-flexflash-controller", "reset-partition-default", "sync-card-configuration"], []),
            "auto_sync": MoPropertyMeta("auto_sync", "autoSync", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "no", "yes"], []),
            "card_slot": MoPropertyMeta("card_slot", "cardSlot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, ["none", "slot-1", "slot-2"], []),
            "configured_mode": MoPropertyMeta("configured_mode", "configuredMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["mirror", "util"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "non_util_partition_name": MoPropertyMeta("non_util_partition_name", "nonUtilPartitionName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 15, None, [], []),
            "partition_name": MoPropertyMeta("partition_name", "partitionName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 0, 15, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "cards_manageable": MoPropertyMeta("cards_manageable", "cardsManageable", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "controller_status": MoPropertyMeta("controller_status", "controllerStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "fw_version": MoPropertyMeta("fw_version", "fwVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "internal_state": MoPropertyMeta("internal_state", "internalState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "running_fw_version": MoPropertyMeta("running_fw_version", "runningFwVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "startup_fw_version": MoPropertyMeta("startup_fw_version", "startupFwVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "autoSync": "auto_sync", 
            "cardSlot": "card_slot", 
            "configuredMode": "configured_mode", 
            "dn": "dn", 
            "nonUtilPartitionName": "non_util_partition_name", 
            "partitionName": "partition_name", 
            "rn": "rn", 
            "status": "status", 
            "cardsManageable": "cards_manageable", 
            "childAction": "child_action", 
            "controllerStatus": "controller_status", 
            "fwVersion": "fw_version", 
            "health": "health", 
            "id": "id", 
            "internalState": "internal_state", 
            "productName": "product_name", 
            "runningFwVersion": "running_fw_version", 
            "startupFwVersion": "startup_fw_version", 
            "vendor": "vendor", 
            "virtualDrive": "virtual_drive", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "autoSync": "auto_sync", 
            "cardSlot": "card_slot", 
            "configuredMode": "configured_mode", 
            "dn": "dn", 
            "nonUtilPartitionName": "non_util_partition_name", 
            "partitionName": "partition_name", 
            "rn": "rn", 
            "status": "status", 
            "cardsManageable": "cards_manageable", 
            "childAction": "child_action", 
            "controllerStatus": "controller_status", 
            "fwVersion": "fw_version", 
            "health": "health", 
            "id": "id", 
            "internalState": "internal_state", 
            "productName": "product_name", 
            "runningFwVersion": "running_fw_version", 
            "startupFwVersion": "startup_fw_version", 
            "vendor": "vendor", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_action = None
        self.auto_sync = None
        self.card_slot = None
        self.configured_mode = None
        self.non_util_partition_name = None
        self.partition_name = None
        self.status = None
        self.cards_manageable = None
        self.child_action = None
        self.controller_status = None
        self.fw_version = None
        self.health = None
        self.internal_state = None
        self.product_name = None
        self.running_fw_version = None
        self.startup_fw_version = None
        self.vendor = None
        self.virtual_drive = None

        ManagedObject.__init__(self, "StorageFlexFlashController", parent_mo_or_dn, **kwargs)

