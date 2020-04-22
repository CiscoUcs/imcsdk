"""This module contains the general information for StorageFlexUtilHealth ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexUtilHealthConsts:
    pass


class StorageFlexUtilHealth(ManagedObject):
    """This is StorageFlexUtilHealth class."""

    consts = StorageFlexUtilHealthConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StorageFlexUtilHealth", "storageFlexUtilHealth", "health", VersionMeta.Version304a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageFlexUtilController'], [], ["Get"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version304a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "health": "health", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.health = None
        self.status = None

        ManagedObject.__init__(self, "StorageFlexUtilHealth", parent_mo_or_dn, **kwargs)

