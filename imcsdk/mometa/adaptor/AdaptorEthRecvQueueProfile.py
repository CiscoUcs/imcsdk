"""This module contains the general information for AdaptorEthRecvQueueProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorEthRecvQueueProfileConsts:
    pass


class AdaptorEthRecvQueueProfile(ManagedObject):
    """This is AdaptorEthRecvQueueProfile class."""

    consts = AdaptorEthRecvQueueProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorEthRecvQueueProfile", "adaptorEthRecvQueueProfile", "eth-rcv-q", VersionMeta.Version151f, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], [u'adaptorHostEthIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorEthRecvQueueProfile", "adaptorEthRecvQueueProfile", "eth-rcv-q", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], [u'adaptorHostEthIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "count": MoPropertyMeta("count", "count", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["1-256"]), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "ring_size": MoPropertyMeta("ring_size", "ringSize", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["64-4096"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "count": MoPropertyMeta("count", "count", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["1-256"]), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "ring_size": MoPropertyMeta("ring_size", "ringSize", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["64-4096"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "count": "count", 
            "dn": "dn", 
            "ringSize": "ring_size", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "count": "count", 
            "dn": "dn", 
            "ringSize": "ring_size", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.count = None
        self.ring_size = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorEthRecvQueueProfile", parent_mo_or_dn, **kwargs)

