# Copyright 2016 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
This module implements apis to configure ldap
"""

import logging
from imcsdk.imcexception import ImcOperationError
from imcsdk.apis.utils import _get_mo, _is_valid_arg, _is_invalid_value
from imcsdk.mometa.aaa.AaaLdap import AaaLdap
from imcsdk.mometa.aaa.AaaLdapRoleGroup import AaaLdapRoleGroup

log = logging.getLogger('imc')

_LDAP_SERVERS = ['ldap_server1', 'ldap_server2', 'ldap_server3',
                 'ldap_server4', 'ldap_server5', 'ldap_server6']
_LDAP_SERVER_PORTS = ['ldap_server_port1', 'ldap_server_port2',
                      'ldap_server_port3', 'ldap_server_port4',
                      'ldap_server_port5', 'ldap_server_port6']
LDAP_DN = "sys/ldap-ext"


def _set_ldap_servers(mo, ldap_servers):
    if len(ldap_servers) > len(_LDAP_SERVERS):
        raise ImcOperationError("Configure LDAP", "Cannot configure more than"
                                "%d servers" % len(_LDAP_SERVERS))
    servers = {}
    ports = {}
    for server in ldap_servers:
        servers['ldap_server' + str(server['id'])] = server['ip']
        ports['ldap_server_port' + str(server['id'])] = str(server['port'])

    mo.set_prop_multiple(**servers)
    mo.set_prop_multiple(**ports)


def ldap_configure(handle, enabled=False, basedn=None, domain=None,
                   encryption=True, timeout=60, user_search_precedence='local-user-db',
                   bind_method='login-credentials', bind_dn=None,
                   password=None, filter='sAMAccountName',
                   attribute='CiscoAvPair', group_attribute='memberOf',
                   group_nested_search=128, group_auth=False,
                   ldap_servers=[], locate_directory_using_dns=False,
                   dns_domain_source='extracted-domain',
                   dns_search_domain=None, dns_search_forest=None, **kwargs):
    """
    Configures LDAP

    Args:
        handle (ImcHandle)
        enabled (bool)
        basedn (str): Represents the Base Distinguished Name. Describes where to load users and groups from.
                      It must be in the 'dc=domain,dc=com' format for Active Directory servers.
        domain (str): The domain that all users must be in.
        encryption (bool)
        timeout (int): [0-180] The number of seconds the Cisco IMC waits until the LDAP search operation times out.
        user_search_precedence (str): ['local-user-db', 'ldap-user-db']. Preference to search in local user db versus ldap user db
        bind_method (str): ['login-credentials', 'configured-credentials', 'anonymous']
        bind_dn (str): Represents the distinguished name (DN) of the user.
                       This field is applicable only for bind_method='configured-credentials'
        password (str): The password of the user.
                        This field is applicable only for bind_method='configured-credentials'
        filter (str): Represents the filter attribute in the schema on the LDAP server.
        attribute (str): Represents the role and locale information. Should match the attribute specified on the LDAP server.
        group_attribute (str): Represents the group attribute in the schema on the LDAP server.
        group_nested_search (int): Represents the depth of a nested group search
        group_auth (bool): Enables authentication at the group level for LDAP users that are not found in the local user database.
        ldap_servers (list): Represents the list of preconfigured LDAP server.
                             List of dictionaries in the format:-
                             [{"id": 1, "ip": "192.168.1.1", "port": 300},
                              {"id": 2, "ip": "192.168.1.2", "port": 400}]
        locate_directory_using_dns (bool):
        dns_domain_source (str): Represents the method to obtain domain name
                                 ['extracted-domain', 'configured-domain', 'extracted-configured-domain']
        dns_search_domain: Domain name to be used for DNS query. Disabled when domain_name_source='extracted-domain'
        dns_search_forest: Forest name to used for DNS query. Disabled when domain_name_source='extracted-domain'
        kwargs: Key-Value paired arguments. Reserved for future use

    Returns:
        AaaLdap object

    Raises:
        ImcOperationError when AaaLdap object doesn't exist

    Examples:
        ldap_configure(handle, enabled=True,
                       basedn='DC=LAB,DC=cisco,DC=com',
                       domain='LAB.cisco.com',
                       timeout=20, group_auth=True,
                       bind_dn='CN=administrator,CN=Users,DC=LAB,DC=cisco,DC=com',
                       password='abcdefg', ldap_servers=ldap_servers)
    """

    mo = _get_mo(handle, dn=LDAP_DN)

    params = {
        'admin_state': ('disabled', 'enabled')[enabled],
        'basedn': basedn,
        'domain': domain,
        'encryption': ('disabled', 'enabled')[encryption],
        'timeout': str(timeout),
        'user_search_precedence': user_search_precedence,
        'bind_method': bind_method,
        'bind_dn': bind_dn,
        'password': password,
        'filter': filter,
        'attribute': attribute,
        'group_attribute': group_attribute,
        'group_nested_search': str(group_nested_search),
        'group_auth': ('disabled', 'enabled')[group_auth],
        'locate_directory_using_dns': ('no', 'yes')[locate_directory_using_dns],
        'dns_domain_source': dns_domain_source,
        'dns_search_domain': dns_search_domain,
        'dns_search_forest': dns_search_forest
        }

    mo.set_prop_multiple(**params)

    if ldap_servers:
        _set_ldap_servers(mo, ldap_servers)

    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def _check_match(prop1, prop2):
    if _is_invalid_value(prop1) and _is_invalid_value(prop2):
        return None
    return prop1 == prop2


def _check_ldap_server_match(ldap_mo, ldap_servers):
    mo = AaaLdap(parent_mo_or_dn="sys")
    _set_ldap_servers(mo, ldap_servers)
    for server, port in zip(_LDAP_SERVERS, _LDAP_SERVER_PORTS):
        conf_server = getattr(ldap_mo, server)
        in_server = getattr(mo, server)

        match = _check_match(conf_server, in_server)
        # IMC assigns a default value of port even when a valid server ip is
        # not assigned. The following logic will skip checking for ports where
        # the server ip itself is not specified, but default port is set.
        if match is None:
            continue

        if not match:
            return False

        conf_port = getattr(ldap_mo, port)
        in_port = getattr(mo, port)

        if _check_match(conf_port, in_port) is False:
            return False

    return True


def _get_ldap_params(kwargs):
    params = {}
    if _is_valid_arg('enabled', kwargs):
        params['admin_state'] = ('disabled', 'enabled')[kwargs.pop('enabled')]

    if _is_valid_arg('encryption', kwargs):
        params['encryption'] = ('disabled', 'enabled')[kwargs.pop('encryption')]

    if _is_valid_arg('group_auth', kwargs):
        params['group_auth'] = ('disabled', 'enabled')[kwargs.pop('group_auth')]

    if _is_valid_arg('locate_directory_using_dns', kwargs):
        params['locate_directory_using_dns'] = ('no', 'yes')[kwargs.pop('locate_directory_using_dns')]

    if _is_valid_arg('timeout', kwargs):
        params['timeout'] = str(kwargs.pop('timeout'))

    if _is_valid_arg('group_nested_search', kwargs):
        params['group_nested_search'] = str(kwargs.pop('group_nested_search'))

    # pop the password property if it exists
    if _is_valid_arg('password', kwargs):
        kwargs.pop('password')

    return params


def ldap_settings_exist(handle, **kwargs):
    """
    Checks if the specified LDAP settings are already applied

    Args:
        handle (ImcHandle)
        kwargs: Key-Value paired arguments

    Returns:
        (True, AaaLdap) if settings match, else (False, None)

    Examples:
        match, mo = ldap_settings_exist(
                        handle, enabled=True,
                        basedn='DC=LAB,DC=cisco,DC=com',
                        domain='LAB.cisco.com',
                        timeout=20, group_auth=True,
                        bind_dn='CN=administrator,CN=Users,DC=LAB,DC=cisco,DC=com',
                        password='abcdefg', ldap_servers=ldap_servers)
    """

    mo = _get_mo(handle, dn=LDAP_DN)

    params = _get_ldap_params(kwargs)
    if not mo.check_prop_match(**params):
        return False, None

    if _is_valid_arg('ldap_servers', kwargs):
        if not _check_ldap_server_match(mo, kwargs.pop('ldap_servers')):
            return False, None

    if not mo.check_prop_match(**kwargs):
        return False, None

    return True, mo


def is_ldap_enabled(handle):
    """
    Checks if LDAP is enabled

    Args:
        handle (ImcHandle)

    Returns:
        bool

    Examples:
        is_ldap_enabled(handle)
    """

    mo = _get_mo(handle, dn=LDAP_DN)
    return mo.admin_state.lower() == "enabled"


def _get_free_ldap_role_group_id(handle):
    mos = handle.query_classid('AaaLdapRoleGroup')
    for mo in mos:
        if not mo.name and not mo.domain:
            return mo.id

    raise ImcOperationError("LDAP role group create", "No free role group available")


def ldap_role_group_create(handle, domain, name, role='read-only', **kwargs):
    """
    Creates an LDAP role group

    Args:
        handle (ImcHandle)
        domain (str): The LDAP server domain the group resides in.
        name (str): The name of the group in the LDAP server database.
        role (str): The role assigned to all users in this LDAP server group.
                    ['read-only', 'user', 'admin']
        kwargs: Key-Value paired arguments for future use

    Raises:
        ImcOperationError if LDAP is not enabled or
            LDAP group authorization is not enabled

    Returns:
        AaaLdapRoleGroup object

    Examples:
        ldap_role_group_create(handle, domain='abcd.pqrs.com', name='abcd', role='user')
    """

    ldap_mo = _get_mo(handle, dn=LDAP_DN)
    if ldap_mo.admin_state.lower() != "enabled" or ldap_mo.group_auth.lower() != "enabled":
        raise ImcOperationError("LDAP Role Group Create",
                                "Either of LDAP or LDAP group auth is not enabled")

    match, mo = ldap_role_group_exists(handle, domain=domain, name=name, role=role)
    if match:
        log.info("LDAP Role Group with domain:%s name:%s exists" % (domain, name))
        return mo

    free_id = _get_free_ldap_role_group_id(handle)
    mo = AaaLdapRoleGroup(parent_mo_or_dn=LDAP_DN, id=free_id)
    mo.domain = domain
    mo.name = name
    mo.role = role
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def ldap_role_group_get(handle, domain, name, **kwargs):
    """
    Gets the ldap role group based on domain and name

    Args:
        handle (ImcHandle)
        domain (str): The LDAP server domain the group resides in.
        name (str): The name of the group in the LDAP server database.
        kwargs: Key-Value paired arguments for future use

    Returns:
        AaaLdapRoleGroup object

    Examples:
        ldap_role_group_get(handle, domain='abcd.pqrs.com', name='abcd')
    """

    mos = handle.query_classid('AaaLdapRoleGroup')
    for mo in mos:
        if mo.domain == domain and mo.name == name:
            return mo

    return None


def ldap_role_group_exists(handle, **kwargs):
    """
    Checks if the ldap group exists with the specified settings

    Args:
        handle (ImcHandle)
        kwargs: Key-Value paired arguments for future use

    Returns:
        (True, AaaLdapRoleGroup) if match found, else (False, None)

    Examples:
        ldap_role_group_exists(handle, domain='abcd.pqrs.com', name='abcd', role='user')
    """
    domain = kwargs.get('domain')
    name = kwargs.get('name')
    mo = ldap_role_group_get(handle, domain=domain, name=name)
    if not mo:
        return False, None

    if _is_valid_arg('role', kwargs):
        if mo.role != kwargs.get('role'):
            return False, None

    return True, mo


def ldap_role_group_delete(handle, domain, name, **kwargs):
    """
    Deletes the ldap role group based on domain and name

    Args:
        handle (ImcHandle)
        domain (str): The LDAP server domain the group resides in.
        name (str): The name of the group in the LDAP server database.
        kwargs: Key-Value paired arguments for future use

    Returns:
        None

    Examples:
        ldap_role_group_delete(handle, domain='abcd.pqrs.com', name='abcd')
    """

    mo = ldap_role_group_get(handle, domain=domain, name=name, **kwargs)
    if mo is None:
        raise ImcOperationError("Delete LDAP Role Group",
                                "Role Group Not found")

    mo.admin_action = 'clear'
    handle.set_mo(mo)


def ldap_certificate_management_enable(handle):
    """
    Enables ldap certificate management

    Args:
        handle (ImcHandle)

    Returns:
        LdapCACertificateManagement object
    """
    mo = _get_mo(handle, dn="sys/ldap-ext/ldap-ca-cert-mgmt")
    mo.binding_certificate = "enabled"
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def ldap_certificate_management_disable(handle):
    """
    Disables ldap certificate management

    Args:
        handle (ImcHandle)

    Returns:
        LdapCACertificateManagement object
    """
    mo = _get_mo(handle, dn="sys/ldap-ext/ldap-ca-cert-mgmt")
    mo.binding_certificate = "disabled"
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def is_ldap_certificate_management_enabled(handle):
    """
    Checks if LDAP certificate management is enabled

    Args:
        handle (ImcHandle)

    Returns:
        bool
    """
    mo = _get_mo(handle, dn="sys/ldap-ext/ldap-ca-cert-mgmt")
    return mo.binding_certificate.lower() == "enabled"


def ldap_certificate_download(handle, remote_server, remote_file,
                              user=None, pwd=None, protocol='tftp', **kwargs):
    """
    Download LDAP CA certificate from remote server to Cisco IMC

    Args:
        handle (ImcHandle)
        remote_server (str): Remote Server IP or Hostname
        remote_file (str): Remote file path
        user (str): Username for the remote server
        pwd (str): Password for the remote server
        protocol (str): Protocol for downloading the certificate
                        ['tftp', 'ftp', 'http', 'scp', 'sftp']
        kwargs: Key-Value paired arguments for future use

    Returns:
        DownloadLdapCACertificate object

    Examples:
        ldap_certificate_download(handle, user='abcd', pwd='pqrs',
            remote_server='1.1.1.1', remote_file='/tmp/cert', protocol='scp')
    """
    mo = _get_mo(handle, dn='sys/ldap-ext/ldap-ca-cert-mgmt/ldap-ca-cert-download')
    params = {
        'user': user,
        'pwd': pwd,
        'remote_server': remote_server,
        'remote_file': remote_file,
        'protocol': protocol
    }
    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def ldap_certificate_export(handle, remote_server, remote_file,
                            user=None, pwd=None, protocol='tftp', **kwargs):
    """
    Export the LDAP CA certificate from the Cisco IMC to a remote location

    Args:
        handle (ImcHandle)
        remote_server (str): Remote Server IP or Hostname
        remote_file (str): Remote file path
        user (str): Username for the remote server
        pwd (str): Password for the remote server
        protocol (str): Protocol for downloading the certificate
                        ['tftp', 'ftp', 'http', 'scp', 'sftp']
        kwargs: Key-Value paired arguments for future use

    Returns:
        ExportLdapCACertificate object

    Examples:
        ldap_certificate_export(handle, user='abcd', pwd='pqrs',
            remote_server='1.1.1.1', remote_file='/tmp/cert', protocol='scp')
    """
    mo = _get_mo(handle, dn='sys/ldap-ext/ldap-ca-cert-mgmt/ldap-ca-cert-export')
    params = {
        'user': user,
        'pwd': pwd,
        'remote_server': remote_server,
        'remote_file': remote_file,
        'protocol': protocol
    }
    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def ldap_certificate_binding_check(handle, user=None, pwd=None, **kwargs):
    """
    Tests the LDAP CA certificate binding

    Args:
        handle (ImcHandle)
        user (str): Username for the remote server
        pwd (str): Password for the remote server

    Returns:
        LdapCACertificate object

    Examples:
        ldap_certificate_binding_check(handle, user='abcd', pwd='pqrs')
    """
    mo = _get_mo(handle, dn='sys/ldap-ext/ldap-ca-cert-mgmt/ldap-ca-cert')
    params = {
        'user': user,
        'pwd': pwd,
        'admin_action': 'test-ldap-binding'
    }
    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def ldap_certificate_delete(handle):
    """
    Deletes the LDAP CA certificate

    Args:
        handle (ImcHandle)
        user (str): Username for the remote server
        pwd (str): Password for the remote server

    Returns:
        LdapCACertificate object

    Examples:
        ldap_certificate_delete(handle)
    """
    mo = _get_mo(handle, dn='sys/ldap-ext/ldap-ca-cert-mgmt/ldap-ca-cert')
    mo.admin_action = 'delete-ca-certificate'
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)
