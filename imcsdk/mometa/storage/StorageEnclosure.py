"""This module contains the general information for StorageEnclosure ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageEnclosureConsts:
    ADMIN_ACTION_RESET_ZONE_SETTINGS = "reset-zone-settings"
    DRIVE_POWER_POLICY_ACTIVE = "active"
    DRIVE_POWER_POLICY_POWER_SAVE = "power-save"


class StorageEnclosure(ManagedObject):
    """This is StorageEnclosure class."""

    consts = StorageEnclosureConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("StorageEnclosure", "storageEnclosure", "enc-1", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['equipmentChassis'], ['storageEnclosureDisk', 'storageEnclosureDiskFwHelper', 'storageEnclosureDiskSlotEp', 'storageEnclosureDiskSlotZoneHelper'], ["Get", "Set"])
    }


    prop_meta = {

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["reset-zone-settings"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "drive_power_policy": MoPropertyMeta("drive_power_policy", "drivePowerPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["active", "power-save"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "modular": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "description": "description", 
            "dn": "dn", 
            "drivePowerPolicy": "drive_power_policy", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.child_action = None
        self.description = None
        self.drive_power_policy = None
        self.status = None

        ManagedObject.__init__(self, "StorageEnclosure", parent_mo_or_dn, **kwargs)

