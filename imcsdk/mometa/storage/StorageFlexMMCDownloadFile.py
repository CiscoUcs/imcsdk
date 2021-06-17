"""This module contains the general information for StorageFlexMMCDownloadFile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexMMCDownloadFileConsts:
    ADMIN_ACTION_CANCEL_DOWNLOAD_FILE = "cancel-download-file"
    ADMIN_ACTION_DOWNLOAD_FILE = "download-file"
    LOCATION_IMC_IMAGE = "IMC Image"
    LOCATION_IMC_IMAGES = "IMC Images"
    LOCATION_NONE = "None"
    LOCATION_USER_FILES = "User Files"
    MAP_CIFS = "cifs"
    MAP_NFS = "nfs"
    MAP_WWW = "www"


class StorageFlexMMCDownloadFile(ManagedObject):
    """This is StorageFlexMMCDownloadFile class."""

    consts = StorageFlexMMCDownloadFileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StorageFlexMMCDownloadFile", "storageFlexMMCDownloadFile", "download-file", VersionMeta.Version421a, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], ['storageFlexMMC'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["cancel-download-file", "download-file"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "file_size": MoPropertyMeta("file_size", "fileSize", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 256, None, [], []),
            "location": MoPropertyMeta("location", "location", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["IMC Image", "IMC Images", "None", "User Files"], []),
            "map": MoPropertyMeta("map", "map", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["cifs", "nfs", "www"], []),
            "mount_options": MoPropertyMeta("mount_options", "mountOptions", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x20, 1, 248, None, [], []),
            "operation_status": MoPropertyMeta("operation_status", "operationStatus", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "progress": MoPropertyMeta("progress", "progress", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 256, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[ !#$=%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,768}""", [], []),
            "remote_share": MoPropertyMeta("remote_share", "remoteShare", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[ !#$=%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,768}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "dn": "dn", 
            "fileSize": "file_size", 
            "location": "location", 
            "map": "map", 
            "mountOptions": "mount_options", 
            "operationStatus": "operation_status", 
            "password": "password", 
            "progress": "progress", 
            "remoteFile": "remote_file", 
            "remoteShare": "remote_share", 
            "rn": "rn", 
            "status": "status", 
            "username": "username", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.child_action = None
        self.file_size = None
        self.location = None
        self.map = None
        self.mount_options = None
        self.operation_status = None
        self.password = None
        self.progress = None
        self.remote_file = None
        self.remote_share = None
        self.status = None
        self.username = None

        ManagedObject.__init__(self, "StorageFlexMMCDownloadFile", parent_mo_or_dn, **kwargs)

