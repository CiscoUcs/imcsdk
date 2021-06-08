"""This module contains the general information for BiosVfSelectPprType ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSelectPprTypeConsts:
    VP_SELECT_PPR_TYPE_DISABLED = "Disabled"
    VP_SELECT_PPR_TYPE_HARD_PPR = "Hard PPR"
    VP_SELECT_PPR_TYPE_SOFT_PPR = "Soft PPR"
    _VP_SELECT_PPR_TYPE_DISABLED = "disabled"
    VP_SELECT_PPR_TYPE_PLATFORM_DEFAULT = "platform-default"


class BiosVfSelectPprType(ManagedObject):
    """This is BiosVfSelectPprType class."""

    consts = BiosVfSelectPprTypeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSelectPprType", "biosVfSelectPprType", "select-ppr-type", VersionMeta.Version411c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfSelectPprType", "biosVfSelectPprType", "select-ppr-type", VersionMeta.Version411c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_select_ppr_type": MoPropertyMeta("vp_select_ppr_type", "vpSelectPprType", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Hard PPR", "Soft PPR", "disabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_select_ppr_type": MoPropertyMeta("vp_select_ppr_type", "vpSelectPprType", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Hard PPR", "disabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSelectPprType": "vp_select_ppr_type", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSelectPprType": "vp_select_ppr_type", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_select_ppr_type = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfSelectPprType", parent_mo_or_dn, **kwargs)

