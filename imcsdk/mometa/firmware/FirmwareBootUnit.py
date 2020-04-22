"""This module contains the general information for FirmwareBootUnit ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class FirmwareBootUnitConsts:
    ADMIN_STATE_CANCEL_PENDING_ACTIVATE = "cancel-pending-activate"
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"
    IGNORE_COMP_CHECK_FALSE = "false"
    IGNORE_COMP_CHECK_NO = "no"
    IGNORE_COMP_CHECK_TRUE = "true"
    IGNORE_COMP_CHECK_YES = "yes"
    IMAGE_BACKUP = "backup"
    IMAGE_RUNNING = "running"
    OPER_STATE_ACTIVATING = "activating"
    OPER_STATE_BAD_IMAGE = "bad-image"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_PENDING_NEXT_BOOT = "pending-next-boot"
    OPER_STATE_READY = "ready"
    OPER_STATE_REBOOTING = "rebooting"
    OPER_STATE_SCHEDULED = "scheduled"
    OPER_STATE_SET_STARTUP = "set-startup"
    OPER_STATE_THROTTLED = "throttled"
    OPER_STATE_UPDATING = "updating"
    RESET_ON_ACTIVATE_NO = "No"
    RESET_ON_ACTIVATE_YES = "Yes"
    RESET_ON_ACTIVATE_FALSE = "false"
    _RESET_ON_ACTIVATE_NO = "no"
    RESET_ON_ACTIVATE_TRUE = "true"
    _RESET_ON_ACTIVATE_YES = "yes"


class FirmwareBootUnit(ManagedObject):
    """This is FirmwareBootUnit class."""

    consts = FirmwareBootUnitConsts()
    naming_props = set(['type'])

    mo_meta = {
        "classic": MoMeta("FirmwareBootUnit", "firmwareBootUnit", "bootunit-[type]", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['firmwareBootDefinition'], [], ["Get", "Set"]),
        "modular": MoMeta("FirmwareBootUnit", "firmwareBootUnit", "bootunit-[type]", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['firmwareBootDefinition'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["cancel-pending-activate", "trigger", "triggered"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "image": MoPropertyMeta("image", "image", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["backup", "running"], []),
            "reset_on_activate": MoPropertyMeta("reset_on_activate", "resetOnActivate", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "ignore_comp_check": MoPropertyMeta("ignore_comp_check", "ignoreCompCheck", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
            "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "bad-image", "failed", "pending-next-boot", "ready", "rebooting", "scheduled", "set-startup", "throttled", "updating"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["cancel-pending-activate", "trigger", "triggered"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "image": MoPropertyMeta("image", "image", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["backup", "running"], []),
            "reset_on_activate": MoPropertyMeta("reset_on_activate", "resetOnActivate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["No", "Yes", "no", "yes"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "ignore_comp_check": MoPropertyMeta("ignore_comp_check", "ignoreCompCheck", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
            "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "bad-image", "failed", "pending-next-boot", "ready", "rebooting", "scheduled", "set-startup", "throttled", "updating"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "image": "image", 
            "resetOnActivate": "reset_on_activate", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "description": "description", 
            "ignoreCompCheck": "ignore_comp_check", 
            "operState": "oper_state", 
            "type": "type", 
            "version": "version", 
        },

        "modular": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "image": "image", 
            "resetOnActivate": "reset_on_activate", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "description": "description", 
            "ignoreCompCheck": "ignore_comp_check", 
            "operState": "oper_state", 
            "type": "type", 
            "version": "version", 
        },

    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.admin_state = None
        self.image = None
        self.reset_on_activate = None
        self.status = None
        self.child_action = None
        self.description = None
        self.ignore_comp_check = None
        self.oper_state = None
        self.version = None

        ManagedObject.__init__(self, "FirmwareBootUnit", parent_mo_or_dn, **kwargs)

