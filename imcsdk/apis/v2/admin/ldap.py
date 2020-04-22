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
from imcsdk.imcexception import ImcOperationErrorDetail
from imcsdk.imccoreutils import process_conf_mos_response
from imcsdk.imccoreutils import ConfigConfMosConstants as ccmconst
from imcsdk.imccoreutils import sanitize_message
from imcsdk.apis.v2.utils import _get_mo, _is_valid_arg, _is_invalid_value,\
    _validate_api_prop
from imcsdk.mometa.aaa.AaaLdapRoleGroup import AaaLdapRoleGroup

log = logging.getLogger('imc')

_LDAP_SERVERS = ['ldap_server1', 'ldap_server2', 'ldap_server3',
                 'ldap_server4', 'ldap_server5', 'ldap_server6']
_LDAP_SERVER_PORTS = ['ldap_server_port1', 'ldap_server_port2',
                      'ldap_server_port3', 'ldap_server_port4',
                      'ldap_server_port5', 'ldap_server_port6']
LDAP_DN = "sys/ldap-ext"


def _prepare_ldap_servers(ldap_servers):
    if len(ldap_servers) > len(_LDAP_SERVERS):
        raise ImcOperationError("Configure LDAP", "Cannot configure more than"
                                "%d servers" % len(_LDAP_SERVERS))
    servers = {}
    ports = {}
    for server in ldap_servers:
        if 'id' not in server:
            raise ImcOperationError("Enable LDAP",
                                    "Provide 'id'.")
        id = server['id']
        if id == 0 or id > 6:
            raise ImcOperationError("Enable LDAP",
                                    "Provide valid 'id' (1-6).")
        id = str(id)
        if 'ip' in server:
            servers['ldap_server' + id] = server['ip']
        if 'port' in server:
            ports['ldap_server_port' + id] = str(server['port'])

    return servers, ports


def _set_ldap_servers(mo, ldap_servers):
    servers, ports = _prepare_ldap_servers(ldap_servers)
    mo.set_prop_multiple(**servers)
    mo.set_prop_multiple(**ports)


def ldap_enable(handle,
                basedn=None,
                domain=None,
                encryption=None,
                timeout=None,
                user_search_precedence=None,
                bind_method=None,
                bind_dn=None,
                change_password=False,
                password=None,
                filter=None,
                group_attribute=None,
                attribute=None,
                group_nested_search=None,
                group_auth=None,
                ldap_servers=[],
                locate_directory_using_dns=None,
                dns_domain_source=None,
                dns_search_domain=None,
                dns_search_forest=None,
                **kwargs):
    """
    Configures LDAP

    Args:
        handle (ImcHandle)
        basedn (str): Represents the Base Distinguished Name. Describes where
            to load users and groups from. It must be in the 'dc=domain,dc=com'
            format for Active Directory servers.
        domain (str): The domain that all users must be in.
        encryption (str): "Disabled", "Enabled", "disabled", "enabled"
        timeout (int): [0-180] The number of seconds the Cisco IMC waits until
            the LDAP search operation times out.
        user_search_precedence (str): ['local-user-db', 'ldap-user-db'].
            Preference to search in local user db versus ldap user db
        bind_method (str): ['login-credentials', 'configured-credentials',
            'anonymous']
        bind_dn (str): Represents the distinguished name (DN) of the user. This
            field is applicable only for bind_method='configured-credentials'
        change_password (bool): True if you want to change the user password.
        password (str): The password of the user. This field is applicable only
            for bind_method='configured-credentials'
        filter (str): Represents the filter attribute in the schema on the LDAP
            server.
        attribute (str): Represents the role and locale information. Should
            match the attribute specified on the LDAP server.
        group_attribute (str): Represents the group attribute in the schema on
            the LDAP server.
        group_nested_search (int): Represents the depth of a nested group
            search
        group_auth (str): "disabled" or "enabled". Enables authentication at
            the group level for LDAP users that are not found in the local user
            database.
        ldap_servers (list): Represents the list of preconfigured LDAP server.
                             List of dictionaries in the format:-
                             [{"id": 1, "ip": "192.168.1.1", "port": 300},
                              {"id": 2, "ip": "192.168.1.2", "port": 400}]
        locate_directory_using_dns (str): "yes" or "no"
        dns_domain_source (str): Represents the method to obtain domain name.
            ['extracted-domain', 'configured-domain',
            'extracted-configured-domain']
        dns_search_domain: Domain name to be used for DNS query. Disabled when
            domain_name_source='extracted-domain'
        dns_search_forest: Forest name to used for DNS query. Disabled when
            domain_name_source='extracted-domain'
        kwargs: Key-Value paired arguments. Reserved for future use

    Returns:
        AaaLdap object

    Raises:
        ImcOperationError when AaaLdap object doesn't exist

    Examples:
        ldap_configure(handle,
                       basedn='DC=LAB,DC=cisco,DC=com',
                       domain='LAB.cisco.com',
                       timeout=20, group_auth='enabled',
                       bind_dn='CN=administrator,CN=Users,DC=LAB,DC=cisco,
                       DC=com', password='abcdefg', ldap_servers=ldap_servers)
    """

    mo = _get_mo(handle, dn=LDAP_DN)

    params = {
        'admin_state': 'enabled',
        'basedn': basedn,
        'domain': domain,
        'encryption': encryption,
        'timeout': str(timeout) if timeout is not None else None,
        'user_search_precedence': user_search_precedence,
        'bind_method': bind_method,
        'bind_dn': bind_dn,
        'password': password if change_password else None,
        'filter': filter,
        'attribute': attribute,
        'group_attribute': group_attribute,
        'group_nested_search':
            str(group_nested_search) if group_nested_search else None,
        'group_auth': group_auth,
        'locate_directory_using_dns': locate_directory_using_dns,
        'dns_domain_source': dns_domain_source,
        'dns_search_domain': None if dns_search_domain == "" else dns_search_domain, #IMC XML API issue : CSCvg92190
        'dns_search_forest': None if dns_search_forest == "" else dns_search_forest
        }

    mo.set_prop_multiple(**params)

    if ldap_servers:
        _set_ldap_servers(mo, ldap_servers)

    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return mo


