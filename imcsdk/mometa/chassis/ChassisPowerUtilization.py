"""This module contains the general information for ChassisPowerUtilization ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class ChassisPowerUtilizationConsts:
    pass


class ChassisPowerUtilization(ManagedObject):
    """This is ChassisPowerUtilization class."""

    consts = ChassisPowerUtilizationConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("ChassisPowerUtilization", "chassisPowerUtilization", "utilization", VersionMeta.Version2013e, "OutputOnly", 0x7, [], ["admin", "read-only", "user"], ['equipmentChassis'], [], ["Get"])
    }


    prop_meta = {

        "modular": {
            "chassis_utilization": MoPropertyMeta("chassis_utilization", "chassisUtilization", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "server1_utilization": MoPropertyMeta("server1_utilization", "server1Utilization", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "server2_utilization": MoPropertyMeta("server2_utilization", "server2Utilization", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "modular": {
            "chassisUtilization": "chassis_utilization", 
            "dn": "dn", 
            "rn": "rn", 
            "server1Utilization": "server1_utilization", 
            "server2Utilization": "server2_utilization", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.chassis_utilization = None
        self.server1_utilization = None
        self.server2_utilization = None

        ManagedObject.__init__(self, "ChassisPowerUtilization", parent_mo_or_dn, **kwargs)

