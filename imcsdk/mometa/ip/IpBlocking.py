"""This module contains the general information for IpBlocking ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class IpBlockingConsts:
    pass


class IpBlocking(ManagedObject):
    """This is IpBlocking class."""

    consts = IpBlockingConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("IpBlocking", "ipBlocking", "ip-block", VersionMeta.Version151f, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['mgmtIf'], [], ["Get", "Set"]),
        "modular": MoMeta("IpBlocking", "ipBlocking", "ip-block", VersionMeta.Version2013e, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['mgmtIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "enable": MoPropertyMeta("enable", "enable", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "fail_count": MoPropertyMeta("fail_count", "failCount", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["3-10"]),
            "fail_window": MoPropertyMeta("fail_window", "failWindow", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["60-120"]),
            "penalty_time": MoPropertyMeta("penalty_time", "penaltyTime", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["300-900"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "enable": MoPropertyMeta("enable", "enable", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "no", "yes"], []),
            "fail_count": MoPropertyMeta("fail_count", "failCount", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["3-10"]),
            "fail_window": MoPropertyMeta("fail_window", "failWindow", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["60-280"]),
            "penalty_time": MoPropertyMeta("penalty_time", "penaltyTime", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["300-900"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "enable": "enable", 
            "failCount": "fail_count", 
            "failWindow": "fail_window", 
            "penaltyTime": "penalty_time", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "description": "description", 
        },

        "modular": {
            "dn": "dn", 
            "enable": "enable", 
            "failCount": "fail_count", 
            "failWindow": "fail_window", 
            "penaltyTime": "penalty_time", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "description": "description", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.enable = None
        self.fail_count = None
        self.fail_window = None
        self.penalty_time = None
        self.status = None
        self.child_action = None
        self.description = None

        ManagedObject.__init__(self, "IpBlocking", parent_mo_or_dn, **kwargs)

