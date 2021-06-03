"""This module contains the general information for BiosVfBurstAndPostponedRefresh ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfBurstAndPostponedRefreshConsts:
    VP_BURST_AND_POSTPONED_REFRESH_DISABLED = "Disabled"
    VP_BURST_AND_POSTPONED_REFRESH_ENABLED = "Enabled"
    _VP_BURST_AND_POSTPONED_REFRESH_DISABLED = "disabled"
    _VP_BURST_AND_POSTPONED_REFRESH_ENABLED = "enabled"
    VP_BURST_AND_POSTPONED_REFRESH_PLATFORM_DEFAULT = "platform-default"


class BiosVfBurstAndPostponedRefresh(ManagedObject):
    """This is BiosVfBurstAndPostponedRefresh class."""

    consts = BiosVfBurstAndPostponedRefreshConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfBurstAndPostponedRefresh", "biosVfBurstAndPostponedRefresh", "burst-and-postponed-refresh", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_burst_and_postponed_refresh": MoPropertyMeta("vp_burst_and_postponed_refresh", "vpBurstAndPostponedRefresh", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpBurstAndPostponedRefresh": "vp_burst_and_postponed_refresh", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_burst_and_postponed_refresh = None

        ManagedObject.__init__(self, "BiosVfBurstAndPostponedRefresh", parent_mo_or_dn, **kwargs)

