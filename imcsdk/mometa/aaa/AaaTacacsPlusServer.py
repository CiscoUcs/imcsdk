"""This module contains the general information for AaaTacacsPlusServer ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AaaTacacsPlusServerConsts:
    ADMIN_ACTION_CLEAR = "clear"


class AaaTacacsPlusServer(ManagedObject):
    """This is AaaTacacsPlusServer class."""

    consts = AaaTacacsPlusServerConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("AaaTacacsPlusServer", "aaaTacacsPlusServer", "server-[id]", VersionMeta.Version413a, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['aaaTacacsPlus'], [], [None]),
        "modular": MoMeta("AaaTacacsPlusServer", "aaaTacacsPlusServer", "server-[id]", VersionMeta.Version413a, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['aaaTacacsPlus'], [], [None])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version413a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-6"]),
            "ip_address": MoPropertyMeta("ip_address", "ipAddress", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []),
            "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x20, 1, 64, None, [], []),
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-65535"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version413a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-6"]),
            "ip_address": MoPropertyMeta("ip_address", "ipAddress", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], []),
            "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x20, 1, 64, None, [], []),
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-65535"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "id": "id", 
            "ipAddress": "ip_address", 
            "key": "key", 
            "port": "port", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "id": "id", 
            "ipAddress": "ip_address", 
            "key": "key", 
            "port": "port", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_action = None
        self.ip_address = None
        self.key = None
        self.port = None
        self.status = None

        ManagedObject.__init__(self, "AaaTacacsPlusServer", parent_mo_or_dn, **kwargs)

