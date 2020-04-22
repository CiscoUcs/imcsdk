"""This module contains the general information for StorageVirtualDriveCreatorUsingUnusedPhysicalDrive ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageVirtualDriveCreatorUsingUnusedPhysicalDriveConsts:
    ACCESS_POLICY_ = ""
    ACCESS_POLICY_BLOCKED = "blocked"
    ACCESS_POLICY_DEFAULT = "default"
    ACCESS_POLICY_HIDDEN = "hidden"
    ACCESS_POLICY_READ_ONLY = "read-only"
    ACCESS_POLICY_READ_WRITE = "read-write"
    ADMIN_ACTION_ENABLE_SELF_ENCRYPT = "enable-self-encrypt"
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
    RAID_LEVEL_ = ""
    RAID_LEVEL_0 = "0"
    RAID_LEVEL_1 = "1"
    RAID_LEVEL_10 = "10"
    RAID_LEVEL_5 = "5"
    RAID_LEVEL_50 = "50"
    RAID_LEVEL_6 = "6"
    RAID_LEVEL_60 = "60"
    READ_POLICY_ = ""
    READ_POLICY_ALWAYS_READ_AHEAD = "always-read-ahead"
    READ_POLICY_DEFAULT = "default"
    READ_POLICY_NO_READ_AHEAD = "no-read-ahead"
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


class StorageVirtualDriveCreatorUsingUnusedPhysicalDrive(ManagedObject):
    """This is StorageVirtualDriveCreatorUsingUnusedPhysicalDrive class."""

    consts = StorageVirtualDriveCreatorUsingUnusedPhysicalDriveConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StorageVirtualDriveCreatorUsingUnusedPhysicalDrive", "storageVirtualDriveCreatorUsingUnusedPhysicalDrive", "virtual-drive-create", VersionMeta.Version201a, "InputOutput", 0xffff, [], ["admin"], ['storageController'], ['storageUnusedLocalDisk'], ["Get", "Set"]),
        "modular": MoMeta("StorageVirtualDriveCreatorUsingUnusedPhysicalDrive", "storageVirtualDriveCreatorUsingUnusedPhysicalDrive", "virtual-drive-create", VersionMeta.Version2013e, "InputOutput", 0xffff, [], ["admin"], ['storageController'], ['storageUnusedLocalDisk'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "access_policy": MoPropertyMeta("access_policy", "accessPolicy", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["", "blocked", "default", "hidden", "read-only", "read-write"], []),
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, ["enable-self-encrypt"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["trigger", "triggered"], []),
            "cache_policy": MoPropertyMeta("cache_policy", "cachePolicy", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "cached-io", "default", "direct-io"], []),
            "disk_cache_policy": MoPropertyMeta("disk_cache_policy", "diskCachePolicy", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "default", "disabled", "enabled", "unchanged"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "drive_group": MoPropertyMeta("drive_group", "driveGroup", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x80, 1, 512, r"""((\[\d+(,\d+)*\])(\[\d+(,\d+)*\])*)""", [], []),
            "raid_level": MoPropertyMeta("raid_level", "raidLevel", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "0", "1", "10", "5", "50", "6", "60"], []),
            "read_policy": MoPropertyMeta("read_policy", "readPolicy", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "always-read-ahead", "default", "no-read-ahead"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x400, 0, 255, None, [], []),
            "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x800, 1, 20, r"""(\d+\s?([MGT]B)?)""", [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "strip_size": MoPropertyMeta("strip_size", "stripSize", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["", "1024k", "128k", "16k", "256k", "32k", "512k", "64k", "8k", "default"], []),
            "virtual_drive_name": MoPropertyMeta("virtual_drive_name", "virtualDriveName", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x4000, 0, 15, None, [], []),
            "write_policy": MoPropertyMeta("write_policy", "writePolicy", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["", "Always Write Back", "Write Back Good BBU", "Write Through", "always-write-back", "default", "write-back-good-bbu", "write-through"], []),
            "created_virtual_drive_dn": MoPropertyMeta("created_virtual_drive_dn", "createdVirtualDriveDn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "min_required_physical_drives": MoPropertyMeta("min_required_physical_drives", "minRequiredPhysicalDrives", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "oper_status": MoPropertyMeta("oper_status", "operStatus", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "access_policy": MoPropertyMeta("access_policy", "accessPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["", "blocked", "default", "hidden", "read-only", "read-write"], []),
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, ["enable-self-encrypt"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["trigger", "triggered"], []),
            "cache_policy": MoPropertyMeta("cache_policy", "cachePolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "cached-io", "default", "direct-io"], []),
            "disk_cache_policy": MoPropertyMeta("disk_cache_policy", "diskCachePolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "default", "disabled", "enabled", "unchanged"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "drive_group": MoPropertyMeta("drive_group", "driveGroup", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 1, 512, r"""((\[\d+(,\d+)*\])(\[\d+(,\d+)*\])*)""", [], []),
            "raid_level": MoPropertyMeta("raid_level", "raidLevel", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "0", "1", "10", "5", "50", "6", "60"], []),
            "read_policy": MoPropertyMeta("read_policy", "readPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "always-read-ahead", "default", "no-read-ahead"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, 0, 255, None, [], []),
            "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, 1, 20, r"""(\d+\s?([MGT]B)?)""", [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "strip_size": MoPropertyMeta("strip_size", "stripSize", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, 0, 510, None, ["1024k", "128k", "256k", "512k", "64k", "default"], []),
            "virtual_drive_name": MoPropertyMeta("virtual_drive_name", "virtualDriveName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000, 0, 15, None, [], []),
            "write_policy": MoPropertyMeta("write_policy", "writePolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["", "Always Write Back", "Write Back Good BBU", "Write Through", "default"], []),
            "created_virtual_drive_dn": MoPropertyMeta("created_virtual_drive_dn", "createdVirtualDriveDn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "min_required_physical_drives": MoPropertyMeta("min_required_physical_drives", "minRequiredPhysicalDrives", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "oper_status": MoPropertyMeta("oper_status", "operStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "accessPolicy": "access_policy", 
            "adminAction": "admin_action", 
            "adminState": "admin_state", 
            "cachePolicy": "cache_policy", 
            "diskCachePolicy": "disk_cache_policy", 
            "dn": "dn", 
            "driveGroup": "drive_group", 
            "raidLevel": "raid_level", 
            "readPolicy": "read_policy", 
            "rn": "rn", 
            "size": "size", 
            "status": "status", 
            "stripSize": "strip_size", 
            "virtualDriveName": "virtual_drive_name", 
            "writePolicy": "write_policy", 
            "createdVirtualDriveDn": "created_virtual_drive_dn", 
            "description": "description", 
            "minRequiredPhysicalDrives": "min_required_physical_drives", 
            "operStatus": "oper_status", 
        },

        "modular": {
            "accessPolicy": "access_policy", 
            "adminAction": "admin_action", 
            "adminState": "admin_state", 
            "cachePolicy": "cache_policy", 
            "diskCachePolicy": "disk_cache_policy", 
            "dn": "dn", 
            "driveGroup": "drive_group", 
            "raidLevel": "raid_level", 
            "readPolicy": "read_policy", 
            "rn": "rn", 
            "size": "size", 
            "status": "status", 
            "stripSize": "strip_size", 
            "virtualDriveName": "virtual_drive_name", 
            "writePolicy": "write_policy", 
            "createdVirtualDriveDn": "created_virtual_drive_dn", 
            "description": "description", 
            "minRequiredPhysicalDrives": "min_required_physical_drives", 
            "operStatus": "oper_status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.access_policy = None
        self.admin_action = None
        self.admin_state = None
        self.cache_policy = None
        self.disk_cache_policy = None
        self.drive_group = None
        self.raid_level = None
        self.read_policy = None
        self.size = None
        self.status = None
        self.strip_size = None
        self.virtual_drive_name = None
        self.write_policy = None
        self.created_virtual_drive_dn = None
        self.description = None
        self.min_required_physical_drives = None
        self.oper_status = None

        ManagedObject.__init__(self, "StorageVirtualDriveCreatorUsingUnusedPhysicalDrive", parent_mo_or_dn, **kwargs)

