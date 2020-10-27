"""This module contains the general information for AaaLdap ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AaaLdapConsts:
    BIND_METHOD_ANONYMOUS = "anonymous"
    BIND_METHOD_CONFIGURED_CREDENTIALS = "configured-credentials"
    BIND_METHOD_LOGIN_CREDENTIALS = "login-credentials"
    DNS_DOMAIN_SOURCE_CONFIGURED_DOMAIN = "configured-domain"
    DNS_DOMAIN_SOURCE_EXTRACTED_CONFIGURED_DOMAIN = "extracted-configured-domain"
    DNS_DOMAIN_SOURCE_EXTRACTED_DOMAIN = "extracted-domain"
    LOCATE_DIRECTORY_USING_DNS_NO = "no"
    LOCATE_DIRECTORY_USING_DNS_YES = "yes"
    USER_SEARCH_PRECEDENCE_LDAP_USER_DB = "ldap-user-db"
    USER_SEARCH_PRECEDENCE_LOCAL_USER_DB = "local-user-db"


class AaaLdap(ManagedObject):
    """This is AaaLdap class."""

    consts = AaaLdapConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AaaLdap", "aaaLdap", "ldap-ext", VersionMeta.Version151f, "InputOutput", 0x3ffffffff, [], ["admin", "read-only", "user"], ['topSystem'], ['aaaLdapRoleGroup', 'ldapCACertificateManagement', 'secureLdap'], ["Get", "Set"]),
        "modular": MoMeta("AaaLdap", "aaaLdap", "ldap-ext", VersionMeta.Version2013e, "InputOutput", 0x3ffffffff, [], ["admin", "read-only", "user"], ['topSystem'], ['aaaLdapRoleGroup', 'ldapCACertificateManagement', 'secureLdap'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "attribute": MoPropertyMeta("attribute", "attribute", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 64, r"""([a-zA-Z0-9][a-zA-Z0-9\-\.]*[a-zA-Z0-9\-]){0,64}""", [], []),
            "basedn": MoPropertyMeta("basedn", "basedn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 254, None, [], []),
            "bind_dn": MoPropertyMeta("bind_dn", "bindDn", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x10, 0, 254, None, [], []),
            "bind_method": MoPropertyMeta("bind_method", "bindMethod", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["anonymous", "configured-credentials", "login-credentials"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "dns_domain_source": MoPropertyMeta("dns_domain_source", "dnsDomainSource", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["configured-domain", "extracted-configured-domain", "extracted-domain"], []),
            "dns_search_domain": MoPropertyMeta("dns_search_domain", "dnsSearchDomain", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x100, 0, 64, r"""(([a-zA-Z0-9])|([a-zA-Z0-9][a-zA-Z0-9\.\-]*[a-zA-Z0-9]){0,64})""", [], []),
            "dns_search_forest": MoPropertyMeta("dns_search_forest", "dnsSearchForest", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x200, 0, 64, r"""(([a-zA-Z0-9])|([a-zA-Z0-9][a-zA-Z0-9\.\-]*[a-zA-Z0-9]){0,64})""", [], []),
            "domain": MoPropertyMeta("domain", "domain", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x400, 0, 254, None, [], []),
            "encryption": MoPropertyMeta("encryption", "encryption", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "filter": MoPropertyMeta("filter", "filter", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x1000, 0, 20, r"""[a-zA-Z0-9][a-zA-Z0-9_#@$%&\-\^]*[a-zA-Z0-9\-]""", [], []),
            "group_attribute": MoPropertyMeta("group_attribute", "groupAttribute", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x2000, 0, 254, r"""[a-zA-Z0-9][a-zA-Z0-9_#@$%&\-\^]*[a-zA-Z0-9\-]""", [], []),
            "group_auth": MoPropertyMeta("group_auth", "groupAuth", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "group_nested_search": MoPropertyMeta("group_nested_search", "groupNestedSearch", "uint", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], ["1-128"]),
            "ldap_server1": MoPropertyMeta("ldap_server1", "ldapServer1", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x10000, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], []),
            "ldap_server2": MoPropertyMeta("ldap_server2", "ldapServer2", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x20000, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], []),
            "ldap_server3": MoPropertyMeta("ldap_server3", "ldapServer3", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x40000, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], []),
            "ldap_server4": MoPropertyMeta("ldap_server4", "ldapServer4", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x80000, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], []),
            "ldap_server5": MoPropertyMeta("ldap_server5", "ldapServer5", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x100000, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], []),
            "ldap_server6": MoPropertyMeta("ldap_server6", "ldapServer6", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x200000, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], []),
            "ldap_server_port1": MoPropertyMeta("ldap_server_port1", "ldapServerPort1", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x400000, None, None, None, [], ["1-65535"]),
            "ldap_server_port2": MoPropertyMeta("ldap_server_port2", "ldapServerPort2", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x800000, None, None, None, [], ["1-65535"]),
            "ldap_server_port3": MoPropertyMeta("ldap_server_port3", "ldapServerPort3", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x1000000, None, None, None, [], ["1-65535"]),
            "ldap_server_port4": MoPropertyMeta("ldap_server_port4", "ldapServerPort4", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x2000000, None, None, None, [], ["1-65535"]),
            "ldap_server_port5": MoPropertyMeta("ldap_server_port5", "ldapServerPort5", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x4000000, None, None, None, [], ["1-65535"]),
            "ldap_server_port6": MoPropertyMeta("ldap_server_port6", "ldapServerPort6", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x8000000, None, None, None, [], ["1-65535"]),
            "locate_directory_using_dns": MoPropertyMeta("locate_directory_using_dns", "locateDirectoryUsingDNS", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x10000000, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x20000000, None, None, r"""[\S+]{0,254}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40000000, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80000000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100000000, None, None, None, [], ["0-180", "0-1800"]),
            "user_search_precedence": MoPropertyMeta("user_search_precedence", "userSearchPrecedence", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x200000000, None, None, None, ["ldap-user-db", "local-user-db"], []),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "attribute": MoPropertyMeta("attribute", "attribute", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 64, r"""([a-zA-Z0-9][a-zA-Z0-9\-\.]*[a-zA-Z0-9\-]){0,64}""", [], []),
            "basedn": MoPropertyMeta("basedn", "basedn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 254, None, [], []),
            "bind_dn": MoPropertyMeta("bind_dn", "bindDn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 254, None, [], []),
            "bind_method": MoPropertyMeta("bind_method", "bindMethod", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["anonymous", "configured-credentials", "login-credentials"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "dns_domain_source": MoPropertyMeta("dns_domain_source", "dnsDomainSource", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["configured-domain", "extracted-configured-domain", "extracted-domain"], []),
            "dns_search_domain": MoPropertyMeta("dns_search_domain", "dnsSearchDomain", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 64, r"""(([a-zA-Z0-9])|([a-zA-Z0-9][a-zA-Z0-9\.\-]*[a-zA-Z0-9]){0,64})""", [], []),
            "dns_search_forest": MoPropertyMeta("dns_search_forest", "dnsSearchForest", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, 0, 64, r"""(([a-zA-Z0-9])|([a-zA-Z0-9][a-zA-Z0-9\.\-]*[a-zA-Z0-9]){0,64})""", [], []),
            "domain": MoPropertyMeta("domain", "domain", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, 0, 254, None, [], []),
            "encryption": MoPropertyMeta("encryption", "encryption", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "filter": MoPropertyMeta("filter", "filter", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, 0, 20, r"""[a-zA-Z0-9][a-zA-Z0-9_#@$%&\-\^]*[a-zA-Z0-9\-]""", [], []),
            "group_attribute": MoPropertyMeta("group_attribute", "groupAttribute", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, 0, 254, r"""[a-zA-Z0-9][a-zA-Z0-9_#@$%&\-\^]*[a-zA-Z0-9\-]""", [], []),
            "group_auth": MoPropertyMeta("group_auth", "groupAuth", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "group_nested_search": MoPropertyMeta("group_nested_search", "groupNestedSearch", "uint", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], ["1-128"]),
            "ldap_server1": MoPropertyMeta("ldap_server1", "ldapServer1", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [""], []),
            "ldap_server2": MoPropertyMeta("ldap_server2", "ldapServer2", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20000, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [""], []),
            "ldap_server3": MoPropertyMeta("ldap_server3", "ldapServer3", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40000, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [""], []),
            "ldap_server4": MoPropertyMeta("ldap_server4", "ldapServer4", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80000, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [""], []),
            "ldap_server5": MoPropertyMeta("ldap_server5", "ldapServer5", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100000, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [""], []),
            "ldap_server6": MoPropertyMeta("ldap_server6", "ldapServer6", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200000, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [""], []),
            "ldap_server_port1": MoPropertyMeta("ldap_server_port1", "ldapServerPort1", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400000, None, None, None, [], ["1-65535"]),
            "ldap_server_port2": MoPropertyMeta("ldap_server_port2", "ldapServerPort2", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800000, None, None, None, [], ["1-65535"]),
            "ldap_server_port3": MoPropertyMeta("ldap_server_port3", "ldapServerPort3", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000000, None, None, None, [], ["1-65535"]),
            "ldap_server_port4": MoPropertyMeta("ldap_server_port4", "ldapServerPort4", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000000, None, None, None, [], ["1-65535"]),
            "ldap_server_port5": MoPropertyMeta("ldap_server_port5", "ldapServerPort5", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000000, None, None, None, [], ["1-65535"]),
            "ldap_server_port6": MoPropertyMeta("ldap_server_port6", "ldapServerPort6", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000000, None, None, None, [], ["1-65535"]),
            "locate_directory_using_dns": MoPropertyMeta("locate_directory_using_dns", "locateDirectoryUsingDNS", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000000, None, None, None, ["No", "Yes", "no", "yes"], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20000000, None, None, r"""[\S+]{0,254}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40000000, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80000000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100000000, None, None, None, [], ["0-180", "0-1800"]),
            "user_search_precedence": MoPropertyMeta("user_search_precedence", "userSearchPrecedence", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x200000000, None, None, None, ["ldap-user-db", "local-user-db"], []),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "attribute": "attribute", 
            "basedn": "basedn", 
            "bindDn": "bind_dn", 
            "bindMethod": "bind_method", 
            "dn": "dn", 
            "dnsDomainSource": "dns_domain_source", 
            "dnsSearchDomain": "dns_search_domain", 
            "dnsSearchForest": "dns_search_forest", 
            "domain": "domain", 
            "encryption": "encryption", 
            "filter": "filter", 
            "groupAttribute": "group_attribute", 
            "groupAuth": "group_auth", 
            "groupNestedSearch": "group_nested_search", 
            "ldapServer1": "ldap_server1", 
            "ldapServer2": "ldap_server2", 
            "ldapServer3": "ldap_server3", 
            "ldapServer4": "ldap_server4", 
            "ldapServer5": "ldap_server5", 
            "ldapServer6": "ldap_server6", 
            "ldapServerPort1": "ldap_server_port1", 
            "ldapServerPort2": "ldap_server_port2", 
            "ldapServerPort3": "ldap_server_port3", 
            "ldapServerPort4": "ldap_server_port4", 
            "ldapServerPort5": "ldap_server_port5", 
            "ldapServerPort6": "ldap_server_port6", 
            "locateDirectoryUsingDNS": "locate_directory_using_dns", 
            "password": "password", 
            "rn": "rn", 
            "status": "status", 
            "timeout": "timeout", 
            "userSearchPrecedence": "user_search_precedence", 
        },

        "modular": {
            "adminState": "admin_state", 
            "attribute": "attribute", 
            "basedn": "basedn", 
            "bindDn": "bind_dn", 
            "bindMethod": "bind_method", 
            "dn": "dn", 
            "dnsDomainSource": "dns_domain_source", 
            "dnsSearchDomain": "dns_search_domain", 
            "dnsSearchForest": "dns_search_forest", 
            "domain": "domain", 
            "encryption": "encryption", 
            "filter": "filter", 
            "groupAttribute": "group_attribute", 
            "groupAuth": "group_auth", 
            "groupNestedSearch": "group_nested_search", 
            "ldapServer1": "ldap_server1", 
            "ldapServer2": "ldap_server2", 
            "ldapServer3": "ldap_server3", 
            "ldapServer4": "ldap_server4", 
            "ldapServer5": "ldap_server5", 
            "ldapServer6": "ldap_server6", 
            "ldapServerPort1": "ldap_server_port1", 
            "ldapServerPort2": "ldap_server_port2", 
            "ldapServerPort3": "ldap_server_port3", 
            "ldapServerPort4": "ldap_server_port4", 
            "ldapServerPort5": "ldap_server_port5", 
            "ldapServerPort6": "ldap_server_port6", 
            "locateDirectoryUsingDNS": "locate_directory_using_dns", 
            "password": "password", 
            "rn": "rn", 
            "status": "status", 
            "timeout": "timeout", 
            "userSearchPrecedence": "user_search_precedence", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.attribute = None
        self.basedn = None
        self.bind_dn = None
        self.bind_method = None
        self.dns_domain_source = None
        self.dns_search_domain = None
        self.dns_search_forest = None
        self.domain = None
        self.encryption = None
        self.filter = None
        self.group_attribute = None
        self.group_auth = None
        self.group_nested_search = None
        self.ldap_server1 = None
        self.ldap_server2 = None
        self.ldap_server3 = None
        self.ldap_server4 = None
        self.ldap_server5 = None
        self.ldap_server6 = None
        self.ldap_server_port1 = None
        self.ldap_server_port2 = None
        self.ldap_server_port3 = None
        self.ldap_server_port4 = None
        self.ldap_server_port5 = None
        self.ldap_server_port6 = None
        self.locate_directory_using_dns = None
        self.password = None
        self.status = None
        self.timeout = None
        self.user_search_precedence = None

        ManagedObject.__init__(self, "AaaLdap", parent_mo_or_dn, **kwargs)

