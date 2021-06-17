"""This module contains the general information for BiosVfUmaBasedClustering ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfUmaBasedClusteringConsts:
    VP_UMA_BASED_CLUSTERING_DISABLE_ALL2_ALL = "Disable (All2All)"
    VP_UMA_BASED_CLUSTERING_HEMISPHERE_2_CLUSTERS = "Hemisphere (2-clusters)"
    VP_UMA_BASED_CLUSTERING_PLATFORM_DEFAULT = "platform-default"


class BiosVfUmaBasedClustering(ManagedObject):
    """This is BiosVfUmaBasedClustering class."""

    consts = BiosVfUmaBasedClusteringConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfUmaBasedClustering", "biosVfUmaBasedClustering", "Uma-based-clustering", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_uma_based_clustering": MoPropertyMeta("vp_uma_based_clustering", "vpUmaBasedClustering", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disable (All2All)", "Hemisphere (2-clusters)", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpUmaBasedClustering": "vp_uma_based_clustering", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_uma_based_clustering = None

        ManagedObject.__init__(self, "BiosVfUmaBasedClustering", parent_mo_or_dn, **kwargs)

