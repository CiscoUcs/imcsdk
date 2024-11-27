"""This module contains the general information for BiosVfPrmrrSize ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPrmrrSizeConsts:
    VP_PRMRR_SIZE_128_G = "128G"
    VP_PRMRR_SIZE_128_M = "128M"
    VP_PRMRR_SIZE_16_G = "16G"
    VP_PRMRR_SIZE_1_G = "1G"
    VP_PRMRR_SIZE_256_G = "256G"
    VP_PRMRR_SIZE_256_M = "256M"
    VP_PRMRR_SIZE_2_G = "2G"
    VP_PRMRR_SIZE_32_G = "32G"
    VP_PRMRR_SIZE_4_G = "4G"
    VP_PRMRR_SIZE_512_G = "512G"
    VP_PRMRR_SIZE_512_M = "512M"
    VP_PRMRR_SIZE_64_G = "64G"
    VP_PRMRR_SIZE_8_G = "8G"
    VP_PRMRR_SIZE_AUTO = "Auto"
    VP_PRMRR_SIZE_INVALID_CONFIG_ = "Invalid Config."
    VP_PRMRR_SIZE_PLATFORM_DEFAULT = "platform-default"


class BiosVfPrmrrSize(ManagedObject):
    """This is BiosVfPrmrrSize class."""

    consts = BiosVfPrmrrSizeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPrmrrSize", "biosVfPrmrrSize", "PRMRR-Size", VersionMeta.Version432_230190, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version432_230190, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_prmrr_size": MoPropertyMeta("vp_prmrr_size", "vpPrmrrSize", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["128G", "128M", "16G", "1G", "256G", "256M", "2G", "32G", "4G", "512G", "512M", "64G", "8G", "Auto", "Invalid Config.", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPrmrrSize": "vp_prmrr_size", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_prmrr_size = None

        ManagedObject.__init__(self, "BiosVfPrmrrSize", parent_mo_or_dn, **kwargs)

