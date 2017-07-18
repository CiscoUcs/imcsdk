"""This module contains the general information for AdaptorEthGenProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorEthGenProfileConsts:
    ARFS_DISABLED = "Disabled"
    ARFS_ENABLED = "Enabled"
    _ARFS_DISABLED = "disabled"
    _ARFS_ENABLED = "enabled"
    RATE_LIMIT_OFF = "OFF"
    UPLINK_FAILOVER_DISABLED = "Disabled"
    UPLINK_FAILOVER_ENABLED = "Enabled"
    _UPLINK_FAILOVER_DISABLED = "disabled"
    _UPLINK_FAILOVER_ENABLED = "enabled"
    VLAN_NONE = "NONE"
    VLAN_MODE_ACCESS = "ACCESS"
    VLAN_MODE_TRUNK = "TRUNK"
    VMQ_DISABLED = "Disabled"
    VMQ_ENABLED = "Enabled"
    _VMQ_DISABLED = "disabled"
    _VMQ_ENABLED = "enabled"
    ORDER_ANY = "ANY"


class AdaptorEthGenProfile(ManagedObject):
    """This is AdaptorEthGenProfile class."""

    consts = AdaptorEthGenProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorEthGenProfile", "adaptorEthGenProfile", "general", VersionMeta.Version151f, "InputOutput", 0xffff, [], ["admin", "read-only", "user"], [u'adaptorHostEthIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorEthGenProfile", "adaptorEthGenProfile", "general", VersionMeta.Version2013e, "InputOutput", 0x1fff, [], ["admin", "read-only", "user"], [u'adaptorHostEthIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "arfs": MoPropertyMeta("arfs", "arfs", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-17"]), 
            "rate_limit": MoPropertyMeta("rate_limit", "rateLimit", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""(([1-9]\d?\d?\d?|10000) Mbps)""", ["OFF"], ["1-40000"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "trusted_class_of_service": MoPropertyMeta("trusted_class_of_service", "trustedClassOfService", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "uplink_failback_timeout": MoPropertyMeta("uplink_failback_timeout", "uplinkFailbackTimeout", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""(0{0,2}[0-9]|0?[1-9][0-9]|[1-5][0-9][0-9]|600)""", [], []), 
            "uplink_failover": MoPropertyMeta("uplink_failover", "uplinkFailover", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "vlan": MoPropertyMeta("vlan", "vlan", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["NONE"], ["1-4094"]), 
            "vlan_mode": MoPropertyMeta("vlan_mode", "vlanMode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["ACCESS", "TRUNK"], []), 
            "vmq": MoPropertyMeta("vmq", "vmq", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "nvgre": MoPropertyMeta("nvgre", "nvgre", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "pci_link": MoPropertyMeta("pci_link", "pciLink", "uint", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, [], ["0-1"]), 
            "vxlan": MoPropertyMeta("vxlan", "vxlan", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        },

        "modular": {
            "arfs": MoPropertyMeta("arfs", "arfs", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[0-9]|1[0-7]""", ["ANY"], []), 
            "rate_limit": MoPropertyMeta("rate_limit", "rateLimit", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""(([1-9]\d?\d?\d?|10000) Mbps)""", ["OFF"], ["1-40000"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "trusted_class_of_service": MoPropertyMeta("trusted_class_of_service", "trustedClassOfService", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "uplink_failback_timeout": MoPropertyMeta("uplink_failback_timeout", "uplinkFailbackTimeout", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""(0{0,2}[0-9]|0?[1-9][0-9]|[1-5][0-9][0-9]|600)""", [], []), 
            "uplink_failover": MoPropertyMeta("uplink_failover", "uplinkFailover", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "vlan": MoPropertyMeta("vlan", "vlan", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["NONE"], ["1-4094"]), 
            "vlan_mode": MoPropertyMeta("vlan_mode", "vlanMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["ACCESS", "TRUNK"], []), 
            "vmq": MoPropertyMeta("vmq", "vmq", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        },

    }

    prop_map = {

        "classic": {
            "arfs": "arfs", 
            "childAction": "child_action", 
            "dn": "dn", 
            "order": "order", 
            "rateLimit": "rate_limit", 
            "rn": "rn", 
            "status": "status", 
            "trustedClassOfService": "trusted_class_of_service", 
            "uplinkFailbackTimeout": "uplink_failback_timeout", 
            "uplinkFailover": "uplink_failover", 
            "vlan": "vlan", 
            "vlanMode": "vlan_mode", 
            "vmq": "vmq", 
            "nvgre": "nvgre", 
            "pciLink": "pci_link", 
            "vxlan": "vxlan", 
        },

        "modular": {
            "arfs": "arfs", 
            "childAction": "child_action", 
            "dn": "dn", 
            "order": "order", 
            "rateLimit": "rate_limit", 
            "rn": "rn", 
            "status": "status", 
            "trustedClassOfService": "trusted_class_of_service", 
            "uplinkFailbackTimeout": "uplink_failback_timeout", 
            "uplinkFailover": "uplink_failover", 
            "vlan": "vlan", 
            "vlanMode": "vlan_mode", 
            "vmq": "vmq", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.arfs = None
        self.child_action = None
        self.order = None
        self.rate_limit = None
        self.status = None
        self.trusted_class_of_service = None
        self.uplink_failback_timeout = None
        self.uplink_failover = None
        self.vlan = None
        self.vlan_mode = None
        self.vmq = None
        self.nvgre = None
        self.pci_link = None
        self.vxlan = None

        ManagedObject.__init__(self, "AdaptorEthGenProfile", parent_mo_or_dn, **kwargs)

