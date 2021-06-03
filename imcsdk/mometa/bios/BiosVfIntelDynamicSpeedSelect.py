"""This module contains the general information for BiosVfIntelDynamicSpeedSelect ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfIntelDynamicSpeedSelectConsts:
    VP_INTEL_DYNAMIC_SPEED_SELECT_DISABLED = "Disabled"
    VP_INTEL_DYNAMIC_SPEED_SELECT_ENABLED = "Enabled"
    _VP_INTEL_DYNAMIC_SPEED_SELECT_DISABLED = "disabled"
    _VP_INTEL_DYNAMIC_SPEED_SELECT_ENABLED = "enabled"
    VP_INTEL_DYNAMIC_SPEED_SELECT_PLATFORM_DEFAULT = "platform-default"


class BiosVfIntelDynamicSpeedSelect(ManagedObject):
    """This is BiosVfIntelDynamicSpeedSelect class."""

    consts = BiosVfIntelDynamicSpeedSelectConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfIntelDynamicSpeedSelect", "biosVfIntelDynamicSpeedSelect", "Intel-Dynamic-Speed-Select", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_intel_dynamic_speed_select": MoPropertyMeta("vp_intel_dynamic_speed_select", "vpIntelDynamicSpeedSelect", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIntelDynamicSpeedSelect": "vp_intel_dynamic_speed_select", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_intel_dynamic_speed_select = None

        ManagedObject.__init__(self, "BiosVfIntelDynamicSpeedSelect", parent_mo_or_dn, **kwargs)

