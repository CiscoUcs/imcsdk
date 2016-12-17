"""This module contains the general information for LsbootVirtualMedia ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LsbootVirtualMediaConsts:
    ACCESS_READ_ONLY = "read-only"
    ACCESS_READ_WRITE = "read-write"
    TYPE_VIRTUAL_MEDIA = "virtual-media"


class LsbootVirtualMedia(ManagedObject):
    """This is LsbootVirtualMedia class."""

    consts = LsbootVirtualMediaConsts()
    naming_props = set([u'access'])

    mo_meta = {
        "classic": MoMeta("LsbootVirtualMedia", "lsbootVirtualMedia", "vm-[access]", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'lsbootDef'], [], ["Add", "Get"]),
        "modular": MoMeta("LsbootVirtualMedia", "lsbootVirtualMedia", "vm-[access]", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'lsbootDef'], [], ["Add", "Get"])
    }


    prop_meta = {

        "classic": {
            "access": MoPropertyMeta("access", "access", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x2, None, None, None, ["read-only", "read-write"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["1", "2", "3", "4", "5"], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["virtual-media"], []), 
        },

        "modular": {
            "access": MoPropertyMeta("access", "access", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x2, None, None, None, ["read-only", "read-write"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["1", "2", "3", "4", "5"], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["virtual-media"], []), 
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

    def __init__(self, parent_mo_or_dn, access, **kwargs):
        self._dirty_mask = 0
        self.access = access
        self.child_action = None
        self.order = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LsbootVirtualMedia", parent_mo_or_dn, **kwargs)

