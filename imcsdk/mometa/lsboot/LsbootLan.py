"""This module contains the general information for LsbootLan ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LsbootLanConsts:
    ACCESS_READ_ONLY = "read-only"
    PROT_GPXE = "gpxe"
    PROT_I_SCSI = "iSCSI"
    PROT_PXE = "pxe"
    TYPE_LAN = "lan"


class LsbootLan(ManagedObject):
    """This is LsbootLan class."""

    consts = LsbootLanConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("LsbootLan", "lsbootLan", "lan-read-only", VersionMeta.Version151f, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['lsbootDef'], [], ["Add", "Get", "Remove", "Set"]),
        "modular": MoMeta("LsbootLan", "lsbootLan", "lan-read-only", VersionMeta.Version2013e, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['lsbootDef'], [], ["Add", "Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "access": MoPropertyMeta("access", "access", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["read-only"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["1", "2", "3", "4", "5"], []),
            "prot": MoPropertyMeta("prot", "prot", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["gpxe", "iSCSI", "pxe"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["lan"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "access": MoPropertyMeta("access", "access", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["read-only"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["1", "2", "3", "4", "5"], []),
            "prot": MoPropertyMeta("prot", "prot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["gpxe", "iSCSI", "pxe"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["lan"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "access": "access", 
            "dn": "dn", 
            "order": "order", 
            "prot": "prot", 
            "rn": "rn", 
            "status": "status", 
            "type": "type", 
            "childAction": "child_action", 
        },

        "modular": {
            "access": "access", 
            "dn": "dn", 
            "order": "order", 
            "prot": "prot", 
            "rn": "rn", 
            "status": "status", 
            "type": "type", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.access = None
        self.order = None
        self.prot = None
        self.status = None
        self.type = None
        self.child_action = None

        ManagedObject.__init__(self, "LsbootLan", parent_mo_or_dn, **kwargs)