def _check_match(prop1, prop2):
    if _is_invalid_value(prop1) and _is_invalid_value(prop2):
        return None
    return prop1 == prop2


def _check_ldap_server_match(ldap_mo, ldap_servers):
    servers, ports = _prepare_ldap_servers(ldap_servers)

    for server in servers:
        if servers[server] != getattr(ldap_mo, server):
            return False

    for port in ports:
        if ports[port] != getattr(ldap_mo, port):
            return False

    return True


def ldap_exists(handle, change_password=False, **kwargs):
    """
    Checks if the specified LDAP settings are already applied

    Args:
        handle (ImcHandle)
        kwargs: Key-Value paired arguments

    Returns:
        (True, AaaLdap) if settings match, else (False, None)

    Examples:
        match, mo = ldap_exists(
                    handle, enabled=True,
                    basedn='DC=LAB,DC=cisco,DC=com',
                    domain='LAB.cisco.com',
                    timeout=20, group_auth=True,
                    bind_dn='CN=administrator,CN=Users,DC=LAB,DC=cisco,DC=com',
                    password='abcdefg', ldap_servers=ldap_servers)
    """

    mo = _get_mo(handle, dn=LDAP_DN)
    if mo is None:
        return False, None

    if _is_valid_arg('ldap_servers', kwargs):
        if not _check_ldap_server_match(mo, kwargs.pop('ldap_servers')):
            return False, mo

    if 'password' in kwargs and not change_password:
        kwargs.pop('password', None)

    if 'dns_search_domain' in kwargs and kwargs['dns_search_domain'] == "":
        kwargs.pop('dns_search_domain', None)

    if 'dns_search_forest' in kwargs and kwargs['dns_search_forest'] == "":
        kwargs.pop('dns_search_forest', None)

    kwargs['admin_state'] = 'enabled'
    if not mo.check_prop_match(**kwargs):
        return False, mo

    return True, mo


