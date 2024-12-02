"""This module contains the general information for PciAdapterPortStatus ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PciAdapterPortStatusConsts:
    pass


class PciAdapterPortStatus(ManagedObject):
    """This is PciAdapterPortStatus class."""

    consts = PciAdapterPortStatusConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("PciAdapterPortStatus", "pciAdapterPortStatus", "pci-adapter-portstatus-[id]", VersionMeta.Version433_240024, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['pciAdapterFruInventory'], ['faultInst'], [None]),
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "link_speed": MoPropertyMeta("link_speed", "linkSpeed", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "port_status": MoPropertyMeta("port_status", "portStatus", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "id": "id", 
            "linkSpeed": "link_speed", 
            "portStatus": "port_status", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.link_speed = None
        self.port_status = None
        self.status = None

        ManagedObject.__init__(self, "PciAdapterPortStatus", parent_mo_or_dn, **kwargs)

