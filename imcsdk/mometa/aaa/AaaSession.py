"""This module contains the general information for AaaSession ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AaaSessionConsts:
    UI_EP = "ep"
    UI_NONE = "none"
    UI_REDFISH = "redfish"
    UI_SECURELOGIN = "securelogin"
    UI_SERIAL = "serial"
    UI_SHELL = "shell"
    UI_SOL = "sol"
    UI_V_MEDIA = "vMedia"
    UI_WEB = "web"
    UI_SERVER_1_SOL = "server-1:SOL"
    UI_SERVER_1_V_KVM = "server-1:vKVM"
    UI_SERVER_1_V_MEDIA = "server-1:vMedia"
    UI_SERVER_2_SOL = "server-2:SOL"
    UI_SERVER_2_V_KVM = "server-2:vKVM"
    UI_SERVER_2_V_MEDIA = "server-2:vMedia"


class AaaSession(ManagedObject):
    """This is AaaSession class."""

    consts = AaaSessionConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("AaaSession", "aaaSession", "term-[id]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['aaaUserEp'], [], ["Get"]),
        "modular": MoMeta("AaaSession", "aaaSession", "term-[id]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['aaaUserEp'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "host": MoPropertyMeta("host", "host", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, 1, 32, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "ui": MoPropertyMeta("ui", "ui", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ep", "none", "redfish", "securelogin", "serial", "shell", "sol", "vMedia", "web"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "host": MoPropertyMeta("host", "host", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 1, 32, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "ui": MoPropertyMeta("ui", "ui", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ep", "none", "redfish", "serial", "server-1:SOL", "server-1:vKVM", "server-1:vMedia", "server-2:SOL", "server-2:vKVM", "server-2:vMedia", "shell", "vMedia", "web"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "host": "host", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
            "ui": "ui", 
            "user": "user", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "host": "host", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
            "ui": "ui", 
            "user": "user", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.host = None
        self.status = None
        self.ui = None
        self.user = None

        ManagedObject.__init__(self, "AaaSession", parent_mo_or_dn, **kwargs)

