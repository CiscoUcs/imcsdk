"""This module contains the general information for SysdebugMEpLog ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class SysdebugMEpLogConsts:
    ADMIN_STATE_BACKUP = "backup"
    ADMIN_STATE_CLEAR = "clear"
    ADMIN_STATE_POLICY = "policy"
    CAPACITY_AVAILABLE = "available"
    CAPACITY_FULL = "full"
    CAPACITY_LOW = "low"
    CAPACITY_UNKNOWN = "unknown"
    CAPACITY_VERY_LOW = "very-low"
    TYPE_OBFL = "OBFL"
    TYPE_SEL = "SEL"
    TYPE_SYSLOG = "Syslog"


class SysdebugMEpLog(ManagedObject):
    """This is SysdebugMEpLog class."""

    consts = SysdebugMEpLogConsts()
    naming_props = set(['type', 'id'])

    mo_meta = {
        "classic": MoMeta("SysdebugMEpLog", "sysdebugMEpLog", "log-[type]-[id]", VersionMeta.Version151f, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['mgmtController'], ['faultInst'], ["Get", "Set"]),
        "modular": MoMeta("SysdebugMEpLog", "sysdebugMEpLog", "log-[type]-[id]", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['mgmtController'], ['faultInst'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["backup", "clear", "policy"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x20, None, None, None, ["OBFL", "SEL", "Syslog"], []),
            "capacity": MoPropertyMeta("capacity", "capacity", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["available", "full", "low", "unknown", "very-low"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-8"]),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["backup", "clear", "policy"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x20, None, None, None, ["OBFL", "SEL", "Syslog"], []),
            "capacity": MoPropertyMeta("capacity", "capacity", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["available", "full", "low", "unknown", "very-low"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-8"]),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "type": "type", 
            "capacity": "capacity", 
            "childAction": "child_action", 
            "id": "id", 
        },

        "modular": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "type": "type", 
            "capacity": "capacity", 
            "childAction": "child_action", 
            "id": "id", 
        },

    }

    def __init__(self, parent_mo_or_dn, type, id, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.id = id
        self.admin_state = None
        self.status = None
        self.capacity = None
        self.child_action = None

        ManagedObject.__init__(self, "SysdebugMEpLog", parent_mo_or_dn, **kwargs)

