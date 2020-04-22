"""This module contains the general information for LsbootPxe ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LsbootPxeConsts:
    IPTYPE_ = ""
    IPTYPE_IPV4 = "IPv4"
    IPTYPE_IPV6 = "IPv6"
    MAC_ADDRESS_ = ""
    STATE_DISABLED = "Disabled"
    STATE_ENABLED = "Enabled"
    SUBTYPE_PXE = "PXE"
    TYPE_PXE = "PXE"


class LsbootPxe(ManagedObject):
    """This is LsbootPxe class."""

    consts = LsbootPxeConsts()
    naming_props = set(['name'])

    mo_meta = {
        "classic": MoMeta("LsbootPxe", "lsbootPxe", "pxe-[name]", VersionMeta.Version201a, "InputOutput", 0x1fff, [], ["admin", "read-only", "user"], ['lsbootDevPrecision'], [], ["Add", "Get", "Remove", "Set"]),
        "modular": MoMeta("LsbootPxe", "lsbootPxe", "pxe-[name]", VersionMeta.Version2013e, "InputOutput", 0x1fff, [], ["admin", "read-only", "user"], ['lsbootDevPrecision'], [], ["Add", "Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "iptype": MoPropertyMeta("iptype", "iptype", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["", "IPv4", "IPv6"], []),
            "mac_address": MoPropertyMeta("mac_address", "macAddress", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [""], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201a, MoPropertyMeta.NAMING, 0x10, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []),
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-255"]),
            "port": MoPropertyMeta("port", "port", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]|L|MLOM|L1|L2|OCP){0,1}""", [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "subtype": MoPropertyMeta("subtype", "subtype", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["PXE"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["PXE"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "iptype": MoPropertyMeta("iptype", "iptype", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["", "IPv4", "IPv6"], []),
            "mac_address": MoPropertyMeta("mac_address", "macAddress", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [""], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x10, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []),
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-255"]),
            "port": MoPropertyMeta("port", "port", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]|L|MLOM|SIOC1|SIOC2|IOESlot1|IOESlot2|SBLOM1){0,1}""", [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "subtype": MoPropertyMeta("subtype", "subtype", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["PXE"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["PXE"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "iptype": "iptype", 
            "macAddress": "mac_address", 
            "name": "name", 
            "order": "order", 
            "port": "port", 
            "rn": "rn", 
            "slot": "slot", 
            "state": "state", 
            "status": "status", 
            "subtype": "subtype", 
            "type": "type", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "iptype": "iptype", 
            "macAddress": "mac_address", 
            "name": "name", 
            "order": "order", 
            "port": "port", 
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
        self.iptype = None
        self.mac_address = None
        self.order = None
        self.port = None
        self.slot = None
        self.state = None
        self.status = None
        self.subtype = None
        self.type = None
        self.child_action = None

        ManagedObject.__init__(self, "LsbootPxe", parent_mo_or_dn, **kwargs)

