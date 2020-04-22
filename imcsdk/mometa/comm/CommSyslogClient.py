"""This module contains the general information for CommSyslogClient ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommSyslogClientConsts:
    ADMIN_ACTION_CLEAR = "clear"
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    NAME_PRIMARY = "primary"
    NAME_SECONDARY = "secondary"
    NAME_TERTIARY = "tertiary"
    PROTO_TCP = "tcp"
    PROTO_UDP = "udp"


class CommSyslogClient(ManagedObject):
    """This is CommSyslogClient class."""

    consts = CommSyslogClientConsts()
    naming_props = set(['name'])

    mo_meta = {
        "classic": MoMeta("CommSyslogClient", "commSyslogClient", "client-[name]", VersionMeta.Version151f, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['commSyslog'], [], ["Get"]),
        "modular": MoMeta("CommSyslogClient", "commSyslogClient", "client-[name]", VersionMeta.Version2013e, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['commSyslog'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version208d, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x20, None, None, None, ["primary", "secondary", "tertiary"], []),
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-65535"]),
            "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["tcp", "udp"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x20, None, None, None, ["primary", "secondary", "tertiary"], []),
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-65535"]),
            "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["tcp", "udp"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "adminState": "admin_state", 
            "dn": "dn", 
            "hostname": "hostname", 
            "name": "name", 
            "port": "port", 
            "proto": "proto", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "adminState": "admin_state", 
            "dn": "dn", 
            "hostname": "hostname", 
            "name": "name", 
            "port": "port", 
            "proto": "proto", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_action = None
        self.admin_state = None
        self.hostname = None
        self.port = None
        self.proto = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "CommSyslogClient", parent_mo_or_dn, **kwargs)

