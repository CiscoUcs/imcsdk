"""This module contains the general information for StorageFlexFlashPhysicalDrive ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexFlashPhysicalDriveConsts:
    pass


class StorageFlexFlashPhysicalDrive(ManagedObject):
    """This is StorageFlexFlashPhysicalDrive class."""

    consts = StorageFlexFlashPhysicalDriveConsts()
    naming_props = set(['physicalDriveId'])

    mo_meta = {
        "classic": MoMeta("StorageFlexFlashPhysicalDrive", "storageFlexFlashPhysicalDrive", "card-[physical_drive_id]", VersionMeta.Version202c, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageFlexFlashController'], ['faultInst'], ["Get"]),
        "modular": MoMeta("StorageFlexFlashPhysicalDrive", "storageFlexFlashPhysicalDrive", "card-[physical_drive_id]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageFlexFlashController'], ['faultInst'], ["Get"])
    }


    prop_meta = {

        "classic": {
            "block_size": MoPropertyMeta("block_size", "blockSize", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "capacity": MoPropertyMeta("capacity", "capacity", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "card_mode": MoPropertyMeta("card_mode", "cardMode", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "card_status": MoPropertyMeta("card_status", "cardStatus", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "card_type": MoPropertyMeta("card_type", "cardType", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "controller": MoPropertyMeta("controller", "controller", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dirty_partition_map": MoPropertyMeta("dirty_partition_map", "dirtyPartitionMap", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "drives_enabled": MoPropertyMeta("drives_enabled", "drivesEnabled", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "manufacturer_date": MoPropertyMeta("manufacturer_date", "manufacturerDate", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "manufacturer_id": MoPropertyMeta("manufacturer_id", "manufacturerId", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "oem_id": MoPropertyMeta("oem_id", "oemId", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "partition_count": MoPropertyMeta("partition_count", "partitionCount", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "password_protected": MoPropertyMeta("password_protected", "passwordProtected", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pd_status": MoPropertyMeta("pd_status", "pdStatus", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "physical_drive": MoPropertyMeta("physical_drive", "physicalDrive", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "physical_drive_id": MoPropertyMeta("physical_drive_id", "physicalDriveId", "string", VersionMeta.Version202c, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_revision": MoPropertyMeta("product_revision", "productRevision", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "raid_role": MoPropertyMeta("raid_role", "raidRole", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "read_error_count": MoPropertyMeta("read_error_count", "readErrorCount", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "read_error_threshold": MoPropertyMeta("read_error_threshold", "readErrorThreshold", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "serial_number": MoPropertyMeta("serial_number", "serialNumber", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "signature": MoPropertyMeta("signature", "signature", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "slot_number": MoPropertyMeta("slot_number", "slotNumber", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "stale_partition_map": MoPropertyMeta("stale_partition_map", "stalePartitionMap", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "sync_mode": MoPropertyMeta("sync_mode", "syncMode", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "write_enabled": MoPropertyMeta("write_enabled", "writeEnabled", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "write_error_count": MoPropertyMeta("write_error_count", "writeErrorCount", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "write_error_threshold": MoPropertyMeta("write_error_threshold", "writeErrorThreshold", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "block_size": MoPropertyMeta("block_size", "blockSize", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "capacity": MoPropertyMeta("capacity", "capacity", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "card_mode": MoPropertyMeta("card_mode", "cardMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "card_status": MoPropertyMeta("card_status", "cardStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "card_type": MoPropertyMeta("card_type", "cardType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "controller": MoPropertyMeta("controller", "controller", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "drives_enabled": MoPropertyMeta("drives_enabled", "drivesEnabled", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "manufacturer_date": MoPropertyMeta("manufacturer_date", "manufacturerDate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "manufacturer_id": MoPropertyMeta("manufacturer_id", "manufacturerId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "oem_id": MoPropertyMeta("oem_id", "oemId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "partition_count": MoPropertyMeta("partition_count", "partitionCount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "password_protected": MoPropertyMeta("password_protected", "passwordProtected", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pd_status": MoPropertyMeta("pd_status", "pdStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "physical_drive": MoPropertyMeta("physical_drive", "physicalDrive", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "physical_drive_id": MoPropertyMeta("physical_drive_id", "physicalDriveId", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_revision": MoPropertyMeta("product_revision", "productRevision", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "raid_role": MoPropertyMeta("raid_role", "raidRole", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "read_error_count": MoPropertyMeta("read_error_count", "readErrorCount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "read_error_threshold": MoPropertyMeta("read_error_threshold", "readErrorThreshold", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "serial_number": MoPropertyMeta("serial_number", "serialNumber", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "signature": MoPropertyMeta("signature", "signature", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "slot_number": MoPropertyMeta("slot_number", "slotNumber", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "sync_mode": MoPropertyMeta("sync_mode", "syncMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "write_enabled": MoPropertyMeta("write_enabled", "writeEnabled", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "write_error_count": MoPropertyMeta("write_error_count", "writeErrorCount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "write_error_threshold": MoPropertyMeta("write_error_threshold", "writeErrorThreshold", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "blockSize": "block_size", 
            "capacity": "capacity", 
            "cardMode": "card_mode", 
            "cardStatus": "card_status", 
            "cardType": "card_type", 
            "childAction": "child_action", 
            "controller": "controller", 
            "dirtyPartitionMap": "dirty_partition_map", 
            "dn": "dn", 
            "drivesEnabled": "drives_enabled", 
            "health": "health", 
            "manufacturerDate": "manufacturer_date", 
            "manufacturerId": "manufacturer_id", 
            "oemId": "oem_id", 
            "partitionCount": "partition_count", 
            "passwordProtected": "password_protected", 
            "pdStatus": "pd_status", 
            "physicalDrive": "physical_drive", 
            "physicalDriveId": "physical_drive_id", 
            "productName": "product_name", 
            "productRevision": "product_revision", 
            "raidRole": "raid_role", 
            "readErrorCount": "read_error_count", 
            "readErrorThreshold": "read_error_threshold", 
            "rn": "rn", 
            "serialNumber": "serial_number", 
            "signature": "signature", 
            "slotNumber": "slot_number", 
            "stalePartitionMap": "stale_partition_map", 
            "status": "status", 
            "syncMode": "sync_mode", 
            "writeEnabled": "write_enabled", 
            "writeErrorCount": "write_error_count", 
            "writeErrorThreshold": "write_error_threshold", 
        },

        "modular": {
            "blockSize": "block_size", 
            "capacity": "capacity", 
            "cardMode": "card_mode", 
            "cardStatus": "card_status", 
            "cardType": "card_type", 
            "childAction": "child_action", 
            "controller": "controller", 
            "dn": "dn", 
            "drivesEnabled": "drives_enabled", 
            "health": "health", 
            "manufacturerDate": "manufacturer_date", 
            "manufacturerId": "manufacturer_id", 
            "oemId": "oem_id", 
            "partitionCount": "partition_count", 
            "passwordProtected": "password_protected", 
            "pdStatus": "pd_status", 
            "physicalDrive": "physical_drive", 
            "physicalDriveId": "physical_drive_id", 
            "productName": "product_name", 
            "productRevision": "product_revision", 
            "raidRole": "raid_role", 
            "readErrorCount": "read_error_count", 
            "readErrorThreshold": "read_error_threshold", 
            "rn": "rn", 
            "serialNumber": "serial_number", 
            "signature": "signature", 
            "slotNumber": "slot_number", 
            "status": "status", 
            "syncMode": "sync_mode", 
            "writeEnabled": "write_enabled", 
            "writeErrorCount": "write_error_count", 
            "writeErrorThreshold": "write_error_threshold", 
        },

    }

    def __init__(self, parent_mo_or_dn, physical_drive_id, **kwargs):
        self._dirty_mask = 0
        self.physical_drive_id = physical_drive_id
        self.block_size = None
        self.capacity = None
        self.card_mode = None
        self.card_status = None
        self.card_type = None
        self.child_action = None
        self.controller = None
        self.dirty_partition_map = None
        self.drives_enabled = None
        self.health = None
        self.manufacturer_date = None
        self.manufacturer_id = None
        self.oem_id = None
        self.partition_count = None
        self.password_protected = None
        self.pd_status = None
        self.physical_drive = None
        self.product_name = None
        self.product_revision = None
        self.raid_role = None
        self.read_error_count = None
        self.read_error_threshold = None
        self.serial_number = None
        self.signature = None
        self.slot_number = None
        self.stale_partition_map = None
        self.status = None
        self.sync_mode = None
        self.write_enabled = None
        self.write_error_count = None
        self.write_error_threshold = None

        ManagedObject.__init__(self, "StorageFlexFlashPhysicalDrive", parent_mo_or_dn, **kwargs)

