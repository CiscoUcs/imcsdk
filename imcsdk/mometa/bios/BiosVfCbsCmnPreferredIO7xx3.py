"""This module contains the general information for BiosVfCbsCmnPreferredIO7xx3 ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnPreferredIO7xx3Consts:
    VP_CBS_CMN_PREFERRED_IO7XX3_AUTO = "Auto"
    VP_CBS_CMN_PREFERRED_IO7XX3_BUS = "Bus"
    VP_CBS_CMN_PREFERRED_IO7XX3_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnPreferredIO7xx3(ManagedObject):
    """This is BiosVfCbsCmnPreferredIO7xx3 class."""

    consts = BiosVfCbsCmnPreferredIO7xx3Consts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnPreferredIO7xx3", "biosVfCbsCmnPreferredIO7xx3", "preferred-io-7xx3", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_preferred_i_o7xx3": MoPropertyMeta("vp_cbs_cmn_preferred_i_o7xx3", "vpCbsCmnPreferredIO7xx3", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Bus", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnPreferredIO7xx3": "vp_cbs_cmn_preferred_i_o7xx3", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_preferred_i_o7xx3 = None

        ManagedObject.__init__(self, "BiosVfCbsCmnPreferredIO7xx3", parent_mo_or_dn, **kwargs)

