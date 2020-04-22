# Copyright 2017 Cisco Systems, Inc.
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
This module implements all the services
"""
from imcsdk.imcexception import ImcOperationError, ImcValidationException
from imcsdk.imccoreutils import IMC_PLATFORM
from imcsdk.apis.v2.utils import _is_valid_arg


def _get_mgmtif_mo_dn(handle):
    """
    Internal method to get the mgmt_if dn based on the type of platform
    """
    if handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        return("sys/rack-unit-1/mgmt/if-1")
    elif handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        return("sys/chassis-1/if-1")
    else:
        raise ImcValidationException("Invalid platform detected:%s" %
                                     handle.platform)


def _get_mgmtif_mo(handle):
    """
    Internal method to get the mgmt_if mo
    """
    dn = _get_mgmtif_mo_dn(handle)
    mo = handle.query_dn(dn)
    if mo is None:
        raise ImcOperationError("common_prop_configure",
                                "%s does not exist." % dn)
    return mo


def common_prop_configure(handle, hostname=None, ddns_enable=None,
                          ddns_domain=None):
    """
    Configures networking common properties.

    Args:
        handle (ImcHandle)
        ddns_enable (string): Dynamic DNS. "yes" or "no"
        ddns_domain (string): Dynamic DNS update domain.

    Returns:
        MgmtIf object

    Raises:
        ImcOperationError

    Example:
        common_prop_configure(handle, ddns_enable="yes")
    """
    return mgmt_if_configure(
        handle,
        hostname=hostname,
        ddns_enable=ddns_enable,
        ddns_domain=ddns_domain
    )


def ipv4_configure(handle, dhcp_enable=None, ext_ip=None, ext_mask=None,
                   ext_gw=None, dns_using_dhcp=None, dns_alternate=None,
                   dns_preferred=None,
                   ):
    """
    Configures networking ipv4 properties.

    Args:
        handle (ImcHandle)
        dhcp_enable (string): Use DHCP. "yes" or "no"
        ext_ip (string):
        ext_mask (string):
        dns_using_dhcp (string): Use DHCP for DNS servers. "yes" or "no"
        dns_alternate (string):
        dns_preferred (string):

    Returns:
        MgmtIf object

    Raises:
        ImcOperationError

    Example:
        ipv4_configure(handle, dns_using_dhcp="yes")
    """
    return mgmt_if_configure(
        handle,
        dhcp_enable=dhcp_enable,
        ext_ip=ext_ip,
        ext_mask=ext_mask,
        ext_gw=ext_gw,
        dns_using_dhcp=dns_using_dhcp,
        dns_alternate=dns_alternate,
        dns_preferred=dns_preferred
    )


def ipv6_configure(handle, v6ext_enabled=None, v6dhcp_enable=None,
                   v6ext_ip=None, v6ext_gw=None, v6prefix=None,
                   v6dns_using_dhcp=None, v6dns_preferred=None,
                   v6dns_alternate=None,
                   ):
    """
    Configures networking ipv4 properties.

    Args:
        handle (ImcHandle)
        v6ext_enabled (string): Use DHCP. "yes" or "no"
        v6dhcp_enable (string): Use DHCP. "yes" or "no"
        v6ext_ip (string):
        v6ext_gw (string):
        v6prefix (int):
        v6dns_using_dhcp (string): Use DHCP for DNS servers. "yes" or "no"
        v6dns_preferred (string):
        v6dns_alternate (string):

    Returns:
        MgmtIf object

    Raises:
        ImcOperationError

    Example:
        ipv6_configure(handle, v6ext_enabled="yes")
    """
    return mgmt_if_configure(
        handle,
        v6ext_enabled=v6ext_enabled,
        v6dhcp_enable=v6dhcp_enable,
        v6ext_ip=v6ext_ip,
        v6ext_gw=v6ext_gw,
        v6prefix=str(v6prefix) if v6prefix is not None else None,
        v6dns_using_dhcp=v6dns_using_dhcp,
        v6dns_preferred=v6dns_preferred,
        v6dns_alternate=v6dns_alternate
    )


def vlan_enable(handle, vlan_id=None, vlan_priority=None):
    """
    Enables management vlan

    Args:
        handle (ImcHandle)
        vlan_id (int): VLAN Id. 1-4094
        vlan_priority (int): VLAN Priority. 0-7

    Returns:
        MgmtIf object

    Raises:
        ImcOperationError

    Example:
        vlan_enable(handle)
    """
    mo = mgmt_if_configure(
        handle,
        vlan_enable="yes",
        vlan_id=str(vlan_id) if vlan_id is not None else None,
        vlan_priority=str(vlan_priority)
        if vlan_priority is not None else None,
    )
    return mo


def vlan_exists(handle, **kwargs):
    """
    Checks if management vlan exists.

    Args:
        handle (ImcHandle)
        kwargs: key-value paired arguments

    Returns:
        True/False, MO/None

    Raises:
        ImcOperationError

    Example:
        vlan_exists(handle)
    """
    exists, mo = mgmt_if_exists(handle, **kwargs)
    if exists and mo:
        if mo.vlan_enable.lower() in ["yes", "true"]:
            return True, mo
    return False, mo


def vlan_disable(handle):
    """
    Disables management vlan

    Args:
        handle (ImcHandle)

    Returns:
        MgmtIf object

    Raises:
        ImcOperationError

    Example:
        vlan_disable(handle)
    """
    return mgmt_if_configure(handle, vlan_enable="no")


def mgmt_if_configure(handle,
                      admin_duplex=None,
                      admin_net_speed=None,
                      auto_neg=None,
                      ddns_domain=None,
                      ddns_enable=None,
                      dhcp_enable=None,
                      dns_alternate=None,
                      dns_preferred=None,
                      dns_using_dhcp=None,
                      ext_gw=None,
                      ext_ip=None,
                      ext_mask=None,
                      hostname=None,
                      nic_mode=None,
                      nic_redundancy=None,
                      port_profile=None,
                      v4_ip_addr=None,
                      v4_ip_addr_bmc1=None,
                      v4_ip_addr_bmc2=None,
                      v4_ip_addr_cmc1=None,
                      v4_ip_addr_cmc2=None,
                      v6_ip_addr=None,
                      v6_ip_addr_bmc1=None,
                      v6_ip_addr_bmc2=None,
                      v6_ip_addr_cmc1=None,
                      v6_ip_addr_cmc2=None,
                      v6dhcp_enable=None,
                      v6dns_alternate=None,
                      v6dns_preferred=None,
                      v6dns_using_dhcp=None,
                      v6ext_enabled=None,
                      v6ext_gw=None,
                      v6ext_ip=None,
                      v6prefix=None,
                      v_hostname=None,
                      vic_slot=None,
                      vlan_enable=None,
                      vlan_id=None,
                      vlan_priority=None,
                      **kwargs
                      ):
    """
    This method configures the network settings of CIMC.

    Args:
        handle(ImcHandle)
        admin_duplex(str):
        admin_net_speed(str):
        auto_neg(str):
        ddns_domain(str):
        ddns_enable(str):
        dhcp_enable(str):
        dns_alternate(str):
        dns_preferred(str):
        dns_using_dhcp(str):
        ext_gw(str):
        ext_ip(str):
        ext_mask(str):
        hostname(str):
        nic_mode(str):
        nic_redundancy(str):
        port_profile(str):
        v4_ip_addr(str):
        v4_ip_addr_bmc1(str):
        v4_ip_addr_bmc2(str):
        v4_ip_addr_cmc1(str):
        v4_ip_addr_cmc2(str):
        v6_ip_addr(str):
        v6_ip_addr_bmc1(str):
        v6_ip_addr_bmc2(str):
        v6_ip_addr_cmc1(str):
        v6_ip_addr_cmc2(str):
        v6dhcp_enable(str):
        v6dns_alternate(str):
        v6dns_preferred(str):
        v6dns_using_dhcp(str):
        v6ext_enabled(str):
        v6ext_gw(str):
        v6ext_ip(str):
        v6prefix(str):
        v_hostname(str):
        vic_slot(str):
        vlan_enable(str):
        vlan_id(str):
        vlan_priority(str):

    Returns:
        MgmtIf object

    Raises:
        ImcOperationError

    Example:
        mgmt_if_configure(handle)
    """
    mo = _get_mgmtif_mo(handle)

    args = {
        'admin_duplex': admin_duplex,
        'admin_net_speed': admin_net_speed,
        'auto_neg': auto_neg,
        'ddns_domain': ddns_domain,
        'ddns_enable': ddns_enable,
        'dhcp_enable': dhcp_enable,
        'dns_alternate': dns_alternate,
        'dns_preferred': dns_preferred,
        'dns_using_dhcp': dns_using_dhcp,
        'ext_gw': ext_gw,
        'ext_ip': ext_ip,
        'ext_mask': ext_mask,
        'hostname': hostname,
        'nic_mode': nic_mode,
        'nic_redundancy': nic_redundancy,
        'port_profile': port_profile,
        'v4_ip_addr': v4_ip_addr,
        'v4_ip_addr_bmc1': v4_ip_addr_bmc1,
        'v4_ip_addr_bmc2': v4_ip_addr_bmc2,
        'v4_ip_addr_cmc1': v4_ip_addr_cmc1,
        'v4_ip_addr_cmc2': v4_ip_addr_cmc2,
        'v6_ip_addr': v6_ip_addr,
        'v6_ip_addr_bmc1': v6_ip_addr_bmc1,
        'v6_ip_addr_bmc2': v6_ip_addr_bmc2,
        'v6_ip_addr_cmc1': v6_ip_addr_cmc1,
        'v6_ip_addr_cmc2': v6_ip_addr_cmc2,
        'v6dhcp_enable': v6dhcp_enable,
        'v6dns_alternate': v6dns_alternate,
        'v6dns_preferred': v6dns_preferred,
        'v6dns_using_dhcp': v6dns_using_dhcp,
        'v6ext_enabled': v6ext_enabled,
        'v6ext_gw': v6ext_gw,
        'v6ext_ip': v6ext_ip,
        'v6prefix': str(v6prefix) if v6prefix is not None else None,
        'v_hostname': v_hostname,
        'vic_slot': vic_slot,
        'vlan_enable': vlan_enable,
        'vlan_id': str(vlan_id) if vlan_id is not None else None,
        'vlan_priority': str(vlan_priority) if vlan_priority is not None else None,
    }

    mo.set_prop_multiple(**args)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return mo


def _match_yes_no_value(prop_name, prop_value, mo):
    _ENABLE = ['true', 'yes']

    prop_value = prop_value.lower()
    mo_prop_value = getattr(mo, prop_name).lower()

    if prop_value in _ENABLE and mo_prop_value not in _ENABLE:
        return False
    elif prop_value not in _ENABLE and mo_prop_value in _ENABLE:
        return False
    return True


def mgmt_if_exists(handle, **kwargs):

    try:
        mo = _get_mgmtif_mo(handle)
    except:
        return False, None

    ddns_enable = kwargs.pop('ddns_enable', None)
    if ddns_enable and not _match_yes_no_value('ddns_enable',
                                               ddns_enable,
                                               mo):
        return False, mo

    dhcp_enable = kwargs.pop('dhcp_enable', None)
    if dhcp_enable and not _match_yes_no_value('dhcp_enable',
                                               dhcp_enable,
                                               mo):
        return False, mo

    dns_using_dhcp = kwargs.pop('dns_using_dhcp', None)
    if dns_using_dhcp and not _match_yes_no_value('dns_using_dhcp',
                                                  dns_using_dhcp,
                                                  mo):
        return False, mo

    v6dhcp_enable = kwargs.pop('v6dhcp_enable', None)
    if v6dhcp_enable and not _match_yes_no_value('v6dhcp_enable',
                                                 v6dhcp_enable,
                                                 mo):
        return False, mo

    v6dns_using_dhcp = kwargs.pop('v6dns_using_dhcp', None)
    if v6dns_using_dhcp and not _match_yes_no_value('v6dns_using_dhcp',
                                                    v6dns_using_dhcp,
                                                    mo):
        return False, mo

    v6ext_enabled = kwargs.pop('v6ext_enabled', None)
    if v6ext_enabled and not _match_yes_no_value('v6ext_enabled',
                                                 v6ext_enabled,
                                                 mo):
        return False, mo

    vlan_enable = kwargs.pop('vlan_enable', None)
    if vlan_enable and not _match_yes_no_value('vlan_enable',
                                               vlan_enable,
                                               mo):
        return False, mo

    if 'v6prefix' in kwargs:
        kwargs['v6prefix'] = str(kwargs['v6prefix']) if kwargs['v6prefix'] is not None else None

    if 'vlan_id' in kwargs:
        kwargs['vlan_id'] = str(kwargs['vlan_id']) if kwargs['vlan_id'] is not None else None

    if 'vlan_priority' in kwargs:
        kwargs['vlan_priority'] = str(kwargs['vlan_priority']) if kwargs['vlan_priority'] is not None else None



    return mo.check_prop_match(**kwargs), mo


def ip_blocking_enable(handle, fail_count=None, fail_window=None,
                       penalty_time=None, **kwargs):
    """
    Enables IP Blocking and Configures.

    Args:
        handle (ImcHandle)
        fail_count (int): 3-10
        fail_window (int): 60-120
        penalty_time (int): 300-900

    Returns:
        IPBlocing object

    Raises:
        ImcOperationError

    Example:
        ip_blocking_enable(handle, fail_count=3)
    """
    dn = _get_mgmtif_mo_dn(handle) + "/ip-block"
    mo = handle.query_dn(dn)
    if mo is None:
        raise ImcOperationError("ip_blocking_enable",
                                "%s does not exist." % dn)

    args = {
        'enable': "yes",
        'fail_count': str(fail_count) if fail_count is not None else None,
        'fail_window': str(fail_window) if fail_count is not None else None,
        'penalty_time':
        str(penalty_time) if penalty_time is not None else None
    }

    mo.set_prop_multiple(**args)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return mo


def ip_blocking_exists(handle, **kwargs):
    """
    Checks if IP blocking is enabled.

    Args:
        handle (ImcHandle)
        kwargs: key-value paired arguments

    Returns:
        True/False, MO/None

    Raises:
        None

    Example:
        ip_blocking_exists(handle, fail_count=3)
    """
    dn = _get_mgmtif_mo_dn(handle) + "/ip-block"
    mo = handle.query_dn(dn)
    if mo is None:
        return False, None

    if mo.enable.lower() not in ["yes", "true"]:
        return False, mo

    return mo.check_prop_match(**kwargs), mo


def ip_blocking_disable(handle):
    """
    Disables IP Blocking.

    Args:
        handle (ImcHandle)

    Returns:
        IPBlocing object

    Raises:
        ImcOperationError

    Example:
        ip_blocking_disable(handle)
    """
    dn = _get_mgmtif_mo_dn(handle) + "/ip-block"
    mo = handle.query_dn(dn)
    if mo is None:
        raise ImcOperationError("ip_blocking_enable",
                                "%s does not exist." % dn)

    mo.enable = "no"
    handle.set_mo(mo)
    return mo


_IP_FILTERS_LIST = ["filter1", "filter2", "filter3", "filter4"]


def _get_ip_filters(ip_filters):
    return {"filter" + str(x["id"]): x["ip_filter"] for x in ip_filters}


def _set_ip_filters(mo, ip_filters):
    if len(ip_filters) > len(_IP_FILTERS_LIST):
        raise ImcOperationError("Set IP Filters",
                                "Cannot specify more than %d filters"
                                % len(_IP_FILTERS_LIST))
    args = _get_ip_filters(ip_filters)
    mo.set_prop_multiple(**args)


def ip_filtering_enable(handle, ip_filters=None):
    """
    Enables NTP and configures the NTP servers provided

    Args:
        handle (ImcHandle)
        ip_filters (list): List of dictionaries in the format
                            [{"id": 1, "ip_filter": "192.168.1.1"},
                             {"id": 2, "ip": "192.168.1.2-192.168.1.4"}]
                            Upto 4 ip filters can be specified.

    Returns:
        IPFiltering object

    Example:
        ip_filtering_enable(handle,
                   ip_filters = [
                   {"id": 1, "ip_filter": "192.168.1.1"},
                   {"id": 2, "ip_filter": "192.168.1.2-192.168.1.4"}]
    """
    dn = _get_mgmtif_mo_dn(handle) + "/ip-filter"
    mo = handle.query_dn(dn)
    if mo is None:
        raise ImcOperationError("ip_filtering_enable",
                                "%s does not exist." % dn)
    mo.enable = 'yes'

    _set_ip_filters(mo, ip_filters)
    handle.set_mo(mo)
    return mo


def ip_filtering_disable(handle):
    """
    Disables IP Filtering.

    Args:
        handle (ImcHandle)

    Returns:
        IPFiltering object

    Raises:
        ImcOperationError

    Example:
        ip_filtering_disable(handle)
    """
    dn = _get_mgmtif_mo_dn(handle) + "/ip-filter"
    mo = handle.query_dn(dn)
    if mo is None:
        raise ImcOperationError("ip_filtering_enable",
                                "%s does not exist." % dn)

    mo.enable = "no"
    handle.set_mo(mo)
    return mo


def ip_filtering_exists(handle, **kwargs):
    """
    Checks if the ip filtering already exists.
    Args:
        handle (ImcHandle)
        kwargs: key-value paired arguments

    Returns:
        True/False, MO/None
    """
    dn = _get_mgmtif_mo_dn(handle) + "/ip-filter"
    mo = handle.query_dn(dn)
    if mo is None:
        return False, None

    kwargs['enable'] = 'yes'

    if _is_valid_arg("ip_filters", kwargs):
        args = _get_ip_filters(kwargs['ip_filters'])
        del kwargs['ip_filters']
        kwargs.update(args)

    return mo.check_prop_match(**kwargs), mo
