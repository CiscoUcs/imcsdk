"""This module contains the general information for StorageFlexUtilController ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexUtilControllerConsts:
    ADMIN_ACTION_RESET_CARD_CONFIGURATION = "reset-card-configuration"


class StorageFlexUtilController(ManagedObject):
    """This is StorageFlexUtilController class."""

    consts = StorageFlexUtilControllerConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("StorageFlexUtilController", "storageFlexUtilController", "storage-flexutil-[id]", VersionMeta.Version304a, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['computeBoard'], ['faultInst', 'storageFlexUtilHealth', 'storageFlexUtilOperationalProfile', 'storageFlexUtilPhysicalDrive', 'storageFlexUtilVirtualDrive', 'storageFlexUtilVirtualDriveImageMap'], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["reset-card-configuration"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version304a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "configured_mode": MoPropertyMeta("configured_mode", "configuredMode", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "controller_name": MoPropertyMeta("controller_name", "controllerName", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "controller_status": MoPropertyMeta("controller_status", "controllerStatus", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "internal_state": MoPropertyMeta("internal_state", "internalState", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "physical_drive_count": MoPropertyMeta("physical_drive_count", "physicalDriveCount", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "virtual_drive_count": MoPropertyMeta("virtual_drive_count", "virtualDriveCount", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "configuredMode": "configured_mode", 
            "controllerName": "controller_name", 
            "controllerStatus": "controller_status", 
            "dn": "dn", 
            "id": "id", 
            "internalState": "internal_state", 
            "physicalDriveCount": "physical_drive_count", 
            "productName": "product_name", 
            "rn": "rn", 
            "status": "status", 
            "virtualDriveCount": "virtual_drive_count", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_action = None
        self.child_action = None
        self.configured_mode = None
        self.controller_name = None
        self.controller_status = None
        self.internal_state = None
        self.physical_drive_count = None
        self.product_name = None
        self.status = None
        self.virtual_drive_count = None

        ManagedObject.__init__(self, "StorageFlexUtilController", parent_mo_or_dn, **kwargs)

