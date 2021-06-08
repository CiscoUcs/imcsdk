"""This module contains the general information for StorageFlexMMCFile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexMMCFileConsts:
    ADMIN_ACTION_DELETE_FILE = "delete-file"
    ADMIN_ACTION_MAP_FILE = "map-file"
    ADMIN_ACTION_UNMAP_FILE = "unmap-file"
    LOCATION_IMC_IMAGE = "IMC Image"
    LOCATION_USER_FILES = "User Files"


class StorageFlexMMCFile(ManagedObject):
    """This is StorageFlexMMCFile class."""

    consts = StorageFlexMMCFileConsts()
    naming_props = set(['fileId'])

    mo_meta = {
        "classic": MoMeta("StorageFlexMMCFile", "storageFlexMMCFile", "file-[file_id]", VersionMeta.Version421a, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['storageFlexMMC'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete-file", "map-file", "unmap-file"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "file_id": MoPropertyMeta("file_id", "fileId", "uint", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
            "file_name": MoPropertyMeta("file_name", "fileName", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 1024, None, [], []),
            "file_size": MoPropertyMeta("file_size", "fileSize", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 256, None, [], []),
            "file_type": MoPropertyMeta("file_type", "fileType", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 256, None, [], []),
            "location": MoPropertyMeta("location", "location", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["IMC Image", "User Files"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 256, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "update_time": MoPropertyMeta("update_time", "updateTime", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 1024, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "dn": "dn", 
            "fileId": "file_id", 
            "fileName": "file_name", 
            "fileSize": "file_size", 
            "fileType": "file_type", 
            "location": "location", 
            "rn": "rn", 
            "state": "state", 
            "status": "status", 
            "updateTime": "update_time", 
        },

    }

    def __init__(self, parent_mo_or_dn, file_id, **kwargs):
        self._dirty_mask = 0
        self.file_id = file_id
        self.admin_action = None
        self.child_action = None
        self.file_name = None
        self.file_size = None
        self.file_type = None
        self.location = None
        self.state = None
        self.status = None
        self.update_time = None

        ManagedObject.__init__(self, "StorageFlexMMCFile", parent_mo_or_dn, **kwargs)

