"""This module contains the general information for StorageFlexFlashVirtualDrive ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexFlashVirtualDriveConsts:
    ADMIN_ACTION_DISABLE_VD = "disable-vd"
    ADMIN_ACTION_ENABLE_VD = "enable-vd"
    ADMIN_ACTION_ERASE_VD = "erase-vd"
    ADMIN_ACTION_SYNC_VD = "sync-vd"
    ADMIN_ACTION_UPDATE_VD = "update-vd"


class StorageFlexFlashVirtualDrive(ManagedObject):
    """This is StorageFlexFlashVirtualDrive class."""

    consts = StorageFlexFlashVirtualDriveConsts()
    naming_props = set([u'partitionId'])

    mo_meta = {
        "classic": MoMeta("StorageFlexFlashVirtualDrive", "storageFlexFlashVirtualDrive", "vd-[partition_id]", VersionMeta.Version202c, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'storageFlexFlashController'], [u'faultInst'], ["Get", "Set"]),
        "modular": MoMeta("StorageFlexFlashVirtualDrive", "storageFlexFlashVirtualDrive", "vd-[partition_id]", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'storageFlexFlashController'], [u'faultInst'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["disable-vd", "enable-vd", "erase-vd", "sync-vd", "update-vd"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "drive_scope": MoPropertyMeta("drive_scope", "driveScope", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "drive_status": MoPropertyMeta("drive_status", "driveStatus", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "drive_type": MoPropertyMeta("drive_type", "driveType", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "host_accessible": MoPropertyMeta("host_accessible", "hostAccessible", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "last_operation_status": MoPropertyMeta("last_operation_status", "lastOperationStatus", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "operation_in_progress": MoPropertyMeta("operation_in_progress", "operationInProgress", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "partition_id": MoPropertyMeta("partition_id", "partitionId", "string", VersionMeta.Version202c, MoPropertyMeta.NAMING, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "virtual_drive": MoPropertyMeta("virtual_drive", "virtualDrive", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["disable-vd", "enable-vd", "erase-vd", "sync-vd", "update-vd"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "drive_scope": MoPropertyMeta("drive_scope", "driveScope", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "drive_status": MoPropertyMeta("drive_status", "driveStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "drive_type": MoPropertyMeta("drive_type", "driveType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "host_accessible": MoPropertyMeta("host_accessible", "hostAccessible", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "last_operation_status": MoPropertyMeta("last_operation_status", "lastOperationStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "operation_in_progress": MoPropertyMeta("operation_in_progress", "operationInProgress", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "partition_id": MoPropertyMeta("partition_id", "partitionId", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "virtual_drive": MoPropertyMeta("virtual_drive", "virtualDrive", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
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
            "operationInProgress": "operation_in_progress", 
            "partitionId": "partition_id", 
            "rn": "rn", 
            "size": "size", 
            "status": "status", 
            "virtualDrive": "virtual_drive", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "dn": "dn", 
            "driveScope": "drive_scope", 
            "driveStatus": "drive_status", 
            "driveType": "drive_type", 
            "hostAccessible": "host_accessible", 
            "lastOperationStatus": "last_operation_status", 
            "operationInProgress": "operation_in_progress", 
            "partitionId": "partition_id", 
            "rn": "rn", 
            "size": "size", 
            "status": "status", 
            "virtualDrive": "virtual_drive", 
        },

    }

    def __init__(self, parent_mo_or_dn, partition_id, **kwargs):
        self._dirty_mask = 0
        self.partition_id = partition_id
        self.admin_action = None
        self.child_action = None
        self.drive_scope = None
        self.drive_status = None
        self.drive_type = None
        self.host_accessible = None
        self.last_operation_status = None
        self.operation_in_progress = None
        self.size = None
        self.status = None
        self.virtual_drive = None

        ManagedObject.__init__(self, "StorageFlexFlashVirtualDrive", parent_mo_or_dn, **kwargs)

