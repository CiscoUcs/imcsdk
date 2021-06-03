"""This module contains the general information for BiosVfCbsCmnApbdis ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnApbdisConsts:
    VP_CBS_CMN_APBDIS_0 = "0"
    VP_CBS_CMN_APBDIS_1 = "1"
    VP_CBS_CMN_APBDIS_AUTO = "Auto"
    VP_CBS_CMN_APBDIS_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnApbdis(ManagedObject):
    """This is BiosVfCbsCmnApbdis class."""

    consts = BiosVfCbsCmnApbdisConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnApbdis", "biosVfCbsCmnApbdis", "apbdis", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_apbdis": MoPropertyMeta("vp_cbs_cmn_apbdis", "vpCbsCmnApbdis", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["0", "1", "Auto", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnApbdis": "vp_cbs_cmn_apbdis", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_apbdis = None

        ManagedObject.__init__(self, "BiosVfCbsCmnApbdis", parent_mo_or_dn, **kwargs)

