"""This module contains the general information for StorageVirtualDriveCreatorUsingVirtualDriveGroup ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageVirtualDriveCreatorUsingVirtualDriveGroupConsts:
    ACCESS_POLICY_ = ""
    ACCESS_POLICY_BLOCKED = "blocked"
    ACCESS_POLICY_DEFAULT = "default"
    ACCESS_POLICY_HIDDEN = "hidden"
    ACCESS_POLICY_READ_ONLY = "read-only"
    ACCESS_POLICY_READ_WRITE = "read-write"
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"
    CACHE_POLICY_ = ""
    CACHE_POLICY_CACHED_IO = "cached-io"
    CACHE_POLICY_DEFAULT = "default"
    CACHE_POLICY_DIRECT_IO = "direct-io"
    DISK_CACHE_POLICY_ = ""
    DISK_CACHE_POLICY_DEFAULT = "default"
    DISK_CACHE_POLICY_DISABLED = "disabled"
    DISK_CACHE_POLICY_ENABLED = "enabled"
    DISK_CACHE_POLICY_UNCHANGED = "unchanged"
    READ_POLICY_ = ""
    READ_POLICY_ALWAYS_READ_AHEAD = "always-read-ahead"
    READ_POLICY_DEFAULT = "default"
    READ_POLICY_NO_READ_AHEAD = "no-read-ahead"
    SHARED_VIRTUAL_DRIVE_ID_ = ""
    STRIP_SIZE_ = ""
    STRIP_SIZE_1024K = "1024k"
    STRIP_SIZE_128K = "128k"
    STRIP_SIZE_16K = "16k"
    STRIP_SIZE_256K = "256k"
    STRIP_SIZE_32K = "32k"
    STRIP_SIZE_512K = "512k"
    STRIP_SIZE_64K = "64k"
    STRIP_SIZE_8K = "8k"
    STRIP_SIZE_DEFAULT = "default"
    WRITE_POLICY_ = ""
    WRITE_POLICY_ALWAYS_WRITE_BACK = "Always Write Back"
    WRITE_POLICY_WRITE_BACK_GOOD_BBU = "Write Back Good BBU"
    WRITE_POLICY_WRITE_THROUGH = "Write Through"
    _WRITE_POLICY_ALWAYS_WRITE_BACK = "always-write-back"
    WRITE_POLICY_DEFAULT = "default"
    _WRITE_POLICY_WRITE_BACK_GOOD_BBU = "write-back-good-bbu"
    _WRITE_POLICY_WRITE_THROUGH = "write-through"


class StorageVirtualDriveCreatorUsingVirtualDriveGroup(ManagedObject):
    """This is StorageVirtualDriveCreatorUsingVirtualDriveGroup class."""

    consts = StorageVirtualDriveCreatorUsingVirtualDriveGroupConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StorageVirtualDriveCreatorUsingVirtualDriveGroup", "storageVirtualDriveCreatorUsingVirtualDriveGroup", "virtual-drive-carve", VersionMeta.Version201a, "InputOutput", 0x3fff, [], ["admin"], ['storageController'], ['storageVirtualDriveWithDriveGroupSpace'], ["Get", "Set"]),
        "modular": MoMeta("StorageVirtualDriveCreatorUsingVirtualDriveGroup", "storageVirtualDriveCreatorUsingVirtualDriveGroup", "virtual-drive-carve", VersionMeta.Version2013e, "InputOutput", 0x3fff, [], ["admin"], ['storageController'], ['storageVirtualDriveWithDriveGroupSpace'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "access_policy": MoPropertyMeta("access_policy", "accessPolicy", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["", "blocked", "default", "hidden", "read-only", "read-write"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["trigger", "triggered"], []),
            "cache_policy": MoPropertyMeta("cache_policy", "cachePolicy", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "cached-io", "default", "direct-io"], []),
            "disk_cache_policy": MoPropertyMeta("disk_cache_policy", "diskCachePolicy", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "default", "disabled", "enabled", "unchanged"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "read_policy": MoPropertyMeta("read_policy", "readPolicy", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "always-read-ahead", "default", "no-read-ahead"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "shared_virtual_drive_id": MoPropertyMeta("shared_virtual_drive_id", "sharedVirtualDriveId", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [""], ["0-4294967295"]),
            "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x200, 1, 20, r"""(\d+\s?([MGT]B)?)""", [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "strip_size": MoPropertyMeta("strip_size", "stripSize", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["", "1024k", "128k", "16k", "256k", "32k", "512k", "64k", "8k", "default"], []),
            "virtual_drive_name": MoPropertyMeta("virtual_drive_name", "virtualDriveName", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x1000, 0, 15, None, [], []),
            "write_policy": MoPropertyMeta("write_policy", "writePolicy", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["", "Always Write Back", "Write Back Good BBU", "Write Through", "always-write-back", "default", "write-back-good-bbu", "write-through"], []),
            "created_virtual_drive_dn": MoPropertyMeta("created_virtual_drive_dn", "createdVirtualDriveDn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "oper_status": MoPropertyMeta("oper_status", "operStatus", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "access_policy": MoPropertyMeta("access_policy", "accessPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["", "blocked", "default", "hidden", "read-only", "read-write"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["trigger", "triggered"], []),
            "cache_policy": MoPropertyMeta("cache_policy", "cachePolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "cached-io", "default", "direct-io"], []),
            "disk_cache_policy": MoPropertyMeta("disk_cache_policy", "diskCachePolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "default", "disabled", "enabled", "unchanged"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "read_policy": MoPropertyMeta("read_policy", "readPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "always-read-ahead", "default", "no-read-ahead"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "shared_virtual_drive_id": MoPropertyMeta("shared_virtual_drive_id", "sharedVirtualDriveId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, [], ["0-4294967295"]),
            "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, 1, 20, r"""(\d+\s?([MGT]B)?)""", [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "strip_size": MoPropertyMeta("strip_size", "stripSize", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, 0, 510, None, ["1024k", "128k", "256k", "512k", "64k", "default"], []),
            "virtual_drive_name": MoPropertyMeta("virtual_drive_name", "virtualDriveName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, 0, 15, None, [], []),
            "write_policy": MoPropertyMeta("write_policy", "writePolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["", "Always Write Back", "Write Back Good BBU", "Write Through", "default"], []),
            "created_virtual_drive_dn": MoPropertyMeta("created_virtual_drive_dn", "createdVirtualDriveDn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "oper_status": MoPropertyMeta("oper_status", "operStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "accessPolicy": "access_policy", 
            "adminState": "admin_state", 
            "cachePolicy": "cache_policy", 
            "diskCachePolicy": "disk_cache_policy", 
            "dn": "dn", 
            "readPolicy": "read_policy", 
            "rn": "rn", 
            "sharedVirtualDriveId": "shared_virtual_drive_id", 
            "size": "size", 
            "status": "status", 
            "stripSize": "strip_size", 
            "virtualDriveName": "virtual_drive_name", 
            "writePolicy": "write_policy", 
            "createdVirtualDriveDn": "created_virtual_drive_dn", 
            "description": "description", 
            "operStatus": "oper_status", 
        },

        "modular": {
            "accessPolicy": "access_policy", 
            "adminState": "admin_state", 
            "cachePolicy": "cache_policy", 
            "diskCachePolicy": "disk_cache_policy", 
            "dn": "dn", 
            "readPolicy": "read_policy", 
            "rn": "rn", 
            "sharedVirtualDriveId": "shared_virtual_drive_id", 
            "size": "size", 
            "status": "status", 
            "stripSize": "strip_size", 
            "virtualDriveName": "virtual_drive_name", 
            "writePolicy": "write_policy", 
            "createdVirtualDriveDn": "created_virtual_drive_dn", 
            "description": "description", 
            "operStatus": "oper_status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.access_policy = None
        self.admin_state = None
        self.cache_policy = None
        self.disk_cache_policy = None
        self.read_policy = None
        self.shared_virtual_drive_id = None
        self.size = None
        self.status = None
        self.strip_size = None
        self.virtual_drive_name = None
        self.write_policy = None
        self.created_virtual_drive_dn = None
        self.description = None
        self.oper_status = None

        ManagedObject.__init__(self, "StorageVirtualDriveCreatorUsingVirtualDriveGroup", parent_mo_or_dn, **kwargs)

