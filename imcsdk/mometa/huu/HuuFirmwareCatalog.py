"""This module contains the general information for HuuFirmwareCatalog ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class HuuFirmwareCatalogConsts:
    pass


class HuuFirmwareCatalog(ManagedObject):
    """This is HuuFirmwareCatalog class."""

    consts = HuuFirmwareCatalogConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("HuuFirmwareCatalog", "huuFirmwareCatalog", "firmwareCatalog", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['huuController'], ['huuFirmwareCatalogComponent'], ["Get"]),
        "modular": MoMeta("HuuFirmwareCatalog", "huuFirmwareCatalog", "firmwareCatalog", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['huuController'], ['huuFirmwareCatalogComponent'], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "num_of_components": MoPropertyMeta("num_of_components", "numOfComponents", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "num_of_components": MoPropertyMeta("num_of_components", "numOfComponents", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "description": "description", 
            "dn": "dn", 
            "numOfComponents": "num_of_components", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "description": "description", 
            "dn": "dn", 
            "numOfComponents": "num_of_components", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.description = None
        self.num_of_components = None
        self.status = None

        ManagedObject.__init__(self, "HuuFirmwareCatalog", parent_mo_or_dn, **kwargs)

