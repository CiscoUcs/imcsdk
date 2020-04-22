"""This module contains the general information for AaaUserPasswordExpiration ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AaaUserPasswordExpirationConsts:
    ADMIN_ACTION_RESTORE_DEFAULT = "restore-default"


class AaaUserPasswordExpiration(ManagedObject):
    """This is AaaUserPasswordExpiration class."""

    consts = AaaUserPasswordExpirationConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AaaUserPasswordExpiration", "aaaUserPasswordExpiration", "password-expiration", VersionMeta.Version301c, "InputOutput", 0x1ff, [], ["admin", "user"], ['aaaUserEp'], [], ["Get", "Set"]),
        "modular": MoMeta("AaaUserPasswordExpiration", "aaaUserPasswordExpiration", "password-expiration", VersionMeta.Version301c, "InputOutput", 0x1ff, [], ["admin", "user"], ['aaaUserEp'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["restore-default"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "password_expiry_duration": MoPropertyMeta("password_expiry_duration", "passwordExpiryDuration", "uint", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-3650"]),
            "password_grace_period": MoPropertyMeta("password_grace_period", "passwordGracePeriod", "uint", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-5"]),
            "password_history": MoPropertyMeta("password_history", "passwordHistory", "uint", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-5"]),
            "password_notification_period": MoPropertyMeta("password_notification_period", "passwordNotificationPeriod", "uint", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-15"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["restore-default"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "password_expiry_duration": MoPropertyMeta("password_expiry_duration", "passwordExpiryDuration", "uint", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-3650"]),
            "password_grace_period": MoPropertyMeta("password_grace_period", "passwordGracePeriod", "uint", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-5"]),
            "password_history": MoPropertyMeta("password_history", "passwordHistory", "uint", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-5"]),
            "password_notification_period": MoPropertyMeta("password_notification_period", "passwordNotificationPeriod", "uint", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-15"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "passwordExpiryDuration": "password_expiry_duration", 
            "passwordGracePeriod": "password_grace_period", 
            "passwordHistory": "password_history", 
            "passwordNotificationPeriod": "password_notification_period", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "passwordExpiryDuration": "password_expiry_duration", 
            "passwordGracePeriod": "password_grace_period", 
            "passwordHistory": "password_history", 
            "passwordNotificationPeriod": "password_notification_period", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.password_expiry_duration = None
        self.password_grace_period = None
        self.password_history = None
        self.password_notification_period = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "AaaUserPasswordExpiration", parent_mo_or_dn, **kwargs)

