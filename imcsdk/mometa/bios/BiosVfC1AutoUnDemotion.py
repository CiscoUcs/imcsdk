"""This module contains the general information for BiosVfC1AutoUnDemotion ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfC1AutoUnDemotionConsts:
    VP_C1_AUTO_UN_DEMOTION_AUTO = "Auto"
    VP_C1_AUTO_UN_DEMOTION_DISABLED = "Disabled"
    VP_C1_AUTO_UN_DEMOTION_ENABLED = "Enabled"
    _VP_C1_AUTO_UN_DEMOTION_DISABLED = "disabled"
    _VP_C1_AUTO_UN_DEMOTION_ENABLED = "enabled"
    VP_C1_AUTO_UN_DEMOTION_PLATFORM_DEFAULT = "platform-default"


class BiosVfC1AutoUnDemotion(ManagedObject):
    """This is BiosVfC1AutoUnDemotion class."""

    consts = BiosVfC1AutoUnDemotionConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfC1AutoUnDemotion", "biosVfC1AutoUnDemotion", "C1-Auto-UnDemotion", VersionMeta.Version421b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_c1_auto_un_demotion": MoPropertyMeta("vp_c1_auto_un_demotion", "vpC1AutoUnDemotion", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpC1AutoUnDemotion": "vp_c1_auto_un_demotion", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_c1_auto_un_demotion = None

        ManagedObject.__init__(self, "BiosVfC1AutoUnDemotion", parent_mo_or_dn, **kwargs)

