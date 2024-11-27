"""This module contains the general information for AaaUser ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AaaUserConsts:
    ACCOUNT_STATUS_ACTIVE = "active"
    ACCOUNT_STATUS_INACTIVE = "inactive"
    ADMIN_ACTION_CLEAR = "clear"
    AUTH_ = ""
    AUTH_NONE = "None"
    AUTH_SHA = "SHA"
    AUTH_SHA_224 = "SHA-224"
    AUTH_SHA_256 = "SHA-256"
    AUTH_SHA_384 = "SHA-384"
    AUTH_SHA_512 = "SHA-512"
    PRIV_ = ""
    PRIV_ADMIN = "admin"
    PRIV_READ_ONLY = "read-only"
    PRIV_SNMPONLY = "snmponly"
    PRIV_USER = "user"
    PRIVACY_ = ""
    PRIVACY_AES = "AES"
    PRIVACY_NONE = "None"


class AaaUser(ManagedObject):
    """This is AaaUser class."""

    consts = AaaUserConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("AaaUser", "aaaUser", "user-[id]", VersionMeta.Version151f, "InputOutput", 0xffff, [], ["admin", "read-only", "user"], ['aaaUserEp'], ['aaaUserSSHKey'], ["Get", "Set"]),
        "modular": MoMeta("AaaUser", "aaaUser", "user-[id]", VersionMeta.Version2013e, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['aaaUserEp'], ['aaaUserSSHKey'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "account_status": MoPropertyMeta("account_status", "accountStatus", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["active", "inactive"], []),
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version208d, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, ["clear"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-32"]),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[a-zA-Z0-9\._\+\-]{0,32}""", [], []),
            "priv": MoPropertyMeta("priv", "priv", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "admin", "read-only", "snmponly", "user"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "auth": MoPropertyMeta("auth", "auth", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "None", "SHA", "SHA-224", "SHA-256", "SHA-384", "SHA-512"], []),
            "auth_pwd": MoPropertyMeta("auth_pwd", "authPwd", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""(.{8,64})?""", [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "ipmi_pwd": MoPropertyMeta("ipmi_pwd", "ipmiPwd", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""(.{8,64})?""", [], []),
            "privacy": MoPropertyMeta("privacy", "privacy", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["", "AES", "None"], []),
            "privacy_pwd": MoPropertyMeta("privacy_pwd", "privacyPwd", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""(.{8,64})?""", [], []),
            "user_type": MoPropertyMeta("user_type", "userType", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], []),
        },

        "modular": {
            "account_status": MoPropertyMeta("account_status", "accountStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["active", "inactive"], []),
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, ["clear"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-15"]),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[a-zA-Z0-9\._\+\-]{0,16}""", [], []),
            "priv": MoPropertyMeta("priv", "priv", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "admin", "read-only", "user"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[!""#%&'$\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,20}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "accountStatus": "account_status", 
            "adminAction": "admin_action", 
            "dn": "dn", 
            "id": "id", 
            "name": "name", 
            "priv": "priv", 
            "pwd": "pwd", 
            "rn": "rn", 
            "status": "status", 
            "auth": "auth", 
            "authPwd": "auth_pwd", 
            "childAction": "child_action", 
            "ipmiPwd": "ipmi_pwd", 
            "privacy": "privacy", 
            "privacyPwd": "privacy_pwd", 
            "userType": "user_type", 
        },

        "modular": {
            "accountStatus": "account_status", 
            "adminAction": "admin_action", 
            "dn": "dn", 
            "id": "id", 
            "name": "name", 
            "priv": "priv", 
            "pwd": "pwd", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.account_status = None
        self.admin_action = None
        self.name = None
        self.priv = None
        self.pwd = None
        self.status = None
        self.auth = None
        self.auth_pwd = None
        self.child_action = None
        self.ipmi_pwd = None
        self.privacy = None
        self.privacy_pwd = None
        self.user_type = None

        ManagedObject.__init__(self, "AaaUser", parent_mo_or_dn, **kwargs)

