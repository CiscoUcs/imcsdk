"""This module contains the general information for BiosVfPartialMirrorPercent ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPartialMirrorPercentConsts:
    VP_PARTIAL_MIRROR_PERCENT_PLATFORM_DEFAULT = "platform-default"


class BiosVfPartialMirrorPercent(ManagedObject):
    """This is BiosVfPartialMirrorPercent class."""

    consts = BiosVfPartialMirrorPercentConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPartialMirrorPercent", "biosVfPartialMirrorPercent", "Partial-Mirror-Percent", VersionMeta.Version411c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfPartialMirrorPercent", "biosVfPartialMirrorPercent", "Partial-Mirror-Percent", VersionMeta.Version411c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_partial_mirror_percent": MoPropertyMeta("vp_partial_mirror_percent", "vpPartialMirrorPercent", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""(\d+(\.\d{1,2})?)""", ["platform-default"], ["0.00-50.00"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_partial_mirror_percent": MoPropertyMeta("vp_partial_mirror_percent", "vpPartialMirrorPercent", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""(\d+(\.\d{1,2})?)""", ["platform-default"], ["0.00-50.00"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPartialMirrorPercent": "vp_partial_mirror_percent", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPartialMirrorPercent": "vp_partial_mirror_percent", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_partial_mirror_percent = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfPartialMirrorPercent", parent_mo_or_dn, **kwargs)

