"""This module contains the general information for BiosVfCbsCmncTDPCtl ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmncTDPCtlConsts:
    VP_CBS_CMNC_TDPCTL_AUTO = "Auto"
    VP_CBS_CMNC_TDPCTL_MANUAL = "Manual"
    VP_CBS_CMNC_TDPCTL_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmncTDPCtl(ManagedObject):
    """This is BiosVfCbsCmncTDPCtl class."""

    consts = BiosVfCbsCmncTDPCtlConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmncTDPCtl", "biosVfCbsCmncTDPCtl", "ctdp-control", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmnc_tdp_ctl": MoPropertyMeta("vp_cbs_cmnc_tdp_ctl", "vpCbsCmncTDPCtl", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Manual", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmncTDPCtl": "vp_cbs_cmnc_tdp_ctl", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmnc_tdp_ctl = None

        ManagedObject.__init__(self, "BiosVfCbsCmncTDPCtl", parent_mo_or_dn, **kwargs)

