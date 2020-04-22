"""This module contains the general information for CommKvm ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommKvmConsts:
    pass


class CommKvm(ManagedObject):
    """This is CommKvm class."""

    consts = CommKvmConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("CommKvm", "commKvm", "kvm-svc", VersionMeta.Version151f, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['commSvcEp'], [], ["Get", "Set"]),
        "modular": MoMeta("CommKvm", "commKvm", "kvm-svc", VersionMeta.Version2013e, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['commSvcRack'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "encryption_state": MoPropertyMeta("encryption_state", "encryptionState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "local_video_state": MoPropertyMeta("local_video_state", "localVideoState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-65535"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "total_sessions": MoPropertyMeta("total_sessions", "totalSessions", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["1-4"]),
            "active_sessions": MoPropertyMeta("active_sessions", "activeSessions", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "encryption_state": MoPropertyMeta("encryption_state", "encryptionState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "local_video_state": MoPropertyMeta("local_video_state", "localVideoState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-65535"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "total_sessions": MoPropertyMeta("total_sessions", "totalSessions", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["1-4"]),
            "active_sessions": MoPropertyMeta("active_sessions", "activeSessions", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "encryptionState": "encryption_state", 
            "localVideoState": "local_video_state", 
            "port": "port", 
            "rn": "rn", 
            "status": "status", 
            "totalSessions": "total_sessions", 
            "activeSessions": "active_sessions", 
            "childAction": "child_action", 
        },

        "modular": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "encryptionState": "encryption_state", 
            "localVideoState": "local_video_state", 
            "port": "port", 
            "rn": "rn", 
            "status": "status", 
            "totalSessions": "total_sessions", 
            "activeSessions": "active_sessions", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.encryption_state = None
        self.local_video_state = None
        self.port = None
        self.status = None
        self.total_sessions = None
        self.active_sessions = None
        self.child_action = None

        ManagedObject.__init__(self, "CommKvm", parent_mo_or_dn, **kwargs)

