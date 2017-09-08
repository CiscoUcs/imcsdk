"""This module contains the general information for CommMailAlert ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommMailAlertConsts:
    MIN_SEVERITY_LEVEL_CONDITION = "condition"
    MIN_SEVERITY_LEVEL_CRITICAL = "critical"
    MIN_SEVERITY_LEVEL_MAJOR = "major"
    MIN_SEVERITY_LEVEL_MINOR = "minor"
    MIN_SEVERITY_LEVEL_WARNING = "warning"


class CommMailAlert(ManagedObject):
    """This is CommMailAlert class."""

    consts = CommMailAlertConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("CommMailAlert", "commMailAlert", "mail-alert-svc", VersionMeta.Version303a, "InputOutput", 0xff, [], ["admin", "read-only", "user"], [u'commSvcEp'], [u'mailRecipient'], ["Get", "Set"]),
        "modular": MoMeta("CommMailAlert", "commMailAlert", "mail-alert-svc", VersionMeta.Version303a, "InputOutput", 0xff, [], ["admin", "read-only", "user"], [u'commSvcEp'], [u'mailRecipient'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "ip_address": MoPropertyMeta("ip_address", "ipAddress", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []), 
            "min_severity_level": MoPropertyMeta("min_severity_level", "minSeverityLevel", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["condition", "critical", "major", "minor", "warning"], []), 
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-65535"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "ip_address": MoPropertyMeta("ip_address", "ipAddress", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, r"""([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []), 
            "min_severity_level": MoPropertyMeta("min_severity_level", "minSeverityLevel", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["condition", "critical", "major", "minor", "warning"], []), 
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-65535"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "ipAddress": "ip_address", 
            "minSeverityLevel": "min_severity_level", 
            "port": "port", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "ipAddress": "ip_address", 
            "minSeverityLevel": "min_severity_level", 
            "port": "port", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.ip_address = None
        self.min_severity_level = None
        self.port = None
        self.status = None

        ManagedObject.__init__(self, "CommMailAlert", parent_mo_or_dn, **kwargs)

