"""This module contains the general information for AaaUserAuthPrecedence ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AaaUserAuthPrecedenceConsts:
    AUTH_PRECEDENCE1_LDAP_USER_DB = "ldap-user-db"
    AUTH_PRECEDENCE1_LOCAL_USER_DB = "local-user-db"
    AUTH_PRECEDENCE1_TACACS_USER_DB = "tacacs-user-db"
    AUTH_PRECEDENCE2_LDAP_USER_DB = "ldap-user-db"
    AUTH_PRECEDENCE2_LOCAL_USER_DB = "local-user-db"
    AUTH_PRECEDENCE2_TACACS_USER_DB = "tacacs-user-db"
    AUTH_PRECEDENCE3_LDAP_USER_DB = "ldap-user-db"
    AUTH_PRECEDENCE3_LOCAL_USER_DB = "local-user-db"
    AUTH_PRECEDENCE3_TACACS_USER_DB = "tacacs-user-db"


class AaaUserAuthPrecedence(ManagedObject):
    """This is AaaUserAuthPrecedence class."""

    consts = AaaUserAuthPrecedenceConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AaaUserAuthPrecedence", "aaaUserAuthPrecedence", "auth-precedence", VersionMeta.Version413a, "InputOutput", 0x7f, [], ["admin"], ['aaaUserEp'], [], [None]),
        "modular": MoMeta("AaaUserAuthPrecedence", "aaaUserAuthPrecedence", "auth-precedence", VersionMeta.Version413a, "InputOutput", 0x7f, [], ["admin"], ['aaaUserEp'], [], [None])
    }


    prop_meta = {

        "classic": {
            "auth_precedence1": MoPropertyMeta("auth_precedence1", "authPrecedence1", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["ldap-user-db", "local-user-db", "tacacs-user-db"], []),
            "auth_precedence2": MoPropertyMeta("auth_precedence2", "authPrecedence2", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["ldap-user-db", "local-user-db", "tacacs-user-db"], []),
            "auth_precedence3": MoPropertyMeta("auth_precedence3", "authPrecedence3", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["ldap-user-db", "local-user-db", "tacacs-user-db"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "auth_precedence1": MoPropertyMeta("auth_precedence1", "authPrecedence1", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["ldap-user-db", "local-user-db", "tacacs-user-db"], []),
            "auth_precedence2": MoPropertyMeta("auth_precedence2", "authPrecedence2", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["ldap-user-db", "local-user-db", "tacacs-user-db"], []),
            "auth_precedence3": MoPropertyMeta("auth_precedence3", "authPrecedence3", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["ldap-user-db", "local-user-db", "tacacs-user-db"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "authPrecedence1": "auth_precedence1", 
            "authPrecedence2": "auth_precedence2", 
            "authPrecedence3": "auth_precedence3", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "authPrecedence1": "auth_precedence1", 
            "authPrecedence2": "auth_precedence2", 
            "authPrecedence3": "auth_precedence3", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.auth_precedence1 = None
        self.auth_precedence2 = None
        self.auth_precedence3 = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "AaaUserAuthPrecedence", parent_mo_or_dn, **kwargs)

