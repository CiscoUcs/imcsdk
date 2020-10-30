"""This module contains the general information for StorageVirtualDrive ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageVirtualDriveConsts:
    ACCESS_POLICY_ = ""
    ACCESS_POLICY_TRANSPORT_READY = "Transport Ready"
    ACCESS_POLICY_BLOCKED = "blocked"
    ACCESS_POLICY_DEFAULT = "default"
    ACCESS_POLICY_HIDDEN = "hidden"
    ACCESS_POLICY_READ_ONLY = "read-only"
    ACCESS_POLICY_READ_WRITE = "read-write"
    ADMIN_ACTION_CANCEL_INITIALIZATION = "cancel-initialization"
    ADMIN_ACTION_CLEAR_TRANSPORT_READY = "clear-transport-ready"
    ADMIN_ACTION_ENABLE_SELF_ENCRYPT = "enable-self-encrypt"
    ADMIN_ACTION_HIDE_VIRTUAL_DRIVE = "hide-virtual-drive"
    ADMIN_ACTION_RECONSTRUCT_VIRTUAL_DRIVE = "reconstruct-virtual-drive"
    ADMIN_ACTION_SET_BOOT_DRIVE = "set-boot-drive"
    ADMIN_ACTION_SET_TRANSPORT_READY = "set-transport-ready"
    ADMIN_ACTION_START_FAST_INITIALIZATION = "start-fast-initialization"
    ADMIN_ACTION_START_FULL_INITIALIZATION = "start-full-initialization"
    ADMIN_ACTION_UNHIDE_VIRTUAL_DRIVE = "unhide-virtual-drive"
    CACHE_POLICY_ = ""
    CACHE_POLICY_CACHED_IO = "cached-io"
    CACHE_POLICY_DEFAULT = "default"
    CACHE_POLICY_DIRECT_IO = "direct-io"
    DISK_CACHE_POLICY_ = ""
    DISK_CACHE_POLICY_DEFAULT = "default"
    DISK_CACHE_POLICY_DISABLED = "disabled"
    DISK_CACHE_POLICY_ENABLED = "enabled"
    DISK_CACHE_POLICY_UNCHANGED = "unchanged"
    HOTSPARE_ACTION_EXCLUDE_ALL = "exclude-all"
    HOTSPARE_ACTION_INCLUDE_ALL = "include-all"
    HOTSPARE_ACTION_INCLUDE_DHSP = "include-dhsp"
    RAID_LEVEL_0 = "0"
    RAID_LEVEL_1 = "1"
    RAID_LEVEL_5 = "5"
    RAID_LEVEL_6 = "6"
    READ_POLICY_ = ""
    READ_POLICY_ALWAYS_READ_AHEAD = "always-read-ahead"
    READ_POLICY_DEFAULT = "default"
    READ_POLICY_NO_READ_AHEAD = "no-read-ahead"
    REQUESTED_WRITE_CACHE_POLICY_ALWAYS_WRITE_BACK = "Always Write Back"
    REQUESTED_WRITE_CACHE_POLICY_WRITE_BACK_GOOD_BBU = "Write Back Good BBU"
    REQUESTED_WRITE_CACHE_POLICY_WRITE_THROUGH = "Write Through"
    _REQUESTED_WRITE_CACHE_POLICY_ALWAYS_WRITE_BACK = "always-write-back"
    REQUESTED_WRITE_CACHE_POLICY_DEFAULT = "default"
    _REQUESTED_WRITE_CACHE_POLICY_WRITE_BACK_GOOD_BBU = "write-back-good-bbu"
    _REQUESTED_WRITE_CACHE_POLICY_WRITE_THROUGH = "write-through"
    STRIP_SIZE_ = ""
    STRIP_SIZE_1024K = "1024k"
    STRIP_SIZE_128K = "128k"
    STRIP_SIZE_16K = "16k"
    STRIP_SIZE_256K = "256k"
    STRIP_SIZE_32K = "32k"
    STRIP_SIZE_512K = "512k"
    STRIP_SIZE_64K = "64k"
    STRIP_SIZE_8K = "8k"
    __REQUESTED_WRITE_CACHE_POLICY_ALWAYS_WRITE_BACK = "always-write-back"
    __REQUESTED_WRITE_CACHE_POLICY_WRITE_BACK_GOOD_BBU = "write-back-good-bbu"
    __REQUESTED_WRITE_CACHE_POLICY_WRITE_THROUGH = "write-through"


class StorageVirtualDrive(ManagedObject):
    """This is StorageVirtualDrive class."""

    consts = StorageVirtualDriveConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("StorageVirtualDrive", "storageVirtualDrive", "vd-[id]", VersionMeta.Version151f, "InputOutput", 0x7fff, [], ["admin", "read-only", "user"], ['storageController'], ['faultInst', 'storageLocalDiskUsage', 'storageOperation'], ["Get", "Remove", "Set"]),
        "modular": MoMeta("StorageVirtualDrive", "storageVirtualDrive", "vd-[id]", VersionMeta.Version2013e, "InputOutput", 0x7fff, [], ["admin", "read-only", "user"], ['storageController'], ['faultInst', 'storageLocalDiskUsage', 'storageOperation'], ["Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "access_policy": MoPropertyMeta("access_policy", "accessPolicy", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["", "Transport Ready", "blocked", "default", "hidden", "read-only", "read-write"], []),
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, ["cancel-initialization", "clear-transport-ready", "enable-self-encrypt", "hide-virtual-drive", "reconstruct-virtual-drive", "set-boot-drive", "set-transport-ready", "start-fast-initialization", "start-full-initialization", "unhide-virtual-drive"], []),
            "cache_policy": MoPropertyMeta("cache_policy", "cachePolicy", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "cached-io", "default", "direct-io"], []),
            "disk_cache_policy": MoPropertyMeta("disk_cache_policy", "diskCachePolicy", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "default", "disabled", "enabled", "unchanged"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "hotspare_action": MoPropertyMeta("hotspare_action", "hotspareAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, ["exclude-all", "include-all", "include-dhsp"], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x80, 0, 510, None, [], ["0-4294967295"]),
            "physical_drives_list": MoPropertyMeta("physical_drives_list", "physicalDrivesList", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x100, 1, 512, r"""(\d+(,\d+)*)""", [], []),
            "raid_level": MoPropertyMeta("raid_level", "raidLevel", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, 0, 510, None, ["0", "1", "5", "6"], []),
            "read_policy": MoPropertyMeta("read_policy", "readPolicy", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "always-read-ahead", "default", "no-read-ahead"], []),
            "requested_write_cache_policy": MoPropertyMeta("requested_write_cache_policy", "requestedWriteCachePolicy", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x800, 0, 510, None, ["Always Write Back", "Write Back Good BBU", "Write Through", "always-write-back", "default", "write-back-good-bbu", "write-through"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x1000, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "virtual_drive_name": MoPropertyMeta("virtual_drive_name", "virtualDriveName", "string", VersionMeta.Version208d, MoPropertyMeta.READ_WRITE, 0x4000, 0, 15, None, [], []),
            "allow_background_init": MoPropertyMeta("allow_background_init", "allowBackgroundInit", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "auto_delete_oldest": MoPropertyMeta("auto_delete_oldest", "autoDeleteOldest", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "auto_snapshot": MoPropertyMeta("auto_snapshot", "autoSnapshot", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "boot_drive": MoPropertyMeta("boot_drive", "bootDrive", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_write_cache_policy": MoPropertyMeta("current_write_cache_policy", "currentWriteCachePolicy", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "drive_state": MoPropertyMeta("drive_state", "driveState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "drives_per_span": MoPropertyMeta("drives_per_span", "drivesPerSpan", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "fde_capable": MoPropertyMeta("fde_capable", "fdeCapable", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "fde_enabled": MoPropertyMeta("fde_enabled", "fdeEnabled", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "span_depth": MoPropertyMeta("span_depth", "spanDepth", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "strip_size": MoPropertyMeta("strip_size", "stripSize", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "1024k", "128k", "16k", "256k", "32k", "512k", "64k", "8k"], []),
            "target_id": MoPropertyMeta("target_id", "targetId", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vd_status": MoPropertyMeta("vd_status", "vdStatus", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "write_cache_policy": MoPropertyMeta("write_cache_policy", "writeCachePolicy", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "access_policy": MoPropertyMeta("access_policy", "accessPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["blocked", "default", "read-only", "read-write"], []),
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, ["cancel-initialization", "clear-transport-ready", "enable-self-encrypt", "hide-virtual-drive", "reconstruct-virtual-drive", "set-boot-drive", "set-transport-ready", "start-fast-initialization", "start-full-initialization", "unhide-virtual-drive"], []),
            "cache_policy": MoPropertyMeta("cache_policy", "cachePolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, ["cached-io", "default", "direct-io"], []),
            "disk_cache_policy": MoPropertyMeta("disk_cache_policy", "diskCachePolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, ["default", "disabled", "enabled", "unchanged"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "hotspare_action": MoPropertyMeta("hotspare_action", "hotspareAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, ["exclude-all", "include-all", "include-dhsp"], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x80, 0, 510, None, [], ["0-4294967295"]),
            "physical_drives_list": MoPropertyMeta("physical_drives_list", "physicalDrivesList", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 1, 512, r"""(\d+(,\d+)*)""", [], []),
            "raid_level": MoPropertyMeta("raid_level", "raidLevel", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, 0, 510, None, ["0", "1", "5", "6"], []),
            "read_policy": MoPropertyMeta("read_policy", "readPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["always-read-ahead", "default", "no-read-ahead"], []),
            "requested_write_cache_policy": MoPropertyMeta("requested_write_cache_policy", "requestedWriteCachePolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, 0, 510, None, ["Always Write Back", "Write Back Good BBU", "Write Through", "always-write-back", "default", "write-back-good-bbu", "write-through"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "virtual_drive_name": MoPropertyMeta("virtual_drive_name", "virtualDriveName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000, 0, 15, None, [], []),
            "allow_background_init": MoPropertyMeta("allow_background_init", "allowBackgroundInit", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "auto_delete_oldest": MoPropertyMeta("auto_delete_oldest", "autoDeleteOldest", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "auto_snapshot": MoPropertyMeta("auto_snapshot", "autoSnapshot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "boot_drive": MoPropertyMeta("boot_drive", "bootDrive", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_write_cache_policy": MoPropertyMeta("current_write_cache_policy", "currentWriteCachePolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "drive_state": MoPropertyMeta("drive_state", "driveState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "drives_per_span": MoPropertyMeta("drives_per_span", "drivesPerSpan", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "fde_capable": MoPropertyMeta("fde_capable", "fdeCapable", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "no", "yes"], []),
            "fde_enabled": MoPropertyMeta("fde_enabled", "fdeEnabled", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "no", "yes"], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "read_ahead_policy": MoPropertyMeta("read_ahead_policy", "readAheadPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "span_depth": MoPropertyMeta("span_depth", "spanDepth", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "strip_size": MoPropertyMeta("strip_size", "stripSize", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "target_id": MoPropertyMeta("target_id", "targetId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vd_status": MoPropertyMeta("vd_status", "vdStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "write_cache_policy": MoPropertyMeta("write_cache_policy", "writeCachePolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "accessPolicy": "access_policy", 
            "adminAction": "admin_action", 
            "cachePolicy": "cache_policy", 
            "diskCachePolicy": "disk_cache_policy", 
            "dn": "dn", 
            "hotspareAction": "hotspare_action", 
            "id": "id", 
            "physicalDrivesList": "physical_drives_list", 
            "raidLevel": "raid_level", 
            "readPolicy": "read_policy", 
            "requestedWriteCachePolicy": "requested_write_cache_policy", 
            "rn": "rn", 
            "status": "status", 
            "virtualDriveName": "virtual_drive_name", 
            "allowBackgroundInit": "allow_background_init", 
            "autoDeleteOldest": "auto_delete_oldest", 
            "autoSnapshot": "auto_snapshot", 
            "bootDrive": "boot_drive", 
            "childAction": "child_action", 
            "currentWriteCachePolicy": "current_write_cache_policy", 
            "driveState": "drive_state", 
            "drivesPerSpan": "drives_per_span", 
            "fdeCapable": "fde_capable", 
            "fdeEnabled": "fde_enabled", 
            "health": "health", 
            "name": "name", 
            "size": "size", 
            "spanDepth": "span_depth", 
            "stripSize": "strip_size", 
            "targetId": "target_id", 
            "vdStatus": "vd_status", 
            "writeCachePolicy": "write_cache_policy", 
        },

        "modular": {
            "accessPolicy": "access_policy", 
            "adminAction": "admin_action", 
            "cachePolicy": "cache_policy", 
            "diskCachePolicy": "disk_cache_policy", 
            "dn": "dn", 
            "hotspareAction": "hotspare_action", 
            "id": "id", 
            "physicalDrivesList": "physical_drives_list", 
            "raidLevel": "raid_level", 
            "readPolicy": "read_policy", 
            "requestedWriteCachePolicy": "requested_write_cache_policy", 
            "rn": "rn", 
            "status": "status", 
            "virtualDriveName": "virtual_drive_name", 
            "allowBackgroundInit": "allow_background_init", 
            "autoDeleteOldest": "auto_delete_oldest", 
            "autoSnapshot": "auto_snapshot", 
            "bootDrive": "boot_drive", 
            "childAction": "child_action", 
            "currentWriteCachePolicy": "current_write_cache_policy", 
            "driveState": "drive_state", 
            "drivesPerSpan": "drives_per_span", 
            "fdeCapable": "fde_capable", 
            "fdeEnabled": "fde_enabled", 
            "health": "health", 
            "name": "name", 
            "readAheadPolicy": "read_ahead_policy", 
            "size": "size", 
            "spanDepth": "span_depth", 
            "stripSize": "strip_size", 
            "targetId": "target_id", 
            "vdStatus": "vd_status", 
            "writeCachePolicy": "write_cache_policy", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.access_policy = None
        self.admin_action = None
        self.cache_policy = None
        self.disk_cache_policy = None
        self.hotspare_action = None
        self.physical_drives_list = None
        self.raid_level = None
        self.read_policy = None
        self.requested_write_cache_policy = None
        self.status = None
        self.virtual_drive_name = None
        self.allow_background_init = None
        self.auto_delete_oldest = None
        self.auto_snapshot = None
        self.boot_drive = None
        self.child_action = None
        self.current_write_cache_policy = None
        self.drive_state = None
        self.drives_per_span = None
        self.fde_capable = None
        self.fde_enabled = None
        self.health = None
        self.name = None
        self.size = None
        self.span_depth = None
        self.strip_size = None
        self.target_id = None
        self.vd_status = None
        self.write_cache_policy = None
        self.read_ahead_policy = None

        ManagedObject.__init__(self, "StorageVirtualDrive", parent_mo_or_dn, **kwargs)

