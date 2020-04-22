"""This module contains the general information for BiosVfDRAMClockThrottling ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfDRAMClockThrottlingConsts:
    VP_DRAMCLOCK_THROTTLING_AUTO = "Auto"
    VP_DRAMCLOCK_THROTTLING_BALANCED = "Balanced"
    VP_DRAMCLOCK_THROTTLING_ENERGY_EFFICIENT = "Energy Efficient"
    VP_DRAMCLOCK_THROTTLING_PERFORMANCE = "Performance"
    VP_DRAMCLOCK_THROTTLING_PLATFORM_DEFAULT = "platform-default"


class BiosVfDRAMClockThrottling(ManagedObject):
    """This is BiosVfDRAMClockThrottling class."""

    consts = BiosVfDRAMClockThrottlingConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfDRAMClockThrottling", "biosVfDRAMClockThrottling", "DRAM-Clock-Throttling", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfDRAMClockThrottling", "biosVfDRAMClockThrottling", "DRAM-Clock-Throttling", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_dram_clock_throttling": MoPropertyMeta("vp_dram_clock_throttling", "vpDRAMClockThrottling", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Balanced", "Energy Efficient", "Performance", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_dram_clock_throttling": MoPropertyMeta("vp_dram_clock_throttling", "vpDRAMClockThrottling", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Balanced", "Energy Efficient", "Performance", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpDRAMClockThrottling": "vp_dram_clock_throttling", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpDRAMClockThrottling": "vp_dram_clock_throttling", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_dram_clock_throttling = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfDRAMClockThrottling", parent_mo_or_dn, **kwargs)

