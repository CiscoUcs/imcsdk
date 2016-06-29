"""This module contains the general information for CommVMedia ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommVMediaConsts:
    pass


class CommVMedia(ManagedObject):
    """This is CommVMedia class."""

    consts = CommVMediaConsts()
    naming_props = set([])

    mo_meta = MoMeta("CommVMedia", "commVMedia", "vmedia-svc", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'commSvcEp'], [u'commVMediaMap'], ["Get", "Set"])

    prop_meta = {
        "active_sessions": MoPropertyMeta("active_sessions", "activeSessions", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
        "encryption_state": MoPropertyMeta("encryption_state", "encryptionState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "low_power_usb_state": MoPropertyMeta("low_power_usb_state", "lowPowerUsbState", "string", VersionMeta.Version208d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
    }

    prop_map = {
        "activeSessions": "active_sessions", 
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "encryptionState": "encryption_state", 
        "lowPowerUsbState": "low_power_usb_state", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.active_sessions = None
        self.admin_state = None
        self.child_action = None
        self.encryption_state = None
        self.low_power_usb_state = None
        self.status = None

        ManagedObject.__init__(self, "CommVMedia", parent_mo_or_dn, **kwargs)

