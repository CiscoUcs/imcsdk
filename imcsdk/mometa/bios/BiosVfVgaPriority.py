"""This module contains the general information for BiosVfVgaPriority ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfVgaPriorityConsts:
    VP_VGA_PRIORITY_OFFBOARD = "Offboard"
    VP_VGA_PRIORITY_ONBOARD = "Onboard"
    VP_VGA_PRIORITY_ONBOARD_VGA_DISABLED = "Onboard VGA Disabled"
    VP_VGA_PRIORITY_PLATFORM_DEFAULT = "platform-default"


class BiosVfVgaPriority(ManagedObject):
    """This is BiosVfVgaPriority class."""

    consts = BiosVfVgaPriorityConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfVgaPriority", "biosVfVgaPriority", "VgaPriority", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfVgaPriority", "biosVfVgaPriority", "VgaPriority", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_vga_priority": MoPropertyMeta("vp_vga_priority", "vpVgaPriority", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Offboard", "Onboard", "Onboard VGA Disabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_vga_priority": MoPropertyMeta("vp_vga_priority", "vpVgaPriority", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Offboard", "Onboard", "Onboard VGA Disabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpVgaPriority": "vp_vga_priority", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpVgaPriority": "vp_vga_priority", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_vga_priority = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfVgaPriority", parent_mo_or_dn, **kwargs)

