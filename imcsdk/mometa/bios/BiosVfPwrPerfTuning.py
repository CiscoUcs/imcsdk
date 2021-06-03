"""This module contains the general information for BiosVfPwrPerfTuning ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPwrPerfTuningConsts:
    VP_PWR_PERF_TUNING_BIOS = "bios"
    VP_PWR_PERF_TUNING_OS = "os"
    VP_PWR_PERF_TUNING_PECI = "peci"
    VP_PWR_PERF_TUNING_PLATFORM_DEFAULT = "platform-default"


class BiosVfPwrPerfTuning(ManagedObject):
    """This is BiosVfPwrPerfTuning class."""

    consts = BiosVfPwrPerfTuningConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPwrPerfTuning", "biosVfPwrPerfTuning", "Pwr-Perf-Tuning", VersionMeta.Version204c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfPwrPerfTuning", "biosVfPwrPerfTuning", "Pwr-Perf-Tuning", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pwr_perf_tuning": MoPropertyMeta("vp_pwr_perf_tuning", "vpPwrPerfTuning", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["bios", "os", "peci", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pwr_perf_tuning": MoPropertyMeta("vp_pwr_perf_tuning", "vpPwrPerfTuning", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["bios", "os", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPwrPerfTuning": "vp_pwr_perf_tuning", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPwrPerfTuning": "vp_pwr_perf_tuning", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_pwr_perf_tuning = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfPwrPerfTuning", parent_mo_or_dn, **kwargs)

