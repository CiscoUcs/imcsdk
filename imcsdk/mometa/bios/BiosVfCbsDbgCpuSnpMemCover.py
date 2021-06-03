"""This module contains the general information for BiosVfCbsDbgCpuSnpMemCover ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsDbgCpuSnpMemCoverConsts:
    VP_CBS_DBG_CPU_SNP_MEM_COVER_AUTO = "Auto"
    VP_CBS_DBG_CPU_SNP_MEM_COVER_CUSTOM = "Custom"
    VP_CBS_DBG_CPU_SNP_MEM_COVER_DISABLED = "Disabled"
    VP_CBS_DBG_CPU_SNP_MEM_COVER_ENABLED = "Enabled"
    _VP_CBS_DBG_CPU_SNP_MEM_COVER_DISABLED = "disabled"
    _VP_CBS_DBG_CPU_SNP_MEM_COVER_ENABLED = "enabled"
    VP_CBS_DBG_CPU_SNP_MEM_COVER_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsDbgCpuSnpMemCover(ManagedObject):
    """This is BiosVfCbsDbgCpuSnpMemCover class."""

    consts = BiosVfCbsDbgCpuSnpMemCoverConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsDbgCpuSnpMemCover", "biosVfCbsDbgCpuSnpMemCover", "Cpu-Snp-Mem-Cover", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_dbg_cpu_snp_mem_cover": MoPropertyMeta("vp_cbs_dbg_cpu_snp_mem_cover", "vpCbsDbgCpuSnpMemCover", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Custom", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsDbgCpuSnpMemCover": "vp_cbs_dbg_cpu_snp_mem_cover", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_dbg_cpu_snp_mem_cover = None

        ManagedObject.__init__(self, "BiosVfCbsDbgCpuSnpMemCover", parent_mo_or_dn, **kwargs)

