"""This module contains the general information for AdaptorEthGenProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorEthGenProfileConsts:
    ARFS_DISABLED = "Disabled"
    ARFS_ENABLED = "Enabled"
    _ARFS_DISABLED = "disabled"
    _ARFS_ENABLED = "enabled"
    MULTI_QUEUE_DISABLED = "Disabled"
    MULTI_QUEUE_ENABLED = "Enabled"
    _MULTI_QUEUE_DISABLED = "disabled"
    _MULTI_QUEUE_ENABLED = "enabled"
    ORDER_ANY = "ANY"
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


class AdaptorEthGenProfile(ManagedObject):
    """This is AdaptorEthGenProfile class."""

    consts = AdaptorEthGenProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorEthGenProfile", "adaptorEthGenProfile", "general", VersionMeta.Version151f, "InputOutput", 0xfffff, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorEthGenProfile", "adaptorEthGenProfile", "general", VersionMeta.Version2013e, "InputOutput", 0x3ffff, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "arfs": MoPropertyMeta("arfs", "arfs", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "geneve_offload": MoPropertyMeta("geneve_offload", "geneveOffload", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "multi_queue": MoPropertyMeta("multi_queue", "multiQueue", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "no_of_sub_vni_cs": MoPropertyMeta("no_of_sub_vni_cs", "noOfSubVNICs", "uint", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-64", "1-64"]),
            "nvgre": MoPropertyMeta("nvgre", "nvgre", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[0-9]|1[0-7]""", ["ANY"], []),
            "rate_limit": MoPropertyMeta("rate_limit", "rateLimit", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""(([1-9]\d?\d?\d?|10000) Mbps)""", ["OFF"], ["1-100000"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "trusted_class_of_service": MoPropertyMeta("trusted_class_of_service", "trustedClassOfService", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "uplink_failback_timeout": MoPropertyMeta("uplink_failback_timeout", "uplinkFailbackTimeout", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""(0{0,2}[0-9]|0?[1-9][0-9]|[1-5][0-9][0-9]|600)""", [], []),
            "uplink_failover": MoPropertyMeta("uplink_failover", "uplinkFailover", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "vlan": MoPropertyMeta("vlan", "vlan", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["NONE"], ["1-4094"]),
            "vlan_mode": MoPropertyMeta("vlan_mode", "vlanMode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["ACCESS", "TRUNK"], []),
            "vmq": MoPropertyMeta("vmq", "vmq", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "vxlan": MoPropertyMeta("vxlan", "vxlan", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "pci_link": MoPropertyMeta("pci_link", "pciLink", "uint", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, [], ["0-1"]),
            "ptp": MoPropertyMeta("ptp", "ptp", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x80000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
        },

        "modular": {
            "arfs": MoPropertyMeta("arfs", "arfs", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "geneve_offload": MoPropertyMeta("geneve_offload", "geneveOffload", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "multi_queue": MoPropertyMeta("multi_queue", "multiQueue", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "no_of_sub_vni_cs": MoPropertyMeta("no_of_sub_vni_cs", "noOfSubVNICs", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-64", "1-64"]),
            "nvgre": MoPropertyMeta("nvgre", "nvgre", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[0-9]|1[0-7]""", ["ANY"], []),
            "rate_limit": MoPropertyMeta("rate_limit", "rateLimit", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""(([1-9]\d?\d?\d?|10000) Mbps)""", ["OFF"], ["1-100000"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "trusted_class_of_service": MoPropertyMeta("trusted_class_of_service", "trustedClassOfService", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "uplink_failback_timeout": MoPropertyMeta("uplink_failback_timeout", "uplinkFailbackTimeout", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""(0{0,2}[0-9]|0?[1-9][0-9]|[1-5][0-9][0-9]|600)""", [], []),
            "uplink_failover": MoPropertyMeta("uplink_failover", "uplinkFailover", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "vlan": MoPropertyMeta("vlan", "vlan", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["NONE"], ["1-4094"]),
            "vlan_mode": MoPropertyMeta("vlan_mode", "vlanMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["ACCESS", "TRUNK"], []),
            "vmq": MoPropertyMeta("vmq", "vmq", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "vxlan": MoPropertyMeta("vxlan", "vxlan", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "pci_link": MoPropertyMeta("pci_link", "pciLink", "uint", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-1"]),
        },

    }

    prop_map = {

        "classic": {
            "arfs": "arfs", 
            "dn": "dn", 
            "geneveOffload": "geneve_offload", 
            "multiQueue": "multi_queue", 
            "noOfSubVNICs": "no_of_sub_vni_cs", 
            "nvgre": "nvgre", 
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
            "vxlan": "vxlan", 
            "childAction": "child_action", 
            "pciLink": "pci_link", 
            "ptp": "ptp", 
        },

        "modular": {
            "arfs": "arfs", 
            "dn": "dn", 
            "geneveOffload": "geneve_offload", 
            "multiQueue": "multi_queue", 
            "noOfSubVNICs": "no_of_sub_vni_cs", 
            "nvgre": "nvgre", 
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
            "vxlan": "vxlan", 
            "childAction": "child_action", 
            "pciLink": "pci_link", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.arfs = None
        self.geneve_offload = None
        self.multi_queue = None
        self.no_of_sub_vni_cs = None
        self.nvgre = None
        self.order = None
        self.rate_limit = None
        self.status = None
        self.trusted_class_of_service = None
        self.uplink_failback_timeout = None
        self.uplink_failover = None
        self.vlan = None
        self.vlan_mode = None
        self.vmq = None
        self.vxlan = None
        self.child_action = None
        self.pci_link = None
        self.ptp = None

        ManagedObject.__init__(self, "AdaptorEthGenProfile", parent_mo_or_dn, **kwargs)

