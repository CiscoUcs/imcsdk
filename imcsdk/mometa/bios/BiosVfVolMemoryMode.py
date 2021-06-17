"""This module contains the general information for BiosVfVolMemoryMode ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfVolMemoryModeConsts:
    VP_VOL_MEMORY_MODE_1_LM = "1LM"
    VP_VOL_MEMORY_MODE_2_LM = "2LM"
    VP_VOL_MEMORY_MODE_PLATFORM_DEFAULT = "platform-default"


class BiosVfVolMemoryMode(ManagedObject):
    """This is BiosVfVolMemoryMode class."""

    consts = BiosVfVolMemoryModeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfVolMemoryMode", "biosVfVolMemoryMode", "Vol-Memory-Mode", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_vol_memory_mode": MoPropertyMeta("vp_vol_memory_mode", "vpVolMemoryMode", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1LM", "2LM", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpVolMemoryMode": "vp_vol_memory_mode", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_vol_memory_mode = None

        ManagedObject.__init__(self, "BiosVfVolMemoryMode", parent_mo_or_dn, **kwargs)

