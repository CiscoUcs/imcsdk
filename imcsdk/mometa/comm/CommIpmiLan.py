"""This module contains the general information for CommIpmiLan ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommIpmiLanConsts:
    PRIV_ADMIN = "admin"
    PRIV_READ_ONLY = "read-only"
    PRIV_USER = "user"


class CommIpmiLan(ManagedObject):
    """This is CommIpmiLan class."""

    consts = CommIpmiLanConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("CommIpmiLan", "commIpmiLan", "ipmi-lan-svc", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'commSvcEp'], [], ["Get", "Set"]),
        "modular": MoMeta("CommIpmiLan", "commIpmiLan", "ipmi-lan-svc", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'commSvcRack'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[a-fA-F0-9]{40}""", [], []), 
            "priv": MoPropertyMeta("priv", "priv", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["admin", "read-only", "user"], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[a-fA-F0-9]{40}""", [], []), 
            "priv": MoPropertyMeta("priv", "priv", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["admin", "read-only", "user"], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "key": "key", 
            "priv": "priv", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "key": "key", 
            "priv": "priv", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.key = None
        self.priv = None
        self.status = None

        ManagedObject.__init__(self, "CommIpmiLan", parent_mo_or_dn, **kwargs)

