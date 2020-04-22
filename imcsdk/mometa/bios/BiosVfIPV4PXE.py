"""This module contains the general information for BiosVfIPV4PXE ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfIPV4PXEConsts:
    VP_IPV4_PXE_DISABLED = "Disabled"
    VP_IPV4_PXE_ENABLED = "Enabled"
    _VP_IPV4_PXE_DISABLED = "disabled"
    _VP_IPV4_PXE_ENABLED = "enabled"
    VP_IPV4_PXE_PLATFORM_DEFAULT = "platform-default"


class BiosVfIPV4PXE(ManagedObject):
    """This is BiosVfIPV4PXE class."""

    consts = BiosVfIPV4PXEConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfIPV4PXE", "biosVfIPV4PXE", "IPv4-Pxe", VersionMeta.Version411c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfIPV4PXE", "biosVfIPV4PXE", "IPv4-Pxe", VersionMeta.Version411c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_ip_v4_pxe": MoPropertyMeta("vp_ip_v4_pxe", "vpIPV4PXE", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_ip_v4_pxe": MoPropertyMeta("vp_ip_v4_pxe", "vpIPV4PXE", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version411c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIPV4PXE": "vp_ip_v4_pxe", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIPV4PXE": "vp_ip_v4_pxe", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_ip_v4_pxe = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfIPV4PXE", parent_mo_or_dn, **kwargs)

