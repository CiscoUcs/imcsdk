"""This module contains the general information for EquipmentRackEnclosure ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class EquipmentRackEnclosureConsts:
    pass


class EquipmentRackEnclosure(ManagedObject):
    """This is EquipmentRackEnclosure class."""

    consts = EquipmentRackEnclosureConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("EquipmentRackEnclosure", "equipmentRackEnclosure", "sys/rack-enclosure-1", VersionMeta.Version401a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['topSystem'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "model": "model", 
            "rn": "rn", 
            "serial": "serial", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.model = None
        self.serial = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentRackEnclosure", parent_mo_or_dn, **kwargs)

