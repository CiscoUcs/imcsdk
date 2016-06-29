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

    mo_meta = MoMeta("AdaptorFcPortProfile", "adaptorFcPortProfile", "fc-port", VersionMeta.Version151f, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], [u'adaptorHostFcIf'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
        "io_throttle_count": MoPropertyMeta("io_throttle_count", "ioThrottleCount", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-1024"]), 
        "luns_per_target": MoPropertyMeta("luns_per_target", "lunsPerTarget", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-1024"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ioThrottleCount": "io_throttle_count", 
        "lunsPerTarget": "luns_per_target", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.io_throttle_count = None
        self.luns_per_target = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorFcPortProfile", parent_mo_or_dn, **kwargs)

