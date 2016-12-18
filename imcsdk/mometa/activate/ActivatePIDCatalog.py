"""This module contains the general information for ActivatePIDCatalog ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class ActivatePIDCatalogConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"


class ActivatePIDCatalog(ManagedObject):
    """This is ActivatePIDCatalog class."""

    consts = ActivatePIDCatalogConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("ActivatePIDCatalog", "activatePIDCatalog", "activate-catalog", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'pidCatalog'], [], ["Get", "Set"]),
        "modular": MoMeta("ActivatePIDCatalog", "activatePIDCatalog", "activate-catalog", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'pidCatalog'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "pid_activation_status": MoPropertyMeta("pid_activation_status", "pidActivationStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "pid_activation_status": MoPropertyMeta("pid_activation_status", "pidActivationStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "pidActivationStatus": "pid_activation_status", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "pidActivationStatus": "pid_activation_status", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.pid_activation_status = None
        self.status = None

        ManagedObject.__init__(self, "ActivatePIDCatalog", parent_mo_or_dn, **kwargs)

