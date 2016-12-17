"""This module contains the general information for LsbootStorage ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LsbootStorageConsts:
    ACCESS_READ_WRITE = "read-write"
    TYPE_STORAGE = "storage"


class LsbootStorage(ManagedObject):
    """This is LsbootStorage class."""

    consts = LsbootStorageConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("LsbootStorage", "lsbootStorage", "storage-read-write", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'lsbootDef'], [], ["Add", "Get", "Remove", "Set"]),
        "modular": MoMeta("LsbootStorage", "lsbootStorage", "storage-read-write", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'lsbootDef'], [], ["Add", "Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "access": MoPropertyMeta("access", "access", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["read-write"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["1", "2", "3", "4", "5"], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["storage"], []), 
        },

        "modular": {
            "access": MoPropertyMeta("access", "access", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["read-write"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["1", "2", "3", "4", "5"], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["storage"], []), 
        },

    }

    prop_map = {

        "classic": {
            "access": "access", 
            "childAction": "child_action", 
            "dn": "dn", 
            "order": "order", 
            "rn": "rn", 
            "status": "status", 
            "type": "type", 
        },

        "modular": {
            "access": "access", 
            "childAction": "child_action", 
            "dn": "dn", 
            "order": "order", 
            "rn": "rn", 
            "status": "status", 
            "type": "type", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.access = None
        self.child_action = None
        self.order = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LsbootStorage", parent_mo_or_dn, **kwargs)

