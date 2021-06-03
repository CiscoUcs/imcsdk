"""This module contains the general information for BiosVfEdpcEn ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfEdpcEnConsts:
    VP_EDPC_EN_DISABLED = "Disabled"
    VP_EDPC_EN_ON_FATAL_ERROR = "On Fatal Error"
    VP_EDPC_EN_ON_FATAL_AND_NON_FATAL_ERRORS = "On Fatal and Non-Fatal Errors"
    VP_EDPC_EN_PLATFORM_DEFAULT = "platform-default"


class BiosVfEdpcEn(ManagedObject):
    """This is BiosVfEdpcEn class."""

    consts = BiosVfEdpcEnConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfEdpcEn", "biosVfEdpcEn", "Edpc-En", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_edpc_en": MoPropertyMeta("vp_edpc_en", "vpEdpcEn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "On Fatal Error", "On Fatal and Non-Fatal Errors", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEdpcEn": "vp_edpc_en", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_edpc_en = None

        ManagedObject.__init__(self, "BiosVfEdpcEn", parent_mo_or_dn, **kwargs)

