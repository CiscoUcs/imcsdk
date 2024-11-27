"""This module contains the general information for BiosVfAdaptiveRefreshMgmtLevel ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfAdaptiveRefreshMgmtLevelConsts:
    VP_ADAPTIVE_REFRESH_MGMT_LEVEL_DEFAULT = "Default"
    VP_ADAPTIVE_REFRESH_MGMT_LEVEL_LEVEL_A = "Level A"
    VP_ADAPTIVE_REFRESH_MGMT_LEVEL_LEVEL_B = "Level B"
    VP_ADAPTIVE_REFRESH_MGMT_LEVEL_LEVEL_C = "Level C"
    VP_ADAPTIVE_REFRESH_MGMT_LEVEL_PLATFORM_DEFAULT = "platform-default"


class BiosVfAdaptiveRefreshMgmtLevel(ManagedObject):
    """This is BiosVfAdaptiveRefreshMgmtLevel class."""

    consts = BiosVfAdaptiveRefreshMgmtLevelConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfAdaptiveRefreshMgmtLevel", "biosVfAdaptiveRefreshMgmtLevel", "Adaptive-Refresh-Mgmt-Level", VersionMeta.Version431a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version431a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_adaptive_refresh_mgmt_level": MoPropertyMeta("vp_adaptive_refresh_mgmt_level", "vpAdaptiveRefreshMgmtLevel", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Default", "Level A", "Level B", "Level C", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpAdaptiveRefreshMgmtLevel": "vp_adaptive_refresh_mgmt_level", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_adaptive_refresh_mgmt_level = None

        ManagedObject.__init__(self, "BiosVfAdaptiveRefreshMgmtLevel", parent_mo_or_dn, **kwargs)

