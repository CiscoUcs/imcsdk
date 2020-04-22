"""This module contains the general information for GraphicsCardTemperature ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class GraphicsCardTemperatureConsts:
    pass


class GraphicsCardTemperature(ManagedObject):
    """This is GraphicsCardTemperature class."""

    consts = GraphicsCardTemperatureConsts()
    naming_props = set(['id'])

    mo_meta = {
        "modular": MoMeta("GraphicsCardTemperature", "graphicsCardTemperature", "graphics-card-temp-[id]", VersionMeta.Version411c, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['pciEquipSlot'], [], [None])
    }


    prop_meta = {

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version411c, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "temperature": MoPropertyMeta("temperature", "temperature", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "modular": {
            "dn": "dn", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
            "temperature": "temperature", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.status = None
        self.temperature = None

        ManagedObject.__init__(self, "GraphicsCardTemperature", parent_mo_or_dn, **kwargs)

