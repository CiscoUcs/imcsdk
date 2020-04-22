"""This module contains the general information for StorageFlexFlashControllerProps ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexFlashControllerPropsConsts:
    pass


class StorageFlexFlashControllerProps(ManagedObject):
    """This is StorageFlexFlashControllerProps class."""

    consts = StorageFlexFlashControllerPropsConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StorageFlexFlashControllerProps", "storageFlexFlashControllerProps", "flexflashcontroller-props", VersionMeta.Version202c, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageFlexFlashController'], [], ["Get"]),
        "modular": MoMeta("StorageFlexFlashControllerProps", "storageFlexFlashControllerProps", "flexflashcontroller-props", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageFlexFlashController'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "auto_sync": MoPropertyMeta("auto_sync", "autoSync", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "card_slot": MoPropertyMeta("card_slot", "cardSlot", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "cards_manageable": MoPropertyMeta("cards_manageable", "cardsManageable", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "configured_mode": MoPropertyMeta("configured_mode", "configuredMode", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "controller_name": MoPropertyMeta("controller_name", "controllerName", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "controller_status": MoPropertyMeta("controller_status", "controllerStatus", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "fw_version": MoPropertyMeta("fw_version", "fwVersion", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "internal_state": MoPropertyMeta("internal_state", "internalState", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "non_util_partition_name": MoPropertyMeta("non_util_partition_name", "nonUtilPartitionName", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "operating_mode": MoPropertyMeta("operating_mode", "operatingMode", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "partition_name": MoPropertyMeta("partition_name", "partitionName", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "physical_drive_count": MoPropertyMeta("physical_drive_count", "physicalDriveCount", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "running_fw_version": MoPropertyMeta("running_fw_version", "runningFwVersion", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "startup_fw_version": MoPropertyMeta("startup_fw_version", "startupFwVersion", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "virtual_drive_count": MoPropertyMeta("virtual_drive_count", "virtualDriveCount", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "auto_sync": MoPropertyMeta("auto_sync", "autoSync", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "card_slot": MoPropertyMeta("card_slot", "cardSlot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "cards_manageable": MoPropertyMeta("cards_manageable", "cardsManageable", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "configured_mode": MoPropertyMeta("configured_mode", "configuredMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "controller_name": MoPropertyMeta("controller_name", "controllerName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "controller_status": MoPropertyMeta("controller_status", "controllerStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "fw_version": MoPropertyMeta("fw_version", "fwVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "internal_state": MoPropertyMeta("internal_state", "internalState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "non_util_partition_name": MoPropertyMeta("non_util_partition_name", "nonUtilPartitionName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "operating_mode": MoPropertyMeta("operating_mode", "operatingMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "partition_name": MoPropertyMeta("partition_name", "partitionName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "physical_drive_count": MoPropertyMeta("physical_drive_count", "physicalDriveCount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "running_fw_version": MoPropertyMeta("running_fw_version", "runningFwVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "startup_fw_version": MoPropertyMeta("startup_fw_version", "startupFwVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "virtual_drive_count": MoPropertyMeta("virtual_drive_count", "virtualDriveCount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "autoSync": "auto_sync", 
            "cardSlot": "card_slot", 
            "cardsManageable": "cards_manageable", 
            "childAction": "child_action", 
            "configuredMode": "configured_mode", 
            "controllerName": "controller_name", 
            "controllerStatus": "controller_status", 
            "dn": "dn", 
            "fwVersion": "fw_version", 
            "health": "health", 
            "internalState": "internal_state", 
            "nonUtilPartitionName": "non_util_partition_name", 
            "operatingMode": "operating_mode", 
            "partitionName": "partition_name", 
            "physicalDriveCount": "physical_drive_count", 
            "productName": "product_name", 
            "rn": "rn", 
            "runningFwVersion": "running_fw_version", 
            "startupFwVersion": "startup_fw_version", 
            "status": "status", 
            "vendor": "vendor", 
            "virtualDriveCount": "virtual_drive_count", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "autoSync": "auto_sync", 
            "cardSlot": "card_slot", 
            "cardsManageable": "cards_manageable", 
            "childAction": "child_action", 
            "configuredMode": "configured_mode", 
            "controllerName": "controller_name", 
            "controllerStatus": "controller_status", 
            "dn": "dn", 
            "fwVersion": "fw_version", 
            "health": "health", 
            "internalState": "internal_state", 
            "nonUtilPartitionName": "non_util_partition_name", 
            "operatingMode": "operating_mode", 
            "partitionName": "partition_name", 
            "physicalDriveCount": "physical_drive_count", 
            "productName": "product_name", 
            "rn": "rn", 
            "runningFwVersion": "running_fw_version", 
            "startupFwVersion": "startup_fw_version", 
            "status": "status", 
            "vendor": "vendor", 
            "virtualDriveCount": "virtual_drive_count", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.auto_sync = None
        self.card_slot = None
        self.cards_manageable = None
        self.child_action = None
        self.configured_mode = None
        self.controller_name = None
        self.controller_status = None
        self.fw_version = None
        self.health = None
        self.internal_state = None
        self.non_util_partition_name = None
        self.operating_mode = None
        self.partition_name = None
        self.physical_drive_count = None
        self.product_name = None
        self.running_fw_version = None
        self.startup_fw_version = None
        self.status = None
        self.vendor = None
        self.virtual_drive_count = None

        ManagedObject.__init__(self, "StorageFlexFlashControllerProps", parent_mo_or_dn, **kwargs)

