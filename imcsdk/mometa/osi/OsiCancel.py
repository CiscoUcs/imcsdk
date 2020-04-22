"""This module contains the general information for OsiCancel ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class OsiCancelConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"


class OsiCancel(ManagedObject):
    """This is OsiCancel class."""

    consts = OsiCancelConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("OsiCancel", "osiCancel", "osiCancel", VersionMeta.Version301c, "InputOutput", 0x3f, [], ["admin"], ['osiController'], [], [None]),
        "modular": MoMeta("OsiCancel", "osiCancel", "osiCancel", VersionMeta.Version301c, "InputOutput", 0x3f, [], ["admin"], ['osiController'], [], [None])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "time_out": MoPropertyMeta("time_out", "timeOut", "uint", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["30-240"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "time_out": MoPropertyMeta("time_out", "timeOut", "uint", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["30-240"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "timeOut": "time_out", 
            "childAction": "child_action", 
        },

        "modular": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "timeOut": "time_out", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.status = None
        self.time_out = None
        self.child_action = None

        ManagedObject.__init__(self, "OsiCancel", parent_mo_or_dn, **kwargs)

