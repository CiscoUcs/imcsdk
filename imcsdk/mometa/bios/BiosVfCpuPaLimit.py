"""This module contains the general information for BiosVfCpuPaLimit ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCpuPaLimitConsts:
    VP_CPU_PA_LIMIT_DISABLED = "Disabled"
    VP_CPU_PA_LIMIT_ENABLED = "Enabled"
    _VP_CPU_PA_LIMIT_DISABLED = "disabled"
    _VP_CPU_PA_LIMIT_ENABLED = "enabled"
    VP_CPU_PA_LIMIT_PLATFORM_DEFAULT = "platform-default"


class BiosVfCpuPaLimit(ManagedObject):
    """This is BiosVfCpuPaLimit class."""

    consts = BiosVfCpuPaLimitConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCpuPaLimit", "biosVfCpuPaLimit", "Cpu-Pa-Limit", VersionMeta.Version422a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version422a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cpu_pa_limit": MoPropertyMeta("vp_cpu_pa_limit", "vpCpuPaLimit", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCpuPaLimit": "vp_cpu_pa_limit", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cpu_pa_limit = None

        ManagedObject.__init__(self, "BiosVfCpuPaLimit", parent_mo_or_dn, **kwargs)

