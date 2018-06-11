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
This module provides APIs for bios related configuration like boot order
"""

import logging
import json
import imcsdk.imccoreutils as imccoreutils
from imcsdk.imcexception import ImcOperationError
from imcsdk.apis.utils import _is_valid_arg

log = logging.getLogger('imc')


def _get_bios_dn(handle, server_id=1):
    server_dn = imccoreutils.get_server_dn(handle, server_id)
    return (server_dn + '/bios')


def _get_bios_profile_mo(handle, name, server_id=1):
    bios_dn = _get_bios_dn(handle, server_id)
    parent_dn = bios_dn + '/profile-mgmt'
    mos = handle.query_children(in_dn=parent_dn)
    for mo in mos:
        if mo._class_id == 'BiosProfile' and mo.name == name:
            return mo
    return None


def _get_bios_profile(handle, name, server_id=1):
    mo = _get_bios_profile_mo(handle, name=name, server_id=server_id)
    if mo is None:
        raise ImcOperationError("Get BiosProfile: %s " % name,
                                "Managed Object not found")
    return mo


def bios_profile_backup_running(handle, server_id=1, **kwargs):
    """
    Backups up the running configuration of various bios tokens to create a
    'cisco_backup_profile'.
    Will overwrite the existing backup profile if it exists.

    Args:
        handle (ImcHandle)
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms
        kwargs : Key-Value paired arguments for future use

    Returns:
        BiosProfile object corresponding to the backup profile created

    Raises:
        ImcOperationError if the backup profile is not created

    Examples:
        bios_profile_backup_running(handle, server_id=1)
    """

    from imcsdk.mometa.bios.BiosProfileManagement import BiosProfileManagement
    from imcsdk.mometa.bios.BiosProfileManagement import \
        BiosProfileManagementConsts

    mo = BiosProfileManagement(parent_mo_or_dn=_get_bios_dn(handle, server_id))
    mo.admin_action = BiosProfileManagementConsts.ADMIN_ACTION_BACKUP
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)

    return _get_bios_profile(handle, name='cisco_backup_profile',
                             server_id=server_id)


def bios_profile_upload(handle, remote_server, remote_file, protocol='tftp',
                        user=None, pwd=None, server_id=1, **kwargs):
    """
    Uploads a user configured bios profile in json format.
    Cisco IMC supports uploading a maximum of 3 profiles

    Args:
        handle (ImcHandle)
        remote_server (str): Remote Server IP or Hostname
        remote_file (str): Remote file path
        protocol (str): Protocol for downloading the certificate
                        ['tftp', 'ftp', 'http', 'scp', 'sftp']
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms
        kwargs: Key-Value paired arguments for future use

    Returns:
        UploadBiosProfile object

    Examples:
        bios_profile_upload(handle, remote_server='1.1.1.1',
                        remote_file='/tmp/bios_profile', protocol='scp',
                        user='abcd', pwd='pqrs')
    """

    from imcsdk.mometa.upload.UploadBiosProfile import UploadBiosProfile
    bios_dn = _get_bios_dn(handle, server_id=server_id)
    mo = UploadBiosProfile(
            parent_mo_or_dn=bios_dn + '/profile-mgmt')
    params = {
        'remote_server': remote_server,
        'remote_file': remote_file,
        'protocol': protocol,
        'user': user,
        'pwd': pwd
    }
    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def bios_profile_get(handle, name, server_id=1):
    """
    Gets the bios profile corresponding to the name specified

    Args:
        handle (ImcHandle)
        name (str): Name of the bios profile.
                    Corresponds to the name field in the json file.
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms

    Returns:
        BiosProfile object corresponding to the name specified

    Raises:
        ImcOperationError if the bios profile is not found

    Examples:
        bios_profile_get(handle, name='simple')
    """

    return _get_bios_profile_mo(handle, name=name, server_id=server_id)


def bios_profile_activate(handle, name, backup_on_activate=True,
                          reboot_on_activate=False, server_id=1, **kwargs):
    """
    Activates the bios profile specified by name on the Cisco IMC Server

    Args:
        handle (ImcHandle)
        name (str): Name of the bios profile.
                    Corresponds to the name field in the json file.
        backup_on_activate (bool): Backup running bios configuration
                                   before activating this profile.
                                   Will overwrite the previous backup.
        reboot_on_activate (bool): Reboot the host/server for the newer bios
                                   configuration to be applied.
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms.
        kwargs: Key-Value paired arguments for future use.

    Returns:
        BiosProfile object corresponding to the name specified

    Raises:
        ImcOperationError if the bios profile is not found

    Examples:
        bios_profile_activate(handle, name='simple',
                              backup_on_activate=True,
                              reboot_on_activate=False)
    """

    from imcsdk.mometa.bios.BiosProfile import BiosProfileConsts
    mo = _get_bios_profile(handle, name=name, server_id=server_id)
    params = {
        'backup_on_activate': ('no', 'yes')[backup_on_activate],
        'reboot_on_activate': ('no', 'yes')[reboot_on_activate],
        'enabled': 'yes',
        'admin_action': BiosProfileConsts.ADMIN_ACTION_ACTIVATE
    }
    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(mo.dn)


def bios_profile_delete(handle, name, server_id=1):
    """
    Deletes the bios profile specified by the name on the Cisco IMC server

    Args:
        handle (ImcHandle)
        name (str): Name of the bios profile.
                    Corresponds to the name field in the json file.
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms.

    Returns:
        None

    Raises:
        ImcOperationError if the bios profile is not found

    Examples:
        bios_profile_delete(handle, name='simple', server_id=2)
    """
    from imcsdk.mometa.bios.BiosProfile import BiosProfileConsts
    mo = _get_bios_profile(handle, name=name, server_id=server_id)
    mo.admin_action = BiosProfileConsts.ADMIN_ACTION_DELETE
    handle.set_mo(mo)


def is_bios_profile_enabled(handle, name, server_id=1):
    """
    Args:
        handle (ImcHandle)
        name (str): Name of the bios profile.
                    Corresponds to the name field in the json file.
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms.

    Returns:
        bool

    Raises:
        ImcOperationError if the bios profile is not found

    Examples:
        is_bios_profile_enabled(handle,
                                name='simple',
                                server_id=1)
    """
    mo = _get_bios_profile(handle, name=name, server_id=server_id)
    return mo.enabled.lower() in ['yes', 'true']


def bios_profile_exists(handle, name, server_id=1, **kwargs):
    """
    Checks if the bios profile with the specified params exists

    Args:
        handle (ImcHandle)
        name (str): Name of the bios profile.
                    Corresponds to the name field in the json file.
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms.
        kwargs: Key-Value paired arguments relevant to BiosProfile object

    Returns:
        (True, BiosProfile) if the settings match, else (False, None)

    Examples:
        match, mo = bios_profile_exists(handle, name='simple',
                                        enabled=True)
    """

    mo = _get_bios_profile_mo(handle, name=name, server_id=server_id)
    if mo is None:
        return False, None

    params = {}

    if _is_valid_arg('enabled', kwargs):
        params['enabled'] = ('No', 'Yes')[kwargs.pop('enabled')]

    if not mo.check_prop_match(**params):
        return False, None

    if not mo.check_prop_match(**kwargs):
        return False, None

    return True, mo


def bios_profile_generate_json(handle, name, server_id=1, file_name=None):
    """
    Generates a json output of the bios profile specified by the name on
    the Cisco IMC server.
    If a file name is specified, it writes the output to the file.

    Args:
        handle (ImcHandle)
        name (str): Name of the bios profile.
                    Corresponds to the name field in the json file.
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms.

    Returns:
        JSON Output of the Bios Tokens

    Raises:
        ImcOperationError if the bios profile is not found

    Examples:
        bios_profile_generate_json(handle, name='simple', server_id=2)
    """

    output = {}
    output['tokens'] = {}

    mo = _get_bios_profile(handle, name=name, server_id=server_id)
    output['name'] = mo.name
    output['description'] = mo.description

    tokens = handle.query_children(in_dn=mo.dn)
    output['tokens'] = {x.name: x.configured_value for x in tokens}

    if file_name:
        f = open(file_name, 'w')
        f.write(json.dumps(output))
        f.close()

    return output


def bios_tokens_set(handle, tokens={}, server_id=1):
    """
    Args:
        handle (ImcHandle)
        tokens (dictionary) : (key, value) pair of bios tokens with key being the name of the token
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms.

    Returns:
        None

    Examples:
        bios_tokens_set(handle,
                        tokens = {
                            "BaudRate": "19200",
                            "IntelVTDATSSupport": "enabled",
                            "ConsoleRedirection": "com-1",
                            "FlowControl": "rts-cts"},
                        server_id=2)
    """

    from imcsdk.imccoreutils import load_class

    parent_dn = _get_bios_dn(handle, server_id) + "/bios-settings"
    mo_table = _get_bios_mo_table(handle, tokens, server_id)

    for mo_name, props in mo_table.items():
        mo_class = load_class(mo_name)
        mo_obj = mo_class(parent_mo_or_dn=parent_dn, **props)
        handle.set_mo(mo_obj)


def bios_tokens_exist(handle, tokens={}, server_id=1):
    """
    Args:
        handle (ImcHandle)
        tokens (dictionary) : (key, value) pair of bios tokens with key being the name of the token
        server_id (int): Id of the server to perform
                         this operation on C3260 platforms.

    Returns:
        True/False based on the match with the server side tokens

    Examples:
        bios_tokens_exist(handle,
                          tokens = {
                            "BaudRate": "19200",
                            "IntelVTDATSSupport": "enabled",
                            "ConsoleRedirection": "com-1",
                            "FlowControl": "rts-cts"},
                          server_id=2)
