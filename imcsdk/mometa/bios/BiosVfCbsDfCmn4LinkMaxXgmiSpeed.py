"""This module contains the general information for BiosVfCbsDfCmn4LinkMaxXgmiSpeed ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsDfCmn4LinkMaxXgmiSpeedConsts:
    VP_CBS_DF_CMN4_LINK_MAX_XGMI_SPEED_20_GBPS = "20Gbps"
    VP_CBS_DF_CMN4_LINK_MAX_XGMI_SPEED_25_GBPS = "25Gbps"
    VP_CBS_DF_CMN4_LINK_MAX_XGMI_SPEED_32_GBPS = "32Gbps"
    VP_CBS_DF_CMN4_LINK_MAX_XGMI_SPEED_AUTO = "Auto"
    VP_CBS_DF_CMN4_LINK_MAX_XGMI_SPEED_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsDfCmn4LinkMaxXgmiSpeed(ManagedObject):
    """This is BiosVfCbsDfCmn4LinkMaxXgmiSpeed class."""

    consts = BiosVfCbsDfCmn4LinkMaxXgmiSpeedConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsDfCmn4LinkMaxXgmiSpeed", "biosVfCbsDfCmn4LinkMaxXgmiSpeed", "4-link-xGMI-max-speed", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_df_cmn4_link_max_xgmi_speed": MoPropertyMeta("vp_cbs_df_cmn4_link_max_xgmi_speed", "vpCbsDfCmn4LinkMaxXgmiSpeed", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["20Gbps", "25Gbps", "32Gbps", "Auto", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsDfCmn4LinkMaxXgmiSpeed": "vp_cbs_df_cmn4_link_max_xgmi_speed", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_df_cmn4_link_max_xgmi_speed = None

        ManagedObject.__init__(self, "BiosVfCbsDfCmn4LinkMaxXgmiSpeed", parent_mo_or_dn, **kwargs)

