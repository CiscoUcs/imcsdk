"""This module contains the general information for StorageEnclosureDisk ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageEnclosureDiskConsts:
    DRIVE_POWER_POLICY_N_A = "N/A"
    DRIVE_POWER_POLICY_ACTIVE = "active"
    DRIVE_POWER_POLICY_POWER_SAVE = "power-save"
    DRIVE_POWER_POLICY_TRANSITIONING = "transitioning"
    DRIVE_POWER_POLICY_UNKNOWN = "unknown"


class StorageEnclosureDisk(ManagedObject):
    """This is StorageEnclosureDisk class."""

    consts = StorageEnclosureDiskConsts()
    naming_props = set(['slot'])

    mo_meta = {
        "modular": MoMeta("StorageEnclosureDisk", "storageEnclosureDisk", "disk-[slot]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageEnclosure'], [], ["Get"])
    }


    prop_meta = {

        "modular": {
            "blockcount": MoPropertyMeta("blockcount", "blockcount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "blocksize": MoPropertyMeta("blocksize", "blocksize", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "diskstate": MoPropertyMeta("diskstate", "diskstate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "drive_power_policy": MoPropertyMeta("drive_power_policy", "drivePowerPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A", "active", "power-save", "transitioning", "unknown"], []),
            "expander1linkspeed": MoPropertyMeta("expander1linkspeed", "expander1linkspeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "expander2linkspeed": MoPropertyMeta("expander2linkspeed", "expander2linkspeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "fw_update_oper_state": MoPropertyMeta("fw_update_oper_state", "fwUpdateOperState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "fw_update_progress": MoPropertyMeta("fw_update_progress", "fwUpdateProgress", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "ownership": MoPropertyMeta("ownership", "ownership", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_id": MoPropertyMeta("product_id", "productId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "sasaddress1": MoPropertyMeta("sasaddress1", "sasaddress1", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sasaddress2": MoPropertyMeta("sasaddress2", "sasaddress2", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "modular": {
            "blockcount": "blockcount", 
            "blocksize": "blocksize", 
            "childAction": "child_action", 
            "diskstate": "diskstate", 
            "dn": "dn", 
            "drivePowerPolicy": "drive_power_policy", 
            "expander1linkspeed": "expander1linkspeed", 
            "expander2linkspeed": "expander2linkspeed", 
            "fwUpdateOperState": "fw_update_oper_state", 
            "fwUpdateProgress": "fw_update_progress", 
            "health": "health", 
            "ownership": "ownership", 
            "productId": "product_id", 
            "revision": "revision", 
            "rn": "rn", 
            "sasaddress1": "sasaddress1", 
            "sasaddress2": "sasaddress2", 
            "serial": "serial", 
            "size": "size", 
            "slot": "slot", 
            "status": "status", 
            "vendor": "vendor", 
        },

    }

    def __init__(self, parent_mo_or_dn, slot, **kwargs):
        self._dirty_mask = 0
        self.slot = slot
        self.blockcount = None
        self.blocksize = None
        self.child_action = None
        self.diskstate = None
        self.drive_power_policy = None
        self.expander1linkspeed = None
        self.expander2linkspeed = None
        self.fw_update_oper_state = None
        self.fw_update_progress = None
        self.health = None
        self.ownership = None
        self.product_id = None
        self.revision = None
        self.sasaddress1 = None
        self.sasaddress2 = None
        self.serial = None
        self.size = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "StorageEnclosureDisk", parent_mo_or_dn, **kwargs)

