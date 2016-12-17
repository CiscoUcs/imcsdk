"""This module contains the general information for CommRedfish ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommRedfishConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"


class CommRedfish(ManagedObject):
    """This is CommRedfish class."""

    consts = CommRedfishConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("CommRedfish", "commRedfish", "redfish-svc", VersionMeta.Version301c, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'commSvcEp'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "active_sessions": MoPropertyMeta("active_sessions", "activeSessions", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "maximum_sessions": MoPropertyMeta("maximum_sessions", "maximumSessions", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "classic": {
            "activeSessions": "active_sessions", 
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "maximumSessions": "maximum_sessions", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.active_sessions = None
        self.admin_state = None
        self.child_action = None
        self.maximum_sessions = None
        self.status = None

        ManagedObject.__init__(self, "CommRedfish", parent_mo_or_dn, **kwargs)

