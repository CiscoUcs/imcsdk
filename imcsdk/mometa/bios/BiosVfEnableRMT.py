"""This module contains the general information for BiosVfEnableRMT ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfEnableRMTConsts:
    VP_ENABLE_RMT_DISABLED = "Disabled"
    VP_ENABLE_RMT_ENABLED = "Enabled"
    _VP_ENABLE_RMT_DISABLED = "disabled"
    _VP_ENABLE_RMT_ENABLED = "enabled"
    VP_ENABLE_RMT_PLATFORM_DEFAULT = "platform-default"


class BiosVfEnableRMT(ManagedObject):
    """This is BiosVfEnableRMT class."""

    consts = BiosVfEnableRMTConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfEnableRMT", "biosVfEnableRMT", "Rank-Margin-Tool", VersionMeta.Version431a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version431a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_enable_rmt": MoPropertyMeta("vp_enable_rmt", "vpEnableRMT", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEnableRMT": "vp_enable_rmt", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_enable_rmt = None

        ManagedObject.__init__(self, "BiosVfEnableRMT", parent_mo_or_dn, **kwargs)

