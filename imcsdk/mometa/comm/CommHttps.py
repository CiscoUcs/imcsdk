"""This module contains the general information for CommHttps ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommHttpsConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    PROTO_ALL = "all"
    PROTO_NONE = "none"
    PROTO_TCP = "tcp"
    PROTO_UDP = "udp"


class CommHttps(ManagedObject):
    """This is CommHttps class."""

    consts = CommHttpsConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("CommHttps", "commHttps", "https-svc", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['commSvcEp'], [], ["Get", "Set"]),
        "modular": MoMeta("CommHttps", "commHttps", "https-svc", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['commSvcEp'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-65535"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "session_timeout": MoPropertyMeta("session_timeout", "sessionTimeout", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["60-10800"]),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "active_sessions": MoPropertyMeta("active_sessions", "activeSessions", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
            "maximum_sessions": MoPropertyMeta("maximum_sessions", "maximumSessions", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
            "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], []),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-65535"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "session_timeout": MoPropertyMeta("session_timeout", "sessionTimeout", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["60-10800"]),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "active_sessions": MoPropertyMeta("active_sessions", "activeSessions", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
            "maximum_sessions": MoPropertyMeta("maximum_sessions", "maximumSessions", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
            "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], []),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "port": "port", 
            "rn": "rn", 
            "sessionTimeout": "session_timeout", 
            "status": "status", 
            "activeSessions": "active_sessions", 
            "childAction": "child_action", 
            "descr": "descr", 
            "maximumSessions": "maximum_sessions", 
            "name": "name", 
            "proto": "proto", 
        },

        "modular": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "port": "port", 
            "rn": "rn", 
            "sessionTimeout": "session_timeout", 
            "status": "status", 
            "activeSessions": "active_sessions", 
            "childAction": "child_action", 
            "descr": "descr", 
            "maximumSessions": "maximum_sessions", 
            "name": "name", 
            "proto": "proto", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.port = None
        self.session_timeout = None
        self.status = None
        self.active_sessions = None
        self.child_action = None
        self.descr = None
        self.maximum_sessions = None
        self.name = None
        self.proto = None

        ManagedObject.__init__(self, "CommHttps", parent_mo_or_dn, **kwargs)

