"""This module contains the general information for AdaptorEthISCSIProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorEthISCSIProfileConsts:
    INITIATOR_PRIORITY_PRIMARY = "primary"
    INITIATOR_PRIORITY_SECONDARY = "secondary"


class AdaptorEthISCSIProfile(ManagedObject):
    """This is AdaptorEthISCSIProfile class."""

    consts = AdaptorEthISCSIProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorEthISCSIProfile", "adaptorEthISCSIProfile", "ethiscsi", VersionMeta.Version151f, "InputOutput", 0x3fffffff, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], ["Add", "Get", "Remove", "Set"]),
        "modular": MoMeta("AdaptorEthISCSIProfile", "adaptorEthISCSIProfile", "ethiscsi", VersionMeta.Version2013e, "InputOutput", 0x3fffffff, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], ["Add", "Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "dhcp_iscsi": MoPropertyMeta("dhcp_iscsi", "dhcpISCSI", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dhcp_id": MoPropertyMeta("dhcp_id", "dhcpId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 63, None, [], []),
            "dhcp_network_settings": MoPropertyMeta("dhcp_network_settings", "dhcpNetworkSettings", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dhcp_timeout": MoPropertyMeta("dhcp_timeout", "dhcpTimeout", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["60-300"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "initiator_chap_name": MoPropertyMeta("initiator_chap_name", "initiatorChapName", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[a-zA-Z0-9]{0,49}""", [], []),
            "initiator_chap_secret": MoPropertyMeta("initiator_chap_secret", "initiatorChapSecret", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,49}""", [], []),
            "initiator_gateway": MoPropertyMeta("initiator_gateway", "initiatorGateway", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "initiator_ip_address": MoPropertyMeta("initiator_ip_address", "initiatorIPAddress", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "initiator_name": MoPropertyMeta("initiator_name", "initiatorName", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""[0-9a-zA-Z\.:-]{0,222}""", [], []),
            "initiator_primary_dns": MoPropertyMeta("initiator_primary_dns", "initiatorPrimaryDns", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "initiator_priority": MoPropertyMeta("initiator_priority", "initiatorPriority", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["primary", "secondary"], []),
            "initiator_secondary_dns": MoPropertyMeta("initiator_secondary_dns", "initiatorSecondaryDns", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "initiator_subnet_mask": MoPropertyMeta("initiator_subnet_mask", "initiatorSubnetMask", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "initiator_tcp_timeout": MoPropertyMeta("initiator_tcp_timeout", "initiatorTCPTimeout", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], ["0-255"]),
            "link_busy_retry_count": MoPropertyMeta("link_busy_retry_count", "linkBusyRetryCount", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, [], ["0-255"]),
            "linkup_timeout": MoPropertyMeta("linkup_timeout", "linkupTimeout", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, [], ["0-255"]),
            "primary_target_boot_lun": MoPropertyMeta("primary_target_boot_lun", "primaryTargetBootLun", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, [], ["0-65535"]),
            "primary_target_chap_name": MoPropertyMeta("primary_target_chap_name", "primaryTargetChapName", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80000, None, None, r"""[a-zA-Z0-9]{0,49}""", [], []),
            "primary_target_chap_secret": MoPropertyMeta("primary_target_chap_secret", "primaryTargetChapSecret", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100000, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,49}""", [], []),
            "primary_target_ip_address": MoPropertyMeta("primary_target_ip_address", "primaryTargetIPAddress", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "primary_target_name": MoPropertyMeta("primary_target_name", "primaryTargetName", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400000, None, None, r"""[0-9a-zA-Z\.:-]{0,222}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800000, 0, 255, None, [], []),
            "secondary_target_boot_lun": MoPropertyMeta("secondary_target_boot_lun", "secondaryTargetBootLun", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x1000000, None, None, None, [], ["0-65535"]),
            "secondary_target_chap_name": MoPropertyMeta("secondary_target_chap_name", "secondaryTargetChapName", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2000000, None, None, r"""[a-zA-Z0-9]{0,49}""", [], []),
            "secondary_target_chap_secret": MoPropertyMeta("secondary_target_chap_secret", "secondaryTargetChapSecret", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4000000, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,49}""", [], []),
            "secondary_target_ip_address": MoPropertyMeta("secondary_target_ip_address", "secondaryTargetIPAddress", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8000000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "secondary_target_name": MoPropertyMeta("secondary_target_name", "secondaryTargetName", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10000000, None, None, r"""[0-9a-zA-Z\.:-]{0,222}""", [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20000000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "ip_ver": MoPropertyMeta("ip_ver", "ipVer", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "primary_target_port": MoPropertyMeta("primary_target_port", "primaryTargetPort", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "secondary_target_port": MoPropertyMeta("secondary_target_port", "secondaryTargetPort", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

        "modular": {
            "dhcp_iscsi": MoPropertyMeta("dhcp_iscsi", "dhcpISCSI", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dhcp_id": MoPropertyMeta("dhcp_id", "dhcpId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 63, None, [], []),
            "dhcp_network_settings": MoPropertyMeta("dhcp_network_settings", "dhcpNetworkSettings", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dhcp_timeout": MoPropertyMeta("dhcp_timeout", "dhcpTimeout", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["60-300"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "initiator_chap_name": MoPropertyMeta("initiator_chap_name", "initiatorChapName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[a-zA-Z0-9]{0,49}""", [], []),
            "initiator_chap_secret": MoPropertyMeta("initiator_chap_secret", "initiatorChapSecret", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,49}""", [], []),
            "initiator_gateway": MoPropertyMeta("initiator_gateway", "initiatorGateway", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "initiator_ip_address": MoPropertyMeta("initiator_ip_address", "initiatorIPAddress", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "initiator_name": MoPropertyMeta("initiator_name", "initiatorName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""[0-9a-zA-Z\.:-]{0,222}""", [], []),
            "initiator_primary_dns": MoPropertyMeta("initiator_primary_dns", "initiatorPrimaryDns", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "initiator_priority": MoPropertyMeta("initiator_priority", "initiatorPriority", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["primary", "secondary"], []),
            "initiator_secondary_dns": MoPropertyMeta("initiator_secondary_dns", "initiatorSecondaryDns", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "initiator_subnet_mask": MoPropertyMeta("initiator_subnet_mask", "initiatorSubnetMask", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "initiator_tcp_timeout": MoPropertyMeta("initiator_tcp_timeout", "initiatorTCPTimeout", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], ["0-255"]),
            "link_busy_retry_count": MoPropertyMeta("link_busy_retry_count", "linkBusyRetryCount", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, [], ["0-255"]),
            "linkup_timeout": MoPropertyMeta("linkup_timeout", "linkupTimeout", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, [], ["0-255"]),
            "primary_target_boot_lun": MoPropertyMeta("primary_target_boot_lun", "primaryTargetBootLun", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, [], ["0-65535"]),
            "primary_target_chap_name": MoPropertyMeta("primary_target_chap_name", "primaryTargetChapName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80000, None, None, r"""[a-zA-Z0-9]{0,49}""", [], []),
            "primary_target_chap_secret": MoPropertyMeta("primary_target_chap_secret", "primaryTargetChapSecret", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100000, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,49}""", [], []),
            "primary_target_ip_address": MoPropertyMeta("primary_target_ip_address", "primaryTargetIPAddress", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "primary_target_name": MoPropertyMeta("primary_target_name", "primaryTargetName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400000, None, None, r"""[0-9a-zA-Z\.:-]{0,222}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800000, 0, 255, None, [], []),
            "secondary_target_boot_lun": MoPropertyMeta("secondary_target_boot_lun", "secondaryTargetBootLun", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000000, None, None, None, [], ["0-65535"]),
            "secondary_target_chap_name": MoPropertyMeta("secondary_target_chap_name", "secondaryTargetChapName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000000, None, None, r"""[a-zA-Z0-9]{0,49}""", [], []),
            "secondary_target_chap_secret": MoPropertyMeta("secondary_target_chap_secret", "secondaryTargetChapSecret", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000000, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,49}""", [], []),
            "secondary_target_ip_address": MoPropertyMeta("secondary_target_ip_address", "secondaryTargetIPAddress", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000000, 0, 255, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], []),
            "secondary_target_name": MoPropertyMeta("secondary_target_name", "secondaryTargetName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000000, None, None, r"""[0-9a-zA-Z\.:-]{0,222}""", [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20000000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "ip_ver": MoPropertyMeta("ip_ver", "ipVer", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "primary_target_port": MoPropertyMeta("primary_target_port", "primaryTargetPort", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "secondary_target_port": MoPropertyMeta("secondary_target_port", "secondaryTargetPort", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dhcpISCSI": "dhcp_iscsi", 
            "dhcpId": "dhcp_id", 
            "dhcpNetworkSettings": "dhcp_network_settings", 
            "dhcpTimeout": "dhcp_timeout", 
            "dn": "dn", 
            "initiatorChapName": "initiator_chap_name", 
            "initiatorChapSecret": "initiator_chap_secret", 
            "initiatorGateway": "initiator_gateway", 
            "initiatorIPAddress": "initiator_ip_address", 
            "initiatorName": "initiator_name", 
            "initiatorPrimaryDns": "initiator_primary_dns", 
            "initiatorPriority": "initiator_priority", 
            "initiatorSecondaryDns": "initiator_secondary_dns", 
            "initiatorSubnetMask": "initiator_subnet_mask", 
            "initiatorTCPTimeout": "initiator_tcp_timeout", 
            "linkBusyRetryCount": "link_busy_retry_count", 
            "linkupTimeout": "linkup_timeout", 
            "primaryTargetBootLun": "primary_target_boot_lun", 
            "primaryTargetChapName": "primary_target_chap_name", 
            "primaryTargetChapSecret": "primary_target_chap_secret", 
            "primaryTargetIPAddress": "primary_target_ip_address", 
            "primaryTargetName": "primary_target_name", 
            "rn": "rn", 
            "secondaryTargetBootLun": "secondary_target_boot_lun", 
            "secondaryTargetChapName": "secondary_target_chap_name", 
            "secondaryTargetChapSecret": "secondary_target_chap_secret", 
            "secondaryTargetIPAddress": "secondary_target_ip_address", 
            "secondaryTargetName": "secondary_target_name", 
            "status": "status", 
            "childAction": "child_action", 
            "ipVer": "ip_ver", 
            "primaryTargetPort": "primary_target_port", 
            "secondaryTargetPort": "secondary_target_port", 
        },

        "modular": {
            "dhcpISCSI": "dhcp_iscsi", 
            "dhcpId": "dhcp_id", 
            "dhcpNetworkSettings": "dhcp_network_settings", 
            "dhcpTimeout": "dhcp_timeout", 
            "dn": "dn", 
            "initiatorChapName": "initiator_chap_name", 
            "initiatorChapSecret": "initiator_chap_secret", 
            "initiatorGateway": "initiator_gateway", 
            "initiatorIPAddress": "initiator_ip_address", 
            "initiatorName": "initiator_name", 
            "initiatorPrimaryDns": "initiator_primary_dns", 
            "initiatorPriority": "initiator_priority", 
            "initiatorSecondaryDns": "initiator_secondary_dns", 
            "initiatorSubnetMask": "initiator_subnet_mask", 
            "initiatorTCPTimeout": "initiator_tcp_timeout", 
            "linkBusyRetryCount": "link_busy_retry_count", 
            "linkupTimeout": "linkup_timeout", 
            "primaryTargetBootLun": "primary_target_boot_lun", 
            "primaryTargetChapName": "primary_target_chap_name", 
            "primaryTargetChapSecret": "primary_target_chap_secret", 
            "primaryTargetIPAddress": "primary_target_ip_address", 
            "primaryTargetName": "primary_target_name", 
            "rn": "rn", 
            "secondaryTargetBootLun": "secondary_target_boot_lun", 
            "secondaryTargetChapName": "secondary_target_chap_name", 
            "secondaryTargetChapSecret": "secondary_target_chap_secret", 
            "secondaryTargetIPAddress": "secondary_target_ip_address", 
            "secondaryTargetName": "secondary_target_name", 
            "status": "status", 
            "childAction": "child_action", 
            "ipVer": "ip_ver", 
            "primaryTargetPort": "primary_target_port", 
            "secondaryTargetPort": "secondary_target_port", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.dhcp_iscsi = None
        self.dhcp_id = None
        self.dhcp_network_settings = None
        self.dhcp_timeout = None
        self.initiator_chap_name = None
        self.initiator_chap_secret = None
        self.initiator_gateway = None
        self.initiator_ip_address = None
        self.initiator_name = None
        self.initiator_primary_dns = None
        self.initiator_priority = None
        self.initiator_secondary_dns = None
        self.initiator_subnet_mask = None
        self.initiator_tcp_timeout = None
        self.link_busy_retry_count = None
        self.linkup_timeout = None
        self.primary_target_boot_lun = None
        self.primary_target_chap_name = None
        self.primary_target_chap_secret = None
        self.primary_target_ip_address = None
        self.primary_target_name = None
        self.secondary_target_boot_lun = None
        self.secondary_target_chap_name = None
        self.secondary_target_chap_secret = None
        self.secondary_target_ip_address = None
        self.secondary_target_name = None
        self.status = None
        self.child_action = None
        self.ip_ver = None
        self.primary_target_port = None
        self.secondary_target_port = None

        ManagedObject.__init__(self, "AdaptorEthISCSIProfile", parent_mo_or_dn, **kwargs)

