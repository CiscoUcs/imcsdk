"""This module contains the general information for BiosVfCPUFrequencyFloor ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCPUFrequencyFloorConsts:
    VP_CPUFREQUENCY_FLOOR_DISABLED = "Disabled"
    VP_CPUFREQUENCY_FLOOR_ENABLED = "Enabled"
    _VP_CPUFREQUENCY_FLOOR_DISABLED = "disabled"
    _VP_CPUFREQUENCY_FLOOR_ENABLED = "enabled"
    VP_CPUFREQUENCY_FLOOR_PLATFORM_DEFAULT = "platform-default"


class BiosVfCPUFrequencyFloor(ManagedObject):
    """This is BiosVfCPUFrequencyFloor class."""

    consts = BiosVfCPUFrequencyFloorConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCPUFrequencyFloor", "biosVfCPUFrequencyFloor", "CPU-FreqFloor", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfCPUFrequencyFloor", "biosVfCPUFrequencyFloor", "CPU-FreqFloor", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cpu_frequency_floor": MoPropertyMeta("vp_cpu_frequency_floor", "vpCPUFrequencyFloor", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cpu_frequency_floor": MoPropertyMeta("vp_cpu_frequency_floor", "vpCPUFrequencyFloor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCPUFrequencyFloor": "vp_cpu_frequency_floor", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCPUFrequencyFloor": "vp_cpu_frequency_floor", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_cpu_frequency_floor = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfCPUFrequencyFloor", parent_mo_or_dn, **kwargs)

