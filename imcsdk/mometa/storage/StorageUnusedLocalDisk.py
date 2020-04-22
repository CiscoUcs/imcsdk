"""This module contains the general information for StorageUnusedLocalDisk ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageUnusedLocalDiskConsts:
    pass


class StorageUnusedLocalDisk(ManagedObject):
    """This is StorageUnusedLocalDisk class."""

    consts = StorageUnusedLocalDiskConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("StorageUnusedLocalDisk", "storageUnusedLocalDisk", "pd-[id]", VersionMeta.Version201a, "InputOutput", 0xf, [], ["admin", "read-only", "user"], ['storageVirtualDriveCreatorUsingUnusedPhysicalDrive'], [], ["Get"]),
        "modular": MoMeta("StorageUnusedLocalDisk", "storageUnusedLocalDisk", "pd-[id]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageVirtualDriveCreatorUsingUnusedPhysicalDrive'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "coerced_size": MoPropertyMeta("coerced_size", "coercedSize", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version201a, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "media_type": MoPropertyMeta("media_type", "mediaType", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pd_status": MoPropertyMeta("pd_status", "pdStatus", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "coerced_size": MoPropertyMeta("coerced_size", "coercedSize", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "media_type": MoPropertyMeta("media_type", "mediaType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pd_status": MoPropertyMeta("pd_status", "pdStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "coercedSize": "coerced_size", 
            "dn": "dn", 
            "health": "health", 
            "id": "id", 
            "mediaType": "media_type", 
            "pdStatus": "pd_status", 
            "rn": "rn", 
            "status": "status", 
            "vendor": "vendor", 
        },

        "modular": {
            "childAction": "child_action", 
            "coercedSize": "coerced_size", 
            "dn": "dn", 
            "health": "health", 
            "id": "id", 
            "mediaType": "media_type", 
            "pdStatus": "pd_status", 
            "rn": "rn", 
            "status": "status", 
            "vendor": "vendor", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.coerced_size = None
        self.health = None
        self.media_type = None
        self.pd_status = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "StorageUnusedLocalDisk", parent_mo_or_dn, **kwargs)

