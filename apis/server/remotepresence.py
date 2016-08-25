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


def kvm_setup(handle, max_sessions=1, port=2068,
              encrypt=False, mirror_locally=False):
    """
    This method will setup and enable kvm console access

    Args:
        handle (ImcHandle)
        max_sessions (int): Max no. of sessions allowed (1-4)
        port (int): Port used for kvm communication
        encrypt (bool): Encrypt video information sent over kvm
        mirror_locally (bool): Mirror the kvm session on local monitor

    Returns:
        CommKvm object

    Examples:
        kvm_setup(handle,
                  max_sessions=4,
                  port=4000,
                  encrypt=True,
                  mirror_locally=False)
    """

    from imcsdk.mometa.comm.CommKvm import CommKvm

    kvm_mo = CommKvm(parent_mo_or_dn="sys/svc-ext")
    kvm_mo.admin_state = "enabled"
    kvm_mo.total_sessions = str(max_sessions)
    kvm_mo.port = str(port)
    if encrypt:
        kvm_mo.encryption_state = "enabled"
    else:
        kvm_mo.encryption_state = "disabled"
    if mirror_locally:
        kvm_mo.local_video_state = "enabled"
    else:
        kvm_mo.local_video_state = "disabled"

    handle.set_mo(kvm_mo)
    return kvm_mo


def kvm_disable(handle):
    """
    This method will disable kvm console access

    Args:
        handle (ImcHandle)

    Returns:
        None
    """

    from imcsdk.mometa.comm.CommKvm import CommKvm

    kvm_mo = CommKvm(parent_mo_or_dn="sys/svc-ext")
    kvm_mo.admin_state = "disabled"

    handle.set_mo(kvm_mo)


def vmedia_setup(handle, encrypt=False, low_power_usb=False):
    """
    This method will enable vmedia and setup the properties

    Args:
        handle (ImcHandle)
        encrypt (bool): Encrypt virtual media communications
        low_power_usb (bool): Enable low power usb

    Returns:
        CommVMedia object

    Examples:
        vmedia_setup(handle, True, True)
    """

    from imcsdk.mometa.comm.CommVMedia import CommVMedia

    vmedia_mo = CommVMedia(parent_mo_or_dn="sys/svc-ext")
    vmedia_mo.admin_state = "enabled"
    if encrypt:
        vmedia_mo.encryption_state = "enabled"
    else:
        vmedia_mo.encryption_state = "disabled"
    if low_power_usb:
        vmedia_mo.low_power_usb_state = "enabled"
    else:
        vmedia_mo.low_power_usb_state = "disabled"

    handle.set_mo(vmedia_mo)
    return vmedia_mo


def vmedia_disable(handle):
    """
    This method will disable vmedia on the server and unmount any virtual media
        already mounted

    Args:
        handle: ImcHandle

    Returns:
        None
    """

    from imcsdk.mometa.comm.CommVMedia import CommVMedia

    vmedia_mo = CommVMedia(parent_mo_or_dn="sys/svc-ext")
    vmedia_mo.admin_state = "disabled"

    handle.set_mo(vmedia_mo)


def vmedia_mount_add(handle, volume_name,
                     device_type, mount_protocol,
                     mount_options, remote_share,
                     remote_file, user_id, password):
    """
    This method will setup the vmedia mapping
    Args:
        handle (ImcHandle)
        volume_name (string): Name of the volume or identity of the image
        device_type (string): "cd", "floppy"
        mount_protocol (string): "cifs", "nfs", "www"
        mount_options (string): Options to be passed while mounting the image
        remote_share (string): URI of the image
        remote_file (string): name of the image
        user_id (string): username
        password (string): password

    Returns:
        CommVMediaMap object

    Examples:
        vmedia_mount_add(
            handle,
            volume_name="c",
            device_type="cd",
            mount_protocol="www",
            mount_options="noauto", "nolock" etc.
            remote_share="http://10.127.150.13/files",
            remote_file="ubuntu-14.04.2-server-amd64.iso",
            user_id="abcd",
            password="xyz")
    """

    from imcsdk.mometa.comm.CommVMediaMap import CommVMediaMap

    vmediamap_mo = CommVMediaMap(
        parent_mo_or_dn="sys/svc-ext/vmedia-svc",
        volume_name=volume_name)
    vmediamap_mo.drive_type = device_type
    vmediamap_mo.map = mount_protocol
    vmediamap_mo.mount_options = mount_options
    vmediamap_mo.remote_share = remote_share
    vmediamap_mo.remote_file = remote_file
    vmediamap_mo.username = user_id
    vmediamap_mo.password = password

    handle.add_mo(vmediamap_mo, modify_present="True")
    return vmediamap_mo


def vmedia_mount_remove(handle, volume_name):
    """
    This method will remove the vmedia mapping referred to by the volume name

    Args:
        handle (ImcHandle)
        volume_name (string): Name of the volume or identity of the image

    Returns:
        None

    Raises:
        Exception when the mapping is not found

    Examples:
        vmedia_mount_remove(handle, volume_name="c")
    """

    from imcsdk.mometa.comm.CommVMediaMap import CommVMediaMap

    vmediamap_mo = CommVMediaMap(
        parent_mo_or_dn="sys/svc-ext/vmedia-svc",
        volume_name=volume_name)
    vmediamap_mo = handle.query_dn(dn=vmediamap_mo.dn)
    if vmediamap_mo is None:
        raise ValueError("Volume '%s' does not exist" % volume_name)

    handle.remove_mo(vmediamap_mo)


def sol_setup(handle, speed, com_port, ssh_port):
    """
    This method will setup serial over lan connection

    Args:
        handle (ImcHandle)
        speed (string): "9600", "19200", "38400", "57600", "115200"
        com_port (string): "com0", "com1"
        ssh_port (int): port for ssh

    Returns:
        SolIf object
    """

    from imcsdk.mometa.sol.SolIf import SolIf, SolIfConsts

    solif_mo = SolIf(parent_mo_or_dn="sys/rack-unit-1")
    solif_mo.admin_state = SolIfConsts.ADMIN_STATE_ENABLE
    solif_mo.speed = speed
    solif_mo.comport = com_port
    solif_mo.ssh_port = str(ssh_port)

    handle.set_mo(solif_mo)


def sol_disable(handle):
    """
    This method will disable Serial over Lan connection

    Args:
        handle (ImcHandle)

    Returns:
        None
    """

    from imcsdk.mometa.sol.SolIf import SolIf, SolIfConsts

    solif_mo = SolIf(parent_mo_or_dn="sys/rack-unit-1")
    solif_mo.admin_state = SolIfConsts.ADMIN_STATE_DISABLE

    handle.set_mo(solif_mo)
