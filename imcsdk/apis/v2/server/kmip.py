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
This module implements all the kmip related config
"""

from imcsdk.imcexception import ImcOperationError
from imcsdk.imccoreutils import IMC_PLATFORM


def _get_server_dn(handle, server_id="1"):
    """
    This method gives the dn for a particular rack server based on
    the type of platform

    For classic: "sys/rack-unit-1"
    For modular: "sys/chassis-1/server-<server_id>"
    """

    if handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        return "sys"
    elif handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        return "sys/chassis-1/server-" + str(server_id)
    else:
        raise ImcOperationError("Unknown platform", "type:%s detected" %
                                handle.platform)


def _get_dn_kmip_mgmt(handle, server_id=1):
    return _get_server_dn(handle, server_id) + "/kmip-mgmt"


def kmip_mgmt_get(handle, server_id=1, caller="kmip_mgmt_get"):
    parent_dn = _get_server_dn(handle, server_id)
    dn = parent_dn + "/kmip-mgmt"
    mo = handle.query_dn(dn)
    if mo is None:
        raise ImcOperationError(caller,
                                "KMIP management '%s' doesn't exist." % dn)
    return mo


def kmip_mgmt_enable(handle, server_id=1, **kwargs):
    """
    This method will enable kmip management server.

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        KmipManagement object
    """

    mo = kmip_mgmt_get(handle, server_id=server_id, caller="kmip_mgmt_enable")
    params = {
        "secure_key_management": "enabled",
    }

    mo.set_prop_multiple(**kwargs)
    mo.set_prop_multiple(**params)
    handle.set_mo(mo)
    return mo


def kmip_mgmt_exists(handle, server_id=1, **kwargs):
    try:
        mo = kmip_mgmt_get(handle, server_id=server_id, caller="sol_exists")
    except ImcOperationError:
        return (False, None)

    kwargs['secure_key_management'] = "enabled"

    mo_exists = mo.check_prop_match(**kwargs)
    return mo_exists, mo


def kmip_mgmt_disable(handle, server_id=1):
    """
    This method will disable kmip management server.

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        KmipManagement object
    """

    mo = kmip_mgmt_get(handle, server_id=server_id, caller="kmip_mgmt_disable")
    params = {
        "secure_key_management": "disabled",
    }

    mo.set_prop_multiple(**params)
    handle.set_mo(mo)
    return mo


def _get_kmip_servers(handle, server_id=1):
    kmip_mgmt = kmip_mgmt_get(handle, server_id)
    return handle.query_children(in_mo=kmip_mgmt, class_id="KmipServer")


def _get_kmip_server(handle, ip_address, server_id=1):
    kmip_servers = _get_kmip_servers(handle, server_id)
    for kmip_server in kmip_servers:
        if kmip_server.ip_address == ip_address:
            return kmip_server
    return None


def _get_free_kmip_server_id(handle, server_id=1):
    kmip_servers = _get_kmip_servers(handle, server_id)
    kmip_ids = []
    for kmip_server in kmip_servers:
        if not kmip_server.ip_address:
            kmip_ids.append(int(kmip_server.id))

    if not kmip_ids:
        raise ImcOperationError("Add KMIP Server",
                                "Max number of servers already added.")

    return str(min(kmip_ids))


def kmip_server_add(handle, ip_address, port=None, timeout=None, server_id=1):
    from imcsdk.mometa.kmip.KmipServer import KmipServer

    args = {
        "ip_address": ip_address,
        "port": str(port) if port else None,
        "timeout": str(timeout) if timeout else None
    }

    mo = _get_kmip_server(handle, ip_address, server_id)
    if not mo:
        id = _get_free_kmip_server_id(handle, server_id)
        parent_dn = _get_dn_kmip_mgmt(handle, server_id)
        mo = KmipServer(parent_mo_or_dn=parent_dn, id=id)

    mo.set_prop_multiple(**args)
    handle.set_mo(mo)
    return mo


def kmip_server_exists(handle, ip_address, server_id=1, **kwargs):
    mo = _get_kmip_server(handle, ip_address, server_id)
    if mo is None:
        return False, None

    return mo.check_prop_match(**kwargs), mo


def kmip_server_remove(handle, ip_address, server_id=1):
    from imcsdk.mometa.kmip.KmipServer import KmipServerConsts

    mo = _get_kmip_server(handle, ip_address, server_id)
    if mo is None:
        raise ImcOperationError("kmip_server_remove",
                                "KMIP server does not exist.")

    mo.admin_action = KmipServerConsts.ADMIN_ACTION_DELETE
    handle.set_mo(mo)
