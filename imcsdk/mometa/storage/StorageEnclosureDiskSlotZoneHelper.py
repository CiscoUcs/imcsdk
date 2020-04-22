"""This module contains the general information for StorageEnclosureDiskSlotZoneHelper ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageEnclosureDiskSlotZoneHelperConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"
    DRIVE_PATH_ = ""
    DRIVE_PATH_PATH_0 = "PATH_0"
    DRIVE_PATH_PATH_1 = "PATH_1"
    DRIVE_PATH_PATH_BOTH = "PATH_BOTH"
    DRIVE_PATH_PATH_NONE = "PATH_NONE"
    OWNERSHIP_ = ""
    OWNERSHIP_HOTSPARE = "hotspare"
    OWNERSHIP_NONE = "none"
    OWNERSHIP_SERVER1 = "server1"
    OWNERSHIP_SERVER2 = "server2"
    OWNERSHIP_SHARED = "shared"


class StorageEnclosureDiskSlotZoneHelper(ManagedObject):
    """This is StorageEnclosureDiskSlotZoneHelper class."""

    consts = StorageEnclosureDiskSlotZoneHelperConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("StorageEnclosureDiskSlotZoneHelper", "storageEnclosureDiskSlotZoneHelper", "zone-drive", VersionMeta.Version2013e, "InputOutput", 0x1ff, [], ["admin"], ['storageEnclosure'], [], ["Get", "Set"])
    }


    prop_meta = {

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "drive_path": MoPropertyMeta("drive_path", "drivePath", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "PATH_0", "PATH_1", "PATH_BOTH", "PATH_NONE"], []),
            "oper_status": MoPropertyMeta("oper_status", "operStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "ownership": MoPropertyMeta("ownership", "ownership", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "hotspare", "none", "server1", "server2", "shared"], []),
            "ownership_controller": MoPropertyMeta("ownership_controller", "ownershipController", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "slot_list": MoPropertyMeta("slot_list", "slotList", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 1, 512, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "modular": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "drivePath": "drive_path", 
            "operStatus": "oper_status", 
            "ownership": "ownership", 
            "ownershipController": "ownership_controller", 
            "rn": "rn", 
            "slotList": "slot_list", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.drive_path = None
        self.oper_status = None
        self.ownership = None
        self.ownership_controller = None
        self.slot_list = None
        self.status = None

        ManagedObject.__init__(self, "StorageEnclosureDiskSlotZoneHelper", parent_mo_or_dn, **kwargs)

