"""This module contains the general information for BiosVfEnhancedIntelSpeedStepTech ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfEnhancedIntelSpeedStepTechConsts:
    VP_ENHANCED_INTEL_SPEED_STEP_TECH_DISABLED = "Disabled"
    VP_ENHANCED_INTEL_SPEED_STEP_TECH_ENABLED = "Enabled"
    _VP_ENHANCED_INTEL_SPEED_STEP_TECH_DISABLED = "disabled"
    _VP_ENHANCED_INTEL_SPEED_STEP_TECH_ENABLED = "enabled"
    VP_ENHANCED_INTEL_SPEED_STEP_TECH_PLATFORM_DEFAULT = "platform-default"


class BiosVfEnhancedIntelSpeedStepTech(ManagedObject):
    """This is BiosVfEnhancedIntelSpeedStepTech class."""

    consts = BiosVfEnhancedIntelSpeedStepTechConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfEnhancedIntelSpeedStepTech", "biosVfEnhancedIntelSpeedStepTech", "Enhanced-Intel-SpeedStep-Tech", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfEnhancedIntelSpeedStepTech", "biosVfEnhancedIntelSpeedStepTech", "Enhanced-Intel-SpeedStep-Tech", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_enhanced_intel_speed_step_tech": MoPropertyMeta("vp_enhanced_intel_speed_step_tech", "vpEnhancedIntelSpeedStepTech", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_enhanced_intel_speed_step_tech": MoPropertyMeta("vp_enhanced_intel_speed_step_tech", "vpEnhancedIntelSpeedStepTech", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEnhancedIntelSpeedStepTech": "vp_enhanced_intel_speed_step_tech", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEnhancedIntelSpeedStepTech": "vp_enhanced_intel_speed_step_tech", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_enhanced_intel_speed_step_tech = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfEnhancedIntelSpeedStepTech", parent_mo_or_dn, **kwargs)

