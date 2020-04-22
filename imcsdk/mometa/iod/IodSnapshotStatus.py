"""This module contains the general information for IodSnapshotStatus ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class IodSnapshotStatusConsts:
    pass


class IodSnapshotStatus(ManagedObject):
    """This is IodSnapshotStatus class."""

    consts = IodSnapshotStatusConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("IodSnapshotStatus", "iodSnapshotStatus", "snapshotStatus", VersionMeta.Version151x, "OutputOnly", 0xf, [], ["read-only"], ['iodController'], [], ["Get"]),
        "modular": MoMeta("IodSnapshotStatus", "iodSnapshotStatus", "snapshotStatus", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["read-only"], ['iodController'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151x, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_status": MoPropertyMeta("current_status", "currentStatus", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "current_time": MoPropertyMeta("current_time", "currentTime", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "iod_image_version": MoPropertyMeta("iod_image_version", "iodImageVersion", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "remote_share_file": MoPropertyMeta("remote_share_file", "remoteShareFile", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "remote_share_ip": MoPropertyMeta("remote_share_ip", "remoteShareIp", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "remote_share_path": MoPropertyMeta("remote_share_path", "remoteSharePath", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "running_time": MoPropertyMeta("running_time", "runningTime", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "snapshot_cancel_op": MoPropertyMeta("snapshot_cancel_op", "snapshotCancelOp", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "snapshot_report": MoPropertyMeta("snapshot_report", "snapshotReport", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "start_time": MoPropertyMeta("start_time", "startTime", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_status": MoPropertyMeta("current_status", "currentStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "current_time": MoPropertyMeta("current_time", "currentTime", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "iod_image_version": MoPropertyMeta("iod_image_version", "iodImageVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "remote_share_file": MoPropertyMeta("remote_share_file", "remoteShareFile", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "remote_share_ip": MoPropertyMeta("remote_share_ip", "remoteShareIp", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "remote_share_path": MoPropertyMeta("remote_share_path", "remoteSharePath", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "running_time": MoPropertyMeta("running_time", "runningTime", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "snapshot_cancel_op": MoPropertyMeta("snapshot_cancel_op", "snapshotCancelOp", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "no", "yes"], []),
            "snapshot_report": MoPropertyMeta("snapshot_report", "snapshotReport", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "no", "yes"], []),
            "start_time": MoPropertyMeta("start_time", "startTime", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "currentStatus": "current_status", 
            "currentTime": "current_time", 
            "dn": "dn", 
            "iodImageVersion": "iod_image_version", 
            "remoteShareFile": "remote_share_file", 
            "remoteShareIp": "remote_share_ip", 
            "remoteSharePath": "remote_share_path", 
            "rn": "rn", 
            "runningTime": "running_time", 
            "snapshotCancelOp": "snapshot_cancel_op", 
            "snapshotReport": "snapshot_report", 
            "startTime": "start_time", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "currentStatus": "current_status", 
            "currentTime": "current_time", 
            "dn": "dn", 
            "iodImageVersion": "iod_image_version", 
            "remoteShareFile": "remote_share_file", 
            "remoteShareIp": "remote_share_ip", 
            "remoteSharePath": "remote_share_path", 
            "rn": "rn", 
            "runningTime": "running_time", 
            "snapshotCancelOp": "snapshot_cancel_op", 
            "snapshotReport": "snapshot_report", 
            "startTime": "start_time", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.current_status = None
        self.current_time = None
        self.iod_image_version = None
        self.remote_share_file = None
        self.remote_share_ip = None
        self.remote_share_path = None
        self.running_time = None
        self.snapshot_cancel_op = None
        self.snapshot_report = None
        self.start_time = None
        self.status = None

        ManagedObject.__init__(self, "IodSnapshotStatus", parent_mo_or_dn, **kwargs)

