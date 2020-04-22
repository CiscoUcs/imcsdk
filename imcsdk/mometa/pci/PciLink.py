"""This module contains the general information for PciLink ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PciLinkConsts:
    pass


class PciLink(ManagedObject):
    """This is PciLink class."""

    consts = PciLinkConsts()
    naming_props = set(['adapter'])

    mo_meta = {
        "classic": MoMeta("PciLink", "pciLink", "pci-link-[adapter]", VersionMeta.Version402c, "OutputOnly", 0xf, [], ["read-only"], ['pciSwitch'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "adapter": MoPropertyMeta("adapter", "adapter", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version402c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "link_speed": MoPropertyMeta("link_speed", "linkSpeed", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "link_status": MoPropertyMeta("link_status", "linkStatus", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "link_width": MoPropertyMeta("link_width", "linkWidth", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "slot_status": MoPropertyMeta("slot_status", "slotStatus", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "adapter": "adapter", 
            "childAction": "child_action", 
            "dn": "dn", 
            "linkSpeed": "link_speed", 
            "linkStatus": "link_status", 
            "linkWidth": "link_width", 
            "rn": "rn", 
            "slot": "slot", 
            "slotStatus": "slot_status", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, adapter, **kwargs):
        self._dirty_mask = 0
        self.adapter = adapter
        self.child_action = None
        self.link_speed = None
        self.link_status = None
        self.link_width = None
        self.slot = None
        self.slot_status = None
        self.status = None

        ManagedObject.__init__(self, "PciLink", parent_mo_or_dn, **kwargs)

