"""This module contains the general information for CommMailAlert ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommMailAlertConsts:
    MIN_SEVERITY_LEVEL_CONDITION = "condition"
    MIN_SEVERITY_LEVEL_CRITICAL = "critical"
    MIN_SEVERITY_LEVEL_INFORMATIONAL = "informational"
    MIN_SEVERITY_LEVEL_MAJOR = "major"
    MIN_SEVERITY_LEVEL_MINOR = "minor"
    MIN_SEVERITY_LEVEL_WARNING = "warning"


class CommMailAlert(ManagedObject):
    """This is CommMailAlert class."""

    consts = CommMailAlertConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("CommMailAlert", "commMailAlert", "mail-alert-svc", VersionMeta.Version303a, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['commSvcEp'], ['mailRecipient'], ["Get", "Set"]),
        "modular": MoMeta("CommMailAlert", "commMailAlert", "mail-alert-svc", VersionMeta.Version303a, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['commSvcEp'], ['mailRecipient'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "from_address": MoPropertyMeta("from_address", "fromAddress", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, 0, 128, r"""((([^<>\(\)\[\]\\\.,;:\s@""]+(\.[^<>\(\)\[\]\\\.,;:\s@""]+)*)|(""\.+""))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,})){0,128}""", [], []),
            "ip_address": MoPropertyMeta("ip_address", "ipAddress", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], []),
            "min_severity_level": MoPropertyMeta("min_severity_level", "minSeverityLevel", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["condition", "critical", "informational", "major", "minor", "warning"], []),
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-65535"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "from_address": MoPropertyMeta("from_address", "fromAddress", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, 0, 64, r"""((([^<>\(\)\[\]\\\.,;:\s@""]+(\.[^<>\(\)\[\]\\\.,;:\s@""]+)*)|(""\.+""))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,})){0,64}""", [], []),
            "ip_address": MoPropertyMeta("ip_address", "ipAddress", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], []),
            "min_severity_level": MoPropertyMeta("min_severity_level", "minSeverityLevel", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["condition", "critical", "informational", "major", "minor", "warning"], []),
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-65535"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "fromAddress": "from_address", 
            "ipAddress": "ip_address", 
            "minSeverityLevel": "min_severity_level", 
            "port": "port", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "fromAddress": "from_address", 
            "ipAddress": "ip_address", 
            "minSeverityLevel": "min_severity_level", 
            "port": "port", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.from_address = None
        self.ip_address = None
        self.min_severity_level = None
        self.port = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "CommMailAlert", parent_mo_or_dn, **kwargs)

