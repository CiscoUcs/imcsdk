"""This module contains the general information for ChassisPowerMonitor ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class ChassisPowerMonitorConsts:
    pass


class ChassisPowerMonitor(ManagedObject):
    """This is ChassisPowerMonitor class."""

    consts = ChassisPowerMonitorConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("ChassisPowerMonitor", "chassisPowerMonitor", "pwrmonitor", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['equipmentChassis'], [], ["Get"])
    }


    prop_meta = {

        "modular": {
            "average": MoPropertyMeta("average", "average", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current": MoPropertyMeta("current", "current", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "maximum": MoPropertyMeta("maximum", "maximum", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "minimum": MoPropertyMeta("minimum", "minimum", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "period": MoPropertyMeta("period", "period", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "modular": {
            "average": "average", 
            "childAction": "child_action", 
            "current": "current", 
            "dn": "dn", 
            "maximum": "maximum", 
            "minimum": "minimum", 
            "period": "period", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.average = None
        self.child_action = None
        self.current = None
        self.maximum = None
        self.minimum = None
        self.period = None
        self.status = None

        ManagedObject.__init__(self, "ChassisPowerMonitor", parent_mo_or_dn, **kwargs)

