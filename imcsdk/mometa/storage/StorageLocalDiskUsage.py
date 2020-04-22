"""This module contains the general information for StorageLocalDiskUsage ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageLocalDiskUsageConsts:
    pass


class StorageLocalDiskUsage(ManagedObject):
    """This is StorageLocalDiskUsage class."""

    consts = StorageLocalDiskUsageConsts()
    naming_props = set(['physicalDrive'])

    mo_meta = {
        "classic": MoMeta("StorageLocalDiskUsage", "storageLocalDiskUsage", "pd-[physical_drive]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageVirtualDrive'], [], ["Get"]),
        "modular": MoMeta("StorageLocalDiskUsage", "storageLocalDiskUsage", "pd-[physical_drive]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageVirtualDrive'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "number_of_blocks": MoPropertyMeta("number_of_blocks", "numberOfBlocks", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pd_status": MoPropertyMeta("pd_status", "pdStatus", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "physical_drive": MoPropertyMeta("physical_drive", "physicalDrive", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "span": MoPropertyMeta("span", "span", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "starting_block": MoPropertyMeta("starting_block", "startingBlock", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "virtual_drive": MoPropertyMeta("virtual_drive", "virtualDrive", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "number_of_blocks": MoPropertyMeta("number_of_blocks", "numberOfBlocks", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pd_status": MoPropertyMeta("pd_status", "pdStatus", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "physical_drive": MoPropertyMeta("physical_drive", "physicalDrive", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "span": MoPropertyMeta("span", "span", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "starting_block": MoPropertyMeta("starting_block", "startingBlock", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "virtual_drive": MoPropertyMeta("virtual_drive", "virtualDrive", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "numberOfBlocks": "number_of_blocks", 
            "pdStatus": "pd_status", 
            "physicalDrive": "physical_drive", 
            "rn": "rn", 
            "span": "span", 
            "startingBlock": "starting_block", 
            "state": "state", 
            "status": "status", 
            "virtualDrive": "virtual_drive", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "numberOfBlocks": "number_of_blocks", 
            "pdStatus": "pd_status", 
            "physicalDrive": "physical_drive", 
            "rn": "rn", 
            "span": "span", 
            "startingBlock": "starting_block", 
            "state": "state", 
            "status": "status", 
            "virtualDrive": "virtual_drive", 
        },

    }

    def __init__(self, parent_mo_or_dn, physical_drive, **kwargs):
        self._dirty_mask = 0
        self.physical_drive = physical_drive
        self.child_action = None
        self.number_of_blocks = None
        self.pd_status = None
        self.span = None
        self.starting_block = None
        self.state = None
        self.status = None
        self.virtual_drive = None

        ManagedObject.__init__(self, "StorageLocalDiskUsage", parent_mo_or_dn, **kwargs)