"""

    parent_dn = _get_bios_dn(handle, server_id) + "/bios-settings"
    mo_table = _get_bios_mo_table(handle, tokens, server_id)

    for mo_name, props in mo_table.items():
        cimc_mos = handle.query_classid(class_id=mo_name)
        cimc_mo = None
        for mo in cimc_mos:
            if mo.dn.startswith(parent_dn):
                cimc_mo = mo
                break

        if cimc_mo is None:
            return False

        # Skip comparison when the value to be checked with is "platform-default"
        modified_props = {x: props[x] for x in props if props[x] != "platform-default"}

        if not cimc_mo.check_prop_match(**modified_props):
            return False

    return True


def _get_bios_mo_table(handle, tokens={}, server_id=1):
    from imcsdk.imcbiostables import bios_tokens_table

    mo_table = {}

    for token, value in tokens.items():
        bios_tokens_table_platform = bios_tokens_table.get(handle.platform,
                                                           bios_tokens_table[
                                                               'classic'])
        entry = bios_tokens_table_platform.get(token)
        if entry is None:
            log.warning("Token not found: %s Platform: %s" % (token,
                        handle.platform))
            continue

        mo_props = mo_table.get(entry["mo_name"], {})
        mo_props[entry["prop_name"]] = value
        mo_table[entry["mo_name"]] = mo_props

    return mo_table
