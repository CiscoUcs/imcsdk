"""This module contains the general information for BiosVfMemorySizeLimit ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfMemorySizeLimitConsts:
    VP_MEMORY_SIZE_LIMIT_PLATFORM_DEFAULT = "platform-default"


class BiosVfMemorySizeLimit(ManagedObject):
    """This is BiosVfMemorySizeLimit class."""

    consts = BiosVfMemorySizeLimitConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfMemorySizeLimit", "biosVfMemorySizeLimit", "Memory-Size-Limit", VersionMeta.Version411c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfMemorySizeLimit", "biosVfMemorySizeLimit", "Memory-Size-Limit", VersionMeta.Version411c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_memory_size_limit": MoPropertyMeta("vp_memory_size_limit", "vpMemorySizeLimit", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["platform-default"], ["0-65535"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_memory_size_limit": MoPropertyMeta("vp_memory_size_limit", "vpMemorySizeLimit", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["platform-default"], ["0-65535"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpMemorySizeLimit": "vp_memory_size_limit", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpMemorySizeLimit": "vp_memory_size_limit", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_memory_size_limit = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfMemorySizeLimit", parent_mo_or_dn, **kwargs)

