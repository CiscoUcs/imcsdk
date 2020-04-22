"""This module contains the general information for LsbootSan ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LsbootSanConsts:
    STATE_DISABLED = "Disabled"
    STATE_ENABLED = "Enabled"
    SUBTYPE_SAN = "SAN"
    TYPE_SAN = "SAN"


class LsbootSan(ManagedObject):
    """This is LsbootSan class."""

    consts = LsbootSanConsts()
    naming_props = set(['name'])

    mo_meta = {
        "classic": MoMeta("LsbootSan", "lsbootSan", "san-[name]", VersionMeta.Version201a, "InputOutput", 0x3fff, [], ["admin", "read-only", "user"], ['lsbootDevPrecision'], [], ["Add", "Get", "Remove", "Set"]),
        "modular": MoMeta("LsbootSan", "lsbootSan", "san-[name]", VersionMeta.Version2013e, "InputOutput", 0x3fff, [], ["admin", "read-only", "user"], ['lsbootDevPrecision'], [], ["Add", "Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "boot_loader_descr": MoPropertyMeta("boot_loader_descr", "boot-loader-descr", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 128, None, [], []),
            "boot_loader_name": MoPropertyMeta("boot_loader_name", "boot-loader-name", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 128, None, [], []),
            "boot_loader_path": MoPropertyMeta("boot_loader_path", "boot-loader-path", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[^\(\)~`'\?"";<>\|&\*\^$%]{0,256}""", [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "lun": MoPropertyMeta("lun", "lun", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201a, MoPropertyMeta.NAMING, 0x40, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []),
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["1-255"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]|MLOM|L1|L2){0,1}""", [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "subtype": MoPropertyMeta("subtype", "subtype", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["SAN"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["SAN"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "boot_loader_descr": MoPropertyMeta("boot_loader_descr", "boot-loader-descr", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 128, None, [], []),
            "boot_loader_name": MoPropertyMeta("boot_loader_name", "boot-loader-name", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 128, None, [], []),
            "boot_loader_path": MoPropertyMeta("boot_loader_path", "boot-loader-path", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[^\(\)~`'\?"";<>\|&\*\^$%]{0,256}""", [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "lun": MoPropertyMeta("lun", "lun", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x40, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []),
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["1-255"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]|MLOM|SIOC1|SIOC2|IOESlot1|IOESlot2){0,1}""", [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "subtype": MoPropertyMeta("subtype", "subtype", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["SAN"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["SAN"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "boot-loader-descr": "boot_loader_descr", 
            "boot-loader-name": "boot_loader_name", 
            "boot-loader-path": "boot_loader_path", 
            "dn": "dn", 
            "lun": "lun", 
            "name": "name", 
            "order": "order", 
            "rn": "rn", 
            "slot": "slot", 
            "state": "state", 
            "status": "status", 
            "subtype": "subtype", 
            "type": "type", 
            "childAction": "child_action", 
        },

        "modular": {
            "boot-loader-descr": "boot_loader_descr", 
            "boot-loader-name": "boot_loader_name", 
            "boot-loader-path": "boot_loader_path", 
            "dn": "dn", 
            "lun": "lun", 
            "name": "name", 
            "order": "order", 
            "rn": "rn", 
            "slot": "slot", 
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
        self.boot_loader_descr = None
        self.boot_loader_name = None
        self.boot_loader_path = None
        self.lun = None
        self.order = None
        self.slot = None
        self.state = None
        self.status = None
        self.subtype = None
        self.type = None
        self.child_action = None

        ManagedObject.__init__(self, "LsbootSan", parent_mo_or_dn, **kwargs)

