"""This module contains the general information for StorageFlexUtilPhysicalDrive ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexUtilPhysicalDriveConsts:
    pass


class StorageFlexUtilPhysicalDrive(ManagedObject):
    """This is StorageFlexUtilPhysicalDrive class."""

    consts = StorageFlexUtilPhysicalDriveConsts()
    naming_props = set(['physicalDrive'])

    mo_meta = {
        "classic": MoMeta("StorageFlexUtilPhysicalDrive", "storageFlexUtilPhysicalDrive", "card-[physical_drive]", VersionMeta.Version304a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageFlexUtilController'], ['faultInst'], ["Get"]),
    }


    prop_meta = {

        "classic": {
            "block_size": MoPropertyMeta("block_size", "blockSize", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "capacity": MoPropertyMeta("capacity", "capacity", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version304a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "controller": MoPropertyMeta("controller", "controller", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "drives_enabled": MoPropertyMeta("drives_enabled", "drivesEnabled", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "manufacturer_date": MoPropertyMeta("manufacturer_date", "manufacturerDate", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "manufacturer_id": MoPropertyMeta("manufacturer_id", "manufacturerId", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "oem_id": MoPropertyMeta("oem_id", "oemId", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "partition_count": MoPropertyMeta("partition_count", "partitionCount", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pd_status": MoPropertyMeta("pd_status", "pdStatus", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "physical_drive": MoPropertyMeta("physical_drive", "physicalDrive", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_revision": MoPropertyMeta("product_revision", "productRevision", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "read_error_count": MoPropertyMeta("read_error_count", "readErrorCount", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "read_error_threshold": MoPropertyMeta("read_error_threshold", "readErrorThreshold", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "serial_number": MoPropertyMeta("serial_number", "serialNumber", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "signature": MoPropertyMeta("signature", "signature", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "write_enabled": MoPropertyMeta("write_enabled", "writeEnabled", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "write_error_count": MoPropertyMeta("write_error_count", "writeErrorCount", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "write_error_threshold": MoPropertyMeta("write_error_threshold", "writeErrorThreshold", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "blockSize": "block_size", 
            "capacity": "capacity", 
            "childAction": "child_action", 
            "controller": "controller", 
            "dn": "dn", 
            "drivesEnabled": "drives_enabled", 
            "health": "health", 
            "manufacturerDate": "manufacturer_date", 
            "manufacturerId": "manufacturer_id", 
            "oemId": "oem_id", 
            "partitionCount": "partition_count", 
            "pdStatus": "pd_status", 
            "physicalDrive": "physical_drive", 
            "productName": "product_name", 
            "productRevision": "product_revision", 
            "readErrorCount": "read_error_count", 
            "readErrorThreshold": "read_error_threshold", 
            "rn": "rn", 
            "serialNumber": "serial_number", 
            "signature": "signature", 
            "status": "status", 
            "writeEnabled": "write_enabled", 
            "writeErrorCount": "write_error_count", 
            "writeErrorThreshold": "write_error_threshold", 
        },

    }

    def __init__(self, parent_mo_or_dn, physical_drive, **kwargs):
        self._dirty_mask = 0
        self.physical_drive = physical_drive
        self.block_size = None
        self.capacity = None
        self.child_action = None
        self.controller = None
        self.drives_enabled = None
        self.health = None
        self.manufacturer_date = None
        self.manufacturer_id = None
        self.oem_id = None
        self.partition_count = None
        self.pd_status = None
        self.product_name = None
        self.product_revision = None
        self.read_error_count = None
        self.read_error_threshold = None
        self.serial_number = None
        self.signature = None
        self.status = None
        self.write_enabled = None
        self.write_error_count = None
        self.write_error_threshold = None

        ManagedObject.__init__(self, "StorageFlexUtilPhysicalDrive", parent_mo_or_dn, **kwargs)