def ldap_disable(handle):
    """
    Disables the ldap settings

    Args:
        handle (ImcHandle)

    Returns:
        AaaLdap Managed Object

    Examples:
        ldap_disable(handle)
    """

    mo = _get_mo(handle, dn=LDAP_DN)
    mo.admin_state = "disabled"
    handle.set_mo(mo)
    return mo


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

    raise ImcOperationError("LDAP role group create",
                            "No free role group available")


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


    Returns:
        AaaLdapRoleGroup object

    Examples:
        ldap_role_group_create(handle, domain='abcd.pqrs.com', name='abcd',
                               role='user')
    """

    match, mo = ldap_role_group_exists(handle, domain=domain, name=name,
                                       role=role)
    if match:
        log.info("LDAP Role Group with domain:%s name:%s exists" % (domain,
                                                                    name))
        return mo

    if mo is None:
        free_id = _get_free_ldap_role_group_id(handle)
        mo = AaaLdapRoleGroup(parent_mo_or_dn=LDAP_DN, id=free_id)

    mo.domain = domain
    mo.name = name
    mo.role = role
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return mo


def ldap_role_group_get(handle, domain, name):
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


def ldap_role_group_exists(handle, domain, name, **kwargs):
    """
    Checks if the ldap group exists with the specified settings

    Args:
        handle (ImcHandle)
        domain (str): The LDAP server domain the group resides in.
        name (str): The name of the group in the LDAP server database.
        kwargs: Key-Value paired arguments for future use

    Returns:
        (True, AaaLdapRoleGroup) if match found, else (False, None)

    Examples:
        ldap_role_group_exists(handle, domain='abcd.pqrs.com', name='abcd',
                               role='user')
    """
    mo = ldap_role_group_get(handle, domain=domain, name=name)
    if not mo:
        return False, None

    if not mo.check_prop_match(**kwargs):
        return False, mo

    return True, mo


def ldap_role_group_delete(handle, domain, name):
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

    mo = ldap_role_group_get(handle, domain=domain, name=name)
    if mo is None:
        raise ImcOperationError("Delete LDAP Role Group",
                                "Role Group Not found")

    mo.admin_action = 'clear'
    handle.set_mo(mo)


def ldap_role_group_create_all(handle, groups=None):
    """
    Creates an LDAP role groups.
    Note: This will overwrite the exisiting role groups.

    Args:
        handle (ImcHandle)
        groups (list of LDAP group dict)
            keys:
            domain (str): The LDAP server domain the group resides in.
            name (str): The name of the group in the LDAP server database.
            role (str): The role assigned to all users in this LDAP server
                        group.
                        ['read-only', 'user', 'admin']
            example:
             [{'domain': 'abcd.pqrs.com',
               'name': 'abcd',
               'role': 'user'}
             ]

    Returns:
        List of AaaLdapRoleGroup object

    Examples:
        ldap_role_group_create_all(handle,
                                   groups= [
                                    {'domain': 'abcd.pqrs.com',
                                     'name': 'abcd',
                                     'role': 'user'}])
    """
    api = 'ldap_role_group_create_all'

    dn_to_group_dict = {}
    domain_name_str_list = []
    mos = []
    id = 0

    if len(groups) > 28:
        raise ImcOperationError(api, "Maximum allowed LDAP groups are 28.")

    for group in groups:
        domain = group.get('domain', None)
        name = group.get('name', None)
        role = group.get('role', 'read-only')

        domain = domain.strip() if domain else None
        name = name.strip() if name else None
        role = role.strip() if role else None

        _validate_api_prop('domain', domain, api)
        _validate_api_prop('name', name, api)
        _validate_api_prop('role', role, api,
                           True, ['read-only', 'user', 'admin'])

        domain_name_str = domain + "_" + name
        if domain_name_str in domain_name_str_list:
            raise ImcOperationError(
                api,
                "LDAP Role Group with domain:%s name:%s already exists." % (
                    domain, name))
        domain_name_str_list.append(domain_name_str)

        params = {
            'domain': domain,
            'name': name,
            'role': role
        }

        id += 1
        mo = AaaLdapRoleGroup(parent_mo_or_dn=LDAP_DN, id=str(id))
        mo.set_prop_multiple(**params)
        mos.append(mo)

        dn_to_group_dict[mo.dn] = mo.name

    ret = []
    response = handle.set_mos(mos)
    if response:
        ret = process_conf_mos_response(response, api, False,
                                        "Create LDAP groups failed",
                                        ldap_role_group_callback,
                                        dn_to_group_dict)

        if len(ret) != 0:
            error_msg = 'Create LDAP groups failed:\n'
            for item in ret:
                object = item["Object"]
                error = item["Error"]
                error = sanitize_message(error)
                error_msg += object + ": " + error + "\n"

            raise ImcOperationErrorDetail(api, error_msg, ret)

    results = {}
    results["changed"] = True
    results["msg"] = ""
    results["msg_params"] = ret

    return results


def ldap_role_group_callback(dn, dn_to_group_dict):
        return dn_to_group_dict.get(dn, "Unknown LDAP Role Group:" + dn)


def ldap_role_group_delete_all(handle):
    """
    Delete all the ldap role groups

    Args:
        handle (ImcHandle)

    Returns:
        None

    Examples:
        ldap_role_group_delete_all(handle)
    """

    api = 'ldap_role_group_delete_all'
    dn_to_group_dict = {}
    mos = []

    groups = handle.query_classid('AaaLdapRoleGroup')
    for group in groups:
        if not group.name and not group.domain:
            continue
        group.admin_action = 'clear'
        mos.append(group)
        dn_to_group_dict[group.dn] = group.name

    ret = []
    response = handle.set_mos(mos)
    if response:
        ret = process_conf_mos_response(response, api, False,
                                        "Delete LDAP groups failed",
                                        ldap_role_group_callback,
                                        dn_to_group_dict)

        if len(ret) != 0:
            error_msg = 'Delete LDAP groups failed:\n'
            for item in ret:
                object = item["Object"]
                error = item["Error"]
                error = sanitize_message(error)
                error_msg += object + ": " + error + "\n"

            raise ImcOperationErrorDetail(api, error_msg, ret)

    results = {}
    results["changed"] = True
    results["msg"] = ""
    results["msg_params"] = ret

    return results


def ldap_role_group_exists_any(handle):
    """
    Checks if any ldap role group exists

    Args:
        handle (ImcHandle)

    Returns:
        None

    Examples:
        ldap_role_group_delete_all(handle)
    """

    mos = handle.query_classid('AaaLdapRoleGroup')
    for mo in mos:
        if mo.name and mo.domain:
            return True

    return False


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
    return mo


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
    return mo


def ldap_certificate_management_exists(handle):
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
    mo = _get_mo(handle,
                 dn='sys/ldap-ext/ldap-ca-cert-mgmt/ldap-ca-cert-download')
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
    mo = _get_mo(handle,
                 dn='sys/ldap-ext/ldap-ca-cert-mgmt/ldap-ca-cert-export')
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
