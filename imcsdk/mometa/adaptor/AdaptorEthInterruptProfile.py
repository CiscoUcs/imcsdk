"""This module contains the general information for AdaptorEthInterruptProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorEthInterruptProfileConsts:
    COALESCING_TYPE_IDLE = "IDLE"
    COALESCING_TYPE_MIN = "MIN"
    MODE_INTX = "INTx"
    MODE_MSI = "MSI"
    MODE_MSIX = "MSIx"


class AdaptorEthInterruptProfile(ManagedObject):
    """This is AdaptorEthInterruptProfile class."""

    consts = AdaptorEthInterruptProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorEthInterruptProfile", "adaptorEthInterruptProfile", "eth-int", VersionMeta.Version151f, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorEthInterruptProfile", "adaptorEthInterruptProfile", "eth-int", VersionMeta.Version2013e, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "coalescing_time": MoPropertyMeta("coalescing_time", "coalescingTime", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-65535"]),
            "coalescing_type": MoPropertyMeta("coalescing_type", "coalescingType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["IDLE", "MIN"], []),
            "count": MoPropertyMeta("count", "count", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-1024"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["INTx", "MSI", "MSIx"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "coalescing_time": MoPropertyMeta("coalescing_time", "coalescingTime", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-65535"]),
            "coalescing_type": MoPropertyMeta("coalescing_type", "coalescingType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["IDLE", "MIN"], []),
            "count": MoPropertyMeta("count", "count", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-514"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["INTx", "MSI", "MSIx"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "coalescingTime": "coalescing_time", 
            "coalescingType": "coalescing_type", 
            "count": "count", 
            "dn": "dn", 
            "mode": "mode", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "coalescingTime": "coalescing_time", 
            "coalescingType": "coalescing_type", 
            "count": "count", 
            "dn": "dn", 
            "mode": "mode", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.coalescing_time = None
        self.coalescing_type = None
        self.count = None
        self.mode = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "AdaptorEthInterruptProfile", parent_mo_or_dn, **kwargs)

