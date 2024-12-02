"""This module contains the general information for BiosVfCbsCmnApbdisDfPstateRs ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnApbdisDfPstateRsConsts:
    VP_CBS_CMN_APBDIS_DF_PSTATE_RS_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnApbdisDfPstateRs(ManagedObject):
    """This is BiosVfCbsCmnApbdisDfPstateRs class."""

    consts = BiosVfCbsCmnApbdisDfPstateRsConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnApbdisDfPstateRs", "biosVfCbsCmnApbdisDfPstateRs", "fixed-soc-pstate-F19h", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_apbdis_df_pstate_rs": MoPropertyMeta("vp_cbs_cmn_apbdis_df_pstate_rs", "vpCbsCmnApbdisDfPstateRs", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["platform-default"], ["0-2"]),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnApbdisDfPstateRs": "vp_cbs_cmn_apbdis_df_pstate_rs", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_apbdis_df_pstate_rs = None

        ManagedObject.__init__(self, "BiosVfCbsCmnApbdisDfPstateRs", parent_mo_or_dn, **kwargs)

