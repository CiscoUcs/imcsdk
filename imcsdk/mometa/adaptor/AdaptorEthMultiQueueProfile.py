"""This module contains the general information for AdaptorEthMultiQueueProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorEthMultiQueueProfileConsts:
    pass


class AdaptorEthMultiQueueProfile(ManagedObject):
    """This is AdaptorEthMultiQueueProfile class."""

    consts = AdaptorEthMultiQueueProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorEthMultiQueueProfile", "adaptorEthMultiQueueProfile", "eth-multi-q", VersionMeta.Version402c, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'adaptorHostEthIf'], [], [None]),
        "modular": MoMeta("AdaptorEthMultiQueueProfile", "adaptorEthMultiQueueProfile", "eth-multi-q", VersionMeta.Version402c, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'adaptorHostEthIf'], [], [None])
    }


    prop_meta = {

        "classic": {
            "completion_count": MoPropertyMeta("completion_count", "completionCount", "uint", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-2000", "1-2000"]), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "receive_count": MoPropertyMeta("receive_count", "receiveCount", "uint", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-1000", "1-1000"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "transmit_count": MoPropertyMeta("transmit_count", "transmitCount", "uint", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-1000", "1-1000"]), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version402c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        },

        "modular": {
            "completion_count": MoPropertyMeta("completion_count", "completionCount", "uint", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-2000", "1-2000"]), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "receive_count": MoPropertyMeta("receive_count", "receiveCount", "uint", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-1000", "1-1000"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "transmit_count": MoPropertyMeta("transmit_count", "transmitCount", "uint", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-1000", "1-1000"]), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version402c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        },

    }

    prop_map = {

        "classic": {
            "completionCount": "completion_count", 
            "dn": "dn", 
            "receiveCount": "receive_count", 
            "rn": "rn", 
            "status": "status", 
            "transmitCount": "transmit_count", 
            "childAction": "child_action", 
        },

        "modular": {
            "completionCount": "completion_count", 
            "dn": "dn", 
            "receiveCount": "receive_count", 
            "rn": "rn", 
            "status": "status", 
            "transmitCount": "transmit_count", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.completion_count = None
        self.receive_count = None
        self.status = None
        self.transmit_count = None
        self.child_action = None

        ManagedObject.__init__(self, "AdaptorEthMultiQueueProfile", parent_mo_or_dn, **kwargs)

