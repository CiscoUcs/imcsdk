"""This module contains the general information for CommSnmpTrap ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommSnmpTrapConsts:
    ADMIN_ACTION_CLEAR = "clear"
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    NOTIFICATION_TYPE_INFORMS = "informs"
    NOTIFICATION_TYPE_TRAPS = "traps"
    VERSION_V1 = "v1"
    VERSION_V2C = "v2c"
    VERSION_V3 = "v3"


class CommSnmpTrap(ManagedObject):
    """This is CommSnmpTrap class."""

    consts = CommSnmpTrapConsts()
    naming_props = set([u'id'])

    mo_meta = {
        "classic": MoMeta("CommSnmpTrap", "commSnmpTrap", "snmp-trap-[id]", VersionMeta.Version151f, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], [u'commSnmp'], [], ["Get", "Set"]),
        "modular": MoMeta("CommSnmpTrap", "commSnmpTrap", "snmp-trap-[id]", VersionMeta.Version2013e, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], [u'commSnmp'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version208d, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear"], []), 
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "community": MoPropertyMeta("community", "community", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[!#$%\)\*\+,\-\./:<=\[\]\^_\{\}~a-zA-Z0-9]{1,32}""", [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []), 
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x20, None, None, None, [], ["1-15"]), 
            "notification_type": MoPropertyMeta("notification_type", "notificationType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["informs", "traps"], []), 
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["1-65535"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, 0, 31, None, [], []), 
            "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["v1", "v2c", "v3"], []), 
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear"], []), 
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "community": MoPropertyMeta("community", "community", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[!#$%\)\*\+,\-\./:<=\[\]\^_\{\}~a-zA-Z0-9]{1,32}""", [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, r"""([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []), 
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x20, None, None, None, [], ["1-15"]), 
            "notification_type": MoPropertyMeta("notification_type", "notificationType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["informs", "traps"], []), 
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["1-65535"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, 0, 31, None, [], []), 
            "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["v1", "v2c", "v3"], []), 
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "community": "community", 
            "dn": "dn", 
            "hostname": "hostname", 
            "id": "id", 
            "notificationType": "notification_type", 
            "port": "port", 
            "rn": "rn", 
            "status": "status", 
            "user": "user", 
            "version": "version", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "community": "community", 
            "dn": "dn", 
            "hostname": "hostname", 
            "id": "id", 
            "notificationType": "notification_type", 
            "port": "port", 
            "rn": "rn", 
            "status": "status", 
            "user": "user", 
            "version": "version", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_action = None
        self.admin_state = None
        self.child_action = None
        self.community = None
        self.hostname = None
        self.notification_type = None
        self.port = None
        self.status = None
        self.user = None
        self.version = None

        ManagedObject.__init__(self, "CommSnmpTrap", parent_mo_or_dn, **kwargs)

