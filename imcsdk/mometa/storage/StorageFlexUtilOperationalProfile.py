"""This module contains the general information for StorageFlexUtilOperationalProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexUtilOperationalProfileConsts:
    pass


class StorageFlexUtilOperationalProfile(ManagedObject):
    """This is StorageFlexUtilOperationalProfile class."""

    consts = StorageFlexUtilOperationalProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StorageFlexUtilOperationalProfile", "storageFlexUtilOperationalProfile", "oper-profile", VersionMeta.Version304a, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['storageFlexUtilController'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version304a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "io_read_error_threshold": MoPropertyMeta("io_read_error_threshold", "ioReadErrorThreshold", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, [], ["0-255"]),
            "io_write_error_threshold": MoPropertyMeta("io_write_error_threshold", "ioWriteErrorThreshold", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], ["0-255"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "ioReadErrorThreshold": "io_read_error_threshold", 
            "ioWriteErrorThreshold": "io_write_error_threshold", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.io_read_error_threshold = None
        self.io_write_error_threshold = None
        self.status = None

        ManagedObject.__init__(self, "StorageFlexUtilOperationalProfile", parent_mo_or_dn, **kwargs)

