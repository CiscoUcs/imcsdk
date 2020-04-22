"""This module contains the general information for AdaptorFcPortFLogiProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorFcPortFLogiProfileConsts:
    RETRIES_INFINITE = "INFINITE"


class AdaptorFcPortFLogiProfile(ManagedObject):
    """This is AdaptorFcPortFLogiProfile class."""

    consts = AdaptorFcPortFLogiProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorFcPortFLogiProfile", "adaptorFcPortFLogiProfile", "fc-port-flogi", VersionMeta.Version151f, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['adaptorHostFcIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorFcPortFLogiProfile", "adaptorFcPortFLogiProfile", "fc-port-flogi", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['adaptorHostFcIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "retries": MoPropertyMeta("retries", "retries", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["INFINITE"], ["0-4294967295"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1000-255000"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "retries": MoPropertyMeta("retries", "retries", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["INFINITE"], ["0-4294967295"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1000-255000"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "retries": "retries", 
            "rn": "rn", 
            "status": "status", 
            "timeout": "timeout", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "retries": "retries", 
            "rn": "rn", 
            "status": "status", 
            "timeout": "timeout", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.retries = None
        self.status = None
        self.timeout = None
        self.child_action = None

        ManagedObject.__init__(self, "AdaptorFcPortFLogiProfile", parent_mo_or_dn, **kwargs)

