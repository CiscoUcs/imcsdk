"""This module contains the general information for AaaUser ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AaaUserConsts:
    ACCOUNT_STATUS_ACTIVE = "active"
    ACCOUNT_STATUS_INACTIVE = "inactive"
    ADMIN_ACTION_CLEAR = "clear"
    PRIV_ = ""
    PRIV_ADMIN = "admin"
    PRIV_READ_ONLY = "read-only"
    PRIV_USER = "user"


class AaaUser(ManagedObject):
    """This is AaaUser class."""

    consts = AaaUserConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("AaaUser", "aaaUser", "user-[id]", VersionMeta.Version151f, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['aaaUserEp'], ['aaaUserSSHKey'], ["Get", "Set"]),
        "modular": MoMeta("AaaUser", "aaaUser", "user-[id]", VersionMeta.Version2013e, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['aaaUserEp'], ['aaaUserSSHKey'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "account_status": MoPropertyMeta("account_status", "accountStatus", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["active", "inactive"], []),
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version208d, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, ["clear"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-15"]),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[a-zA-Z0-9\._\+\-]{0,16}""", [], []),
            "priv": MoPropertyMeta("priv", "priv", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "admin", "read-only", "user"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
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
            "childAction": "child_action", 
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
        self.child_action = None

        ManagedObject.__init__(self, "AaaUser", parent_mo_or_dn, **kwargs)

