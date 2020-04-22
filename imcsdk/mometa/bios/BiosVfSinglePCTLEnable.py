"""This module contains the general information for BiosVfSinglePCTLEnable ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSinglePCTLEnableConsts:
    VP_SINGLE_PCTLENABLE_NO = "No"
    VP_SINGLE_PCTLENABLE_YES = "Yes"
    VP_SINGLE_PCTLENABLE_PLATFORM_DEFAULT = "platform-default"


class BiosVfSinglePCTLEnable(ManagedObject):
    """This is BiosVfSinglePCTLEnable class."""

    consts = BiosVfSinglePCTLEnableConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSinglePCTLEnable", "biosVfSinglePCTLEnable", "Single-PCTL-Enable", VersionMeta.Version303a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_single_pctl_enable": MoPropertyMeta("vp_single_pctl_enable", "vpSinglePCTLEnable", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["No", "Yes", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSinglePCTLEnable": "vp_single_pctl_enable", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_single_pctl_enable = None

        ManagedObject.__init__(self, "BiosVfSinglePCTLEnable", parent_mo_or_dn, **kwargs)

