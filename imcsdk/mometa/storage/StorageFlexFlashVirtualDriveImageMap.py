"""This module contains the general information for StorageFlexFlashVirtualDriveImageMap ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexFlashVirtualDriveImageMapConsts:
    ADMIN_ACTION_MAP = "map"
    ADMIN_ACTION_UNMAP = "unmap"
    MAP_CIFS = "cifs"
    MAP_NFS = "nfs"
    MAP_WWW = "www"


class StorageFlexFlashVirtualDriveImageMap(ManagedObject):
    """This is StorageFlexFlashVirtualDriveImageMap class."""

    consts = StorageFlexFlashVirtualDriveImageMapConsts()
    naming_props = set(['virtualDrive'])

    mo_meta = {
        "classic": MoMeta("StorageFlexFlashVirtualDriveImageMap", "storageFlexFlashVirtualDriveImageMap", "vdrive-map-[virtual_drive]", VersionMeta.Version202c, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], ['storageFlexFlashController'], [], ["Get", "Set"]),
        "modular": MoMeta("StorageFlexFlashVirtualDriveImageMap", "storageFlexFlashVirtualDriveImageMap", "vdrive-map-[virtual_drive]", VersionMeta.Version2013e, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], ['storageFlexFlashController'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["map", "unmap"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "map": MoPropertyMeta("map", "map", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, ["cifs", "nfs", "www"], []),
            "mount_options": MoPropertyMeta("mount_options", "mountOptions", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x10, 1, 248, None, [], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,255}""", [], []),
            "remote_share": MoPropertyMeta("remote_share", "remoteShare", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,235}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "to_enable_mapping": MoPropertyMeta("to_enable_mapping", "toEnableMapping", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "virtual_drive": MoPropertyMeta("virtual_drive", "virtualDrive", "string", VersionMeta.Version202c, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["map", "unmap"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "map": MoPropertyMeta("map", "map", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, ["cifs", "nfs"], []),
            "mount_options": MoPropertyMeta("mount_options", "mountOptions", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 1, 248, None, [], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,255}""", [], []),
            "remote_share": MoPropertyMeta("remote_share", "remoteShare", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,235}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "to_enable_mapping": MoPropertyMeta("to_enable_mapping", "toEnableMapping", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["No", "Yes", "no", "yes"], []),
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "virtual_drive": MoPropertyMeta("virtual_drive", "virtualDrive", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
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
            "toEnableMapping": "to_enable_mapping", 
            "username": "username", 
            "childAction": "child_action", 
            "virtualDrive": "virtual_drive", 
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
            "toEnableMapping": "to_enable_mapping", 
            "username": "username", 
            "childAction": "child_action", 
            "virtualDrive": "virtual_drive", 
        },

    }

    def __init__(self, parent_mo_or_dn, virtual_drive, **kwargs):
        self._dirty_mask = 0
        self.virtual_drive = virtual_drive
        self.admin_action = None
        self.map = None
        self.mount_options = None
        self.password = None
        self.remote_file = None
        self.remote_share = None
        self.status = None
        self.to_enable_mapping = None
        self.username = None
        self.child_action = None

        ManagedObject.__init__(self, "StorageFlexFlashVirtualDriveImageMap", parent_mo_or_dn, **kwargs)

