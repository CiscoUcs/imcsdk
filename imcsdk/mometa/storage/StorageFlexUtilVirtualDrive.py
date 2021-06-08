"""This module contains the general information for StorageFlexUtilVirtualDrive ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexUtilVirtualDriveConsts:
    ADMIN_ACTION_CANCEL_UPDATE = "cancel-update"
    ADMIN_ACTION_DISABLE_VD = "disable-vd"
    ADMIN_ACTION_ENABLE_VD = "enable-vd"
    ADMIN_ACTION_ERASE_VD = "erase-vd"
    ADMIN_ACTION_UPDATE_VD = "update-vd"


class StorageFlexUtilVirtualDrive(ManagedObject):
    """This is StorageFlexUtilVirtualDrive class."""

    consts = StorageFlexUtilVirtualDriveConsts()
    naming_props = set(['partitionName'])

    mo_meta = {
        "classic": MoMeta("StorageFlexUtilVirtualDrive", "storageFlexUtilVirtualDrive", "vd-[partition_name]", VersionMeta.Version304a, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['storageFlexUtilController'], ['faultInst'], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["cancel-update", "disable-vd", "enable-vd", "erase-vd", "update-vd"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version304a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "drive_scope": MoPropertyMeta("drive_scope", "driveScope", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "drive_status": MoPropertyMeta("drive_status", "driveStatus", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "drive_type": MoPropertyMeta("drive_type", "driveType", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "host_accessible": MoPropertyMeta("host_accessible", "hostAccessible", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "last_operation_status": MoPropertyMeta("last_operation_status", "lastOperationStatus", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "lun_id": MoPropertyMeta("lun_id", "lunId", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "operation_in_progress": MoPropertyMeta("operation_in_progress", "operationInProgress", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "partition_id": MoPropertyMeta("partition_id", "partitionId", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "partition_name": MoPropertyMeta("partition_name", "partitionName", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "resident_image": MoPropertyMeta("resident_image", "residentImage", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "virtual_drive": MoPropertyMeta("virtual_drive", "virtualDrive", "string", VersionMeta.Version304a, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "dn": "dn", 
            "driveScope": "drive_scope", 
            "driveStatus": "drive_status", 
            "driveType": "drive_type", 
            "hostAccessible": "host_accessible", 
            "lastOperationStatus": "last_operation_status", 
            "lunId": "lun_id", 
            "operationInProgress": "operation_in_progress", 
            "partitionId": "partition_id", 
            "partitionName": "partition_name", 
            "residentImage": "resident_image", 
            "rn": "rn", 
            "size": "size", 
            "status": "status", 
            "virtualDrive": "virtual_drive", 
        },

    }

    def __init__(self, parent_mo_or_dn, partition_name, **kwargs):
        self._dirty_mask = 0
        self.partition_name = partition_name
        self.admin_action = None
        self.child_action = None
        self.drive_scope = None
        self.drive_status = None
        self.drive_type = None
        self.host_accessible = None
        self.last_operation_status = None
        self.lun_id = None
        self.operation_in_progress = None
        self.partition_id = None
        self.resident_image = None
        self.size = None
        self.status = None
        self.virtual_drive = None

        ManagedObject.__init__(self, "StorageFlexUtilVirtualDrive", parent_mo_or_dn, **kwargs)

