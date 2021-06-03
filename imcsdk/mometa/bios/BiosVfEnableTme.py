"""This module contains the general information for BiosVfEnableTme ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfEnableTmeConsts:
    VP_ENABLE_TME_DISABLED = "Disabled"
    VP_ENABLE_TME_ENABLED = "Enabled"
    _VP_ENABLE_TME_DISABLED = "disabled"
    _VP_ENABLE_TME_ENABLED = "enabled"
    VP_ENABLE_TME_PLATFORM_DEFAULT = "platform-default"


class BiosVfEnableTme(ManagedObject):
    """This is BiosVfEnableTme class."""

    consts = BiosVfEnableTmeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfEnableTme", "biosVfEnableTme", "Enable-Time", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_enable_tme": MoPropertyMeta("vp_enable_tme", "vpEnableTme", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEnableTme": "vp_enable_tme", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_enable_tme = None

        ManagedObject.__init__(self, "BiosVfEnableTme", parent_mo_or_dn, **kwargs)

