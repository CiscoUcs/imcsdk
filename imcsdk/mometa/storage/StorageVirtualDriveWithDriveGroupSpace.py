"""This module contains the general information for StorageVirtualDriveWithDriveGroupSpace ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageVirtualDriveWithDriveGroupSpaceConsts:
    pass


class StorageVirtualDriveWithDriveGroupSpace(ManagedObject):
    """This is StorageVirtualDriveWithDriveGroupSpace class."""

    consts = StorageVirtualDriveWithDriveGroupSpaceConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("StorageVirtualDriveWithDriveGroupSpace", "storageVirtualDriveWithDriveGroupSpace", "vd-[id]", VersionMeta.Version201a, "InputOutput", 0xf, [], ["admin", "read-only", "user"], ['storageVirtualDriveCreatorUsingVirtualDriveGroup'], [], ["Get"]),
        "modular": MoMeta("StorageVirtualDriveWithDriveGroupSpace", "storageVirtualDriveWithDriveGroupSpace", "vd-[id]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageVirtualDriveCreatorUsingVirtualDriveGroup'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version201a, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "max_available_space": MoPropertyMeta("max_available_space", "maxAvailableSpace", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "raid_level": MoPropertyMeta("raid_level", "raidLevel", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "used_physical_drive_ids": MoPropertyMeta("used_physical_drive_ids", "usedPhysicalDriveIds", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vd_status": MoPropertyMeta("vd_status", "vdStatus", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "max_available_space": MoPropertyMeta("max_available_space", "maxAvailableSpace", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "raid_level": MoPropertyMeta("raid_level", "raidLevel", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "used_physical_drive_ids": MoPropertyMeta("used_physical_drive_ids", "usedPhysicalDriveIds", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vd_status": MoPropertyMeta("vd_status", "vdStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "health": "health", 
            "id": "id", 
            "maxAvailableSpace": "max_available_space", 
            "name": "name", 
            "raidLevel": "raid_level", 
            "rn": "rn", 
            "status": "status", 
            "usedPhysicalDriveIds": "used_physical_drive_ids", 
            "vdStatus": "vd_status", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "health": "health", 
            "id": "id", 
            "maxAvailableSpace": "max_available_space", 
            "name": "name", 
            "raidLevel": "raid_level", 
            "rn": "rn", 
            "status": "status", 
            "usedPhysicalDriveIds": "used_physical_drive_ids", 
            "vdStatus": "vd_status", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.health = None
        self.max_available_space = None
        self.name = None
        self.raid_level = None
        self.status = None
        self.used_physical_drive_ids = None
        self.vd_status = None

        ManagedObject.__init__(self, "StorageVirtualDriveWithDriveGroupSpace", parent_mo_or_dn, **kwargs)

