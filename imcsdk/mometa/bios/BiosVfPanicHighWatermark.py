"""This module contains the general information for BiosVfPanicHighWatermark ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPanicHighWatermarkConsts:
    VP_PANIC_HIGH_WATERMARK_HIGH = "High"
    VP_PANIC_HIGH_WATERMARK_LOW = "Low"
    VP_PANIC_HIGH_WATERMARK_PLATFORM_DEFAULT = "platform-default"


class BiosVfPanicHighWatermark(ManagedObject):
    """This is BiosVfPanicHighWatermark class."""

    consts = BiosVfPanicHighWatermarkConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPanicHighWatermark", "biosVfPanicHighWatermark", "Panic-and-High-Watermark", VersionMeta.Version413a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfPanicHighWatermark", "biosVfPanicHighWatermark", "Panic-and-High-Watermark", VersionMeta.Version413a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_panic_high_watermark": MoPropertyMeta("vp_panic_high_watermark", "vpPanicHighWatermark", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["High", "Low", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_panic_high_watermark": MoPropertyMeta("vp_panic_high_watermark", "vpPanicHighWatermark", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["High", "Low", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPanicHighWatermark": "vp_panic_high_watermark", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPanicHighWatermark": "vp_panic_high_watermark", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_panic_high_watermark = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfPanicHighWatermark", parent_mo_or_dn, **kwargs)

