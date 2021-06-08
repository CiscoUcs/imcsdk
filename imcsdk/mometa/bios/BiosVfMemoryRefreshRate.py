"""This module contains the general information for BiosVfMemoryRefreshRate ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfMemoryRefreshRateConsts:
    VP_MEMORY_REFRESH_RATE_1X_REFRESH = "1x Refresh"
    VP_MEMORY_REFRESH_RATE_2X_REFRESH = "2x Refresh"
    VP_MEMORY_REFRESH_RATE_PLATFORM_DEFAULT = "platform-default"


class BiosVfMemoryRefreshRate(ManagedObject):
    """This is BiosVfMemoryRefreshRate class."""

    consts = BiosVfMemoryRefreshRateConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfMemoryRefreshRate", "biosVfMemoryRefreshRate", "Memory-Refresh-Rate", VersionMeta.Version413a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfMemoryRefreshRate", "biosVfMemoryRefreshRate", "Memory-Refresh-Rate", VersionMeta.Version413a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_memory_refresh_rate": MoPropertyMeta("vp_memory_refresh_rate", "vpMemoryRefreshRate", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1x Refresh", "2x Refresh", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_memory_refresh_rate": MoPropertyMeta("vp_memory_refresh_rate", "vpMemoryRefreshRate", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1x Refresh", "2x Refresh", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpMemoryRefreshRate": "vp_memory_refresh_rate", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpMemoryRefreshRate": "vp_memory_refresh_rate", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_memory_refresh_rate = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfMemoryRefreshRate", parent_mo_or_dn, **kwargs)

