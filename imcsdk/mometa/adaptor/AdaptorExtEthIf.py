"""This module contains the general information for AdaptorExtEthIf ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorExtEthIfConsts:
    ADMIN_FEC_MODE_AUTO = "Auto"
    ADMIN_FEC_MODE_OFF = "Off"
    ADMIN_FEC_MODE_CL74 = "cl74"
    ADMIN_FEC_MODE_CL91 = "cl91"
    ADMIN_SPEED_ = "-"
    ADMIN_SPEED_10_GBPS = "10Gbps"
    ADMIN_SPEED_1_GBPS = "1Gbps"
    ADMIN_SPEED_40_GBPS = "40Gbps"
    ADMIN_SPEED_4X10_GBPS = "4x10Gbps"
    ADMIN_SPEED_AUTO = "Auto"
    IF_TYPE_AGGREGATION = "aggregation"
    IF_TYPE_PHYSICAL = "physical"
    IF_TYPE_UNKNOWN = "unknown"
    IF_TYPE_VIRTUAL = "virtual"
    LINK_STATE_ADMIN_DOWN = "admin-down"
    LINK_STATE_DOWN = "down"
    LINK_STATE_ERROR = "error"
    LINK_STATE_UNALLOCATED = "unallocated"
    LINK_STATE_UNAVAILABLE = "unavailable"
    LINK_STATE_UNKNOWN = "unknown"
    LINK_STATE_UP = "up"
    OPER_FEC_MODE_AUTO = "Auto"
    OPER_FEC_MODE_OFF = "Off"
    OPER_FEC_MODE_CL74 = "cl74"
    OPER_FEC_MODE_CL91 = "cl91"
    OPER_SPEED_ = "-"
    OPER_SPEED_100_GBPS = "100Gbps"
    OPER_SPEED_10_GBPS = "10Gbps"
    OPER_SPEED_1_GBPS = "1Gbps"
    OPER_SPEED_25_GBPS = "25Gbps"
    OPER_SPEED_40_GBPS = "40Gbps"
    OPER_SPEED_4X10_GBPS = "4x10Gbps"
    OPER_SPEED_AUTO = "Auto"
    PORT_ID_0 = "0"
    PORT_ID_1 = "1"
    PORT_ID_2 = "2"
    PORT_ID_3 = "3"


class AdaptorExtEthIf(ManagedObject):
    """This is AdaptorExtEthIf class."""

    consts = AdaptorExtEthIfConsts()
    naming_props = set(['portId'])

    mo_meta = {
        "classic": MoMeta("AdaptorExtEthIf", "adaptorExtEthIf", "ext-eth-[port_id]", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['adaptorUnit'], ['adaptorConnectorInfo', 'adaptorLinkTraining', 'adaptorPortProfiles'], ["Get", "Set"]),
        "modular": MoMeta("AdaptorExtEthIf", "adaptorExtEthIf", "ext-eth-[port_id]", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['adaptorUnit'], ['adaptorConnectorInfo', 'adaptorLinkTraining', 'adaptorPortProfiles'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_fec_mode": MoPropertyMeta("admin_fec_mode", "adminFecMode", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Auto", "Off", "cl74", "cl91"], []),
            "admin_speed": MoPropertyMeta("admin_speed", "adminSpeed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["-", "10Gbps", "1Gbps", "40Gbps", "4x10Gbps", "Auto"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "port_id": MoPropertyMeta("port_id", "portId", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x10, None, None, None, ["0", "1", "2", "3"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
            "link_state": MoPropertyMeta("link_state", "linkState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["admin-down", "down", "error", "unallocated", "unavailable", "unknown", "up"], []),
            "mac": MoPropertyMeta("mac", "mac", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
            "oper_fec_mode": MoPropertyMeta("oper_fec_mode", "operFecMode", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Auto", "Off", "cl74", "cl91"], []),
            "oper_speed": MoPropertyMeta("oper_speed", "operSpeed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["-", "100Gbps", "10Gbps", "1Gbps", "25Gbps", "40Gbps", "4x10Gbps", "Auto"], []),
            "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

        "modular": {
            "admin_fec_mode": MoPropertyMeta("admin_fec_mode", "adminFecMode", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Auto", "Off", "cl74", "cl91"], []),
            "admin_speed": MoPropertyMeta("admin_speed", "adminSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["-", "40Gbps", "4x10Gbps", "Auto"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "port_id": MoPropertyMeta("port_id", "portId", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x10, None, None, None, ["0", "1", "2", "3"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
            "link_state": MoPropertyMeta("link_state", "linkState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["admin-down", "down", "error", "unallocated", "unavailable", "unknown", "up"], []),
            "mac": MoPropertyMeta("mac", "mac", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
            "oper_fec_mode": MoPropertyMeta("oper_fec_mode", "operFecMode", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Auto", "Off", "cl74", "cl91"], []),
            "oper_speed": MoPropertyMeta("oper_speed", "operSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["-", "100Gbps", "10Gbps", "1Gbps", "25Gbps", "40Gbps", "4x10Gbps", "Auto"], []),
            "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminFecMode": "admin_fec_mode", 
            "adminSpeed": "admin_speed", 
            "dn": "dn", 
            "portId": "port_id", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "ifType": "if_type", 
            "linkState": "link_state", 
            "mac": "mac", 
            "operFecMode": "oper_fec_mode", 
            "operSpeed": "oper_speed", 
            "transport": "transport", 
        },

        "modular": {
            "adminFecMode": "admin_fec_mode", 
            "adminSpeed": "admin_speed", 
            "dn": "dn", 
            "portId": "port_id", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "ifType": "if_type", 
            "linkState": "link_state", 
            "mac": "mac", 
            "operFecMode": "oper_fec_mode", 
            "operSpeed": "oper_speed", 
            "transport": "transport", 
        },

    }

    def __init__(self, parent_mo_or_dn, port_id, **kwargs):
        self._dirty_mask = 0
        self.port_id = port_id
        self.admin_fec_mode = None
        self.admin_speed = None
        self.status = None
        self.child_action = None
        self.if_type = None
        self.link_state = None
        self.mac = None
        self.oper_fec_mode = None
        self.oper_speed = None
        self.transport = None

        ManagedObject.__init__(self, "AdaptorExtEthIf", parent_mo_or_dn, **kwargs)

