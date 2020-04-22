"""This module contains the general information for GraphicsCard ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class GraphicsCardConsts:
    pass


class GraphicsCard(ManagedObject):
    """This is GraphicsCard class."""

    consts = GraphicsCardConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("GraphicsCard", "graphicsCard", "graphics-card-[id]", VersionMeta.Version402c, "OutputOnly", 0xf, [], ["read-only"], ['computeBoard'], [], [None]),
        "modular": MoMeta("GraphicsCard", "graphicsCard", "graphics-card-[id]", VersionMeta.Version411c, "OutputOnly", 0xf, [], ["read-only"], ['computeBoard'], [], [None])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version402c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version402c, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "no_of_gp_us": MoPropertyMeta("no_of_gp_us", "noOfGPUs", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pid": MoPropertyMeta("pid", "pid", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "slot_name": MoPropertyMeta("slot_name", "slotName", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version411c, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "no_of_gp_us": MoPropertyMeta("no_of_gp_us", "noOfGPUs", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pid": MoPropertyMeta("pid", "pid", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "slot_name": MoPropertyMeta("slot_name", "slotName", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "id": "id", 
            "noOfGPUs": "no_of_gp_us", 
            "pid": "pid", 
            "productName": "product_name", 
            "rn": "rn", 
            "slotName": "slot_name", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "id": "id", 
            "noOfGPUs": "no_of_gp_us", 
            "pid": "pid", 
            "productName": "product_name", 
            "rn": "rn", 
            "slotName": "slot_name", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.no_of_gp_us = None
        self.pid = None
        self.product_name = None
        self.slot_name = None
        self.status = None

        ManagedObject.__init__(self, "GraphicsCard", parent_mo_or_dn, **kwargs)

