"""This module contains the general information for BiosVfPartialMirrorValue3 ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPartialMirrorValue3Consts:
    VP_PARTIAL_MIRROR_VALUE3_PLATFORM_DEFAULT = "platform-default"


class BiosVfPartialMirrorValue3(ManagedObject):
    """This is BiosVfPartialMirrorValue3 class."""

    consts = BiosVfPartialMirrorValue3Consts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPartialMirrorValue3", "biosVfPartialMirrorValue3", "Partial-Mirror-Value3", VersionMeta.Version411c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfPartialMirrorValue3", "biosVfPartialMirrorValue3", "Partial-Mirror-Value3", VersionMeta.Version411c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_partial_mirror_value3": MoPropertyMeta("vp_partial_mirror_value3", "vpPartialMirrorValue3", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["platform-default"], ["0-65535"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_partial_mirror_value3": MoPropertyMeta("vp_partial_mirror_value3", "vpPartialMirrorValue3", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["platform-default"], ["0-65535"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPartialMirrorValue3": "vp_partial_mirror_value3", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPartialMirrorValue3": "vp_partial_mirror_value3", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_partial_mirror_value3 = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfPartialMirrorValue3", parent_mo_or_dn, **kwargs)

