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
import re
import logging

from imcsdk.mometa.comm.CommVMedia import CommVMedia
from imcsdk.mometa.comm.CommVMediaMap import CommVMediaMap
from imcsdk.imcexception import ImcOperationError
from imcsdk.apis.admin.ipmi import _get_comm_mo_dn

from six.moves import urllib

log = logging.getLogger('imc')

CIFS_URI_PATTERN = re.compile('^//\d+\.\d+\.\d+\.\d+\/')
NFS_URI_PATTERN = re.compile('^\d+\.\d+\.\d+\.\d+\:\/')


def _get_vmedia_mo_dn(handle, server_id=1):
    return _get_comm_mo_dn(handle, server_id) + "/vmedia-svc"


def vmedia_enable(handle, encryption_state=None, low_power_usb=None,
                  server_id=1):
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
        vmedia_enable(handle, True, True)
    """

    if encryption_state: encryption_state = 'enabled'
    else: encryption_state = 'disabled'

    if low_power_usb: low_power_usb = 'enabled'
    else: low_power_usb = 'disabled'

    mo = CommVMedia(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    params = {
        "admin_state": "enabled",
        "encryption_state": encryption_state,
        "low_power_usb_state": low_power_usb,
        "low_power_usb": low_power_usb,
    }

    mo.set_prop_multiple(**params)
    handle.set_mo(mo)
    return mo


def vmedia_exists(handle, server_id=1, **kwargs):
    dn = _get_vmedia_mo_dn(handle, server_id=server_id)
    mo = handle.query_dn(dn)
    if mo is None:
        return False, None

    if not (mo.low_power_usb_state or mo.low_power_usb):
        return False, None
    elif mo.low_power_usb_state is None:
        kwargs.pop('low_power_usb_state', None)
    elif mo.low_power_usb is None:
        kwargs.pop('low_power_usb', None)

    kwargs['admin_state'] = "enabled"

    if not mo.check_prop_match(**kwargs):
        return False, None

    return True, mo


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

    mo = CommVMedia(parent_mo_or_dn=_get_comm_mo_dn(handle, server_id))
    mo.admin_state = "disabled"

    handle.set_mo(mo)


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

    vmedias = handle.query_children(in_dn=_get_vmedia_mo_dn(handle, server_id))
    return [vmedia.remote_share + vmedia.remote_file for vmedia in vmedias]


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
    vmedias = handle.query_children(in_dn=_get_vmedia_mo_dn(handle, server_id))
    return [vmedia.mapping_status for vmedia in vmedias]


def vmedia_mount_get(handle, volume_name, server_id=1):
    parent_dn = _get_vmedia_mo_dn(handle, server_id)
    dn = parent_dn + "/vmmap-" + volume_name
    mo = handle.query_dn(dn)
    if mo is None:
        raise ImcOperationError("vmedia_mount_get",
                                "vmedia mount '%s' does not exist" % dn)
    return mo


def vmedia_mount_create(handle, volume_name, remote_share, remote_file,
                        map="www", mount_options="noauto", username="",
                        password="", server_id=1, timeout=60):
    """
    This method will setup the vmedia mapping
    Args:
        handle (ImcHandle)
        volume_name (string): Name of the volume or identity of the image
        map (string): "cifs", "nfs", "www"
        mount_options (string): Options to be passed while mounting the image
        remote_share (string): URI of the image
        remote_file (string): name of the image
        username (string): username
        password (string): password
        server_id (int): Server Id to be specified for C3260 platforms

    Returns:
        CommVMediaMap object

    Examples:
        vmedia_mount_add(
            handle,
            volume_name="c",
            map="www",
            mount_options="noauto", "nolock" etc.
            remote_share="http://1.1.1.1/files",
            remote_file="ubuntu-14.04.2-server-amd64.iso",
            username="abcd",
            password="xyz")
    """
    image_type = remote_file.split('.')[-1]
    vmedia_mount_remove_image(handle, image_type)

    mo = CommVMediaMap(parent_mo_or_dn=_get_vmedia_mo_dn(handle, server_id),
                       volume_name=volume_name)
    mo.map = map
    if mount_options:
        mo.mount_options = mount_options
    mo.remote_share = remote_share
    mo.remote_file = remote_file
    mo.username = username
    mo.password = password

    handle.add_mo(mo, modify_present="True")

    wait_time = 0
    interval = 10
    while wait_time < timeout:
        time.sleep(interval)
        mo = handle.query_dn(mo.dn)
        existing_mapping_status = mo.mapping_status
        if existing_mapping_status == "OK":
            return mo
        elif re.match(r"ERROR", existing_mapping_status):
            raise ImcOperationError("vmedia_mount_create",
                                    mo.mapping_status)
        wait_time += interval

    raise ImcOperationError("vmedia_mount_create",
                            "ERROR - Mapped ISO status stuck at %s" %
                            existing_mapping_status)


def vmedia_mount_exists(handle, volume_name, server_id=1, **kwargs):
    import re

    try:
        mo = vmedia_mount_get(handle, volume_name)
    except ImcOperationError:
        return False, None

    kwargs.pop('timeout', None)
    kwargs.pop('password', None)
    username = kwargs.pop('username', None)
    mount_options = kwargs.pop('mount_options', None)

    if not mo.check_prop_match(**kwargs):
        return False, None

    mo_mount_options = [x.strip() for x in mo.mount_options.split(',')]

    if mount_options:
        mount_options = [x.strip() for x in mount_options.split(',')][0]
        if mount_options not in mo_mount_options:
            return False, None

    if username and mo.map in ['cifs', 'www']:
        mo_username = re.search(r'username=(\S*?),',
                                mo.mount_options).groups()[0]
        if username != mo_username:
            return False, None

    if mo.mapping_status != 'OK':
        return False, None

    return True, mo


def vmedia_mount_iso_uri(handle, uri, volume_name=None, user_id=None,
                         password=None, timeout=60, interval=5, server_id=1):
    """
    This method will setup the vmedia mapping
    Args:
        handle (ImcHandle)
        uri (string): URI of the ISO image
        volume_name (string): optional name of volume
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
        vmedia_mount_iso_uri(
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
    if urllib.parse.urlsplit(uri).scheme == 'http':
        mount_protocol = "www"
    elif urllib.parse.urlsplit(uri).scheme == 'https':
        mount_protocol = "www"
    elif CIFS_URI_PATTERN.match(uri):
        mount_protocol = "cifs"
    elif NFS_URI_PATTERN.match(uri):
        mount_protocol = "nfs"
    else:
        # Raise ValueError and bail
        raise ValueError("Unsupported protocol: " +
                         urllib.parse.urlsplit(uri).scheme)

    # Use remote filename if no volume_name givien
    if not volume_name:
        volume_name = remote_file
    # Convert no user/pass to blank strings
    if not user_id:
        user_id = ''
    if not password:
        password = ''

    # Map the ISO
    vmedia_mount_create(handle,
                        volume_name=volume_name[:45],
                        map=mount_protocol,
                        mount_options=mount_options,
                        remote_share=remote_share,
                        remote_file=remote_file,
                        username=user_id,
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


def vmedia_mount_delete(handle, volume_name, server_id=1):
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


def vmedia_mount_remove_image(handle, image_type, server_id=1):
    """
    This method will remove the vmedia mapping of specific type

    Args:
        handle (ImcHandle)
        image_type (str): 'iso' or 'img'
        server_id (int): Server Id to be specified for C3260 platforms

    Raises:
        Exception if mapping is able to be removed

    Returns:
        True

    Examples:
        vmedia_mount_remove_image(handle, image_type='iso')
    """

    # Get all current virtually mapped ISOs
    virt_media_maps = handle.query_children(in_dn=_get_vmedia_mo_dn(handle,
                                                                    server_id))
    # Loop over each mapped ISO
    for virt_media in virt_media_maps:
        # Remove the mapped ISO
        virt_media_type = virt_media.remote_file.split('.')[-1]
        if virt_media_type == image_type:
            handle.remove_mo(virt_media)
            log.warning("Removing existing mapping '%s'" % virt_media.dn)
            break
