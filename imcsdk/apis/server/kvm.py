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
This module implements all the kvm and sol related samples
"""

import re

from imcsdk.mometa.comm.CommKvm import CommKvm
from imcsdk.apis.admin.ipmi import _get_comm_mo_dn

CIFS_URI_PATTERN = re.compile('^//\d+\.\d+\.\d+\.\d+\/')
NFS_URI_PATTERN = re.compile('^\d+\.\d+\.\d+\.\d+\:\/')


def kvm_enable(handle, total_sessions=None, port=None, encryption_state=None,
               local_video_state=None, server_id=1):
    """
    This method will setup and enable kvm console access

    Args:
        handle (ImcHandle)
        total_sessions (int): Max no. of sessions allowed (1-4)
        port (int): Port used for kvm communication
        encryption_state (str): Encrypt video information sent over kvm
        local_video_state (str): Mirror the kvm session on local monitor
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        CommKvm object

    Examples:
        kvm_setup(handle,
                  total_sessions=4,
                  port=4000,
                  encryption_state="enabled",
                  local_video_state="enabled")
    """

    kvm_mo = CommKvm(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    params = {
        "admin_state": "enabled",
        "total_sessions": str(total_sessions) if total_sessions else None,
        "port": str(port) if port else None,
        "encryption_state": encryption_state,
        "local_video_state": local_video_state,
    }

    kvm_mo.set_prop_multiple(**params)
    handle.set_mo(kvm_mo)
    return kvm_mo


def kvm_disable(handle, server_id=1):
    """
    This method will disable kvm console access

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        None
    """

    kvm_mo = CommKvm(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    kvm_mo.admin_state = "disabled"
    handle.set_mo(kvm_mo)


def kvm_exists(handle, server_id=1, **kwargs):
    """
    This method will check if kvm console access is enabled

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        None
    """

    mo = CommKvm(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    mo = handle.query_dn(mo.dn)
    if mo is None:
        return False, mo

    kwargs['admin_state'] = "enabled"

    mo_exists = mo.check_prop_match(**kwargs)
    return (mo_exists, mo if mo_exists else None)
