"""This module contains the general information for CommSavedVMediaMap ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommSavedVMediaMapConsts:
    ADMIN_ACTION_DELETE_VOLUME = "delete-volume"
    ADMIN_ACTION_REMAP_VOLUME = "remap-volume"
    DRIVE_TYPE_CD = "cd"
    DRIVE_TYPE_FLOPPY = "floppy"
    MAP_CIFS = "cifs"
    MAP_NFS = "nfs"
    MAP_WWW = "www"


class CommSavedVMediaMap(ManagedObject):
    """This is CommSavedVMediaMap class."""

    consts = CommSavedVMediaMapConsts()
    naming_props = set(['volumeName'])

    mo_meta = {
        "classic": MoMeta("CommSavedVMediaMap", "commSavedVMediaMap", "saved-vmmap-[volume_name]", VersionMeta.Version301c, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['commVMedia'], [], ["Get", "Remove", "Set"]),
        "modular": MoMeta("CommSavedVMediaMap", "commSavedVMediaMap", "saved-vmmap-[volume_name]", VersionMeta.Version301c, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['commVMedia'], [], ["Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete-volume", "remap-volume"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "volume_name": MoPropertyMeta("volume_name", "volumeName", "string", VersionMeta.Version301c, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,47}""", [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "drive_type": MoPropertyMeta("drive_type", "driveType", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cd", "floppy"], []),
            "map": MoPropertyMeta("map", "map", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cifs", "nfs", "www"], []),
            "mount_options": MoPropertyMeta("mount_options", "mountOptions", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 248, None, [], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$=%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,255}""", [], []),
            "remote_share": MoPropertyMeta("remote_share", "remoteShare", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,235}""", [], []),
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete-volume", "remap-volume"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "volume_name": MoPropertyMeta("volume_name", "volumeName", "string", VersionMeta.Version301c, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,47}""", [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "drive_type": MoPropertyMeta("drive_type", "driveType", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cd", "floppy"], []),
            "map": MoPropertyMeta("map", "map", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cifs", "nfs", "www"], []),
            "mount_options": MoPropertyMeta("mount_options", "mountOptions", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 1, 248, None, [], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,235}""", [], []),
            "remote_share": MoPropertyMeta("remote_share", "remoteShare", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,235}""", [], []),
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "volumeName": "volume_name", 
            "childAction": "child_action", 
            "driveType": "drive_type", 
            "map": "map", 
            "mountOptions": "mount_options", 
            "password": "password", 
            "remoteFile": "remote_file", 
            "remoteShare": "remote_share", 
            "username": "username", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "volumeName": "volume_name", 
            "childAction": "child_action", 
            "driveType": "drive_type", 
            "map": "map", 
            "mountOptions": "mount_options", 
            "password": "password", 
            "remoteFile": "remote_file", 
            "remoteShare": "remote_share", 
            "username": "username", 
        },

    }

    def __init__(self, parent_mo_or_dn, volume_name, **kwargs):
        self._dirty_mask = 0
        self.volume_name = volume_name
        self.admin_action = None
        self.status = None
        self.child_action = None
        self.drive_type = None
        self.map = None
        self.mount_options = None
        self.password = None
        self.remote_file = None
        self.remote_share = None
        self.username = None

        ManagedObject.__init__(self, "CommSavedVMediaMap", parent_mo_or_dn, **kwargs)

