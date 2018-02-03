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
This module implements the APIs for IP Blocking and IP Filtering
"""
import logging
from imcsdk.mometa.ip.IpBlocking import IpBlocking
from imcsdk.mometa.ip.IpFiltering import IpFiltering, IpFilteringConsts
from imcsdk.apis.utils import _get_mo, _is_valid_arg, _is_invalid_value
from imcsdk.imccoreutils import get_server_dn, IMC_PLATFORM
from imcsdk.imcexception import ImcOperationError

log = logging.getLogger('imc')


def _get_mgmt_if_dn(handle, id=1):
    from imcsdk.mometa.mgmt.MgmtIf import MgmtIf

    if handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        parent_dn = get_server_dn(handle) + '/mgmt'
    elif handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        parent_dn = 'sys/chassis-1'

    mo = MgmtIf(parent_mo_or_dn=parent_dn)
    return mo.dn


def ip_blocking_enable(handle, fail_count='5', fail_window='60',
                       penalty_time='300', **kwargs):
    """
    Enables IP Blocking

    Args:
        handle (ImcHandle)
        fail_count (str): Number of times a user can attempt to log in
                          unsuccessfully, before the system locks that user out
                          Range [3-10] attempts
        fail_window (str): Length of time, in seconds, in which the
                           unsuccessful login attempts must occur in order
                           for the user to be locked out.
                           Range [60-120] seconds
        penalty_time (str): The number of seconds the user remains locked out.
                            Range [300-900] seconds
        kwargs: Key-Value paired arguments for future use

    Returns:
        IpBlocking object

    Examples:
        ip_blocking_enable(handle, fail_count='6',
                           fail_window='120', penalty_time='800')
    """

    mo = IpBlocking(parent_mo_or_dn=_get_mgmt_if_dn(handle))

    params = {
        'enable': 'yes',
        'fail_count': str(fail_count),
        'fail_window': str(fail_window),
        'penalty_time': str(penalty_time)
    }
    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def ip_blocking_disable(handle):
    """
    Disables IP Blocking

    Args:
        handle (ImcHandle)

    Returns:
        None

    Examples:
        ip_blocking_disable(handle)
    """
    mo = IpBlocking(parent_mo_or_dn=_get_mgmt_if_dn(handle))
    mo.enable = 'no'
    handle.set_mo(mo)


def is_ip_blocking_enabled(handle):
    """
    Checks if IP Blocking is enabled

    Args:
        handle (ImcHandle)

    Returns:
        bool

    Examples:
        is_ip_blocking_enabled(handle)
    """
    mo = IpBlocking(parent_mo_or_dn=_get_mgmt_if_dn(handle))
    mo = handle.query_dn(mo.dn)
    return mo.enable.lower() in ['yes', 'true']


def ip_blocking_exists(handle, **kwargs):
    """
    Checks if IP blocking settings match according to the parameters specified.

    Args:
        handle (ImcHandle)
        kwargs: Key-Value paired arguments relevant to IpBlocking object

    Returns:
        (True, IpBlocking object) if exists, else (False, None)

    Examples:
        ip_blocking_exists(handle, fail_count='6',
                           fail_window='120', penalty_time='800')
    """
    mo = IpBlocking(parent_mo_or_dn=_get_mgmt_if_dn(handle))
    mo = _get_mo(handle, dn=mo.dn)

    if mo.check_prop_match(**kwargs):
        return (True, mo)

    return (False, None)


_IP_FILTER_LIST = ['filter1', 'filter2', 'filter3', 'filter4']


def _set_ip_filters(mo, filters):
    if len(filters) > len(_IP_FILTER_LIST):
        raise ImcOperationError("Set Ip Filters",
                                "Cannot specify more than %d filters" %
                                len(_IP_FILTER_LIST))

    params = {'filter' + str(x['id']): str(x['filter']) for x in filters}
    mo.set_prop_multiple(**params)


def ip_filtering_enable(handle, filters=[]):
    """
    Enables IP filtering with the filters specified
    Connection may drop during this activity.

    Args:
        handle (ImcHandle)
        filters (list): List of dictionaries of the format
            {'id': 1, 'filter': "10.10.10.10",
             'id': 2, 'filter': "2.2.2.2-3.3.3.3"}

    Returns:
        IpFiltering object

    Examples:
        ip_filtering_enable(handle, filters=[{"id": 1, "filter": "1.1.1.0-255.255.255.255"},
                                             {"id": 2, "filter": "2.2.2.2"}])
    """
    log.warning('Changes to IP Filtering will be applied immediately. '
                'Connectivity to Cisco IMC will be lost and a re-login is required.')
    mo = IpFiltering(parent_mo_or_dn=_get_mgmt_if_dn(handle))
    mo.enable = 'yes'
    _set_ip_filters(mo, filters)

    handle.set_mo(mo)
    # Not returning the server copy as the connection drops after the above action
    return mo


def ip_filtering_disable(handle):
    """
    Disables IP filtering

    Args:
        handle (ImcHandle)

    Returns:
        None

    Examples:
        ip_filtering_disable(handle)
    """
    mo = IpFiltering(parent_mo_or_dn=_get_mgmt_if_dn(handle))
    mo.enable = 'no'
    handle.set_mo(mo)


def is_ip_filtering_enabled(handle):
    """
    Checks if IP Filtering is enabled

    Args:
        handle (ImcHandle)

    Returns:
        bool

    Examples:
        is_ip_filtering_enabled(handle)
    """
    mo = IpFiltering(parent_mo_or_dn=_get_mgmt_if_dn(handle))
    mo = handle.query_dn(mo.dn)
    return mo.enable.lower() in ['yes', 'true']


def ip_filtering_modify(handle, filters=[]):
    """
    Modifies IP filtering with the filters specified.
    Connection may drop during this activity.

    Args:
        handle (ImcHandle)
        filters (list): List of dictionaries of the format
            [{'id': 1, 'filter': '10.10.10.10'},
             {'id': 2, 'filter': '2.2.2.2-3.3.3.3'}]

    Returns:
        IpFiltering object

    Examples:
        ip_filtering_modify(handle, filters=[{'id': 1, 'filter': '10.10.10.10'}])
    """
    log.warning('Changes to IP Filtering will be applied immediately. '
                'Connectivity to Cisco IMC will be lost and a re-login is required.')
    mo = IpFiltering(parent_mo_or_dn=_get_mgmt_if_dn(handle))
    _set_ip_filters(mo, filters)

    handle.set_mo(mo)
    # Not returning the server copy as the connection drops after the above action
    return mo


def ip_filtering_clear(handle, filter_id=''):
    """
    Clears the IP filters specified by the input.
    Connection may drop during this activity.

    Args:
        handle (ImcHandle)
        filter_id (str): String representing the filter id

    Returns:
        IpFiltering object

    Examples:
        ip_filtering_clear(handle, filter_id='3')
        ip_filtering_clear(handle, filter_id='all')
    """
    log.warning('Changes to IP Filtering will be applied immediately. '
                'Connectivity to Cisco IMC maybe lost based on the filter being cleared')
    mo = IpFiltering(parent_mo_or_dn=_get_mgmt_if_dn(handle))

    if filter_id == 'all':
        mo.admin_action = IpFilteringConsts.ADMIN_ACTION_CLEAR_ALL
        handle.set_mo(mo)
        # Not returning the server copy as the connection drops after the above action
        return mo

    if not filter_id.isdigit():
        raise ImcOperationError("Clear Ip Filter",
                                "Filter-id must be a digit(1-%d) or 'all'" %
                                len(_IP_FILTER_LIST))

    if int(filter_id) > len(_IP_FILTER_LIST):
        raise ImcOperationError("Clear Ip Filter",
                                "Filter-id cannot be more than %d" %
                                len(_IP_FILTER_LIST))

    mo.admin_action = 'clearFilter' + filter_id
    handle.set_mo(mo)
    # Not returning the server copy as the connection drops after the above action
    return mo


def _check_ip_filter_match(ip_mo, mo):
    for prop in _IP_FILTER_LIST:
        configured_value = getattr(ip_mo, prop)
        in_value = getattr(mo, prop)
        if _is_invalid_value(configured_value) and \
                _is_invalid_value(in_value):
            continue
        if configured_value != in_value:
            return False

    return True


def ip_filtering_exists(handle, **kwargs):
    """
    Checks if IP filtering settings match according to the parameters specified.

    Args:
        Args:
        handle (ImcHandle)
        kwargs: Key-Value paired arguments relevant to IpFiltering object

    Returns:
        (True, IpFiltering object) if exists, else (False, None)

    Examples:
        ip_filtering_exists(handle, enable='yes',
                            filters=[{"id": 1, "filter": "1.1.1.0-255.255.255.255"},
                                     {"id": 2, "filter": "2.2.2.2"}])
    """
    ip_mo = IpFiltering(parent_mo_or_dn=_get_mgmt_if_dn(handle))
    ip_mo = handle.query_dn(ip_mo.dn)

    if _is_valid_arg('enable', kwargs):
        if ip_mo.enable.lower() != kwargs.get('enable').lower():
            return False, None

    if _is_valid_arg('filters', kwargs):
        mo = IpFiltering(parent_mo_or_dn=_get_mgmt_if_dn(handle))
        _set_ip_filters(mo, kwargs.get('filters'))
        if not _check_ip_filter_match(ip_mo, mo):
            return False, None

    return True, ip_mo
