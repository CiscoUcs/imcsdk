"""This module contains the general information for PackagePowerLimit ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PackagePowerLimitConsts:
    CONFIGURED_PPL_DEFAULT = "Default"
    CONFIGURED_PPL_MAX = "Max"
    CONFIGURED_PPL_MIN = "Min"


class PackagePowerLimit(ManagedObject):
    """This is PackagePowerLimit class."""

    consts = PackagePowerLimitConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("PackagePowerLimit", "packagePowerLimit", "power-limit", VersionMeta.Version435_240037, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['computeBoard'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version435_240037, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "config_status": MoPropertyMeta("config_status", "configStatus", "string", VersionMeta.Version435_240037, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "configured_ppl": MoPropertyMeta("configured_ppl", "configuredPPL", "string", VersionMeta.Version435_240037, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Default", "Max", "Min"], []),
            "current_ppl": MoPropertyMeta("current_ppl", "currentPPL", "string", VersionMeta.Version435_240037, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "default_ppl": MoPropertyMeta("default_ppl", "defaultPPL", "string", VersionMeta.Version435_240037, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version435_240037, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "max_ppl": MoPropertyMeta("max_ppl", "maxPPL", "string", VersionMeta.Version435_240037, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "min_ppl": MoPropertyMeta("min_ppl", "minPPL", "string", VersionMeta.Version435_240037, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version435_240037, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version435_240037, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "configStatus": "config_status", 
            "configuredPPL": "configured_ppl", 
            "currentPPL": "current_ppl", 
            "defaultPPL": "default_ppl", 
            "dn": "dn", 
            "maxPPL": "max_ppl", 
            "minPPL": "min_ppl", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_status = None
        self.configured_ppl = None
        self.current_ppl = None
        self.default_ppl = None
        self.max_ppl = None
        self.min_ppl = None
        self.status = None

        ManagedObject.__init__(self, "PackagePowerLimit", parent_mo_or_dn, **kwargs)

