"""This module contains the general information for RackUnitPersonality ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class RackUnitPersonalityConsts:
    pass


class RackUnitPersonality(ManagedObject):
    """This is RackUnitPersonality class."""

    consts = RackUnitPersonalityConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("RackUnitPersonality", "rackUnitPersonality", "personality-[id]", VersionMeta.Version421a, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['computeRackUnit'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "additional_info": MoPropertyMeta("additional_info", "additionalInfo", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 2000, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version421a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-1"]),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, 1, 100, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "additionalInfo": "additional_info", 
            "dn": "dn", 
            "id": "id", 
            "name": "name", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.additional_info = None
        self.name = None
        self.status = None

        ManagedObject.__init__(self, "RackUnitPersonality", parent_mo_or_dn, **kwargs)

