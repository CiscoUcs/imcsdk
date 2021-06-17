"""This module contains the general information for BiosVfCbsDfCmnMemIntlvSize ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsDfCmnMemIntlvSizeConsts:
    VP_CBS_DF_CMN_MEM_INTLV_SIZE_1_KB = "1 KB"
    VP_CBS_DF_CMN_MEM_INTLV_SIZE_2_KB = "2 KB"
    VP_CBS_DF_CMN_MEM_INTLV_SIZE_256_BYTES = "256 Bytes"
    VP_CBS_DF_CMN_MEM_INTLV_SIZE_4_KB = "4 KB"
    VP_CBS_DF_CMN_MEM_INTLV_SIZE_512_BYTES = "512 Bytes"
    VP_CBS_DF_CMN_MEM_INTLV_SIZE_AUTO = "Auto"
    VP_CBS_DF_CMN_MEM_INTLV_SIZE_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsDfCmnMemIntlvSize(ManagedObject):
    """This is BiosVfCbsDfCmnMemIntlvSize class."""

    consts = BiosVfCbsDfCmnMemIntlvSizeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsDfCmnMemIntlvSize", "biosVfCbsDfCmnMemIntlvSize", "mem-size-interleave", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_df_cmn_mem_intlv_size": MoPropertyMeta("vp_cbs_df_cmn_mem_intlv_size", "vpCbsDfCmnMemIntlvSize", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1 KB", "2 KB", "256 Bytes", "4 KB", "512 Bytes", "Auto", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsDfCmnMemIntlvSize": "vp_cbs_df_cmn_mem_intlv_size", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_df_cmn_mem_intlv_size = None

        ManagedObject.__init__(self, "BiosVfCbsDfCmnMemIntlvSize", parent_mo_or_dn, **kwargs)

