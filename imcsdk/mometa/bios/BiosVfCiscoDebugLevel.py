"""This module contains the general information for BiosVfCiscoDebugLevel ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCiscoDebugLevelConsts:
    VP_CISCO_DEBUG_LEVEL_MAXIMUM = "Maximum"
    VP_CISCO_DEBUG_LEVEL_MINIMUM = "Minimum"
    VP_CISCO_DEBUG_LEVEL_NORMAL = "Normal"
    VP_CISCO_DEBUG_LEVEL_PLATFORM_DEFAULT = "platform-default"


class BiosVfCiscoDebugLevel(ManagedObject):
    """This is BiosVfCiscoDebugLevel class."""

    consts = BiosVfCiscoDebugLevelConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCiscoDebugLevel", "biosVfCiscoDebugLevel", "Cisco-Debug-Level", VersionMeta.Version402c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfCiscoDebugLevel", "biosVfCiscoDebugLevel", "Cisco-Debug-Level", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cisco_debug_level": MoPropertyMeta("vp_cisco_debug_level", "vpCiscoDebugLevel", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Maximum", "Minimum", "Normal", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version402c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cisco_debug_level": MoPropertyMeta("vp_cisco_debug_level", "vpCiscoDebugLevel", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Maximum", "Minimum", "Normal", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCiscoDebugLevel": "vp_cisco_debug_level", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCiscoDebugLevel": "vp_cisco_debug_level", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_cisco_debug_level = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfCiscoDebugLevel", parent_mo_or_dn, **kwargs)

