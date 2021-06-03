"""This module contains the general information for CommVMediaMap ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommVMediaMapConsts:
    ADMIN_ACTION_SAVE_UNMAPPED_VOLUME = "save-unmapped-volume"
    DRIVE_TYPE_CD = "cd"
    DRIVE_TYPE_FLOPPY = "floppy"
    MAP_CIFS = "cifs"
    MAP_LOCAL = "local"
    MAP_NFS = "nfs"
    MAP_WWW = "www"


class CommVMediaMap(ManagedObject):
    """This is CommVMediaMap class."""

    consts = CommVMediaMapConsts()
    naming_props = set(['volumeName'])

    mo_meta = {
        "classic": MoMeta("CommVMediaMap", "commVMediaMap", "vmmap-[volume_name]", VersionMeta.Version151f, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], ['commVMedia'], [], ["Add", "Get"]),
        "modular": MoMeta("CommVMediaMap", "commVMediaMap", "vmmap-[volume_name]", VersionMeta.Version2013e, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], ['commVMedia'], [], ["Add", "Get"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["save-unmapped-volume"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "map": MoPropertyMeta("map", "map", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["cifs", "local", "nfs", "www"], []),
            "mount_options": MoPropertyMeta("mount_options", "mountOptions", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 1, 248, None, [], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[ !#$=%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,768}""", [], []),
            "remote_share": MoPropertyMeta("remote_share", "remoteShare", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[ !#$=%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,768}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x400, 0, 255, None, [], []),
            "volume_name": MoPropertyMeta("volume_name", "volumeName", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x800, None, None, r"""[\-\.:_a-zA-Z0-9]{1,47}""", [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "drive_type": MoPropertyMeta("drive_type", "driveType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cd", "floppy"], []),
            "mapping_status": MoPropertyMeta("mapping_status", "mappingStatus", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["save-unmapped-volume"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "map": MoPropertyMeta("map", "map", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["cifs", "nfs", "www"], []),
            "mount_options": MoPropertyMeta("mount_options", "mountOptions", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 1, 248, None, [], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[ !#$%&\(\)\+,\-\./:\?@\[\]_\{\}=~a-zA-Z0-9]{1,768}""", [], []),
            "remote_share": MoPropertyMeta("remote_share", "remoteShare", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[ !#$%&\(\)\+,\-\./:\?@\[\]_\{\}~a-zA-Z0-9]{1,768}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, 0, 255, None, [], []),
            "volume_name": MoPropertyMeta("volume_name", "volumeName", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x800, None, None, r"""[\-\.:_a-zA-Z0-9]{1,47}""", [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "drive_type": MoPropertyMeta("drive_type", "driveType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cd", "floppy"], []),
            "mapping_status": MoPropertyMeta("mapping_status", "mappingStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "map": "map", 
            "mountOptions": "mount_options", 
            "password": "password", 
            "remoteFile": "remote_file", 
            "remoteShare": "remote_share", 
            "rn": "rn", 
            "status": "status", 
            "username": "username", 
            "volumeName": "volume_name", 
            "childAction": "child_action", 
            "driveType": "drive_type", 
            "mappingStatus": "mapping_status", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "map": "map", 
            "mountOptions": "mount_options", 
            "password": "password", 
            "remoteFile": "remote_file", 
            "remoteShare": "remote_share", 
            "rn": "rn", 
            "status": "status", 
            "username": "username", 
            "volumeName": "volume_name", 
            "childAction": "child_action", 
            "driveType": "drive_type", 
            "mappingStatus": "mapping_status", 
        },

    }

    def __init__(self, parent_mo_or_dn, volume_name, **kwargs):
        self._dirty_mask = 0
        self.volume_name = volume_name
        self.admin_action = None
        self.map = None
        self.mount_options = None
        self.password = None
        self.remote_file = None
        self.remote_share = None
        self.status = None
        self.username = None
        self.child_action = None
        self.drive_type = None
        self.mapping_status = None

        ManagedObject.__init__(self, "CommVMediaMap", parent_mo_or_dn, **kwargs)

