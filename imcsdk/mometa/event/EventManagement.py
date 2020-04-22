"""This module contains the general information for EventManagement ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class EventManagementConsts:
    ADMIN_ACTION_RESET_EVENT_FILTERS = "reset-event-filters"


class EventManagement(ManagedObject):
    """This is EventManagement class."""

    consts = EventManagementConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("EventManagement", "eventManagement", "event-management", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['computeRackUnit'], ['platformEventFilters'], ["Get", "Set"]),
        "modular": MoMeta("EventManagement", "eventManagement", "event-management", VersionMeta.Version301c, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['equipmentChassis'], ['platformEventFilters'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["reset-event-filters"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["reset-event-filters"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "adminState": "admin_state", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "adminState": "admin_state", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.admin_state = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "EventManagement", parent_mo_or_dn, **kwargs)

