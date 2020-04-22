"""This module contains the general information for BiosVfEngPerfTuning ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfEngPerfTuningConsts:
    VP_ENG_PERF_TUNING_BIOS = "BIOS"
    VP_ENG_PERF_TUNING_OS = "OS"
    VP_ENG_PERF_TUNING_PLATFORM_DEFAULT = "platform-default"


class BiosVfEngPerfTuning(ManagedObject):
    """This is BiosVfEngPerfTuning class."""

    consts = BiosVfEngPerfTuningConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfEngPerfTuning", "biosVfEngPerfTuning", "Eng-Perf-Tuning", VersionMeta.Version303a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_eng_perf_tuning": MoPropertyMeta("vp_eng_perf_tuning", "vpEngPerfTuning", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["BIOS", "OS", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEngPerfTuning": "vp_eng_perf_tuning", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_eng_perf_tuning = None

        ManagedObject.__init__(self, "BiosVfEngPerfTuning", parent_mo_or_dn, **kwargs)

