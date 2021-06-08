"""This module contains the general information for AdaptorEthWorkQueueProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorEthWorkQueueProfileConsts:
    pass


class AdaptorEthWorkQueueProfile(ManagedObject):
    """This is AdaptorEthWorkQueueProfile class."""

    consts = AdaptorEthWorkQueueProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorEthWorkQueueProfile", "adaptorEthWorkQueueProfile", "eth-work-q", VersionMeta.Version151f, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorEthWorkQueueProfile", "adaptorEthWorkQueueProfile", "eth-work-q", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "count": MoPropertyMeta("count", "count", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["1-256"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "ring_size": MoPropertyMeta("ring_size", "ringSize", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["64-16384"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "count": MoPropertyMeta("count", "count", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["1-256"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "ring_size": MoPropertyMeta("ring_size", "ringSize", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["64-4096"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "count": "count", 
            "dn": "dn", 
            "ringSize": "ring_size", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "count": "count", 
            "dn": "dn", 
            "ringSize": "ring_size", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.count = None
        self.ring_size = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "AdaptorEthWorkQueueProfile", parent_mo_or_dn, **kwargs)

