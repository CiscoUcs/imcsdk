"""This module contains the general information for AdaptorFcPersistentBindings ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorFcPersistentBindingsConsts:
    pass


class AdaptorFcPersistentBindings(ManagedObject):
    """This is AdaptorFcPersistentBindings class."""

    consts = AdaptorFcPersistentBindingsConsts()
    naming_props = set(['index'])

    mo_meta = {
        "classic": MoMeta("AdaptorFcPersistentBindings", "adaptorFcPersistentBindings", "perbi-[index]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['adaptorHostFcIf'], [], ["Get"]),
        "modular": MoMeta("AdaptorFcPersistentBindings", "adaptorFcPersistentBindings", "perbi-[index]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['adaptorHostFcIf'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "bus_id": MoPropertyMeta("bus_id", "busId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "host_wwpn": MoPropertyMeta("host_wwpn", "hostWwpn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
            "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "target_id": MoPropertyMeta("target_id", "targetId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "target_wwpn": MoPropertyMeta("target_wwpn", "targetWwpn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
        },

        "modular": {
            "bus_id": MoPropertyMeta("bus_id", "busId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "host_wwpn": MoPropertyMeta("host_wwpn", "hostWwpn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
            "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "target_id": MoPropertyMeta("target_id", "targetId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "target_wwpn": MoPropertyMeta("target_wwpn", "targetWwpn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "busId": "bus_id", 
            "childAction": "child_action", 
            "dn": "dn", 
            "hostWwpn": "host_wwpn", 
            "index": "index", 
            "rn": "rn", 
            "status": "status", 
            "targetId": "target_id", 
            "targetWwpn": "target_wwpn", 
        },

        "modular": {
            "busId": "bus_id", 
            "childAction": "child_action", 
            "dn": "dn", 
            "hostWwpn": "host_wwpn", 
            "index": "index", 
            "rn": "rn", 
            "status": "status", 
            "targetId": "target_id", 
            "targetWwpn": "target_wwpn", 
        },

    }

    def __init__(self, parent_mo_or_dn, index, **kwargs):
        self._dirty_mask = 0
        self.index = index
        self.bus_id = None
        self.child_action = None
        self.host_wwpn = None
        self.status = None
        self.target_id = None
        self.target_wwpn = None

        ManagedObject.__init__(self, "AdaptorFcPersistentBindings", parent_mo_or_dn, **kwargs)

