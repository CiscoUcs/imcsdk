"""This module contains the general information for KmipServerLogin ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class KmipServerLoginConsts:
    ADMIN_ACTION_CLEAR = "clear"


class KmipServerLogin(ManagedObject):
    """This is KmipServerLogin class."""

    consts = KmipServerLoginConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("KmipServerLogin", "kmipServerLogin", "kmip-login", VersionMeta.Version302b, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['kmipManagement'], [], ["Get", "Set"]),
        "modular": MoMeta("KmipServerLogin", "kmipServerLogin", "kmip-login", VersionMeta.Version303a, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['kmipManagement'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "account_status": MoPropertyMeta("account_status", "accountStatus", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, ["clear"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "account_status": MoPropertyMeta("account_status", "accountStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, ["clear"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "accountStatus": "account_status", 
            "adminAction": "admin_action", 
            "dn": "dn", 
            "name": "name", 
            "pwd": "pwd", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "accountStatus": "account_status", 
            "adminAction": "admin_action", 
            "dn": "dn", 
            "name": "name", 
            "pwd": "pwd", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.account_status = None
        self.admin_action = None
        self.name = None
        self.pwd = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "KmipServerLogin", parent_mo_or_dn, **kwargs)

