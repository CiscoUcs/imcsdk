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
# See the License for  the specific language governing permissions and
# limitations under the License.

"""
This module implements all the ssh related functionality
"""

from imcsdk.apis.v2.utils import _get_mo
from imcsdk.imcexception import ImcOperationError

import logging

log = logging.getLogger('imc')
_SSH_DN = 'sys/svc-ext/ssh-svc'


def ssh_enable(handle, port=None, session_timeout=None, **kwargs):
    """
       Enables ssh Policy and sets the given properties

       Args:
           handle (ImcHandle)
           port (int): Port number used by SSH
           session_timeout (int): No of seconds to wait before the system considers a SSH request to have timed out
           kwargs: key-value paired arguments for future use

       Returns:
           CommSsh object

       Raises:
           ImcOperationError if the CommSsh Mo is not present

       Example:
           ssh_enable(handle, 22, 120)
       """
    from imcsdk.mometa.comm.CommSsh import CommSshConsts

    mo = _get_mo(handle, dn=_SSH_DN)
    params = {
        'admin_state': CommSshConsts.ADMIN_STATE_ENABLED,
        'port': str(port) if port else None,
        'session_timeout': str(session_timeout) if session_timeout else None
    }
    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return mo


def ssh_disable(handle):
    """
    Disables ssh.

    Args:
        handle (ImcHandle)

    Returns:
        CommSsh: Managed Object

    Raises:
        ValueError: If CommSsh Mo is not present

    Example:
        ssh_disable(handle)
    """
    from imcsdk.mometa.comm.CommSsh import CommSshConsts

    mo = _get_mo(handle, dn=_SSH_DN)
    mo.admin_state = CommSshConsts.ADMIN_STATE_DISABLED
    handle.set_mo(mo)
    return mo


def ssh_exists(handle, **kwargs):
    """
    Checks if ssh is enabled or not

    Args:
        handle (ImcHandle)
        kwargs: Key-Value paired arguments relevant to CommSsh object

    Returns:
        True/false, CommSsh MO/None

    Example:
        ssh_exists(handle)
    """
    from imcsdk.mometa.comm.CommSsh import CommSshConsts

    try:
        mo = _get_mo(handle, dn=_SSH_DN)
    except:
        return False, None

    kwargs['admin_state'] = CommSshConsts.ADMIN_STATE_ENABLED
    return mo.check_prop_match(**kwargs), mo

