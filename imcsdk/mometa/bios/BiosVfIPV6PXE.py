"""This module contains the general information for BiosVfIPV6PXE ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfIPV6PXEConsts:
    VP_IPV6_PXE_DISABLED = "Disabled"
    VP_IPV6_PXE_ENABLED = "Enabled"
    _VP_IPV6_PXE_DISABLED = "disabled"
    _VP_IPV6_PXE_ENABLED = "enabled"
    VP_IPV6_PXE_PLATFORM_DEFAULT = "platform-default"


class BiosVfIPV6PXE(ManagedObject):
    """This is BiosVfIPV6PXE class."""

    consts = BiosVfIPV6PXEConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfIPV6PXE", "biosVfIPV6PXE", "IPv6-Pxe", VersionMeta.Version311d, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version311d, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_ip_v6_pxe": MoPropertyMeta("vp_ip_v6_pxe", "vpIPV6PXE", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIPV6PXE": "vp_ip_v6_pxe", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_ip_v6_pxe = None

        ManagedObject.__init__(self, "BiosVfIPV6PXE", parent_mo_or_dn, **kwargs)

