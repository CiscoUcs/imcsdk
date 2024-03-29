"""This module contains the general information for BiosVfLLCAlloc ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfLLCAllocConsts:
    VP_LLCALLOC_AUTO = "Auto"
    VP_LLCALLOC_DISABLED = "Disabled"
    VP_LLCALLOC_ENABLED = "Enabled"
    _VP_LLCALLOC_DISABLED = "disabled"
    _VP_LLCALLOC_ENABLED = "enabled"
    VP_LLCALLOC_PLATFORM_DEFAULT = "platform-default"


class BiosVfLLCAlloc(ManagedObject):
    """This is BiosVfLLCAlloc class."""

    consts = BiosVfLLCAllocConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfLLCAlloc", "biosVfLLCAlloc", "LLC-Alloc", VersionMeta.Version421b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_llc_alloc": MoPropertyMeta("vp_llc_alloc", "vpLLCAlloc", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpLLCAlloc": "vp_llc_alloc", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_llc_alloc = None

        ManagedObject.__init__(self, "BiosVfLLCAlloc", parent_mo_or_dn, **kwargs)

