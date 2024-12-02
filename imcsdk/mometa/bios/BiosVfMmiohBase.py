"""This module contains the general information for BiosVfMmiohBase ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfMmiohBaseConsts:
    VP_MMIOH_BASE_16_T = "16T"
    VP_MMIOH_BASE_1_T = "1T"
    VP_MMIOH_BASE_24_T = "24T"
    VP_MMIOH_BASE_2_T = "2T"
    VP_MMIOH_BASE_32_T = "32T"
    VP_MMIOH_BASE_40_T = "40T"
    VP_MMIOH_BASE_4_T = "4T"
    VP_MMIOH_BASE_512_G = "512G"
    VP_MMIOH_BASE_56_T = "56T"
    VP_MMIOH_BASE_PLATFORM_DEFAULT = "platform-default"


class BiosVfMmiohBase(ManagedObject):
    """This is BiosVfMmiohBase class."""

    consts = BiosVfMmiohBaseConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfMmiohBase", "biosVfMmiohBase", "MMIO-High-Base", VersionMeta.Version433_240024, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version433_240024, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_mmioh_base": MoPropertyMeta("vp_mmioh_base", "vpMmiohBase", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["16T", "1T", "24T", "2T", "32T", "40T", "4T", "512G", "56T", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpMmiohBase": "vp_mmioh_base", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_mmioh_base = None

        ManagedObject.__init__(self, "BiosVfMmiohBase", parent_mo_or_dn, **kwargs)

