"""This module contains the general information for PciAdapterFruInventoryInfo ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PciAdapterFruInventoryInfoConsts:
    pass


class PciAdapterFruInventoryInfo(ManagedObject):
    """This is PciAdapterFruInventoryInfo class."""

    consts = PciAdapterFruInventoryInfoConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("PciAdapterFruInventoryInfo", "pciAdapterFruInventoryInfo", "fru-info-inv-[id]", VersionMeta.Version422a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['pciAdapterFruInventory'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "factory_wwnn": MoPropertyMeta("factory_wwnn", "factoryWWNN", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "factory_wwpn": MoPropertyMeta("factory_wwpn", "factoryWWPN", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "wwnn": MoPropertyMeta("wwnn", "wwnn", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "wwpn": MoPropertyMeta("wwpn", "wwpn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "factoryWWNN": "factory_wwnn", 
            "factoryWWPN": "factory_wwpn", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
            "wwnn": "wwnn", 
            "wwpn": "wwpn", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.factory_wwnn = None
        self.factory_wwpn = None
        self.status = None
        self.wwnn = None
        self.wwpn = None

        ManagedObject.__init__(self, "PciAdapterFruInventoryInfo", parent_mo_or_dn, **kwargs)

