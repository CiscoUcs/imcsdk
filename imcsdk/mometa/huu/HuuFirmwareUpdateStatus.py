"""This module contains the general information for HuuFirmwareUpdateStatus ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class HuuFirmwareUpdateStatusConsts:
    pass


class HuuFirmwareUpdateStatus(ManagedObject):
    """This is HuuFirmwareUpdateStatus class."""

    consts = HuuFirmwareUpdateStatusConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("HuuFirmwareUpdateStatus", "huuFirmwareUpdateStatus", "updateStatus", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['huuFirmwareUpdater'], ['huuUpdateComponentStatus'], ["Get"]),
        "modular": MoMeta("HuuFirmwareUpdateStatus", "huuFirmwareUpdateStatus", "updateStatus", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['huuFirmwareUpdater'], ['huuUpdateComponentStatus'], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_time": MoPropertyMeta("current_time", "currentTime", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "huu_image_version": MoPropertyMeta("huu_image_version", "huuImageVersion", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "overall_status": MoPropertyMeta("overall_status", "overallStatus", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 4096, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "update_end_time": MoPropertyMeta("update_end_time", "updateEndTime", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "update_start_time": MoPropertyMeta("update_start_time", "updateStartTime", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_time": MoPropertyMeta("current_time", "currentTime", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "huu_image_version": MoPropertyMeta("huu_image_version", "huuImageVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "overall_status": MoPropertyMeta("overall_status", "overallStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 4096, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "update_end_time": MoPropertyMeta("update_end_time", "updateEndTime", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "update_start_time": MoPropertyMeta("update_start_time", "updateStartTime", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "currentTime": "current_time", 
            "dn": "dn", 
            "huuImageVersion": "huu_image_version", 
            "overallStatus": "overall_status", 
            "rn": "rn", 
            "status": "status", 
            "updateEndTime": "update_end_time", 
            "updateStartTime": "update_start_time", 
        },

        "modular": {
            "childAction": "child_action", 
            "currentTime": "current_time", 
            "dn": "dn", 
            "huuImageVersion": "huu_image_version", 
            "overallStatus": "overall_status", 
            "rn": "rn", 
            "status": "status", 
            "updateEndTime": "update_end_time", 
            "updateStartTime": "update_start_time", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.current_time = None
        self.huu_image_version = None
        self.overall_status = None
        self.status = None
        self.update_end_time = None
        self.update_start_time = None

        ManagedObject.__init__(self, "HuuFirmwareUpdateStatus", parent_mo_or_dn, **kwargs)

