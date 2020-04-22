"""This module contains the general information for AdaptorHostFcIf ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorHostFcIfConsts:
    ADMIN_PERSISTENT_BINDINGS_POLICY = "policy"
    ADMIN_PERSISTENT_BINDINGS_REBUILD = "rebuild"
    IF_TYPE_VIRTUAL = "virtual"
    UPLINK_PORT_0 = "0"
    UPLINK_PORT_1 = "1"
    UPLINK_PORT_2 = "2"
    UPLINK_PORT_3 = "3"
    WWNN_AUTO = "AUTO"
    WWPN_AUTO = "AUTO"


class AdaptorHostFcIf(ManagedObject):
    """This is AdaptorHostFcIf class."""

    consts = AdaptorHostFcIfConsts()
    naming_props = set(['name'])

    mo_meta = {
        "classic": MoMeta("AdaptorHostFcIf", "adaptorHostFcIf", "host-fc-[name]", VersionMeta.Version151f, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], ['adaptorUnit'], ['adaptorFcPersistentBindings'], ["Add", "Get", "Remove", "Set"]),
        "modular": MoMeta("AdaptorHostFcIf", "adaptorHostFcIf", "host-fc-[name]", VersionMeta.Version2013e, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], ['adaptorUnit'], ['adaptorFcPersistentBindings'], ["Add", "Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_persistent_bindings": MoPropertyMeta("admin_persistent_bindings", "adminPersistentBindings", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["policy", "rebuild"], []),
            "channel_number": MoPropertyMeta("channel_number", "channelNumber", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-1000"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x10, None, None, r"""[a-zA-Z0-9\-\._:]{1,31}""", [], []),
            "port_profile": MoPropertyMeta("port_profile", "portProfile", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""(([a-zA-Z0-9_]{1})|([a-zA-Z0-9_]{1}[a-zA-Z0-9_\-]{0,62}))""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "san_boot": MoPropertyMeta("san_boot", "sanBoot", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "uplink_port": MoPropertyMeta("uplink_port", "uplinkPort", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["0", "1", "2", "3"], []),
            "wwnn": MoPropertyMeta("wwnn", "wwnn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", ["AUTO"], []),
            "wwpn": MoPropertyMeta("wwpn", "wwpn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", ["AUTO"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["virtual"], []),
        },

        "modular": {
            "admin_persistent_bindings": MoPropertyMeta("admin_persistent_bindings", "adminPersistentBindings", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["policy", "rebuild"], []),
            "channel_number": MoPropertyMeta("channel_number", "channelNumber", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-1000"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x10, None, None, r"""[a-zA-Z0-9\-\._:]{1,31}""", [], []),
            "port_profile": MoPropertyMeta("port_profile", "portProfile", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""(([a-zA-Z0-9_]{1})|([a-zA-Z0-9_]{1}[a-zA-Z0-9_\-]{0,79}))""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "san_boot": MoPropertyMeta("san_boot", "sanBoot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "uplink_port": MoPropertyMeta("uplink_port", "uplinkPort", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["0", "1", "2", "3"], []),
            "wwnn": MoPropertyMeta("wwnn", "wwnn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", ["AUTO"], []),
            "wwpn": MoPropertyMeta("wwpn", "wwpn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", ["AUTO"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["virtual"], []),
        },

    }

    prop_map = {

        "classic": {
            "adminPersistentBindings": "admin_persistent_bindings", 
            "channelNumber": "channel_number", 
            "dn": "dn", 
            "name": "name", 
            "portProfile": "port_profile", 
            "rn": "rn", 
            "sanBoot": "san_boot", 
            "status": "status", 
            "uplinkPort": "uplink_port", 
            "wwnn": "wwnn", 
            "wwpn": "wwpn", 
            "childAction": "child_action", 
            "ifType": "if_type", 
        },

        "modular": {
            "adminPersistentBindings": "admin_persistent_bindings", 
            "channelNumber": "channel_number", 
            "dn": "dn", 
            "name": "name", 
            "portProfile": "port_profile", 
            "rn": "rn", 
            "sanBoot": "san_boot", 
            "status": "status", 
            "uplinkPort": "uplink_port", 
            "wwnn": "wwnn", 
            "wwpn": "wwpn", 
            "childAction": "child_action", 
            "ifType": "if_type", 
        },

    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_persistent_bindings = None
        self.channel_number = None
        self.port_profile = None
        self.san_boot = None
        self.status = None
        self.uplink_port = None
        self.wwnn = None
        self.wwpn = None
        self.child_action = None
        self.if_type = None

        ManagedObject.__init__(self, "AdaptorHostFcIf", parent_mo_or_dn, **kwargs)

