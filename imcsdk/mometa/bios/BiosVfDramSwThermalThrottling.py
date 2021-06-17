"""This module contains the general information for BiosVfDramSwThermalThrottling ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfDramSwThermalThrottlingConsts:
    VP_DRAM_SW_THERMAL_THROTTLING_DISABLED = "Disabled"
    VP_DRAM_SW_THERMAL_THROTTLING_ENABLED = "Enabled"
    _VP_DRAM_SW_THERMAL_THROTTLING_DISABLED = "disabled"
    _VP_DRAM_SW_THERMAL_THROTTLING_ENABLED = "enabled"
    VP_DRAM_SW_THERMAL_THROTTLING_PLATFORM_DEFAULT = "platform-default"


class BiosVfDramSwThermalThrottling(ManagedObject):
    """This is BiosVfDramSwThermalThrottling class."""

    consts = BiosVfDramSwThermalThrottlingConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfDramSwThermalThrottling", "biosVfDramSwThermalThrottling", "DRAM-SW-Thermal-Throttling", VersionMeta.Version413a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_dram_sw_thermal_throttling": MoPropertyMeta("vp_dram_sw_thermal_throttling", "vpDramSwThermalThrottling", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpDramSwThermalThrottling": "vp_dram_sw_thermal_throttling", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_dram_sw_thermal_throttling = None

        ManagedObject.__init__(self, "BiosVfDramSwThermalThrottling", parent_mo_or_dn, **kwargs)

