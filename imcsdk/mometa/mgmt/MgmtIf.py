"""This module contains the general information for MgmtIf ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MgmtIfConsts:
    ADMIN_DUPLEX_NA = "NA"
    ADMIN_DUPLEX_AUTO = "auto"
    ADMIN_DUPLEX_FULL = "full"
    ADMIN_DUPLEX_HALF = "half"
    ADMIN_NET_SPEED_100_MBPS = "100Mbps"
    ADMIN_NET_SPEED_10_MBPS = "10Mbps"
    ADMIN_NET_SPEED_1_GBPS = "1Gbps"
    ADMIN_NET_SPEED_NA = "NA"
    ADMIN_NET_SPEED_AUTO = "auto"
    IF_TYPE_PHYSICAL = "physical"
    NIC_MODE_CISCO_CARD = "cisco_card"
    NIC_MODE_DEDICATED = "dedicated"
    NIC_MODE_SHARED_LOM = "shared_lom"
    NIC_MODE_SHARED_LOM_10G = "shared_lom_10g"
    NIC_MODE_SHARED_LOM_EXT = "shared_lom_ext"
    NIC_MODE_SHIPPING = "shipping"
    NIC_REDUNDANCY_ACTIVE_ACTIVE = "active-active"
    NIC_REDUNDANCY_ACTIVE_STANDBY = "active-standby"
    NIC_REDUNDANCY_NONE = "none"
    OPER_DUPLEX_NA = "NA"
    OPER_DUPLEX_AUTO = "auto"
    OPER_DUPLEX_FULL = "full"
    OPER_DUPLEX_HALF = "half"
    OPER_NET_SPEED_100_MBPS = "100Mbps"
    OPER_NET_SPEED_10_MBPS = "10Mbps"
    OPER_NET_SPEED_1_GBPS = "1Gbps"
    OPER_NET_SPEED_NA = "NA"
    OPER_NET_SPEED_AUTO = "auto"
    VIC_SLOT_0 = "0"
    VIC_SLOT_1 = "1"
    VIC_SLOT_10 = "10"
    VIC_SLOT_11 = "11"
    VIC_SLOT_12 = "12"
    VIC_SLOT_2 = "2"
    VIC_SLOT_4 = "4"
    VIC_SLOT_5 = "5"
    VIC_SLOT_9 = "9"
    VIC_SLOT_FLEX_LOM = "flex-lom"
    VIC_SLOT_MLOM = "mlom"
    VIC_SLOT_RISER1 = "riser1"
    VIC_SLOT_RISER2 = "riser2"
    VIC_SLOT_RISER3 = "riser3"
    IF_TYPE_VIRTUAL = "virtual"


class MgmtIf(ManagedObject):
    """This is MgmtIf class."""

    consts = MgmtIfConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("MgmtIf", "mgmtIf", "if-1", VersionMeta.Version151f, "InputOutput", 0x1ffffffff, [], ["admin", "read-only", "user"], ['mgmtController'], ['faultInst', 'ipBlocking', 'ipFiltering'], ["Get", "Set"]),
        "modular": MoMeta("MgmtIf", "mgmtIf", "if-1", VersionMeta.Version2013e, "InputOutput", 0x3fffffffffff, [], ["admin", "read-only", "user"], ['equipmentChassis', 'mgmtController'], ['ipBlocking', 'ipFiltering'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_duplex": MoPropertyMeta("admin_duplex", "adminDuplex", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["NA", "auto", "full", "half"], []),
            "admin_net_speed": MoPropertyMeta("admin_net_speed", "adminNetSpeed", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["100Mbps", "10Mbps", "1Gbps", "NA", "auto"], []),
            "auto_neg": MoPropertyMeta("auto_neg", "autoNeg", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "ddns_domain": MoPropertyMeta("ddns_domain", "ddnsDomain", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "ddns_enable": MoPropertyMeta("ddns_enable", "ddnsEnable", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "ddns_refresh_interval": MoPropertyMeta("ddns_refresh_interval", "ddnsRefreshInterval", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-8736"]),
            "dhcp_enable": MoPropertyMeta("dhcp_enable", "dhcpEnable", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "dns_alternate": MoPropertyMeta("dns_alternate", "dnsAlternate", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "dns_preferred": MoPropertyMeta("dns_preferred", "dnsPreferred", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "dns_using_dhcp": MoPropertyMeta("dns_using_dhcp", "dnsUsingDhcp", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "ext_gw": MoPropertyMeta("ext_gw", "extGw", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x1000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "ext_ip": MoPropertyMeta("ext_ip", "extIp", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "ext_mask": MoPropertyMeta("ext_mask", "extMask", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8000, 0, 63, r"""(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])""", [], []),
            "nic_mode": MoPropertyMeta("nic_mode", "nicMode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["cisco_card", "dedicated", "shared_lom", "shared_lom_10g", "shared_lom_ext", "shipping"], []),
            "nic_redundancy": MoPropertyMeta("nic_redundancy", "nicRedundancy", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, ["active-active", "active-standby", "none"], []),
            "port_profile": MoPropertyMeta("port_profile", "portProfile", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40000, None, None, r"""(([a-zA-Z0-9_]{1})|([a-zA-Z0-9_]{1}[a-zA-Z0-9_\-]{0,79}))""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80000, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "v6dhcp_enable": MoPropertyMeta("v6dhcp_enable", "v6dhcpEnable", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x200000, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "v6dns_alternate": MoPropertyMeta("v6dns_alternate", "v6dnsAlternate", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x400000, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6dns_preferred": MoPropertyMeta("v6dns_preferred", "v6dnsPreferred", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x800000, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6dns_using_dhcp": MoPropertyMeta("v6dns_using_dhcp", "v6dnsUsingDhcp", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x1000000, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "v6ext_enabled": MoPropertyMeta("v6ext_enabled", "v6extEnabled", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2000000, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "v6ext_gw": MoPropertyMeta("v6ext_gw", "v6extGw", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x4000000, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6ext_ip": MoPropertyMeta("v6ext_ip", "v6extIp", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x8000000, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6prefix": MoPropertyMeta("v6prefix", "v6prefix", "uint", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x10000000, None, None, None, [], ["1-128"]),
            "vic_slot": MoPropertyMeta("vic_slot", "vicSlot", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x20000000, None, None, None, ["0", "1", "10", "11", "12", "2", "4", "5", "9", "flex-lom", "mlom", "riser1", "riser2", "riser3"], []),
            "vlan_enable": MoPropertyMeta("vlan_enable", "vlanEnable", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40000000, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "vlan_id": MoPropertyMeta("vlan_id", "vlanId", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80000000, None, None, None, [], ["1-4094"]),
            "vlan_priority": MoPropertyMeta("vlan_priority", "vlanPriority", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100000000, None, None, None, [], ["0-7"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "ext_enabled": MoPropertyMeta("ext_enabled", "extEnabled", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["physical"], []),
            "mac": MoPropertyMeta("mac", "mac", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "oper_duplex": MoPropertyMeta("oper_duplex", "operDuplex", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "auto", "full", "half"], []),
            "oper_net_speed": MoPropertyMeta("oper_net_speed", "operNetSpeed", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["100Mbps", "10Mbps", "1Gbps", "NA", "auto"], []),
            "subject": MoPropertyMeta("subject", "subject", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "v6_slaac_ip": MoPropertyMeta("v6_slaac_ip", "v6SlaacIp", "string", VersionMeta.Version202c, MoPropertyMeta.READ_ONLY, None, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6link_local": MoPropertyMeta("v6link_local", "v6linkLocal", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
        },

        "modular": {
            "admin_duplex": MoPropertyMeta("admin_duplex", "adminDuplex", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["NA", "auto", "full", "half"], []),
            "admin_net_speed": MoPropertyMeta("admin_net_speed", "adminNetSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["100Mbps", "10Mbps", "1Gbps", "NA", "auto"], []),
            "auto_neg": MoPropertyMeta("auto_neg", "autoNeg", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "ddns_domain": MoPropertyMeta("ddns_domain", "ddnsDomain", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "ddns_enable": MoPropertyMeta("ddns_enable", "ddnsEnable", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["No", "Yes", "no", "yes"], []),
            "ddns_refresh_interval": MoPropertyMeta("ddns_refresh_interval", "ddnsRefreshInterval", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-8736"]),
            "dhcp_enable": MoPropertyMeta("dhcp_enable", "dhcpEnable", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["No", "Yes", "no", "yes"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "dns_alternate": MoPropertyMeta("dns_alternate", "dnsAlternate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "dns_preferred": MoPropertyMeta("dns_preferred", "dnsPreferred", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "dns_using_dhcp": MoPropertyMeta("dns_using_dhcp", "dnsUsingDhcp", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["No", "Yes", "no", "yes"], []),
            "ext_gw": MoPropertyMeta("ext_gw", "extGw", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "ext_ip": MoPropertyMeta("ext_ip", "extIp", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "ext_mask": MoPropertyMeta("ext_mask", "extMask", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000, 0, 63, r"""(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])""", [], []),
            "nic_mode": MoPropertyMeta("nic_mode", "nicMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["cisco_card", "dedicated", "shared_lom", "shared_lom_10g", "shared_lom_ext", "shipping"], []),
            "nic_redundancy": MoPropertyMeta("nic_redundancy", "nicRedundancy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, ["active-active", "active-standby", "none"], []),
            "port_profile": MoPropertyMeta("port_profile", "portProfile", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40000, None, None, r"""(([a-zA-Z0-9_]{1})|([a-zA-Z0-9_]{1}[a-zA-Z0-9_\-]{0,79}))""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80000, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "v6dhcp_enable": MoPropertyMeta("v6dhcp_enable", "v6dhcpEnable", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200000, None, None, None, ["No", "Yes", "no", "yes"], []),
            "v6dns_alternate": MoPropertyMeta("v6dns_alternate", "v6dnsAlternate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400000, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6dns_preferred": MoPropertyMeta("v6dns_preferred", "v6dnsPreferred", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800000, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6dns_using_dhcp": MoPropertyMeta("v6dns_using_dhcp", "v6dnsUsingDhcp", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000000, None, None, None, ["No", "Yes", "no", "yes"], []),
            "v6ext_enabled": MoPropertyMeta("v6ext_enabled", "v6extEnabled", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000000, None, None, None, ["No", "Yes", "no", "yes"], []),
            "v6ext_gw": MoPropertyMeta("v6ext_gw", "v6extGw", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000000, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6ext_ip": MoPropertyMeta("v6ext_ip", "v6extIp", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000000, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6prefix": MoPropertyMeta("v6prefix", "v6prefix", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000000, None, None, None, [], ["1-128"]),
            "vic_slot": MoPropertyMeta("vic_slot", "vicSlot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20000000, None, None, None, ["0", "1", "10", "2", "4", "5", "9", "flex-lom", "riser1", "riser2"], []),
            "vlan_enable": MoPropertyMeta("vlan_enable", "vlanEnable", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40000000, None, None, None, ["No", "Yes", "no", "yes"], []),
            "vlan_id": MoPropertyMeta("vlan_id", "vlanId", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80000000, None, None, None, [], ["1-4094"]),
            "vlan_priority": MoPropertyMeta("vlan_priority", "vlanPriority", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100000000, None, None, None, [], ["0-7"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "ext_enabled": MoPropertyMeta("ext_enabled", "extEnabled", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["physical", "virtual"], []),
            "mac": MoPropertyMeta("mac", "mac", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "oper_duplex": MoPropertyMeta("oper_duplex", "operDuplex", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "auto", "full", "half"], []),
            "oper_net_speed": MoPropertyMeta("oper_net_speed", "operNetSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["100Mbps", "10Mbps", "1Gbps", "NA", "auto"], []),
            "single_ip_enable": MoPropertyMeta("single_ip_enable", "singleIPEnable", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x200000000, None, None, None, ["No", "Yes", "no", "yes"], []),
            "starting_port": MoPropertyMeta("starting_port", "startingPort", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x400000000, None, None, None, [], ["9000-65529"]),
            "subject": MoPropertyMeta("subject", "subject", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "v4_ip_addr": MoPropertyMeta("v4_ip_addr", "v4IPAddr", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800000000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "v4_ip_addr_bmc1": MoPropertyMeta("v4_ip_addr_bmc1", "v4IPAddrBmc1", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000000000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "v4_ip_addr_bmc2": MoPropertyMeta("v4_ip_addr_bmc2", "v4IPAddrBmc2", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000000000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "v4_ip_addr_cmc1": MoPropertyMeta("v4_ip_addr_cmc1", "v4IPAddrCmc1", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000000000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "v4_ip_addr_cmc2": MoPropertyMeta("v4_ip_addr_cmc2", "v4IPAddrCmc2", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000000000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "v6_ip_addr": MoPropertyMeta("v6_ip_addr", "v6IPAddr", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000000000, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6_ip_addr_bmc1": MoPropertyMeta("v6_ip_addr_bmc1", "v6IPAddrBmc1", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20000000000, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6_ip_addr_bmc2": MoPropertyMeta("v6_ip_addr_bmc2", "v6IPAddrBmc2", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40000000000, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6_ip_addr_cmc1": MoPropertyMeta("v6_ip_addr_cmc1", "v6IPAddrCmc1", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80000000000, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6_ip_addr_cmc2": MoPropertyMeta("v6_ip_addr_cmc2", "v6IPAddrCmc2", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100000000000, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6_slaac_ip": MoPropertyMeta("v6_slaac_ip", "v6SlaacIp", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v6link_local": MoPropertyMeta("v6link_local", "v6linkLocal", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 255, r"""(https?://)?([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []),
            "v_hostname": MoPropertyMeta("v_hostname", "vHostname", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200000000000, 0, 63, r"""(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminDuplex": "admin_duplex", 
            "adminNetSpeed": "admin_net_speed", 
            "autoNeg": "auto_neg", 
            "ddnsDomain": "ddns_domain", 
            "ddnsEnable": "ddns_enable", 
            "ddnsRefreshInterval": "ddns_refresh_interval", 
            "dhcpEnable": "dhcp_enable", 
            "dn": "dn", 
            "dnsAlternate": "dns_alternate", 
            "dnsPreferred": "dns_preferred", 
            "dnsUsingDhcp": "dns_using_dhcp", 
            "extGw": "ext_gw", 
            "extIp": "ext_ip", 
            "extMask": "ext_mask", 
            "hostname": "hostname", 
            "nicMode": "nic_mode", 
            "nicRedundancy": "nic_redundancy", 
            "portProfile": "port_profile", 
            "rn": "rn", 
            "status": "status", 
            "v6dhcpEnable": "v6dhcp_enable", 
            "v6dnsAlternate": "v6dns_alternate", 
            "v6dnsPreferred": "v6dns_preferred", 
            "v6dnsUsingDhcp": "v6dns_using_dhcp", 
            "v6extEnabled": "v6ext_enabled", 
            "v6extGw": "v6ext_gw", 
            "v6extIp": "v6ext_ip", 
            "v6prefix": "v6prefix", 
            "vicSlot": "vic_slot", 
            "vlanEnable": "vlan_enable", 
            "vlanId": "vlan_id", 
            "vlanPriority": "vlan_priority", 
            "childAction": "child_action", 
            "description": "description", 
            "extEnabled": "ext_enabled", 
            "id": "id", 
            "ifType": "if_type", 
            "mac": "mac", 
            "operDuplex": "oper_duplex", 
            "operNetSpeed": "oper_net_speed", 
            "subject": "subject", 
            "v6SlaacIp": "v6_slaac_ip", 
            "v6linkLocal": "v6link_local", 
        },

        "modular": {
            "adminDuplex": "admin_duplex", 
            "adminNetSpeed": "admin_net_speed", 
            "autoNeg": "auto_neg", 
            "ddnsDomain": "ddns_domain", 
            "ddnsEnable": "ddns_enable", 
            "ddnsRefreshInterval": "ddns_refresh_interval", 
            "dhcpEnable": "dhcp_enable", 
            "dn": "dn", 
            "dnsAlternate": "dns_alternate", 
            "dnsPreferred": "dns_preferred", 
            "dnsUsingDhcp": "dns_using_dhcp", 
            "extGw": "ext_gw", 
            "extIp": "ext_ip", 
            "extMask": "ext_mask", 
            "hostname": "hostname", 
            "nicMode": "nic_mode", 
            "nicRedundancy": "nic_redundancy", 
            "portProfile": "port_profile", 
            "rn": "rn", 
            "status": "status", 
            "v6dhcpEnable": "v6dhcp_enable", 
            "v6dnsAlternate": "v6dns_alternate", 
            "v6dnsPreferred": "v6dns_preferred", 
            "v6dnsUsingDhcp": "v6dns_using_dhcp", 
            "v6extEnabled": "v6ext_enabled", 
            "v6extGw": "v6ext_gw", 
            "v6extIp": "v6ext_ip", 
            "v6prefix": "v6prefix", 
            "vicSlot": "vic_slot", 
            "vlanEnable": "vlan_enable", 
            "vlanId": "vlan_id", 
            "vlanPriority": "vlan_priority", 
            "childAction": "child_action", 
            "description": "description", 
            "extEnabled": "ext_enabled", 
            "id": "id", 
            "ifType": "if_type", 
            "mac": "mac", 
            "operDuplex": "oper_duplex", 
            "operNetSpeed": "oper_net_speed", 
            "singleIPEnable": "single_ip_enable", 
            "startingPort": "starting_port", 
            "subject": "subject", 
            "v4IPAddr": "v4_ip_addr", 
            "v4IPAddrBmc1": "v4_ip_addr_bmc1", 
            "v4IPAddrBmc2": "v4_ip_addr_bmc2", 
            "v4IPAddrCmc1": "v4_ip_addr_cmc1", 
            "v4IPAddrCmc2": "v4_ip_addr_cmc2", 
            "v6IPAddr": "v6_ip_addr", 
            "v6IPAddrBmc1": "v6_ip_addr_bmc1", 
            "v6IPAddrBmc2": "v6_ip_addr_bmc2", 
            "v6IPAddrCmc1": "v6_ip_addr_cmc1", 
            "v6IPAddrCmc2": "v6_ip_addr_cmc2", 
            "v6SlaacIp": "v6_slaac_ip", 
            "v6linkLocal": "v6link_local", 
            "vHostname": "v_hostname", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_duplex = None
        self.admin_net_speed = None
        self.auto_neg = None
        self.ddns_domain = None
        self.ddns_enable = None
        self.ddns_refresh_interval = None
        self.dhcp_enable = None
        self.dns_alternate = None
        self.dns_preferred = None
        self.dns_using_dhcp = None
        self.ext_gw = None
        self.ext_ip = None
        self.ext_mask = None
        self.hostname = None
        self.nic_mode = None
        self.nic_redundancy = None
        self.port_profile = None
        self.status = None
        self.v6dhcp_enable = None
        self.v6dns_alternate = None
        self.v6dns_preferred = None
        self.v6dns_using_dhcp = None
        self.v6ext_enabled = None
        self.v6ext_gw = None
        self.v6ext_ip = None
        self.v6prefix = None
        self.vic_slot = None
        self.vlan_enable = None
        self.vlan_id = None
        self.vlan_priority = None
        self.child_action = None
        self.description = None
        self.ext_enabled = None
        self.id = None
        self.if_type = None
        self.mac = None
        self.oper_duplex = None
        self.oper_net_speed = None
        self.subject = None
        self.v6_slaac_ip = None
        self.v6link_local = None
        self.single_ip_enable = None
        self.starting_port = None
        self.v4_ip_addr = None
        self.v4_ip_addr_bmc1 = None
        self.v4_ip_addr_bmc2 = None
        self.v4_ip_addr_cmc1 = None
        self.v4_ip_addr_cmc2 = None
        self.v6_ip_addr = None
        self.v6_ip_addr_bmc1 = None
        self.v6_ip_addr_bmc2 = None
        self.v6_ip_addr_cmc1 = None
        self.v6_ip_addr_cmc2 = None
        self.v_hostname = None

        ManagedObject.__init__(self, "MgmtIf", parent_mo_or_dn, **kwargs)

