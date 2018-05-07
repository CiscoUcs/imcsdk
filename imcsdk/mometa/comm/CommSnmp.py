"""This module contains the general information for CommSnmp ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommSnmpConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    COM2_SEC_NONE = "None"
    COM2_SEC_DISABLED = "disabled"
    COM2_SEC_FULL = "full"
    COM2_SEC_LIMITED = "limited"
    PROTO_ALL = "all"
    PROTO_NONE = "none"
    PROTO_TCP = "tcp"
    PROTO_UDP = "udp"


class CommSnmp(ManagedObject):
    """This is CommSnmp class."""

    consts = CommSnmpConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("CommSnmp", "commSnmp", "snmp-svc", VersionMeta.Version151f, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], [u'commSvcEp'], [u'commSnmpTrap', u'commSnmpUser'], ["Get", "Set"]),
        "modular": MoMeta("CommSnmp", "commSnmp", "snmp-svc", VersionMeta.Version2013e, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], [u'commSvcEp'], [u'commSnmpTrap', u'commSnmpUser'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "com2_sec": MoPropertyMeta("com2_sec", "com2Sec", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["None", "disabled", "full", "limited"], []), 
            "community": MoPropertyMeta("community", "community", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[!#$%\(\)\*\+,\-\./:<=\[\]\^_\{\}~a-zA-Z0-9]{0,18}""", [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "engine_id_key": MoPropertyMeta("engine_id_key", "engineIdKey", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 27, r"""[^#!&]{0,27}""", [], []), 
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-65535"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "sys_contact": MoPropertyMeta("sys_contact", "sysContact", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, 0, 64, None, [], []), 
            "sys_location": MoPropertyMeta("sys_location", "sysLocation", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, 0, 64, None, [], []), 
            "trap_community": MoPropertyMeta("trap_community", "trapCommunity", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""[!#$%\(\)\*\+,\-\./:<=\[\]\^_\{\}~a-zA-Z0-9]{0,18}""", [], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
            "engine_id": MoPropertyMeta("engine_id", "engineId", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []), 
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
            "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], []), 
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "com2_sec": MoPropertyMeta("com2_sec", "com2Sec", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["None", "disabled", "full", "limited"], []), 
            "community": MoPropertyMeta("community", "community", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[!#$%\(\)\*\+,\-\./:<=\[\]\^_\{\}~a-zA-Z0-9]{0,18}""", [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "engine_id_key": MoPropertyMeta("engine_id_key", "engineIdKey", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 27, r"""[^#!&]{0,27}""", [], []), 
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-65535"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "sys_contact": MoPropertyMeta("sys_contact", "sysContact", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, 0, 64, None, [], []), 
            "sys_location": MoPropertyMeta("sys_location", "sysLocation", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, 0, 64, None, [], []), 
            "trap_community": MoPropertyMeta("trap_community", "trapCommunity", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""[!#$%\(\)\*\+,\-\./:<=\[\]\^_\{\}~a-zA-Z0-9]{0,18}""", [], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
            "engine_id": MoPropertyMeta("engine_id", "engineId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []), 
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
            "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], []), 
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "com2Sec": "com2_sec", 
            "community": "community", 
            "dn": "dn", 
            "engineIdKey": "engine_id_key", 
            "port": "port", 
            "rn": "rn", 
            "status": "status", 
            "sysContact": "sys_contact", 
            "sysLocation": "sys_location", 
            "trapCommunity": "trap_community", 
            "childAction": "child_action", 
            "descr": "descr", 
            "engineId": "engine_id", 
            "name": "name", 
            "proto": "proto", 
        },

        "modular": {
            "adminState": "admin_state", 
            "com2Sec": "com2_sec", 
            "community": "community", 
            "dn": "dn", 
            "engineIdKey": "engine_id_key", 
            "port": "port", 
            "rn": "rn", 
            "status": "status", 
            "sysContact": "sys_contact", 
            "sysLocation": "sys_location", 
            "trapCommunity": "trap_community", 
            "childAction": "child_action", 
            "descr": "descr", 
            "engineId": "engine_id", 
            "name": "name", 
            "proto": "proto", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.com2_sec = None
        self.community = None
        self.engine_id_key = None
        self.port = None
        self.status = None
        self.sys_contact = None
        self.sys_location = None
        self.trap_community = None
        self.child_action = None
        self.descr = None
        self.engine_id = None
        self.name = None
        self.proto = None

        ManagedObject.__init__(self, "CommSnmp", parent_mo_or_dn, **kwargs)

