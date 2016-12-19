"""This module contains the general information for StorageEnclosure ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageEnclosureConsts:
    DRIVE_POWER_POLICY_ACTIVE = "active"
    DRIVE_POWER_POLICY_POWER_SAVE = "power-save"


class StorageEnclosure(ManagedObject):
    """This is StorageEnclosure class."""

    consts = StorageEnclosureConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("StorageEnclosure", "storageEnclosure", "enc-1", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'equipmentChassis'], [u'storageEnclosureDisk', u'storageEnclosureDiskFwHelper', u'storageEnclosureDiskSlotEp', u'storageEnclosureDiskSlotZoneHelper'], ["Get", "Set"])
    }


    prop_meta = {

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "drive_power_policy": MoPropertyMeta("drive_power_policy", "drivePowerPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["active", "power-save"], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "modular": {
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
        self.child_action = None
        self.description = None
        self.drive_power_policy = None
        self.status = None

        ManagedObject.__init__(self, "StorageEnclosure", parent_mo_or_dn, **kwargs)

