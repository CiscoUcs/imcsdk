"""This module contains the general information for KmipServer ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class KmipServerConsts:
    ADMIN_ACTION_DELETE = "delete"
    ADMIN_ACTION_TEST_CONNECTION = "test-connection"


class KmipServer(ManagedObject):
    """This is KmipServer class."""

    consts = KmipServerConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("KmipServer", "kmipServer", "kmip-server-[id]", VersionMeta.Version302b, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['kmipManagement'], [], ["Get", "Set"]),
        "modular": MoMeta("KmipServer", "kmipServer", "kmip-server-[id]", VersionMeta.Version303a, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['kmipManagement'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete", "test-connection"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version302b, MoPropertyMeta.NAMING, 0x8, 0, 510, None, [], ["1-2"]),
            "ip_address": MoPropertyMeta("ip_address", "ipAddress", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []),
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-65535"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["0-250"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "test_connction_status": MoPropertyMeta("test_connction_status", "testConnctionStatus", "string", VersionMeta.Version302b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete", "test-connection"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version303a, MoPropertyMeta.NAMING, 0x8, 0, 510, None, [], ["1-2"]),
            "ip_address": MoPropertyMeta("ip_address", "ipAddress", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], []),
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-65535"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["0-250"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "test_connction_status": MoPropertyMeta("test_connction_status", "testConnctionStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "id": "id", 
            "ipAddress": "ip_address", 
            "port": "port", 
            "rn": "rn", 
            "status": "status", 
            "timeout": "timeout", 
            "childAction": "child_action", 
            "testConnctionStatus": "test_connction_status", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "id": "id", 
            "ipAddress": "ip_address", 
            "port": "port", 
            "rn": "rn", 
            "status": "status", 
            "timeout": "timeout", 
            "childAction": "child_action", 
            "testConnctionStatus": "test_connction_status", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_action = None
        self.ip_address = None
        self.port = None
        self.status = None
        self.timeout = None
        self.child_action = None
        self.test_connction_status = None

        ManagedObject.__init__(self, "KmipServer", parent_mo_or_dn, **kwargs)

