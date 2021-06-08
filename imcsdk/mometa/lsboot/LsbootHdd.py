"""This module contains the general information for LsbootHdd ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LsbootHddConsts:
    STATE_DISABLED = "Disabled"
    STATE_ENABLED = "Enabled"
    SUBTYPE_LOCALHDD = "LOCALHDD"
    TYPE_LOCALHDD = "LOCALHDD"


class LsbootHdd(ManagedObject):
    """This is LsbootHdd class."""

    consts = LsbootHddConsts()
    naming_props = set(['name'])

    mo_meta = {
        "classic": MoMeta("LsbootHdd", "lsbootHdd", "hdd-[name]", VersionMeta.Version201a, "InputOutput", 0x1fff, [], ["admin", "read-only", "user"], ['lsbootDevPrecision'], [], ["Add", "Get", "Remove", "Set"]),
        "modular": MoMeta("LsbootHdd", "lsbootHdd", "hdd-[name]", VersionMeta.Version2013e, "InputOutput", 0x1fff, [], ["admin", "read-only", "user"], ['lsbootDevPrecision'], [], ["Add", "Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "boot_loader_descr": MoPropertyMeta("boot_loader_descr", "boot-loader-descr", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 128, None, [], []),
            "boot_loader_name": MoPropertyMeta("boot_loader_name", "boot-loader-name", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 128, None, [], []),
            "boot_loader_path": MoPropertyMeta("boot_loader_path", "boot-loader-path", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[^\(\)~`'\?"";<>\|&\*\^$%]{0,256}""", [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201a, MoPropertyMeta.NAMING, 0x20, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []),
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-255"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]|MRAID|RAID|M|HBA|SAS|MSTOR-RAID|MRAID1|MRAID2){0,1}""", [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "subtype": MoPropertyMeta("subtype", "subtype", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["LOCALHDD"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["LOCALHDD"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "boot_loader_descr": MoPropertyMeta("boot_loader_descr", "boot-loader-descr", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 128, None, [], []),
            "boot_loader_name": MoPropertyMeta("boot_loader_name", "boot-loader-name", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 128, None, [], []),
            "boot_loader_path": MoPropertyMeta("boot_loader_path", "boot-loader-path", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[^\(\)~`'\?"";<>\|&\*\^$%]{0,256}""", [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x20, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []),
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-255"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]|M|HBA|SBMezz1|SBMezz2|IOEMezz1|SBNVMe1|SBNVMe2|SIOCNVMe1|SIOCNVMe2|IOENVMe1|IOENVMe2|IOESlot1|IOESlot2){0,1}""", [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "subtype": MoPropertyMeta("subtype", "subtype", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["LOCALHDD"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["LOCALHDD"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "boot-loader-descr": "boot_loader_descr", 
            "boot-loader-name": "boot_loader_name", 
            "boot-loader-path": "boot_loader_path", 
            "dn": "dn", 
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
        self.order = None
        self.slot = None
        self.state = None
        self.status = None
        self.subtype = None
        self.type = None
        self.child_action = None

        ManagedObject.__init__(self, "LsbootHdd", parent_mo_or_dn, **kwargs)

