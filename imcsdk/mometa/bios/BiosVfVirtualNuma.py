"""This module contains the general information for BiosVfVirtualNuma ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfVirtualNumaConsts:
    VP_VIRTUAL_NUMA_DISABLED = "Disabled"
    VP_VIRTUAL_NUMA_ENABLED = "Enabled"
    _VP_VIRTUAL_NUMA_DISABLED = "disabled"
    _VP_VIRTUAL_NUMA_ENABLED = "enabled"
    VP_VIRTUAL_NUMA_PLATFORM_DEFAULT = "platform-default"


class BiosVfVirtualNuma(ManagedObject):
    """This is BiosVfVirtualNuma class."""

    consts = BiosVfVirtualNumaConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfVirtualNuma", "biosVfVirtualNuma", "Virtual-Numa", VersionMeta.Version421b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_virtual_numa": MoPropertyMeta("vp_virtual_numa", "vpVirtualNuma", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpVirtualNuma": "vp_virtual_numa", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_virtual_numa = None

        ManagedObject.__init__(self, "BiosVfVirtualNuma", parent_mo_or_dn, **kwargs)

