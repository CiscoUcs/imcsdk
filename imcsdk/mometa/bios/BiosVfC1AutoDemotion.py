"""This module contains the general information for BiosVfC1AutoDemotion ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfC1AutoDemotionConsts:
    VP_C1_AUTO_DEMOTION_AUTO = "Auto"
    VP_C1_AUTO_DEMOTION_DISABLED = "Disabled"
    VP_C1_AUTO_DEMOTION_ENABLED = "Enabled"
    _VP_C1_AUTO_DEMOTION_DISABLED = "disabled"
    _VP_C1_AUTO_DEMOTION_ENABLED = "enabled"
    VP_C1_AUTO_DEMOTION_PLATFORM_DEFAULT = "platform-default"


class BiosVfC1AutoDemotion(ManagedObject):
    """This is BiosVfC1AutoDemotion class."""

    consts = BiosVfC1AutoDemotionConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfC1AutoDemotion", "biosVfC1AutoDemotion", "C1-Auto-Demotion", VersionMeta.Version421b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_c1_auto_demotion": MoPropertyMeta("vp_c1_auto_demotion", "vpC1AutoDemotion", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpC1AutoDemotion": "vp_c1_auto_demotion", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_c1_auto_demotion = None

        ManagedObject.__init__(self, "BiosVfC1AutoDemotion", parent_mo_or_dn, **kwargs)

