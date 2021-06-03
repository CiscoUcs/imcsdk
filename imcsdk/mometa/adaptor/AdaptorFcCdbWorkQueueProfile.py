"""This module contains the general information for AdaptorFcCdbWorkQueueProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorFcCdbWorkQueueProfileConsts:
    pass


class AdaptorFcCdbWorkQueueProfile(ManagedObject):
    """This is AdaptorFcCdbWorkQueueProfile class."""

    consts = AdaptorFcCdbWorkQueueProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorFcCdbWorkQueueProfile", "adaptorFcCdbWorkQueueProfile", "fc-cdb-work-q", VersionMeta.Version151f, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['adaptorHostFcIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorFcCdbWorkQueueProfile", "adaptorFcCdbWorkQueueProfile", "fc-cdb-work-q", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['adaptorHostFcIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "count": MoPropertyMeta("count", "count", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["1-245"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "ring_size": MoPropertyMeta("ring_size", "ringSize", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["64-16384"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "count": MoPropertyMeta("count", "count", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["1-245"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "ring_size": MoPropertyMeta("ring_size", "ringSize", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["64-512"]),
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

        ManagedObject.__init__(self, "AdaptorFcCdbWorkQueueProfile", parent_mo_or_dn, **kwargs)

