"""This module contains the general information for BiosVfIohErrorEn ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfIohErrorEnConsts:
    VP_IOH_ERROR_ENABLE_NO = "No"
    VP_IOH_ERROR_ENABLE_YES = "Yes"
    VP_IOH_ERROR_ENABLE_PLATFORM_DEFAULT = "platform-default"


class BiosVfIohErrorEn(ManagedObject):
    """This is BiosVfIohErrorEn class."""

    consts = BiosVfIohErrorEnConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfIohErrorEn", "biosVfIohErrorEn", "Ioh-Error-En", VersionMeta.Version303a, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_ioh_error_enable": MoPropertyMeta("vp_ioh_error_enable", "vpIohErrorEnable", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["No", "Yes", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIohErrorEnable": "vp_ioh_error_enable", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_ioh_error_enable = None

        ManagedObject.__init__(self, "BiosVfIohErrorEn", parent_mo_or_dn, **kwargs)

