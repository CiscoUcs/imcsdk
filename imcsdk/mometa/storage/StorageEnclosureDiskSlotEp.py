"""This module contains the general information for StorageEnclosureDiskSlotEp ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageEnclosureDiskSlotEpConsts:
    DRIVE_PATH_ = ""
    DRIVE_PATH_PATH_0 = "PATH_0"
    DRIVE_PATH_PATH_1 = "PATH_1"
    DRIVE_PATH_PATH_BOTH = "PATH_BOTH"
    DRIVE_PATH_PATH_NONE = "PATH_NONE"


class StorageEnclosureDiskSlotEp(ManagedObject):
    """This is StorageEnclosureDiskSlotEp class."""

    consts = StorageEnclosureDiskSlotEpConsts()
    naming_props = set(['slot'])

    mo_meta = {
        "modular": MoMeta("StorageEnclosureDiskSlotEp", "storageEnclosureDiskSlotEp", "disk-slot-[slot]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageEnclosure'], ['computeServerRef', 'faultInst'], ["Get"])
    }


    prop_meta = {

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "drive_path": MoPropertyMeta("drive_path", "drivePath", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "PATH_0", "PATH_1", "PATH_BOTH", "PATH_NONE"], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "drivePath": "drive_path", 
            "health": "health", 
            "presence": "presence", 
            "rn": "rn", 
            "slot": "slot", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, slot, **kwargs):
        self._dirty_mask = 0
        self.slot = slot
        self.child_action = None
        self.drive_path = None
        self.health = None
        self.presence = None
        self.status = None

        ManagedObject.__init__(self, "StorageEnclosureDiskSlotEp", parent_mo_or_dn, **kwargs)

