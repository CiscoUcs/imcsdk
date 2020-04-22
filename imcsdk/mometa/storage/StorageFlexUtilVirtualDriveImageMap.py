"""This module contains the general information for StorageFlexUtilVirtualDriveImageMap ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexUtilVirtualDriveImageMapConsts:
    ADMIN_ACTION_MAP = "map"
    ADMIN_ACTION_UNMAP = "unmap"
    MAP_CIFS = "cifs"
    MAP_NFS = "nfs"
    MAP_WWW = "www"


class StorageFlexUtilVirtualDriveImageMap(ManagedObject):
    """This is StorageFlexUtilVirtualDriveImageMap class."""

    consts = StorageFlexUtilVirtualDriveImageMapConsts()
    naming_props = set(['virtualDrive'])

    mo_meta = {
        "classic": MoMeta("StorageFlexUtilVirtualDriveImageMap", "storageFlexUtilVirtualDriveImageMap", "vdrive-map-[virtual_drive]", VersionMeta.Version304a, "InputOutput", 0x7ff, [], ["admin", "read-only", "user"], ['storageFlexUtilController'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["map", "unmap"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version304a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "map": MoPropertyMeta("map", "map", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, ["cifs", "nfs", "www"], []),
            "mount_options": MoPropertyMeta("mount_options", "mountOptions", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x10, 1, 248, None, [], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,235}""", [], []),
            "remote_share": MoPropertyMeta("remote_share", "remoteShare", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,235}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, None, [], []),
            "virtual_drive": MoPropertyMeta("virtual_drive", "virtualDrive", "string", VersionMeta.Version304a, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "dn": "dn", 
            "map": "map", 
            "mountOptions": "mount_options", 
            "password": "password", 
            "remoteFile": "remote_file", 
            "remoteShare": "remote_share", 
            "rn": "rn", 
            "status": "status", 
            "username": "username", 
            "virtualDrive": "virtual_drive", 
        },

    }

    def __init__(self, parent_mo_or_dn, virtual_drive, **kwargs):
        self._dirty_mask = 0
        self.virtual_drive = virtual_drive
        self.admin_action = None
        self.child_action = None
        self.map = None
        self.mount_options = None
        self.password = None
        self.remote_file = None
        self.remote_share = None
        self.status = None
        self.username = None

        ManagedObject.__init__(self, "StorageFlexUtilVirtualDriveImageMap", parent_mo_or_dn, **kwargs)

