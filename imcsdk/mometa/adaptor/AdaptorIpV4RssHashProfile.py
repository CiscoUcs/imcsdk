"""This module contains the general information for AdaptorIpV4RssHashProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorIpV4RssHashProfileConsts:
    pass


class AdaptorIpV4RssHashProfile(ManagedObject):
    """This is AdaptorIpV4RssHashProfile class."""

    consts = AdaptorIpV4RssHashProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorIpV4RssHashProfile", "adaptorIpV4RssHashProfile", "ipv4-rss-hash", VersionMeta.Version151f, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorIpV4RssHashProfile", "adaptorIpV4RssHashProfile", "ipv4-rss-hash", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "ip_hash": MoPropertyMeta("ip_hash", "ipHash", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "tcp_hash": MoPropertyMeta("tcp_hash", "tcpHash", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "ip_hash": MoPropertyMeta("ip_hash", "ipHash", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "tcp_hash": MoPropertyMeta("tcp_hash", "tcpHash", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "ipHash": "ip_hash", 
            "rn": "rn", 
            "status": "status", 
            "tcpHash": "tcp_hash", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "ipHash": "ip_hash", 
            "rn": "rn", 
            "status": "status", 
            "tcpHash": "tcp_hash", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.ip_hash = None
        self.status = None
        self.tcp_hash = None
        self.child_action = None

        ManagedObject.__init__(self, "AdaptorIpV4RssHashProfile", parent_mo_or_dn, **kwargs)

