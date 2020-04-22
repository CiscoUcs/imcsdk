"""This module contains the general information for ComputeRackUnitMbTempStats ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class ComputeRackUnitMbTempStatsConsts:
    AMBIENT_TEMP_ = ""
    FRONT_TEMP_ = ""
    IOH1_TEMP_ = ""
    IOH2_TEMP_ = ""
    REAR_TEMP_ = ""


class ComputeRackUnitMbTempStats(ManagedObject):
    """This is ComputeRackUnitMbTempStats class."""

    consts = ComputeRackUnitMbTempStatsConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("ComputeRackUnitMbTempStats", "computeRackUnitMbTempStats", "temp-stats", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['computeBoard'], [], ["Get"]),
    }


    prop_meta = {

        "classic": {
            "ambient_temp": MoPropertyMeta("ambient_temp", "ambientTemp", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [""], ["0-4294967295"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "front_temp": MoPropertyMeta("front_temp", "frontTemp", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [""], ["0-4294967295"]),
            "ioh1_temp": MoPropertyMeta("ioh1_temp", "ioh1Temp", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [""], ["0-4294967295"]),
            "ioh2_temp": MoPropertyMeta("ioh2_temp", "ioh2Temp", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [""], ["0-4294967295"]),
            "rear_temp": MoPropertyMeta("rear_temp", "rearTemp", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [""], ["0-4294967295"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "ambientTemp": "ambient_temp", 
            "childAction": "child_action", 
            "dn": "dn", 
            "frontTemp": "front_temp", 
            "ioh1Temp": "ioh1_temp", 
            "ioh2Temp": "ioh2_temp", 
            "rearTemp": "rear_temp", 
            "rn": "rn", 
            "status": "status", 
            "timeCollected": "time_collected", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.ambient_temp = None
        self.child_action = None
        self.front_temp = None
        self.ioh1_temp = None
        self.ioh2_temp = None
        self.rear_temp = None
        self.status = None
        self.time_collected = None

        ManagedObject.__init__(self, "ComputeRackUnitMbTempStats", parent_mo_or_dn, **kwargs)

