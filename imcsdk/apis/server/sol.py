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
This module implements all the sol related config
"""

from imcsdk.imcexception import ImcOperationError
from imcsdk.imccoreutils import get_server_dn
from imcsdk.mometa.sol.SolIf import SolIfConsts


def sol_get(handle, server_id=1, caller="sol_get"):
    parent_dn = get_server_dn(handle, server_id)
    dn = parent_dn + "/sol-if"
    mo = handle.query_dn(dn)
    if mo is None:
        raise ImcOperationError(caller,
                                "SOL '%s' doesn't exist." % dn)
    return mo


def sol_enable(handle, speed=None, comport=None, ssh_port=None, server_id=1,
               **kwargs):
    """
    This method will setup serial over lan connection

    Args:
        handle (ImcHandle)
        speed (int): 9600, 19200, 38400, 57600, 115200
        comport (string): "com0", "com1"
        ssh_port (int): port for ssh
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        SolIf object
    """

    mo = sol_get(handle, server_id=server_id, caller="sol_enable")
    params = {
        "admin_state": SolIfConsts.ADMIN_STATE_ENABLE,
        "speed": str(speed) if speed else None,
        "comport": comport,
        "ssh_port": str(ssh_port) if ssh_port else None,
    }

    mo.set_prop_multiple(**kwargs)
    mo.set_prop_multiple(**params)
    handle.set_mo(mo)
    return mo


def sol_exists(handle, server_id=1, **kwargs):
    try:
        mo = sol_get(handle, server_id=server_id, caller="sol_enable")
    except ImcOperationError:
        return (False, None)

    kwargs['admin_state'] = SolIfConsts.ADMIN_STATE_ENABLE

    mo_exists = mo.check_prop_match(**kwargs)
    return (mo_exists, mo if mo_exists else None)


def sol_disable(handle, server_id=1):
    """
    This method will disable Serial over Lan connection

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        None
    """

    mo = sol_get(handle, server_id=server_id, caller="sol_enable")
    mo.admin_state = SolIfConsts.ADMIN_STATE_DISABLE
    handle.set_mo(mo)
    return mo
