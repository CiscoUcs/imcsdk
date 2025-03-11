"""This module contains the general information for BiosVfEnableTdx ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfEnableTdxConsts:
    VP_ENABLE_TDX_DISABLED = "Disabled"
    VP_ENABLE_TDX_ENABLED = "Enabled"
    _VP_ENABLE_TDX_DISABLED = "disabled"
    _VP_ENABLE_TDX_ENABLED = "enabled"
    VP_ENABLE_TDX_PLATFORM_DEFAULT = "platform-default"


class BiosVfEnableTdx(ManagedObject):
    """This is BiosVfEnableTdx class."""

    consts = BiosVfEnableTdxConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfEnableTdx", "biosVfEnableTdx", "Trust-Domain-Extension", VersionMeta.Version432_230285, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version432_230285, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version432_230285, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version432_230285, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version432_230285, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_enable_tdx": MoPropertyMeta("vp_enable_tdx", "vpEnableTdx", "string", VersionMeta.Version432_230285, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEnableTdx": "vp_enable_tdx", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_enable_tdx = None

        ManagedObject.__init__(self, "BiosVfEnableTdx", parent_mo_or_dn, **kwargs)

