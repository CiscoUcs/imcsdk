"""This module contains the general information for AdaptorEthRdmaProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorEthRdmaProfileConsts:
    pass


class AdaptorEthRdmaProfile(ManagedObject):
    """This is AdaptorEthRdmaProfile class."""

    consts = AdaptorEthRdmaProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorEthRdmaProfile", "adaptorEthRdmaProfile", "rdmaprofile", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'adaptorHostEthIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorEthRdmaProfile", "adaptorEthRdmaProfile", "rdmaprofile", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'adaptorHostEthIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "memory_regions": MoPropertyMeta("memory_regions", "memoryRegions", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["0-524288"]), 
            "queue_pairs": MoPropertyMeta("queue_pairs", "queuePairs", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-8192"]), 
            "resource_groups": MoPropertyMeta("resource_groups", "resourceGroups", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-128"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "memory_regions": MoPropertyMeta("memory_regions", "memoryRegions", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["0-524288"]), 
            "queue_pairs": MoPropertyMeta("queue_pairs", "queuePairs", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-8192"]), 
            "resource_groups": MoPropertyMeta("resource_groups", "resourceGroups", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-128"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "memoryRegions": "memory_regions", 
            "queuePairs": "queue_pairs", 
            "resourceGroups": "resource_groups", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "memoryRegions": "memory_regions", 
            "queuePairs": "queue_pairs", 
            "resourceGroups": "resource_groups", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.memory_regions = None
        self.queue_pairs = None
        self.resource_groups = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorEthRdmaProfile", parent_mo_or_dn, **kwargs)

