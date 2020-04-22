"""This module contains the general information for GpuInventory ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class GpuInventoryConsts:
    pass


class GpuInventory(ManagedObject):
    """This is GpuInventory class."""

    consts = GpuInventoryConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("GpuInventory", "gpuInventory", "gpu-inv-[id]", VersionMeta.Version303a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['pciEquipSlot'], [], ["Get"]),
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "temperature": MoPropertyMeta("temperature", "temperature", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
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

        ManagedObject.__init__(self, "GpuInventory", parent_mo_or_dn, **kwargs)

