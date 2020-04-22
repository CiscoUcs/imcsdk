"""This module contains the general information for CommVMedia ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommVMediaConsts:
    ADMIN_ACTION_DELETE_ALL_SAVED_MAPPINGS = "delete-all-saved-mappings"


class CommVMedia(ManagedObject):
    """This is CommVMedia class."""

    consts = CommVMediaConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("CommVMedia", "commVMedia", "vmedia-svc", VersionMeta.Version151f, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['commSvcEp'], ['commSavedVMediaMap', 'commVMediaMap'], ["Get", "Set"]),
        "modular": MoMeta("CommVMedia", "commVMedia", "vmedia-svc", VersionMeta.Version2013e, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['commSvcRack'], ['commSavedVMediaMap', 'commVMediaMap'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete-all-saved-mappings"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "encryption_state": MoPropertyMeta("encryption_state", "encryptionState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "active_sessions": MoPropertyMeta("active_sessions", "activeSessions", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "low_power_usb_state": MoPropertyMeta("low_power_usb_state", "lowPowerUsbState", "string", VersionMeta.Version208d, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete-all-saved-mappings"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "encryption_state": MoPropertyMeta("encryption_state", "encryptionState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "active_sessions": MoPropertyMeta("active_sessions", "activeSessions", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "low_power_usb": MoPropertyMeta("low_power_usb", "lowPowerUsb", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "max_sessions": MoPropertyMeta("max_sessions", "maxSessions", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["1-4"]),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "adminState": "admin_state", 
            "dn": "dn", 
            "encryptionState": "encryption_state", 
            "rn": "rn", 
            "status": "status", 
            "activeSessions": "active_sessions", 
            "childAction": "child_action", 
            "lowPowerUsbState": "low_power_usb_state", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "adminState": "admin_state", 
            "dn": "dn", 
            "encryptionState": "encryption_state", 
            "rn": "rn", 
            "status": "status", 
            "activeSessions": "active_sessions", 
            "childAction": "child_action", 
            "lowPowerUsb": "low_power_usb", 
            "maxSessions": "max_sessions", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.admin_state = None
        self.encryption_state = None
        self.status = None
        self.active_sessions = None
        self.child_action = None
        self.low_power_usb_state = None
        self.low_power_usb = None
        self.max_sessions = None

        ManagedObject.__init__(self, "CommVMedia", parent_mo_or_dn, **kwargs)

