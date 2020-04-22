"""This module contains the general information for StorageControllerNextPatrolReadSchedule ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageControllerNextPatrolReadScheduleConsts:
    pass


class StorageControllerNextPatrolReadSchedule(ManagedObject):
    """This is StorageControllerNextPatrolReadSchedule class."""

    consts = StorageControllerNextPatrolReadScheduleConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StorageControllerNextPatrolReadSchedule", "storageControllerNextPatrolReadSchedule", "patrol-read", VersionMeta.Version401a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageController'], [], [None]),
        "modular": MoMeta("StorageControllerNextPatrolReadSchedule", "storageControllerNextPatrolReadSchedule", "patrol-read", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageController'], [], [None])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "exec_frequency": MoPropertyMeta("exec_frequency", "execFrequency", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "next_exec_time": MoPropertyMeta("next_exec_time", "nextExecTime", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pr_schedule_mode": MoPropertyMeta("pr_schedule_mode", "prScheduleMode", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pr_state": MoPropertyMeta("pr_state", "prState", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "exec_frequency": MoPropertyMeta("exec_frequency", "execFrequency", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "next_exec_time": MoPropertyMeta("next_exec_time", "nextExecTime", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pr_schedule_mode": MoPropertyMeta("pr_schedule_mode", "prScheduleMode", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pr_state": MoPropertyMeta("pr_state", "prState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "execFrequency": "exec_frequency", 
            "id": "id", 
            "nextExecTime": "next_exec_time", 
            "prScheduleMode": "pr_schedule_mode", 
            "prState": "pr_state", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "execFrequency": "exec_frequency", 
            "id": "id", 
            "nextExecTime": "next_exec_time", 
            "prScheduleMode": "pr_schedule_mode", 
            "prState": "pr_state", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.exec_frequency = None
        self.id = None
        self.next_exec_time = None
        self.pr_schedule_mode = None
        self.pr_state = None
        self.status = None

        ManagedObject.__init__(self, "StorageControllerNextPatrolReadSchedule", parent_mo_or_dn, **kwargs)

