"""This module contains the general information for StorageOperation ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageOperationConsts:
    pass


class StorageOperation(ManagedObject):
    """This is StorageOperation class."""

    consts = StorageOperationConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StorageOperation", "storageOperation", "storage-operation", VersionMeta.Version201a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageLocalDisk', 'storageVirtualDrive'], [], ["Get"]),
        "modular": MoMeta("StorageOperation", "storageOperation", "storage-operation", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageLocalDisk', 'storageVirtualDrive'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_lrop": MoPropertyMeta("current_lrop", "currentLrop", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "elapsed_seconds": MoPropertyMeta("elapsed_seconds", "elapsedSeconds", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "estimated_seconds_remaining": MoPropertyMeta("estimated_seconds_remaining", "estimatedSecondsRemaining", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "lrop_in_progress": MoPropertyMeta("lrop_in_progress", "lropInProgress", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "progress_percent": MoPropertyMeta("progress_percent", "progressPercent", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_lrop": MoPropertyMeta("current_lrop", "currentLrop", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "elapsed_seconds": MoPropertyMeta("elapsed_seconds", "elapsedSeconds", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "estimated_seconds_remaining": MoPropertyMeta("estimated_seconds_remaining", "estimatedSecondsRemaining", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "lrop_in_progress": MoPropertyMeta("lrop_in_progress", "lropInProgress", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "progress_percent": MoPropertyMeta("progress_percent", "progressPercent", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "currentLrop": "current_lrop", 
            "dn": "dn", 
            "elapsedSeconds": "elapsed_seconds", 
            "estimatedSecondsRemaining": "estimated_seconds_remaining", 
            "lropInProgress": "lrop_in_progress", 
            "progressPercent": "progress_percent", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "currentLrop": "current_lrop", 
            "dn": "dn", 
            "elapsedSeconds": "elapsed_seconds", 
            "estimatedSecondsRemaining": "estimated_seconds_remaining", 
            "lropInProgress": "lrop_in_progress", 
            "progressPercent": "progress_percent", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.current_lrop = None
        self.elapsed_seconds = None
        self.estimated_seconds_remaining = None
        self.lrop_in_progress = None
        self.progress_percent = None
        self.status = None

        ManagedObject.__init__(self, "StorageOperation", parent_mo_or_dn, **kwargs)

