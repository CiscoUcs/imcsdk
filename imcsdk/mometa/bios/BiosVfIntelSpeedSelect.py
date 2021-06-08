"""This module contains the general information for BiosVfIntelSpeedSelect ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfIntelSpeedSelectConsts:
    VP_INTEL_SPEED_SELECT_BASE = "Base"
    VP_INTEL_SPEED_SELECT_CONFIG_1 = "Config 1"
    VP_INTEL_SPEED_SELECT_CONFIG_2 = "Config 2"
    VP_INTEL_SPEED_SELECT_CONFIG_3 = "Config 3"
    VP_INTEL_SPEED_SELECT_CONFIG_4 = "Config 4"
    VP_INTEL_SPEED_SELECT_PLATFORM_DEFAULT = "platform-default"


class BiosVfIntelSpeedSelect(ManagedObject):
    """This is BiosVfIntelSpeedSelect class."""

    consts = BiosVfIntelSpeedSelectConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfIntelSpeedSelect", "biosVfIntelSpeedSelect", "Intel-Speed-Select", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfIntelSpeedSelect", "biosVfIntelSpeedSelect", "Intel-Speed-Select", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_intel_speed_select": MoPropertyMeta("vp_intel_speed_select", "vpIntelSpeedSelect", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Base", "Config 1", "Config 2", "Config 3", "Config 4", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_intel_speed_select": MoPropertyMeta("vp_intel_speed_select", "vpIntelSpeedSelect", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Base", "Config 1", "Config 2", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIntelSpeedSelect": "vp_intel_speed_select", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIntelSpeedSelect": "vp_intel_speed_select", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_intel_speed_select = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfIntelSpeedSelect", parent_mo_or_dn, **kwargs)

