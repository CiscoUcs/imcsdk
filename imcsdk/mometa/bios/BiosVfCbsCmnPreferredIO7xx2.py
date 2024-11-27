"""This module contains the general information for BiosVfCbsCmnPreferredIO7xx2 ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnPreferredIO7xx2Consts:
    VP_CBS_CMN_PREFERRED_IO7XX2_AUTO = "Auto"
    VP_CBS_CMN_PREFERRED_IO7XX2_MANUAL = "Manual"
    VP_CBS_CMN_PREFERRED_IO7XX2_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnPreferredIO7xx2(ManagedObject):
    """This is BiosVfCbsCmnPreferredIO7xx2 class."""

    consts = BiosVfCbsCmnPreferredIO7xx2Consts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnPreferredIO7xx2", "biosVfCbsCmnPreferredIO7xx2", "preferred-io-7xx2", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_preferred_i_o7xx2": MoPropertyMeta("vp_cbs_cmn_preferred_i_o7xx2", "vpCbsCmnPreferredIO7xx2", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Manual", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnPreferredIO7xx2": "vp_cbs_cmn_preferred_i_o7xx2", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_preferred_i_o7xx2 = None

        ManagedObject.__init__(self, "BiosVfCbsCmnPreferredIO7xx2", parent_mo_or_dn, **kwargs)

