"""This module contains the general information for StorageLocalDiskEp ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageLocalDiskEpConsts:
    pass


class StorageLocalDiskEp(ManagedObject):
    """This is StorageLocalDiskEp class."""

    consts = StorageLocalDiskEpConsts()
    naming_props = set([u'id'])

    mo_meta = {
        "modular": MoMeta("StorageLocalDiskEp", "storageLocalDiskEp", "upload-catalog", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'storageController'], [u'faultInst'], [None])
    }


    prop_meta = {

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x200, 0, 255, None, [], []), 
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x200, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "modular": {
            "dn": "dn", 
            "health": "health", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.health = None
        self.status = None

        ManagedObject.__init__(self, "StorageLocalDiskEp", parent_mo_or_dn, **kwargs)

