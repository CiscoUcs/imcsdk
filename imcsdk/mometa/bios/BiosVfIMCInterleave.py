"""This module contains the general information for BiosVfIMCInterleave ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfIMCInterleaveConsts:
    VP_IMCINTERLEAVE_1_WAY_INTERLEAVE = "1-way Interleave"
    VP_IMCINTERLEAVE_2_WAY_INTERLEAVE = "2-way Interleave"
    VP_IMCINTERLEAVE_AUTO = "Auto"
    VP_IMCINTERLEAVE_PLATFORM_DEFAULT = "platform-default"


class BiosVfIMCInterleave(ManagedObject):
    """This is BiosVfIMCInterleave class."""

    consts = BiosVfIMCInterleaveConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfIMCInterleave", "biosVfIMCInterleave", "imc-interleave", VersionMeta.Version311d, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_imc_interleave": MoPropertyMeta("vp_imc_interleave", "vpIMCInterleave", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1-way Interleave", "2-way Interleave", "Auto", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIMCInterleave": "vp_imc_interleave", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_imc_interleave = None

        ManagedObject.__init__(self, "BiosVfIMCInterleave", parent_mo_or_dn, **kwargs)

