"""This module contains the general information for BiosVfCbsCmnCpuSevAsidSpaceLimit ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnCpuSevAsidSpaceLimitConsts:
    VP_CBS_CMN_CPU_SEV_ASID_SPACE_LIMIT_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnCpuSevAsidSpaceLimit(ManagedObject):
    """This is BiosVfCbsCmnCpuSevAsidSpaceLimit class."""

    consts = BiosVfCbsCmnCpuSevAsidSpaceLimitConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnCpuSevAsidSpaceLimit", "biosVfCbsCmnCpuSevAsidSpaceLimit", "Cpu-Sev-Asid-Space-Limit", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_cpu_sev_asid_space_limit": MoPropertyMeta("vp_cbs_cmn_cpu_sev_asid_space_limit", "vpCbsCmnCpuSevAsidSpaceLimit", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["platform-default"], ["1-1007"]),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnCpuSevAsidSpaceLimit": "vp_cbs_cmn_cpu_sev_asid_space_limit", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_cpu_sev_asid_space_limit = None

        ManagedObject.__init__(self, "BiosVfCbsCmnCpuSevAsidSpaceLimit", parent_mo_or_dn, **kwargs)

