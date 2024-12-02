"""This module contains the general information for BiosVfDfxOsbEn ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfDfxOsbEnConsts:
    VP_DFX_OSB_EN_AUTO = "Auto"
    VP_DFX_OSB_EN_DISABLED = "Disabled"
    VP_DFX_OSB_EN_ENABLED = "Enabled"
    _VP_DFX_OSB_EN_DISABLED = "disabled"
    _VP_DFX_OSB_EN_ENABLED = "enabled"
    VP_DFX_OSB_EN_PLATFORM_DEFAULT = "platform-default"


class BiosVfDfxOsbEn(ManagedObject):
    """This is BiosVfDfxOsbEn class."""

    consts = BiosVfDfxOsbEnConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfDfxOsbEn", "biosVfDfxOsbEn", "DFX-OSB", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_dfx_osb_en": MoPropertyMeta("vp_dfx_osb_en", "vpDfxOsbEn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpDfxOsbEn": "vp_dfx_osb_en", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_dfx_osb_en = None

        ManagedObject.__init__(self, "BiosVfDfxOsbEn", parent_mo_or_dn, **kwargs)

