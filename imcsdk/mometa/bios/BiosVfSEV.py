"""This module contains the general information for BiosVfSEV ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSEVConsts:
    VP_SEV_253_ASIDS = "253 ASIDs"
    VP_SEV_509_ASIDS = "509 ASIDs"
    VP_SEV_AUTO = "Auto"
    VP_SEV_PLATFORM_DEFAULT = "platform-default"


class BiosVfSEV(ManagedObject):
    """This is BiosVfSEV class."""

    consts = BiosVfSEVConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSEV", "biosVfSEV", "SEV", VersionMeta.Version413a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_sev": MoPropertyMeta("vp_sev", "vpSEV", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["253 ASIDs", "509 ASIDs", "Auto", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSEV": "vp_sev", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_sev = None

        ManagedObject.__init__(self, "BiosVfSEV", parent_mo_or_dn, **kwargs)

