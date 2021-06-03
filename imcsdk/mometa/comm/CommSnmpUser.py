"""This module contains the general information for CommSnmpUser ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommSnmpUserConsts:
    ADMIN_ACTION_CLEAR = "clear"
    AUTH_ = ""
    AUTH_MD5 = "MD5"
    AUTH_SHA = "SHA"
    AUTH_SHA_224 = "SHA-224"
    AUTH_SHA_256 = "SHA-256"
    AUTH_SHA_384 = "SHA-384"
    AUTH_SHA_512 = "SHA-512"
    CONFIG_CHANGE_COMMIT = "commit"
    CONFIG_CHANGE_NO_COMMIT = "no-commit"
    PRIVACY_ = ""
    PRIVACY_AES = "AES"
    PRIVACY_DES = "DES"
    SECURITY_LEVEL_ = ""
    SECURITY_LEVEL_AUTHNOPRIV = "authnopriv"
    SECURITY_LEVEL_AUTHPRIV = "authpriv"
    SECURITY_LEVEL_NOAUTHNOPRIV = "noauthnopriv"
    PRIVACY_SHA = "SHA"


class CommSnmpUser(ManagedObject):
    """This is CommSnmpUser class."""

    consts = CommSnmpUserConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("CommSnmpUser", "commSnmpUser", "snmpv3-user-[id]", VersionMeta.Version151f, "InputOutput", 0x1fff, [], ["admin", "read-only", "user"], ['commSnmp'], [], ["Get", "Set"]),
        "modular": MoMeta("CommSnmpUser", "commSnmpUser", "snmpv3-user-[id]", VersionMeta.Version2013e, "InputOutput", 0x1fff, [], ["admin", "read-only", "user"], ['commSnmp'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version208d, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear"], []),
            "auth": MoPropertyMeta("auth", "auth", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["", "MD5", "SHA", "SHA-224", "SHA-256", "SHA-384", "SHA-512"], []),
            "auth_pwd": MoPropertyMeta("auth_pwd", "authPwd", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""(.{8,64})?""", [], []),
            "config_change": MoPropertyMeta("config_change", "configChange", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, ["commit", "no-commit"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x40, None, None, None, [], ["1-15"]),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, 0, 31, r"""[a-zA-Z0-9\._\+\-]{0,31}""", [], []),
            "privacy": MoPropertyMeta("privacy", "privacy", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "AES", "DES"], []),
            "privacy_pwd": MoPropertyMeta("privacy_pwd", "privacyPwd", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""(.{8,64})?""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, 0, 255, None, [], []),
            "security_level": MoPropertyMeta("security_level", "securityLevel", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["", "authnopriv", "authpriv", "noauthnopriv"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear"], []),
            "auth": MoPropertyMeta("auth", "auth", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["", "MD5", "SHA"], []),
            "auth_pwd": MoPropertyMeta("auth_pwd", "authPwd", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""(.{8,64})?""", [], []),
            "config_change": MoPropertyMeta("config_change", "configChange", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, ["commit", "no-commit"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x40, None, None, None, [], ["1-15"]),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 0, 31, r"""[a-zA-Z0-9\._\+\-]{0,31}""", [], []),
            "privacy": MoPropertyMeta("privacy", "privacy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "AES", "DES", "SHA"], []),
            "privacy_pwd": MoPropertyMeta("privacy_pwd", "privacyPwd", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""(.{8,64})?""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, 0, 255, None, [], []),
            "security_level": MoPropertyMeta("security_level", "securityLevel", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["", "authnopriv", "authpriv", "noauthnopriv"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "auth": "auth", 
            "authPwd": "auth_pwd", 
            "configChange": "config_change", 
            "dn": "dn", 
            "id": "id", 
            "name": "name", 
            "privacy": "privacy", 
            "privacyPwd": "privacy_pwd", 
            "rn": "rn", 
            "securityLevel": "security_level", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "auth": "auth", 
            "authPwd": "auth_pwd", 
            "configChange": "config_change", 
            "dn": "dn", 
            "id": "id", 
            "name": "name", 
            "privacy": "privacy", 
            "privacyPwd": "privacy_pwd", 
            "rn": "rn", 
            "securityLevel": "security_level", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_action = None
        self.auth = None
        self.auth_pwd = None
        self.config_change = None
        self.name = None
        self.privacy = None
        self.privacy_pwd = None
        self.security_level = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "CommSnmpUser", parent_mo_or_dn, **kwargs)

