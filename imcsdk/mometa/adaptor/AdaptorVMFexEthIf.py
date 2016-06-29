"""This module contains the general information for AdaptorVMFexEthIf ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorVMFexEthIfConsts:
    IF_TYPE_VIRTUAL = "virtual"
    UPLINK_FAILOVER_DISABLED = "Disabled"
    UPLINK_FAILOVER_ENABLED = "Enabled"
    _UPLINK_FAILOVER_DISABLED = "disabled"
    _UPLINK_FAILOVER_ENABLED = "enabled"
    UPLINK_PORT_0 = "0"
    UPLINK_PORT_1 = "1"


class AdaptorVMFexEthIf(ManagedObject):
    """This is AdaptorVMFexEthIf class."""

    consts = AdaptorVMFexEthIfConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("AdaptorVMFexEthIf", "adaptorVMFexEthIf", "vmfex-eth-[name]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'adaptorUnit'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "class_of_service": MoPropertyMeta("class_of_service", "classOfService", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[0-6]""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["virtual"], []), 
        "mtu": MoPropertyMeta("mtu", "mtu", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1500-9000"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, r"""[a-zA-Z0-9\-\._:]{1,32}""", [], []), 
        "pxe_boot": MoPropertyMeta("pxe_boot", "pxeBoot", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        "uplink_failback_timeout": MoPropertyMeta("uplink_failback_timeout", "uplinkFailbackTimeout", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "uplink_failover": MoPropertyMeta("uplink_failover", "uplinkFailover", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "uplink_port": MoPropertyMeta("uplink_port", "uplinkPort", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["0", "1"], []), 
        "vlan": MoPropertyMeta("vlan", "vlan", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "vlan_mode": MoPropertyMeta("vlan_mode", "vlanMode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "classOfService": "class_of_service", 
        "dn": "dn", 
        "ifType": "if_type", 
        "mtu": "mtu", 
        "name": "name", 
        "pxeBoot": "pxe_boot", 
        "rn": "rn", 
        "status": "status", 
        "uplinkFailbackTimeout": "uplink_failback_timeout", 
        "uplinkFailover": "uplink_failover", 
        "uplinkPort": "uplink_port", 
        "vlan": "vlan", 
        "vlanMode": "vlan_mode", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.class_of_service = None
        self.if_type = None
        self.mtu = None
        self.pxe_boot = None
        self.status = None
        self.uplink_failback_timeout = None
        self.uplink_failover = None
        self.uplink_port = None
        self.vlan = None
        self.vlan_mode = None

        ManagedObject.__init__(self, "AdaptorVMFexEthIf", parent_mo_or_dn, **kwargs)

