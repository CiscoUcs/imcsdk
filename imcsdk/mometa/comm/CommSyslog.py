"""This module contains the general information for CommSyslog ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommSyslogConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    LOCAL_SEVERITY_ALERT = "alert"
    LOCAL_SEVERITY_CRITICAL = "critical"
    LOCAL_SEVERITY_DEBUG = "debug"
    LOCAL_SEVERITY_EMERGENCY = "emergency"
    LOCAL_SEVERITY_ERROR = "error"
    LOCAL_SEVERITY_INFORMATIONAL = "informational"
    LOCAL_SEVERITY_NOTICE = "notice"
    LOCAL_SEVERITY_WARNING = "warning"
    PROTO_ALL = "all"
    PROTO_NONE = "none"
    PROTO_TCP = "tcp"
    PROTO_UDP = "udp"
    REMOTE_SEVERITY_ALERT = "alert"
    REMOTE_SEVERITY_CRITICAL = "critical"
    REMOTE_SEVERITY_DEBUG = "debug"
    REMOTE_SEVERITY_EMERGENCY = "emergency"
    REMOTE_SEVERITY_ERROR = "error"
    REMOTE_SEVERITY_INFORMATIONAL = "informational"
    REMOTE_SEVERITY_NOTICE = "notice"
    REMOTE_SEVERITY_WARNING = "warning"


class CommSyslog(ManagedObject):
    """This is CommSyslog class."""

    consts = CommSyslogConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("CommSyslog", "commSyslog", "syslog", VersionMeta.Version151f, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['commSvcEp'], ['commSyslogClient'], ["Get", "Set"]),
        "modular": MoMeta("CommSyslog", "commSyslog", "syslog", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['commSvcEp'], ['commSyslogClient'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "local_severity": MoPropertyMeta("local_severity", "localSeverity", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["alert", "critical", "debug", "emergency", "error", "informational", "notice", "warning"], []),
            "remote_severity": MoPropertyMeta("remote_severity", "remoteSeverity", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["alert", "critical", "debug", "emergency", "error", "informational", "notice", "warning"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
            "port": MoPropertyMeta("port", "port", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
            "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "local_severity": MoPropertyMeta("local_severity", "localSeverity", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["alert", "critical", "debug", "emergency", "error", "informational", "notice", "warning"], []),
            "remote_severity": MoPropertyMeta("remote_severity", "remoteSeverity", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["alert", "critical", "debug", "emergency", "error", "informational", "notice", "warning"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
            "port": MoPropertyMeta("port", "port", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
            "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "localSeverity": "local_severity", 
            "remoteSeverity": "remote_severity", 
            "rn": "rn", 
            "status": "status", 
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "descr": "descr", 
            "name": "name", 
            "port": "port", 
            "proto": "proto", 
        },

        "modular": {
            "dn": "dn", 
            "localSeverity": "local_severity", 
            "remoteSeverity": "remote_severity", 
            "rn": "rn", 
            "status": "status", 
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "descr": "descr", 
            "name": "name", 
            "port": "port", 
            "proto": "proto", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.local_severity = None
        self.remote_severity = None
        self.status = None
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.name = None
        self.port = None
        self.proto = None

        ManagedObject.__init__(self, "CommSyslog", parent_mo_or_dn, **kwargs)

