"""This module contains the general information for BiosVfIPV6HTTP ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfIPV6HTTPConsts:
    VP_IPV6_HTTP_DISABLED = "Disabled"
    VP_IPV6_HTTP_ENABLED = "Enabled"
    _VP_IPV6_HTTP_DISABLED = "disabled"
    _VP_IPV6_HTTP_ENABLED = "enabled"
    VP_IPV6_HTTP_PLATFORM_DEFAULT = "platform-default"


class BiosVfIPV6HTTP(ManagedObject):
    """This is BiosVfIPV6HTTP class."""

    consts = BiosVfIPV6HTTPConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfIPV6HTTP", "biosVfIPV6HTTP", "IPV6-HTTP-Support", VersionMeta.Version413a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfIPV6HTTP", "biosVfIPV6HTTP", "IPV6-HTTP-Support", VersionMeta.Version413a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_ip_v6_http": MoPropertyMeta("vp_ip_v6_http", "vpIPV6HTTP", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_ip_v6_http": MoPropertyMeta("vp_ip_v6_http", "vpIPV6HTTP", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIPV6HTTP": "vp_ip_v6_http", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIPV6HTTP": "vp_ip_v6_http", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_ip_v6_http = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfIPV6HTTP", parent_mo_or_dn, **kwargs)

