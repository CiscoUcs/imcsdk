"""This module contains the general information for StorageFlexFlashOperationalProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexFlashOperationalProfileConsts:
    ADMIN_ACTION_CLEAR_ERRORS = "clear-errors"
    RAID_PRIMARY_MEMBER_SLOT_1 = "slot-1"
    RAID_PRIMARY_MEMBER_SLOT_2 = "slot-2"
    RAID_SECONDARY_ROLE_ACTIVE = "active"
    RAID_SECONDARY_ROLE_INITIALIZING = "initializing"


class StorageFlexFlashOperationalProfile(ManagedObject):
    """This is StorageFlexFlashOperationalProfile class."""

    consts = StorageFlexFlashOperationalProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StorageFlexFlashOperationalProfile", "storageFlexFlashOperationalProfile", "oper-profile", VersionMeta.Version202c, "InputOutput", 0x3fff, [], ["admin", "read-only", "user"], ['storageFlexFlashController'], [], ["Get", "Set"]),
        "modular": MoMeta("StorageFlexFlashOperationalProfile", "storageFlexFlashOperationalProfile", "oper-profile", VersionMeta.Version2013e, "InputOutput", 0x3fff, [], ["admin", "read-only", "user"], ['storageFlexFlashController'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear-errors"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "io_read_error_threshold": MoPropertyMeta("io_read_error_threshold", "ioReadErrorThreshold", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], ["0-255"]),
            "io_write_error_threshold": MoPropertyMeta("io_write_error_threshold", "ioWriteErrorThreshold", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], ["0-255"]),
            "raid_primary_member": MoPropertyMeta("raid_primary_member", "raidPrimaryMember", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, ["slot-1", "slot-2"], []),
            "raid_secondary_role": MoPropertyMeta("raid_secondary_role", "raidSecondaryRole", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, ["active", "initializing"], []),
            "rd_err_count_slot1_threshold": MoPropertyMeta("rd_err_count_slot1_threshold", "rdErrCountSlot1Threshold", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], ["0-255"]),
            "rd_err_count_slot2_threshold": MoPropertyMeta("rd_err_count_slot2_threshold", "rdErrCountSlot2Threshold", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, [], ["0-255"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "virtual_drives_enabled": MoPropertyMeta("virtual_drives_enabled", "virtualDrivesEnabled", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x800, 0, 30, None, [], []),
            "wr_err_count_slot1_threshold": MoPropertyMeta("wr_err_count_slot1_threshold", "wrErrCountSlot1Threshold", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x1000, 0, 510, None, [], ["0-255"]),
            "wr_err_count_slot2_threshold": MoPropertyMeta("wr_err_count_slot2_threshold", "wrErrCountSlot2Threshold", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2000, 0, 510, None, [], ["0-255"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "controller": MoPropertyMeta("controller", "controller", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "operating_mode": MoPropertyMeta("operating_mode", "operatingMode", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear-errors"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "io_read_error_threshold": MoPropertyMeta("io_read_error_threshold", "ioReadErrorThreshold", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], []),
            "io_write_error_threshold": MoPropertyMeta("io_write_error_threshold", "ioWriteErrorThreshold", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], []),
            "raid_primary_member": MoPropertyMeta("raid_primary_member", "raidPrimaryMember", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, ["slot-1", "slot-2"], []),
            "raid_secondary_role": MoPropertyMeta("raid_secondary_role", "raidSecondaryRole", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, ["active", "initializing"], []),
            "rd_err_count_slot1_threshold": MoPropertyMeta("rd_err_count_slot1_threshold", "rdErrCountSlot1Threshold", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], []),
            "rd_err_count_slot2_threshold": MoPropertyMeta("rd_err_count_slot2_threshold", "rdErrCountSlot2Threshold", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "virtual_drives_enabled": MoPropertyMeta("virtual_drives_enabled", "virtualDrivesEnabled", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, 0, 30, None, [], []),
            "wr_err_count_slot1_threshold": MoPropertyMeta("wr_err_count_slot1_threshold", "wrErrCountSlot1Threshold", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, 0, 510, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], []),
            "wr_err_count_slot2_threshold": MoPropertyMeta("wr_err_count_slot2_threshold", "wrErrCountSlot2Threshold", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, 0, 510, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "controller": MoPropertyMeta("controller", "controller", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "operating_mode": MoPropertyMeta("operating_mode", "operatingMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "ioReadErrorThreshold": "io_read_error_threshold", 
            "ioWriteErrorThreshold": "io_write_error_threshold", 
            "raidPrimaryMember": "raid_primary_member", 
            "raidSecondaryRole": "raid_secondary_role", 
            "rdErrCountSlot1Threshold": "rd_err_count_slot1_threshold", 
            "rdErrCountSlot2Threshold": "rd_err_count_slot2_threshold", 
            "rn": "rn", 
            "status": "status", 
            "virtualDrivesEnabled": "virtual_drives_enabled", 
            "wrErrCountSlot1Threshold": "wr_err_count_slot1_threshold", 
            "wrErrCountSlot2Threshold": "wr_err_count_slot2_threshold", 
            "childAction": "child_action", 
            "controller": "controller", 
            "operatingMode": "operating_mode", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "ioReadErrorThreshold": "io_read_error_threshold", 
            "ioWriteErrorThreshold": "io_write_error_threshold", 
            "raidPrimaryMember": "raid_primary_member", 
            "raidSecondaryRole": "raid_secondary_role", 
            "rdErrCountSlot1Threshold": "rd_err_count_slot1_threshold", 
            "rdErrCountSlot2Threshold": "rd_err_count_slot2_threshold", 
            "rn": "rn", 
            "status": "status", 
            "virtualDrivesEnabled": "virtual_drives_enabled", 
            "wrErrCountSlot1Threshold": "wr_err_count_slot1_threshold", 
            "wrErrCountSlot2Threshold": "wr_err_count_slot2_threshold", 
            "childAction": "child_action", 
            "controller": "controller", 
            "operatingMode": "operating_mode", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.io_read_error_threshold = None
        self.io_write_error_threshold = None
        self.raid_primary_member = None
        self.raid_secondary_role = None
        self.rd_err_count_slot1_threshold = None
        self.rd_err_count_slot2_threshold = None
        self.status = None
        self.virtual_drives_enabled = None
        self.wr_err_count_slot1_threshold = None
        self.wr_err_count_slot2_threshold = None
        self.child_action = None
        self.controller = None
        self.operating_mode = None

        ManagedObject.__init__(self, "StorageFlexFlashOperationalProfile", parent_mo_or_dn, **kwargs)

