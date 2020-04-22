"""This module contains the general information for CommEpIpmiLan ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommEpIpmiLanConsts:
    PRIV_ADMIN = "admin"
    PRIV_READ_ONLY = "read-only"
    PRIV_USER = "user"


class CommEpIpmiLan(ManagedObject):
    """This is CommEpIpmiLan class."""

    consts = CommEpIpmiLanConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("CommEpIpmiLan", "commEpIpmiLan", "cmc-ipmi-lan", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['equipmentSharedIOModule', 'equipmentSystemIOController'], [], ["Get", "Set"])
    }


    prop_meta = {

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[a-fA-F0-9]{40}""", [], []),
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-65535"]),
            "priv": MoPropertyMeta("priv", "priv", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["admin", "read-only", "user"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "modular": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "key": "key", 
            "port": "port", 
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
        self.port = None
        self.priv = None
        self.status = None

        ManagedObject.__init__(self, "CommEpIpmiLan", parent_mo_or_dn, **kwargs)

