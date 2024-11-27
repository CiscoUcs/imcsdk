"""This module contains the general information for BiosVfCbsDfDbgXgmiLinkCfg ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsDfDbgXgmiLinkCfgConsts:
    VP_CBS_DF_DBG_XGMI_LINK_CFG_2_X_GMI_LINKS = "2 xGMI Links"
    VP_CBS_DF_DBG_XGMI_LINK_CFG_3_X_GMI_LINKS = "3 xGMI Links"
    VP_CBS_DF_DBG_XGMI_LINK_CFG_4_X_GMI_LINKS = "4 xGMI Links"
    VP_CBS_DF_DBG_XGMI_LINK_CFG_AUTO = "Auto"
    VP_CBS_DF_DBG_XGMI_LINK_CFG_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsDfDbgXgmiLinkCfg(ManagedObject):
    """This is BiosVfCbsDfDbgXgmiLinkCfg class."""

    consts = BiosVfCbsDfDbgXgmiLinkCfgConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsDfDbgXgmiLinkCfg", "biosVfCbsDfDbgXgmiLinkCfg", "xGMI-link-configuration", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_df_dbg_xgmi_link_cfg": MoPropertyMeta("vp_cbs_df_dbg_xgmi_link_cfg", "vpCbsDfDbgXgmiLinkCfg", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["2 xGMI Links", "3 xGMI Links", "4 xGMI Links", "Auto", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsDfDbgXgmiLinkCfg": "vp_cbs_df_dbg_xgmi_link_cfg", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_df_dbg_xgmi_link_cfg = None

        ManagedObject.__init__(self, "BiosVfCbsDfDbgXgmiLinkCfg", parent_mo_or_dn, **kwargs)

