"""This module contains the general information for BiosVfCbsCmnxGmiForceLinkWidthRs ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnxGmiForceLinkWidthRsConsts:
    VP_CBS_CMNX_GMI_FORCE_LINK_WIDTH_RS_0 = "0"
    VP_CBS_CMNX_GMI_FORCE_LINK_WIDTH_RS_1 = "1"
    VP_CBS_CMNX_GMI_FORCE_LINK_WIDTH_RS_2 = "2"
    VP_CBS_CMNX_GMI_FORCE_LINK_WIDTH_RS_AUTO = "Auto"
    VP_CBS_CMNX_GMI_FORCE_LINK_WIDTH_RS_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnxGmiForceLinkWidthRs(ManagedObject):
    """This is BiosVfCbsCmnxGmiForceLinkWidthRs class."""

    consts = BiosVfCbsCmnxGmiForceLinkWidthRsConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnxGmiForceLinkWidthRs", "biosVfCbsCmnxGmiForceLinkWidthRs", "xGMI_Force_Link_Width", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmnx_gmi_force_link_width_rs": MoPropertyMeta("vp_cbs_cmnx_gmi_force_link_width_rs", "vpCbsCmnxGmiForceLinkWidthRs", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["0", "1", "2", "Auto", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnxGmiForceLinkWidthRs": "vp_cbs_cmnx_gmi_force_link_width_rs", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmnx_gmi_force_link_width_rs = None

        ManagedObject.__init__(self, "BiosVfCbsCmnxGmiForceLinkWidthRs", parent_mo_or_dn, **kwargs)

