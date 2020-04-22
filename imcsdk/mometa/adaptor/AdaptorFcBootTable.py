"""This module contains the general information for AdaptorFcBootTable ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorFcBootTableConsts:
    pass


class AdaptorFcBootTable(ManagedObject):
    """This is AdaptorFcBootTable class."""

    consts = AdaptorFcBootTableConsts()
    naming_props = set(['index'])

    mo_meta = {
        "classic": MoMeta("AdaptorFcBootTable", "adaptorFcBootTable", "fcboot-[index]", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['adaptorHostFcIf'], [], ["Add", "Get", "Set"]),
        "modular": MoMeta("AdaptorFcBootTable", "adaptorFcBootTable", "fcboot-[index]", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['adaptorHostFcIf'], [], ["Add", "Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "boot_lun": MoPropertyMeta("boot_lun", "bootLun", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-255"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["0-3"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "target_wwpn": MoPropertyMeta("target_wwpn", "targetWwpn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "boot_lun": MoPropertyMeta("boot_lun", "bootLun", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-255"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["0-3"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "target_wwpn": MoPropertyMeta("target_wwpn", "targetWwpn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "bootLun": "boot_lun", 
            "dn": "dn", 
            "index": "index", 
            "rn": "rn", 
            "status": "status", 
            "targetWwpn": "target_wwpn", 
            "childAction": "child_action", 
        },

        "modular": {
            "bootLun": "boot_lun", 
            "dn": "dn", 
            "index": "index", 
            "rn": "rn", 
            "status": "status", 
            "targetWwpn": "target_wwpn", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, index, **kwargs):
        self._dirty_mask = 0
        self.index = index
        self.boot_lun = None
        self.status = None
        self.target_wwpn = None
        self.child_action = None

        ManagedObject.__init__(self, "AdaptorFcBootTable", parent_mo_or_dn, **kwargs)

