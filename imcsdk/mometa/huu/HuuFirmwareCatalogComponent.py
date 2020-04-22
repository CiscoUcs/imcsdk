"""This module contains the general information for HuuFirmwareCatalogComponent ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class HuuFirmwareCatalogComponentConsts:
    pass


class HuuFirmwareCatalogComponent(ManagedObject):
    """This is HuuFirmwareCatalogComponent class."""

    consts = HuuFirmwareCatalogComponentConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("HuuFirmwareCatalogComponent", "huuFirmwareCatalogComponent", "id-[id]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['huuFirmwareCatalog'], [], ["Get"]),
        "modular": MoMeta("HuuFirmwareCatalogComponent", "huuFirmwareCatalogComponent", "id-[id]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['huuFirmwareCatalog'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "component_name": MoPropertyMeta("component_name", "componentName", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "component_name": MoPropertyMeta("component_name", "componentName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "componentName": "component_name", 
            "description": "description", 
            "dn": "dn", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "componentName": "component_name", 
            "description": "description", 
            "dn": "dn", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.component_name = None
        self.description = None
        self.status = None

        ManagedObject.__init__(self, "HuuFirmwareCatalogComponent", parent_mo_or_dn, **kwargs)

