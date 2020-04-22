"""This module contains the general information for LsbootCdd ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LsbootCddConsts:
    STATE_DISABLED = "Disabled"
    STATE_ENABLED = "Enabled"
    TYPE_LOCALCDD = "LOCALCDD"


class LsbootCdd(ManagedObject):
    """This is LsbootCdd class."""

    consts = LsbootCddConsts()
    naming_props = set(['name'])

    mo_meta = {
        "classic": MoMeta("LsbootCdd", "lsbootCdd", "cdd-[name]", VersionMeta.Version304a, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['lsbootDevPrecision'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version304a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []),
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-255"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["LOCALCDD"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "name": "name", 
            "order": "order", 
            "rn": "rn", 
            "state": "state", 
            "status": "status", 
            "type": "type", 
        },

    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.order = None
        self.state = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LsbootCdd", parent_mo_or_dn, **kwargs)

