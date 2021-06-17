"""This module contains the general information for BiosVfCbsDfCmnMemIntlv ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsDfCmnMemIntlvConsts:
    VP_CBS_DF_CMN_MEM_INTLV_AUTO = "Auto"
    VP_CBS_DF_CMN_MEM_INTLV_CHANNEL = "Channel"
    VP_CBS_DF_CMN_MEM_INTLV_DIE = "Die"
    VP_CBS_DF_CMN_MEM_INTLV_NONE = "None"
    VP_CBS_DF_CMN_MEM_INTLV_SOCKET = "Socket"
    VP_CBS_DF_CMN_MEM_INTLV_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsDfCmnMemIntlv(ManagedObject):
    """This is BiosVfCbsDfCmnMemIntlv class."""

    consts = BiosVfCbsDfCmnMemIntlvConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsDfCmnMemIntlv", "biosVfCbsDfCmnMemIntlv", "mem-interleave", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_df_cmn_mem_intlv": MoPropertyMeta("vp_cbs_df_cmn_mem_intlv", "vpCbsDfCmnMemIntlv", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Channel", "Die", "None", "Socket", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsDfCmnMemIntlv": "vp_cbs_df_cmn_mem_intlv", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_df_cmn_mem_intlv = None

        ManagedObject.__init__(self, "BiosVfCbsDfCmnMemIntlv", parent_mo_or_dn, **kwargs)

