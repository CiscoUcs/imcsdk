"""This module contains the general information for HuuFirmwareUpdateCancel ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class HuuFirmwareUpdateCancelConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"


class HuuFirmwareUpdateCancel(ManagedObject):
    """This is HuuFirmwareUpdateCancel class."""

    consts = HuuFirmwareUpdateCancelConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("HuuFirmwareUpdateCancel", "huuFirmwareUpdateCancel", "firmwareUpdateCancel", VersionMeta.Version152, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'huuController'], [], ["Get", "Set"]),
        "modular": MoMeta("HuuFirmwareUpdateCancel", "huuFirmwareUpdateCancel", "firmwareUpdateCancel", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'huuController'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version152, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version152, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "HuuFirmwareUpdateCancel", parent_mo_or_dn, **kwargs)

