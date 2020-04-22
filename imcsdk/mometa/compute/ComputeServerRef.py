"""This module contains the general information for ComputeServerRef ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class ComputeServerRefConsts:
    DRIVE_PATH_ = ""
    DRIVE_PATH_PATH_0 = "PATH_0"
    DRIVE_PATH_PATH_1 = "PATH_1"
    DRIVE_PATH_PATH_BOTH = "PATH_BOTH"
    DRIVE_PATH_PATH_NONE = "PATH_NONE"


class ComputeServerRef(ManagedObject):
    """This is ComputeServerRef class."""

    consts = ComputeServerRefConsts()
    naming_props = set(['ownership'])

    mo_meta = {
        "modular": MoMeta("ComputeServerRef", "computeServerRef", "server-ref-[ownership]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageEnclosureDiskSlotEp'], [], ["Get"])
    }


    prop_meta = {

        "modular": {
            "diskstate": MoPropertyMeta("diskstate", "diskstate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "drive_path": MoPropertyMeta("drive_path", "drivePath", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "PATH_0", "PATH_1", "PATH_BOTH", "PATH_NONE"], []),
            "ownership": MoPropertyMeta("ownership", "ownership", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "modular": {
            "diskstate": "diskstate", 
            "dn": "dn", 
            "drivePath": "drive_path", 
            "ownership": "ownership", 
            "rn": "rn", 
            "slot": "slot", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, ownership, **kwargs):
        self._dirty_mask = 0
        self.ownership = ownership
        self.diskstate = None
        self.drive_path = None
        self.slot = None
        self.status = None

        ManagedObject.__init__(self, "ComputeServerRef", parent_mo_or_dn, **kwargs)

