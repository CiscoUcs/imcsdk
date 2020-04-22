"""This module contains the general information for OsiStatus ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class OsiStatusConsts:
    pass


class OsiStatus(ManagedObject):
    """This is OsiStatus class."""

    consts = OsiStatusConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("OsiStatus", "osiStatus", "osiStatus", VersionMeta.Version301c, "OutputOnly", 0xf, [], ["read-only"], ['osiController'], [], ["Get"]),
        "modular": MoMeta("OsiStatus", "osiStatus", "osiStatus", VersionMeta.Version301c, "OutputOnly", 0xf, [], ["read-only"], ['osiController'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_status": MoPropertyMeta("current_status", "currentStatus", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "current_time": MoPropertyMeta("current_time", "currentTime", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "osi_cancel_op": MoPropertyMeta("osi_cancel_op", "osiCancelOp", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "osi_image_version": MoPropertyMeta("osi_image_version", "osiImageVersion", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "osi_report": MoPropertyMeta("osi_report", "osiReport", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "remote_share_file": MoPropertyMeta("remote_share_file", "remoteShareFile", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "remote_share_ip": MoPropertyMeta("remote_share_ip", "remoteShareIp", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "remote_share_path": MoPropertyMeta("remote_share_path", "remoteSharePath", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "running_time": MoPropertyMeta("running_time", "runningTime", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "start_time": MoPropertyMeta("start_time", "startTime", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_status": MoPropertyMeta("current_status", "currentStatus", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "current_time": MoPropertyMeta("current_time", "currentTime", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "osi_cancel_op": MoPropertyMeta("osi_cancel_op", "osiCancelOp", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "no", "yes"], []),
            "osi_image_version": MoPropertyMeta("osi_image_version", "osiImageVersion", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "osi_report": MoPropertyMeta("osi_report", "osiReport", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "no", "yes"], []),
            "remote_share_file": MoPropertyMeta("remote_share_file", "remoteShareFile", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "remote_share_ip": MoPropertyMeta("remote_share_ip", "remoteShareIp", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "remote_share_path": MoPropertyMeta("remote_share_path", "remoteSharePath", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "running_time": MoPropertyMeta("running_time", "runningTime", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "start_time": MoPropertyMeta("start_time", "startTime", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "currentStatus": "current_status", 
            "currentTime": "current_time", 
            "dn": "dn", 
            "osiCancelOp": "osi_cancel_op", 
            "osiImageVersion": "osi_image_version", 
            "osiReport": "osi_report", 
            "remoteShareFile": "remote_share_file", 
            "remoteShareIp": "remote_share_ip", 
            "remoteSharePath": "remote_share_path", 
            "rn": "rn", 
            "runningTime": "running_time", 
            "startTime": "start_time", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "currentStatus": "current_status", 
            "currentTime": "current_time", 
            "dn": "dn", 
            "osiCancelOp": "osi_cancel_op", 
            "osiImageVersion": "osi_image_version", 
            "osiReport": "osi_report", 
            "remoteShareFile": "remote_share_file", 
            "remoteShareIp": "remote_share_ip", 
            "remoteSharePath": "remote_share_path", 
            "rn": "rn", 
            "runningTime": "running_time", 
            "startTime": "start_time", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.current_status = None
        self.current_time = None
        self.osi_cancel_op = None
        self.osi_image_version = None
        self.osi_report = None
        self.remote_share_file = None
        self.remote_share_ip = None
        self.remote_share_path = None
        self.running_time = None
        self.start_time = None
        self.status = None

        ManagedObject.__init__(self, "OsiStatus", parent_mo_or_dn, **kwargs)

