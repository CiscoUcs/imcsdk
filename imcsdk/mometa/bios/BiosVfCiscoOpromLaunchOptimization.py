"""This module contains the general information for BiosVfCiscoOpromLaunchOptimization ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCiscoOpromLaunchOptimizationConsts:
    VP_CISCO_OPROM_LAUNCH_OPTIMIZATION_DISABLED = "Disabled"
    VP_CISCO_OPROM_LAUNCH_OPTIMIZATION_ENABLED = "Enabled"
    _VP_CISCO_OPROM_LAUNCH_OPTIMIZATION_DISABLED = "disabled"
    _VP_CISCO_OPROM_LAUNCH_OPTIMIZATION_ENABLED = "enabled"
    VP_CISCO_OPROM_LAUNCH_OPTIMIZATION_PLATFORM_DEFAULT = "platform-default"


class BiosVfCiscoOpromLaunchOptimization(ManagedObject):
    """This is BiosVfCiscoOpromLaunchOptimization class."""

    consts = BiosVfCiscoOpromLaunchOptimizationConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCiscoOpromLaunchOptimization", "biosVfCiscoOpromLaunchOptimization", "Cisco-Opromlaunch-Optimize", VersionMeta.Version402c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfCiscoOpromLaunchOptimization", "biosVfCiscoOpromLaunchOptimization", "Cisco-Opromlaunch-Optimize", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cisco_oprom_launch_optimization": MoPropertyMeta("vp_cisco_oprom_launch_optimization", "vpCiscoOpromLaunchOptimization", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version402c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cisco_oprom_launch_optimization": MoPropertyMeta("vp_cisco_oprom_launch_optimization", "vpCiscoOpromLaunchOptimization", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCiscoOpromLaunchOptimization": "vp_cisco_oprom_launch_optimization", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCiscoOpromLaunchOptimization": "vp_cisco_oprom_launch_optimization", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_cisco_oprom_launch_optimization = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfCiscoOpromLaunchOptimization", parent_mo_or_dn, **kwargs)

