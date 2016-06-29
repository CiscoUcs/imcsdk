"""This module contains the general information for PowerMonitor ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PowerMonitorConsts:
    DOMAIN_CPU = "CPU"
    DOMAIN_MEMORY = "Memory"
    DOMAIN_PLATFORM = "Platform"


class PowerMonitor(ManagedObject):
    """This is PowerMonitor class."""

    consts = PowerMonitorConsts()
    naming_props = set([u'domain'])

    mo_meta = MoMeta("PowerMonitor", "powerMonitor", "pwrmonitor-[domain]", VersionMeta.Version202c, "InputOutput", 0xf, [], ["admin", "read-only", "user"], [u'computeRackUnit'], [], ["Get"])

    prop_meta = {
        "average": MoPropertyMeta("average", "average", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "current": MoPropertyMeta("current", "current", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
        "domain": MoPropertyMeta("domain", "domain", "string", VersionMeta.Version202c, MoPropertyMeta.NAMING, None, None, None, None, ["CPU", "Memory", "Platform"], []), 
        "maximum": MoPropertyMeta("maximum", "maximum", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "minimum": MoPropertyMeta("minimum", "minimum", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "average": "average", 
        "childAction": "child_action", 
        "current": "current", 
        "dn": "dn", 
        "domain": "domain", 
        "maximum": "maximum", 
        "minimum": "minimum", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, domain, **kwargs):
        self._dirty_mask = 0
        self.domain = domain
        self.average = None
        self.child_action = None
        self.current = None
        self.maximum = None
        self.minimum = None
        self.status = None

        ManagedObject.__init__(self, "PowerMonitor", parent_mo_or_dn, **kwargs)

