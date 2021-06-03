"""This module contains the general information for BiosVfCbsDbgCpuSnpMemSizeCover ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsDbgCpuSnpMemSizeCoverConsts:
    VP_CBS_DBG_CPU_SNP_MEM_SIZE_COVER_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsDbgCpuSnpMemSizeCover(ManagedObject):
    """This is BiosVfCbsDbgCpuSnpMemSizeCover class."""

    consts = BiosVfCbsDbgCpuSnpMemSizeCoverConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsDbgCpuSnpMemSizeCover", "biosVfCbsDbgCpuSnpMemSizeCover", "Cpu-Snp-Mem-Size-Cover", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_dbg_cpu_snp_mem_size_cover": MoPropertyMeta("vp_cbs_dbg_cpu_snp_mem_size_cover", "vpCbsDbgCpuSnpMemSizeCover", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["platform-default"], ["0-1048576"]),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsDbgCpuSnpMemSizeCover": "vp_cbs_dbg_cpu_snp_mem_size_cover", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_dbg_cpu_snp_mem_size_cover = None

        ManagedObject.__init__(self, "BiosVfCbsDbgCpuSnpMemSizeCover", parent_mo_or_dn, **kwargs)

