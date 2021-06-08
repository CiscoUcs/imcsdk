"""This module contains the general information for BiosVfEnableClockSpreadSpec ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfEnableClockSpreadSpecConsts:
    VP_ENABLE_CLOCK_SPREAD_SPEC_DISABLED = "Disabled"
    VP_ENABLE_CLOCK_SPREAD_SPEC_ENABLED = "Enabled"
    _VP_ENABLE_CLOCK_SPREAD_SPEC_DISABLED = "disabled"
    _VP_ENABLE_CLOCK_SPREAD_SPEC_ENABLED = "enabled"
    VP_ENABLE_CLOCK_SPREAD_SPEC_PLATFORM_DEFAULT = "platform-default"


class BiosVfEnableClockSpreadSpec(ManagedObject):
    """This is BiosVfEnableClockSpreadSpec class."""

    consts = BiosVfEnableClockSpreadSpecConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfEnableClockSpreadSpec", "biosVfEnableClockSpreadSpec", "External-SSC-Enable", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfEnableClockSpreadSpec", "biosVfEnableClockSpreadSpec", "External-SSC-Enable", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_enable_clock_spread_spec": MoPropertyMeta("vp_enable_clock_spread_spec", "vpEnableClockSpreadSpec", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_enable_clock_spread_spec": MoPropertyMeta("vp_enable_clock_spread_spec", "vpEnableClockSpreadSpec", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEnableClockSpreadSpec": "vp_enable_clock_spread_spec", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEnableClockSpreadSpec": "vp_enable_clock_spread_spec", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_enable_clock_spread_spec = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfEnableClockSpreadSpec", parent_mo_or_dn, **kwargs)

