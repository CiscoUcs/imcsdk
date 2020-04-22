"""This module contains the general information for IodSnapshotCancel ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class IodSnapshotCancelConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"


class IodSnapshotCancel(ManagedObject):
    """This is IodSnapshotCancel class."""

    consts = IodSnapshotCancelConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("IodSnapshotCancel", "iodSnapshotCancel", "snapshotCancel", VersionMeta.Version151x, "InputOutput", 0x3f, [], ["admin"], ['iodController'], [], [None]),
        "modular": MoMeta("IodSnapshotCancel", "iodSnapshotCancel", "snapshotCancel", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin"], ['iodController'], [], [None])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "time_out": MoPropertyMeta("time_out", "timeOut", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["30-240"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151x, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "time_out": MoPropertyMeta("time_out", "timeOut", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["30-240"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
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

        ManagedObject.__init__(self, "IodSnapshotCancel", parent_mo_or_dn, **kwargs)

