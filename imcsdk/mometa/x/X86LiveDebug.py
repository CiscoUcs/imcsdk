"""This module contains the general information for X86LiveDebug ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class X86LiveDebugConsts:
    pass


class X86LiveDebug(ManagedObject):
    """This is X86LiveDebug class."""

    consts = X86LiveDebugConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("X86LiveDebug", "x86LiveDebug", "live-debug", VersionMeta.Version311d, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['computeRackUnit'], [], ["Get"]),
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "live_debug_state": MoPropertyMeta("live_debug_state", "liveDebugState", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "live_debug_timeout": MoPropertyMeta("live_debug_timeout", "liveDebugTimeout", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "liveDebugState": "live_debug_state", 
            "liveDebugTimeout": "live_debug_timeout", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.live_debug_state = None
        self.live_debug_timeout = None
        self.status = None

        ManagedObject.__init__(self, "X86LiveDebug", parent_mo_or_dn, **kwargs)

