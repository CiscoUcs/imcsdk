"""This module contains the general information for BiosVfDramRefreshRate ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfDramRefreshRateConsts:
    VP_DRAM_REFRESH_RATE_1X = "1x"
    VP_DRAM_REFRESH_RATE_2X = "2x"
    VP_DRAM_REFRESH_RATE_3X = "3x"
    VP_DRAM_REFRESH_RATE_4X = "4x"
    VP_DRAM_REFRESH_RATE_AUTO = "Auto"
    VP_DRAM_REFRESH_RATE_PLATFORM_DEFAULT = "platform-default"


class BiosVfDramRefreshRate(ManagedObject):
    """This is BiosVfDramRefreshRate class."""

    consts = BiosVfDramRefreshRateConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfDramRefreshRate", "biosVfDramRefreshRate", "dram-refresh-rate", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfDramRefreshRate", "biosVfDramRefreshRate", "dram-refresh-rate", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_dram_refresh_rate": MoPropertyMeta("vp_dram_refresh_rate", "vpDramRefreshRate", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1x", "2x", "3x", "4x", "Auto", "platform-default"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_dram_refresh_rate": MoPropertyMeta("vp_dram_refresh_rate", "vpDramRefreshRate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1x", "2x", "3x", "4x", "Auto", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpDramRefreshRate": "vp_dram_refresh_rate", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpDramRefreshRate": "vp_dram_refresh_rate", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_dram_refresh_rate = None

        ManagedObject.__init__(self, "BiosVfDramRefreshRate", parent_mo_or_dn, **kwargs)

