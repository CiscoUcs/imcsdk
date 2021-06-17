"""This module contains the general information for LsbootHttp ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LsbootHttpConsts:
    IP_CONFIG_TYPE_ = ""
    IP_CONFIG_TYPE_DHCP = "DHCP"
    IP_CONFIG_TYPE_STATIC = "Static"
    IPTYPE_ = ""
    IPTYPE_IPV4 = "IPv4"
    IPTYPE_IPV6 = "IPv6"
    MAC_ADDRESS_ = ""
    NETMASK_OR_IPV6_PREFIX_ = ""
    STATE_DISABLED = "Disabled"
    STATE_ENABLED = "Enabled"
    SUBTYPE_HTTP = "HTTP"
    TYPE_HTTP = "HTTP"


class LsbootHttp(ManagedObject):
    """This is LsbootHttp class."""

    consts = LsbootHttpConsts()
    naming_props = set(['name'])

    mo_meta = {
        "classic": MoMeta("LsbootHttp", "lsbootHttp", "http-[name]", VersionMeta.Version413a, "InputOutput", 0x7ffff, [], ["admin", "read-only", "user"], ['lsbootDevPrecision'], [], [None]),
        "modular": MoMeta("LsbootHttp", "lsbootHttp", "http-[name]", VersionMeta.Version413a, "InputOutput", 0x7ffff, [], ["admin", "read-only", "user"], ['lsbootDevPrecision'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "dnsserver": MoPropertyMeta("dnsserver", "dnsserver", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [""], []),
            "gateway": MoPropertyMeta("gateway", "gateway", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [""], []),
            "ip_config_type": MoPropertyMeta("ip_config_type", "ipConfigType", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "DHCP", "Static"], []),
            "ipaddress": MoPropertyMeta("ipaddress", "ipaddress", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [""], []),
            "iptype": MoPropertyMeta("iptype", "iptype", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "IPv4", "IPv6"], []),
            "mac_address": MoPropertyMeta("mac_address", "macAddress", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [""], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version413a, MoPropertyMeta.NAMING, 0x100, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []),
            "netmask_or_i_pv6_prefix": MoPropertyMeta("netmask_or_i_pv6_prefix", "netmaskOrIPv6Prefix", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [""], ["1-128"]),
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], ["1-255"]),
            "port": MoPropertyMeta("port", "port", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x1000, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]|L|MLOM|L1|L2|OCP){0,1}""", [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "subtype": MoPropertyMeta("subtype", "subtype", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["HTTP"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, ["HTTP"], []),
            "uri": MoPropertyMeta("uri", "uri", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x40000, 0, 255, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "dnsserver": MoPropertyMeta("dnsserver", "dnsserver", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [""], []),
            "gateway": MoPropertyMeta("gateway", "gateway", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [""], []),
            "ip_config_type": MoPropertyMeta("ip_config_type", "ipConfigType", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "DHCP", "Static"], []),
            "ipaddress": MoPropertyMeta("ipaddress", "ipaddress", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [""], []),
            "iptype": MoPropertyMeta("iptype", "iptype", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "IPv4", "IPv6"], []),
            "mac_address": MoPropertyMeta("mac_address", "macAddress", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [""], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version413a, MoPropertyMeta.NAMING, 0x100, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []),
            "netmask_or_i_pv6_prefix": MoPropertyMeta("netmask_or_i_pv6_prefix", "netmaskOrIPv6Prefix", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [""], ["1-128"]),
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], ["1-255"]),
            "port": MoPropertyMeta("port", "port", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x1000, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]|L|MLOM|SIOC1|SIOC2|IOESlot1|IOESlot2|SBLOM1){0,1}""", [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "subtype": MoPropertyMeta("subtype", "subtype", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["HTTP"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, ["HTTP"], []),
            "uri": MoPropertyMeta("uri", "uri", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x40000, 0, 255, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "dnsserver": "dnsserver", 
            "gateway": "gateway", 
            "ipConfigType": "ip_config_type", 
            "ipaddress": "ipaddress", 
            "iptype": "iptype", 
            "macAddress": "mac_address", 
            "name": "name", 
            "netmaskOrIPv6Prefix": "netmask_or_i_pv6_prefix", 
            "order": "order", 
            "port": "port", 
            "rn": "rn", 
            "slot": "slot", 
            "state": "state", 
            "status": "status", 
            "subtype": "subtype", 
            "type": "type", 
            "uri": "uri", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "dnsserver": "dnsserver", 
            "gateway": "gateway", 
            "ipConfigType": "ip_config_type", 
            "ipaddress": "ipaddress", 
            "iptype": "iptype", 
            "macAddress": "mac_address", 
            "name": "name", 
            "netmaskOrIPv6Prefix": "netmask_or_i_pv6_prefix", 
            "order": "order", 
            "port": "port", 
            "rn": "rn", 
            "slot": "slot", 
            "state": "state", 
            "status": "status", 
            "subtype": "subtype", 
            "type": "type", 
            "uri": "uri", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.dnsserver = None
        self.gateway = None
        self.ip_config_type = None
        self.ipaddress = None
        self.iptype = None
        self.mac_address = None
        self.netmask_or_i_pv6_prefix = None
        self.order = None
        self.port = None
        self.slot = None
        self.state = None
        self.status = None
        self.subtype = None
        self.type = None
        self.uri = None
        self.child_action = None

        ManagedObject.__init__(self, "LsbootHttp", parent_mo_or_dn, **kwargs)

