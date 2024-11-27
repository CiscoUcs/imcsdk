"""This module contains the general information for BiosVfCbsCmnCpuAvx512 ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnCpuAvx512Consts:
    VP_CBS_CMN_CPU_AVX512_AUTO = "Auto"
    VP_CBS_CMN_CPU_AVX512_DISABLED = "Disabled"
    VP_CBS_CMN_CPU_AVX512_ENABLED = "Enabled"
    _VP_CBS_CMN_CPU_AVX512_DISABLED = "disabled"
    _VP_CBS_CMN_CPU_AVX512_ENABLED = "enabled"
    VP_CBS_CMN_CPU_AVX512_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnCpuAvx512(ManagedObject):
    """This is BiosVfCbsCmnCpuAvx512 class."""

    consts = BiosVfCbsCmnCpuAvx512Consts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnCpuAvx512", "biosVfCbsCmnCpuAvx512", "AVX512", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_cpu_avx512": MoPropertyMeta("vp_cbs_cmn_cpu_avx512", "vpCbsCmnCpuAvx512", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnCpuAvx512": "vp_cbs_cmn_cpu_avx512", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_cpu_avx512 = None

        ManagedObject.__init__(self, "BiosVfCbsCmnCpuAvx512", parent_mo_or_dn, **kwargs)

