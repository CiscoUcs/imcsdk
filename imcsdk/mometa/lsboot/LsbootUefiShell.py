"""This module contains the general information for LsbootUefiShell ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LsbootUefiShellConsts:
    STATE_DISABLED = "Disabled"
    STATE_ENABLED = "Enabled"
    TYPE_UEFISHELL = "UEFISHELL"


class LsbootUefiShell(ManagedObject):
    """This is LsbootUefiShell class."""

    consts = LsbootUefiShellConsts()
    naming_props = set([u'name'])

    mo_meta = {
        "classic": MoMeta("LsbootUefiShell", "lsbootUefiShell", "uefishell-[name]", VersionMeta.Version201a, "InputOutput", 0xff, [], ["admin", "read-only", "user"], [u'lsbootDevPrecision'], [], ["Add", "Get", "Remove", "Set"]),
        "modular": MoMeta("LsbootUefiShell", "lsbootUefiShell", "uefishell-[name]", VersionMeta.Version2013e, "InputOutput", 0xff, [], ["admin", "read-only", "user"], [u'lsbootDevPrecision'], [], ["Add", "Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201a, MoPropertyMeta.NAMING, 0x4, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []), 
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-255"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["UEFISHELL"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x4, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []), 
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-255"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["UEFISHELL"], []), 
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

        "modular": {
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

        ManagedObject.__init__(self, "LsbootUefiShell", parent_mo_or_dn, **kwargs)

