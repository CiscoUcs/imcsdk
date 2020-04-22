"""This module contains the general information for SolIf ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class SolIfConsts:
    ADMIN_STATE_DISABLED = "Disabled"
    ADMIN_STATE_ENABLED = "Enabled"
    ADMIN_STATE_DISABLE = "disable"
    _ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLE = "enable"
    _ADMIN_STATE_ENABLED = "enabled"
    COMPORT_COM0 = "com0"
    COMPORT_COM1 = "com1"
    SPEED_115200 = "115200"
    SPEED_19200 = "19200"
    SPEED_38400 = "38400"
    SPEED_57600 = "57600"
    SPEED_9600 = "9600"


class SolIf(ManagedObject):
    """This is SolIf class."""

    consts = SolIfConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("SolIf", "solIf", "sol-if", VersionMeta.Version151f, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['computeRackUnit'], [], ["Get", "Set"]),
        "modular": MoMeta("SolIf", "solIf", "sol-if", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['computeServerNode'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disable", "disabled", "enable", "enabled"], []),
            "comport": MoPropertyMeta("comport", "comport", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["com0", "com1"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "speed": MoPropertyMeta("speed", "speed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["115200", "19200", "38400", "57600", "9600"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
            "ssh_port": MoPropertyMeta("ssh_port", "sshPort", "uint", VersionMeta.Version208d, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["1024-65535"]),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disable", "disabled", "enable", "enabled"], []),
            "comport": MoPropertyMeta("comport", "comport", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["com0", "com1"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "speed": MoPropertyMeta("speed", "speed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["115200", "19200", "38400", "57600", "9600"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
            "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-65535"]),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "comport": "comport", 
            "dn": "dn", 
            "rn": "rn", 
            "speed": "speed", 
            "status": "status", 
            "childAction": "child_action", 
            "name": "name", 
            "sshPort": "ssh_port", 
        },

        "modular": {
            "adminState": "admin_state", 
            "comport": "comport", 
            "dn": "dn", 
            "rn": "rn", 
            "speed": "speed", 
            "status": "status", 
            "childAction": "child_action", 
            "name": "name", 
            "port": "port", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.comport = None
        self.speed = None
        self.status = None
        self.child_action = None
        self.name = None
        self.ssh_port = None
        self.port = None

        ManagedObject.__init__(self, "SolIf", parent_mo_or_dn, **kwargs)

