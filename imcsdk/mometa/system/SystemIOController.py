"""This module contains the general information for SystemIOController ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class SystemIOControllerConsts:
    pass


class SystemIOController(ManagedObject):
    """This is SystemIOController class."""

    consts = SystemIOControllerConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("SystemIOController", "systemIOController", "sioc-[id]", VersionMeta.Version202c, "OutputOnly", 0xf, [], ["read-only"], ['computeRackUnit'], ['firmwareBootDefinition', 'firmwareRunning', 'firmwareUpdatable'], ["Get"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-999"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
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
        self.description = None
        self.status = None

        ManagedObject.__init__(self, "SystemIOController", parent_mo_or_dn, **kwargs)

