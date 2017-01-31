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
import os
import time
import urlparse
import re
from imcsdk.mometa.comm.CommKvm import CommKvm
from imcsdk.mometa.comm.CommVMedia import CommVMedia
from imcsdk.mometa.comm.CommVMediaMap import CommVMediaMap
from imcsdk.mometa.sol.SolIf import SolIf, SolIfConsts
from imcsdk.imcexception import ImcOperationError
from imcsdk.imccoreutils import get_server_dn
from imcsdk.apis.admin.ipmi import _get_comm_mo_dn
CIFS_URI_PATTERN = re.compile('^//\d+\.\d+\.\d+\.\d+\/')
NFS_URI_PATTERN = re.compile('^\d+\.\d+\.\d+\.\d+\:\/')


def kvm_setup(handle, max_sessions=1, port=2068,
              encrypt=False, mirror_locally=False, server_id=1):
    """
    This method will setup and enable kvm console access

    Args:
        handle (ImcHandle)
        max_sessions (int): Max no. of sessions allowed (1-4)
        port (int): Port used for kvm communication
        encrypt (bool): Encrypt video information sent over kvm
        mirror_locally (bool): Mirror the kvm session on local monitor
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        CommKvm object

    Examples:
        kvm_setup(handle,
                  max_sessions=4,
                  port=4000,
                  encrypt=True,
                  mirror_locally=False)
    """

    kvm_mo = CommKvm(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    params = {
        "admin_state": "enabled",
        "total_sessions": str(max_sessions),
        "port": str(port),
        "encryption_state": ("disabled", "enabled") [encrypt],
        "local_video_state": ("disabled", "enabled") [mirror_locally],
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


def is_kvm_enabled(handle, server_id=1):
    """
    This method will check if kvm console access is enabled

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        None
    """

    kvm_mo = CommKvm(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    kvm_mo = handle.query_dn(kvm_mo.dn)
    return(kvm_mo.admin_state.lower() == "enabled")


def _get_vmedia_mo_dn(handle, server_id=1):
    return _get_comm_mo_dn(handle, server_id) + "/vmedia-svc"


def vmedia_setup(handle, encrypt=False, low_power_usb=False, server_id=1):
    """
    This method will enable vmedia and setup the properties

    Args:
        handle (ImcHandle)
        encrypt (bool): Encrypt virtual media communications
        low_power_usb (bool): Enable low power usb
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        CommVMedia object

    Examples:
        vmedia_setup(handle, True, True)
    """

    vmedia_mo = CommVMedia(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    params = {
        "admin_state": "enabled",
        "encryption_state": ("disabled", "enabled")[encrypt],
        "low_power_usb_state": ("disabled", "enabled")[low_power_usb],
        "low_power_usb": ("disabled", "enabled")[low_power_usb],
    }

    vmedia_mo.set_prop_multiple(**params)
    handle.set_mo(vmedia_mo)
    return vmedia_mo


def vmedia_disable(handle, server_id=1):
    """
    This method will disable vmedia on the server and unmount any virtual media
        already mounted

    Args:
        handle: ImcHandle
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        None
    """

    vmedia_mo = CommVMedia(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    vmedia_mo.admin_state = "disabled"

    handle.set_mo(vmedia_mo)


def vmedia_get_existing_uri(handle, server_id=1):
    """
    This method will return list of URIs of existing mountd media
    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        List of URIs of currently mounted virtual media

    Examples:
        vmedia_get_existing_uri(handle)
    """
    # Create list of URIs of all current virtually mapped ISOs
    return [virt_media.remote_share + virt_media.remote_file for virt_media
            in handle.query_children(in_dn=_get_vmedia_mo_dn(handle, server_id))]


def vmedia_get_existing_status(handle, server_id=1):
    """
    This method will return list of status of existing mountd media
    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        List of Status of currently mounted virtual media

    Examples:
        vmedia_get_existing_status(handle)
    """
    # Create list of URIs of all current virtually mapped ISOs
    return [virt_media.mapping_status for virt_media
            in handle.query_children(in_dn=_get_vmedia_mo_dn(handle, server_id))]


def vmedia_mount_add(handle, volume_name, mount_protocol,
                     mount_options=None, remote_share=None,
                     remote_file=None, user_id="", password="", server_id=1):
    """
    This method will setup the vmedia mapping
    Args:
        handle (ImcHandle)
        volume_name (string): Name of the volume or identity of the image
        mount_protocol (string): "cifs", "nfs", "www"
        mount_options (string): Options to be passed while mounting the image
        remote_share (string): URI of the image
        remote_file (string): name of the image
        user_id (string): username
        password (string): password
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        CommVMediaMap object

    Examples:
        vmedia_mount_add(
            handle,
            volume_name="c",
            mount_protocol="www",
            mount_options="noauto", "nolock" etc.
            remote_share="http://1.1.1.1/files",
            remote_file="ubuntu-14.04.2-server-amd64.iso",
            user_id="abcd",
            password="xyz")
    """

    vmediamap_mo = CommVMediaMap(
        parent_mo_or_dn=_get_vmedia_mo_dn(handle, server_id),
        volume_name=volume_name)
    vmediamap_mo.map = mount_protocol
    if mount_options:
        vmediamap_mo.mount_options = mount_options
    vmediamap_mo.remote_share = remote_share
    vmediamap_mo.remote_file = remote_file
    vmediamap_mo.username = user_id
    vmediamap_mo.password = password

    handle.add_mo(vmediamap_mo, modify_present="True")
    return vmediamap_mo


def vmedia_mount_iso_uri(handle, uri, user_id=None, password=None,
                         timeout=60, interval=5, server_id=1):
    """
    This method will setup the vmedia mapping
    Args:
        handle (ImcHandle)
        uri (string): URI of the ISO image
        user_id (string): optional username
        password (string): optional password
        timeout (int): optional timeout to wait for ISO map status to be 'OK'
        interval (int): optional interval to query ISO status
        server_id (int): Server Id to be specified for C3260 platforms

    Raises:
        Exception if invalid protocol in URI
        Exception when the mapping doesn't reach 'OK' status

    Returns:
        True if mapping succeeded

    Examples:
        vmedia_mount_add(
            handle,
            uri="http://1.1.1.1/files/ubuntu-14.04.2-server-amd64.iso"
        )
    """

    # Verify interval not set to zero
    if interval < 1 or type(interval) is not int:
        raise ValueError("ERROR: interval must be positive integer")

    # Parse file/path from URI
    remote_file = os.path.basename(uri)
    remote_share = os.path.dirname(uri) + "/"
    mount_options = "noauto"

    # Set the Map based on the protocol
    if urlparse.urlsplit(uri).scheme == 'http':
        mount_protocol = "www"
    elif urlparse.urlsplit(uri).scheme == 'https':
        mount_protocol = "www"
    elif CIFS_URI_PATTERN.match(uri):
        mount_protocol = "cifs"
    elif NFS_URI_PATTERN.match(uri):
        mount_protocol = "nfs"
    else:
        # Raise ValueError and bail
        raise ValueError("Unsupported protocol: " +
                         urlparse.urlsplit(uri).scheme)

    # Convert no user/pass to blank strings
    if not user_id:
        user_id = ''
    if not password:
        password = ''

    # Map the ISO
    vmedia_mount_add(
        handle,
        volume_name=remote_file,
        mount_protocol=mount_protocol,
        mount_options=mount_options,
        remote_share=remote_share,
        remote_file=remote_file,
        user_id=user_id,
        password=password,
        server_id=server_id)

    # Verify correct URL was mapped
    if uri in vmedia_get_existing_uri(handle, server_id):
        # Loop until mapping moves out of 'In Progress' state
        wait_time = 0
        status_list = vmedia_get_existing_status(handle, server_id)
        while 'In Progress' in status_list:
            # Raise error if we've reached timeout
            if wait_time > timeout:
                raise ImcOperationError(
                    'Mount Virtual Media',
                    '{0}: ERROR - Mapped ISO status stuck at ' +
                    '[In Progress]'.format(handle.ip)
                )
            # Wait interval sec between checks
            time.sleep(interval)
            status_list = vmedia_get_existing_status(handle, server_id)
            wait_time += interval
        else:
            # Verify mapping transitioned to 'OK' state
            if 'OK' in status_list:
                return True
            else:
                raise ImcOperationError(
                    'Mount Virtual Media',
                    '{0}: ERROR - Mapped ISO status ' +
                    'is {1}'.format(handle.ip, status_list)
                )
    else:
        raise ImcOperationError(
            'Mount Virtual Media',
            '{0}: ERROR - ISO {1} did not get mapped.'.format(handle.ip, uri)
        )


def vmedia_mount_remove(handle, volume_name, server_id=1):
    """
    This method will remove the vmedia mapping referred to by the volume name

    Args:
        handle (ImcHandle)
        volume_name (string): Name of the volume or identity of the image
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        None

    Raises:
        Exception when the mapping is not found

    Examples:
        vmedia_mount_remove(handle, volume_name="c")
    """

    vmediamap_mo = CommVMediaMap(
        parent_mo_or_dn=_get_vmedia_mo_dn(handle, server_id),
        volume_name=volume_name)
    vmediamap_mo = handle.query_dn(dn=vmediamap_mo.dn)
    if vmediamap_mo is None:
        raise ValueError("Volume '%s' does not exist" % volume_name)

    handle.remove_mo(vmediamap_mo)


def vmedia_mount_remove_all(handle, server_id=1):
    """
    This method will remove all the vmedia mappings

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Raises:
        Exception if mapping is able to be removed

    Returns:
        True

    Examples:
        vmedia_mount_remove_all(handle)
    """

    # Get all current virtually mapped ISOs
    virt_media_maps = handle.query_children(in_dn=_get_vmedia_mo_dn(handle,
                                                                    server_id))
    # Loop over each mapped ISO
    for virt_media in virt_media_maps:
        # Remove the mapped ISO
        handle.remove_mo(virt_media)
    # Raise error if all mappings not removed
    if len(handle.query_children(in_dn="sys/svc-ext/vmedia-svc")) > 0:
        raise ImcOperationError('Remove Virtual Media',
                                '{0}: ERROR - Unable remove all virtual' +
                                'media mappings'.format(handle.ip))
    # Return True if all mappings removed
    return True


def sol_setup(handle, speed, comport, ssh_port, server_id=1):
    """
    This method will setup serial over lan connection

    Args:
        handle (ImcHandle)
        speed (string): "9600", "19200", "38400", "57600", "115200"
        comport (string): "com0", "com1"
        ssh_port (int): port for ssh
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        SolIf object
    """

    solif_mo = SolIf(parent_mo_or_dn=get_server_dn(handle, server_id))
    params = {
        "admin_state": SolIfConsts.ADMIN_STATE_ENABLE,
        "speed": str(speed),
        "comport": comport,
        "ssh_port": str(ssh_port),
    }

    solif_mo.set_prop_multiple(**params)
    handle.set_mo(solif_mo)
    return handle.query_dn(solif_mo.dn)


def sol_disable(handle, server_id=1):
    """
    This method will disable Serial over Lan connection

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        None
    """

    solif_mo = SolIf(parent_mo_or_dn=get_server_dn(handle, server_id))
    solif_mo.admin_state = SolIfConsts.ADMIN_STATE_DISABLE
    handle.set_mo(solif_mo)


def is_sol_enabled(handle, server_id=1):
    """
    This method will check if Serial over Lan connection is enabled

    Args:
        handle (ImcHandle)
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        None
    """

    solif_mo = SolIf(parent_mo_or_dn=get_server_dn(handle, server_id))
    solif_mo = handle.query_dn(solif_mo.dn)
    return solif_mo.admin_state.lower() in ["enable", "enabled"]
