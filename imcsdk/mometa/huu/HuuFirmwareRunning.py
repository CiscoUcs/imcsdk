"""This module contains the general information for HuuFirmwareRunning ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class HuuFirmwareRunningConsts:
    pass


class HuuFirmwareRunning(ManagedObject):
    """This is HuuFirmwareRunning class."""

    consts = HuuFirmwareRunningConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("HuuFirmwareRunning", "huuFirmwareRunning", "currentFirmware", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['huuController'], ['huuFirmwareComponent'], ["Get"]),
        "modular": MoMeta("HuuFirmwareRunning", "huuFirmwareRunning", "currentFirmware", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['huuController'], ['huuFirmwareComponent'], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_time": MoPropertyMeta("current_time", "currentTime", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "last_queried_time_stamp": MoPropertyMeta("last_queried_time_stamp", "lastQueriedTimeStamp", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_time": MoPropertyMeta("current_time", "currentTime", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "last_queried_time_stamp": MoPropertyMeta("last_queried_time_stamp", "lastQueriedTimeStamp", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "currentTime": "current_time", 
            "description": "description", 
            "dn": "dn", 
            "lastQueriedTimeStamp": "last_queried_time_stamp", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "currentTime": "current_time", 
            "description": "description", 
            "dn": "dn", 
            "lastQueriedTimeStamp": "last_queried_time_stamp", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.current_time = None
        self.description = None
        self.last_queried_time_stamp = None
        self.status = None

        ManagedObject.__init__(self, "HuuFirmwareRunning", parent_mo_or_dn, **kwargs)

