"""This module contains the general information for BiosVfSubNumaClustering ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSubNumaClusteringConsts:
    VP_SNC_AUTO = "Auto"
    VP_SNC_DISABLED = "Disabled"
    VP_SNC_ENABLED = "Enabled"
    _VP_SNC_DISABLED = "disabled"
    _VP_SNC_ENABLED = "enabled"
    VP_SNC_PLATFORM_DEFAULT = "platform-default"


class BiosVfSubNumaClustering(ManagedObject):
    """This is BiosVfSubNumaClustering class."""

    consts = BiosVfSubNumaClusteringConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSubNumaClustering", "biosVfSubNumaClustering", "sub-numa-cluster", VersionMeta.Version311d, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_snc": MoPropertyMeta("vp_snc", "vpSNC", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSNC": "vp_snc", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_snc = None

        ManagedObject.__init__(self, "BiosVfSubNumaClustering", parent_mo_or_dn, **kwargs)

