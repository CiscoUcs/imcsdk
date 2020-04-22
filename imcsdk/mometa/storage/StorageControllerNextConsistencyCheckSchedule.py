"""This module contains the general information for StorageControllerNextConsistencyCheckSchedule ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageControllerNextConsistencyCheckScheduleConsts:
    pass


class StorageControllerNextConsistencyCheckSchedule(ManagedObject):
    """This is StorageControllerNextConsistencyCheckSchedule class."""

    consts = StorageControllerNextConsistencyCheckScheduleConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StorageControllerNextConsistencyCheckSchedule", "storageControllerNextConsistencyCheckSchedule", "consistency-check", VersionMeta.Version401a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageController'], [], [None]),
        "modular": MoMeta("StorageControllerNextConsistencyCheckSchedule", "storageControllerNextConsistencyCheckSchedule", "consistency-check", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageController'], [], [None])
    }


    prop_meta = {

        "classic": {
            "cc_schedule_mode": MoPropertyMeta("cc_schedule_mode", "ccScheduleMode", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "cc_state": MoPropertyMeta("cc_state", "ccState", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "exec_frequency": MoPropertyMeta("exec_frequency", "execFrequency", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "next_exec_time": MoPropertyMeta("next_exec_time", "nextExecTime", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "cc_schedule_mode": MoPropertyMeta("cc_schedule_mode", "ccScheduleMode", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "cc_state": MoPropertyMeta("cc_state", "ccState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "exec_frequency": MoPropertyMeta("exec_frequency", "execFrequency", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "next_exec_time": MoPropertyMeta("next_exec_time", "nextExecTime", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "ccScheduleMode": "cc_schedule_mode", 
            "ccState": "cc_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "execFrequency": "exec_frequency", 
            "id": "id", 
            "nextExecTime": "next_exec_time", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "ccScheduleMode": "cc_schedule_mode", 
            "ccState": "cc_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "execFrequency": "exec_frequency", 
            "id": "id", 
            "nextExecTime": "next_exec_time", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.cc_schedule_mode = None
        self.cc_state = None
        self.child_action = None
        self.exec_frequency = None
        self.id = None
        self.next_exec_time = None
        self.status = None

        ManagedObject.__init__(self, "StorageControllerNextConsistencyCheckSchedule", parent_mo_or_dn, **kwargs)

