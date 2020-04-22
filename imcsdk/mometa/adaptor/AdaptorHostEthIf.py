"""This module contains the general information for AdaptorHostEthIf ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorHostEthIfConsts:
    IF_TYPE_VIRTUAL = "virtual"
    MAC_AUTO = "AUTO"
    UPLINK_PORT_0 = "0"
    UPLINK_PORT_1 = "1"
    UPLINK_PORT_2 = "2"
    UPLINK_PORT_3 = "3"


class AdaptorHostEthIf(ManagedObject):
    """This is AdaptorHostEthIf class."""

    consts = AdaptorHostEthIfConsts()
    naming_props = set(['name'])

    mo_meta = {
        "classic": MoMeta("AdaptorHostEthIf", "adaptorHostEthIf", "host-eth-[name]", VersionMeta.Version151f, "InputOutput", 0x3fff, [], ["admin", "read-only", "user"], ['adaptorUnit'], [], ["Add", "Get", "Remove", "Set"]),
        "modular": MoMeta("AdaptorHostEthIf", "adaptorHostEthIf", "host-eth-[name]", VersionMeta.Version2013e, "InputOutput", 0x3fff, [], ["admin", "read-only", "user"], ['adaptorUnit'], [], ["Add", "Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "advanced_filter": MoPropertyMeta("advanced_filter", "advancedFilter", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "cdn": MoPropertyMeta("cdn", "cdn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[a-zA-Z0-9\-\._:]{0,32}""", [], []),
            "channel_number": MoPropertyMeta("channel_number", "channelNumber", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-1000"]),
            "class_of_service": MoPropertyMeta("class_of_service", "classOfService", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[0-6]""", [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "mac": MoPropertyMeta("mac", "mac", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", ["AUTO"], []),
            "mtu": MoPropertyMeta("mtu", "mtu", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["1500-9000"]),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x100, None, None, r"""[a-zA-Z0-9\-\._:]{1,31}""", [], []),
            "port_profile": MoPropertyMeta("port_profile", "portProfile", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""(([a-zA-Z0-9_]{1})|([a-zA-Z0-9_]{1}[a-zA-Z0-9_\-]{0,62}))""", [], []),
            "pxe_boot": MoPropertyMeta("pxe_boot", "pxeBoot", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "uplink_port": MoPropertyMeta("uplink_port", "uplinkPort", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["0", "1", "2", "3"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["virtual"], []),
            "iscsi_boot": MoPropertyMeta("iscsi_boot", "iscsiBoot", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "usnic_count": MoPropertyMeta("usnic_count", "usnicCount", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-225"]),
        },

        "modular": {
            "advanced_filter": MoPropertyMeta("advanced_filter", "advancedFilter", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "cdn": MoPropertyMeta("cdn", "cdn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[a-zA-Z0-9\-\._:]{0,32}""", [], []),
            "channel_number": MoPropertyMeta("channel_number", "channelNumber", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-1000"]),
            "class_of_service": MoPropertyMeta("class_of_service", "classOfService", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[0-6]""", [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "mac": MoPropertyMeta("mac", "mac", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", ["AUTO"], []),
            "mtu": MoPropertyMeta("mtu", "mtu", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["1500-9000"]),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x100, None, None, r"""[a-zA-Z0-9\-\._:]{1,31}""", [], []),
            "port_profile": MoPropertyMeta("port_profile", "portProfile", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""(([a-zA-Z0-9_]{1})|([a-zA-Z0-9_]{1}[a-zA-Z0-9_\-]{0,79}))""", [], []),
            "pxe_boot": MoPropertyMeta("pxe_boot", "pxeBoot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "uplink_port": MoPropertyMeta("uplink_port", "uplinkPort", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["0", "1", "2", "3"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["virtual"], []),
            "iscsi_boot": MoPropertyMeta("iscsi_boot", "iscsiBoot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "usnic_count": MoPropertyMeta("usnic_count", "usnicCount", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-225"]),
        },

    }

    prop_map = {

        "classic": {
            "advancedFilter": "advanced_filter", 
            "cdn": "cdn", 
            "channelNumber": "channel_number", 
            "classOfService": "class_of_service", 
            "dn": "dn", 
            "mac": "mac", 
            "mtu": "mtu", 
            "name": "name", 
            "portProfile": "port_profile", 
            "pxeBoot": "pxe_boot", 
            "rn": "rn", 
            "status": "status", 
            "uplinkPort": "uplink_port", 
            "childAction": "child_action", 
            "ifType": "if_type", 
            "iscsiBoot": "iscsi_boot", 
            "usnicCount": "usnic_count", 
        },

        "modular": {
            "advancedFilter": "advanced_filter", 
            "cdn": "cdn", 
            "channelNumber": "channel_number", 
            "classOfService": "class_of_service", 
            "dn": "dn", 
            "mac": "mac", 
            "mtu": "mtu", 
            "name": "name", 
            "portProfile": "port_profile", 
            "pxeBoot": "pxe_boot", 
            "rn": "rn", 
            "status": "status", 
            "uplinkPort": "uplink_port", 
            "childAction": "child_action", 
            "ifType": "if_type", 
            "iscsiBoot": "iscsi_boot", 
            "usnicCount": "usnic_count", 
        },

    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.advanced_filter = None
        self.cdn = None
        self.channel_number = None
        self.class_of_service = None
        self.mac = None
        self.mtu = None
        self.port_profile = None
        self.pxe_boot = None
        self.status = None
        self.uplink_port = None
        self.child_action = None
        self.if_type = None
        self.iscsi_boot = None
        self.usnic_count = None

        ManagedObject.__init__(self, "AdaptorHostEthIf", parent_mo_or_dn, **kwargs)

