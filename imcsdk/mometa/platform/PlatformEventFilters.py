"""This module contains the general information for PlatformEventFilters ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PlatformEventFiltersConsts:
    ACTION_NONE = "none"
    ACTION_POWER_CYCLE = "power-cycle"
    ACTION_POWER_OFF = "power-off"
    ACTION_REBOOT = "reboot"


class PlatformEventFilters(ManagedObject):
    """This is PlatformEventFilters class."""

    consts = PlatformEventFiltersConsts()
    naming_props = set([u'id'])

    mo_meta = {
        "classic": MoMeta("PlatformEventFilters", "platformEventFilters", "pef-[id]", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], [u'eventManagement'], [], ["Get", "Set"]),
        "modular": MoMeta("PlatformEventFilters", "platformEventFilters", "pef-[id]", VersionMeta.Version301c, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], [u'eventManagement'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "action": MoPropertyMeta("action", "action", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["none", "power-cycle", "power-off", "reboot"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "event": MoPropertyMeta("event", "event", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x8, 0, 510, None, [], ["1-7"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

        "modular": {
            "action": MoPropertyMeta("action", "action", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["none", "power-cycle", "power-off", "reboot"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "event": MoPropertyMeta("event", "event", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version301c, MoPropertyMeta.NAMING, 0x8, 0, 510, None, [], ["1-7"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "classic": {
            "action": "action", 
            "childAction": "child_action", 
            "dn": "dn", 
            "event": "event", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "action": "action", 
            "childAction": "child_action", 
            "dn": "dn", 
            "event": "event", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.action = None
        self.child_action = None
        self.event = None
        self.status = None

        ManagedObject.__init__(self, "PlatformEventFilters", parent_mo_or_dn, **kwargs)

