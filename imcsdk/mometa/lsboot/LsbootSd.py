"""This module contains the general information for LsbootSd ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LsbootSdConsts:
    STATE_DISABLED = "Disabled"
    STATE_ENABLED = "Enabled"
    SUBTYPE_ = ""
    SUBTYPE_SDCARD = "SDCARD"
    SUBTYPE_FLEX_FLASH = "flex-flash"
    SUBTYPE_FLEX_UTIL = "flex-util"
    TYPE_SDCARD = "SDCARD"


class LsbootSd(ManagedObject):
    """This is LsbootSd class."""

    consts = LsbootSdConsts()
    naming_props = set(['name'])

    mo_meta = {
        "classic": MoMeta("LsbootSd", "lsbootSd", "sd-[name]", VersionMeta.Version201a, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['lsbootDevPrecision'], [], ["Add", "Get", "Remove", "Set"]),
        "modular": MoMeta("LsbootSd", "lsbootSd", "sd-[name]", VersionMeta.Version2013e, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['lsbootDevPrecision'], [], ["Add", "Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "lun": MoPropertyMeta("lun", "lun", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201a, MoPropertyMeta.NAMING, 0x8, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []),
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-255"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "subtype": MoPropertyMeta("subtype", "subtype", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "SDCARD", "flex-flash", "flex-util"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["SDCARD"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "lun": MoPropertyMeta("lun", "lun", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x8, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []),
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-255"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "subtype": MoPropertyMeta("subtype", "subtype", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["SDCARD"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["SDCARD"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "lun": "lun", 
            "name": "name", 
            "order": "order", 
            "rn": "rn", 
            "state": "state", 
            "status": "status", 
            "subtype": "subtype", 
            "type": "type", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "lun": "lun", 
            "name": "name", 
            "order": "order", 
            "rn": "rn", 
            "state": "state", 
            "status": "status", 
            "subtype": "subtype", 
            "type": "type", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.lun = None
        self.order = None
        self.state = None
        self.status = None
        self.subtype = None
        self.type = None
        self.child_action = None

        ManagedObject.__init__(self, "LsbootSd", parent_mo_or_dn, **kwargs)

