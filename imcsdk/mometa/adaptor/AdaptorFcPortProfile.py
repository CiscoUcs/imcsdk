"""This module contains the general information for AdaptorFcPortProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorFcPortProfileConsts:
    pass


class AdaptorFcPortProfile(ManagedObject):
    """This is AdaptorFcPortProfile class."""

    consts = AdaptorFcPortProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorFcPortProfile", "adaptorFcPortProfile", "fc-port", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['adaptorHostFcIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorFcPortProfile", "adaptorFcPortProfile", "fc-port", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['adaptorHostFcIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "io_throttle_count": MoPropertyMeta("io_throttle_count", "ioThrottleCount", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-1024"]),
            "lun_queue_depth": MoPropertyMeta("lun_queue_depth", "lunQueueDepth", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-254"]),
            "luns_per_target": MoPropertyMeta("luns_per_target", "lunsPerTarget", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-1024"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "io_throttle_count": MoPropertyMeta("io_throttle_count", "ioThrottleCount", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-1024"]),
            "lun_queue_depth": MoPropertyMeta("lun_queue_depth", "lunQueueDepth", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-254"]),
            "luns_per_target": MoPropertyMeta("luns_per_target", "lunsPerTarget", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-1024"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "ioThrottleCount": "io_throttle_count", 
            "lunQueueDepth": "lun_queue_depth", 
            "lunsPerTarget": "luns_per_target", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "ioThrottleCount": "io_throttle_count", 
            "lunQueueDepth": "lun_queue_depth", 
            "lunsPerTarget": "luns_per_target", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.io_throttle_count = None
        self.lun_queue_depth = None
        self.luns_per_target = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "AdaptorFcPortProfile", parent_mo_or_dn, **kwargs)

