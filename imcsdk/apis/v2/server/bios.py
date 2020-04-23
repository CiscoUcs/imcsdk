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
from imcsdk.imccoreutils import is_platform_m4, is_platform_m5
from imcsdk.imcexception import ImcOperationError, ImcException
from imcsdk.apis.v2.utils import _is_valid_arg

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
        Dictionary with a failure message, if any.

    Examples:
        bios_tokens_set(handle,
                        tokens = {
                            "baudRate": "19200",
                            "intelVtdatsSupport": "enabled",
                            "consoleRedirection": "com-1",
                            "flowControl": "rts-cts",
                            "sataModeSelect": "platform-default",
                            "txtSupport": "platform-default",
                            "packageCstateLimit": "C0 C1 State"},
                        server_id=2)
    """

    from imcsdk.imccoreutils import load_class, sanitize_xml_parsing_error
    from imcsdk.mometa.bios.BiosSettings import BiosSettings
    from imcsdk.imccoremeta import ImcVersion

    messages = []
    ret = {}

    bios_mo = BiosSettings(parent_mo_or_dn=_get_bios_dn(handle, server_id))
    mo_table = _get_bios_mo_table(handle, tokens, server_id)
    server_mos = _get_server_bios_mo_table(handle, dn=bios_mo.dn)

    # Prepare the filtered table i.e. send only those MOs that exist on the server
    table = {k: v for k, v in mo_table.items() if k in server_mos}

    log.debug("Mo Table       Count: %s Values: %s" % (len(mo_table), mo_table))
    log.debug("Server Table   Count: %s Values: %s" % (len(server_mos), server_mos))
    log.debug("Filtered Table Count: %s Values: %s" % (len(table), table))

    processed_tokens = []
    # Separate the MOs which have only platform-default
    for mo_name, props in table.items():
        non_default_props = {k: v for k, v in props.items() if v != "platform-default"}
        # if there are no non-default props, it can be batched
        if len(non_default_props) == 0:
            # filter properties to only those applicable to the server
            server_mo_props = server_mos[mo_name]
            filtered_props = {k: v for k, v in props.items() if k in server_mo_props and server_mo_props[k]}

            if len(filtered_props) == 0:
                log.debug("skipping token %s props: %s server_mo_props %s " % (mo_name, props, server_mo_props))
                processed_tokens.append(mo_name)
                continue

            # load an instance of the class
            mo_class = load_class(mo_name)
            filtered_props["_handle"] = handle
            mo_obj = mo_class(parent_mo_or_dn=bios_mo, **filtered_props)

            # HACK for CIMC ISSUE. 'rn' is different for M4 and M5
            # rn for M5 for this token has been corrected in GP-MR2
            if mo_name == "BiosVfSataModeSelect" and \
                    is_platform_m5(handle) and \
                    handle.version < ImcVersion("3.1(3a)"):
                mo_obj.rn = "SataModeSelect"
                mo_obj.dn = bios_mo.dn + "/" + mo_obj.rn

            # In HP release, for Janus platform, vp_cbs_cmn_cpu_gen_downcore_ctrl token
            # does not have a platform default value supported on the endpoint
            if mo_name == "BiosVfCbsCmnCpuGenDowncoreCtrl" and \
                    mo_obj.vp_cbs_cmn_cpu_gen_downcore_ctrl == "platform-default" and \
                    handle.version == ImcVersion("4.0(1a)"):
                mo_obj.vp_cbs_cmn_cpu_gen_downcore_ctrl = "Auto"

            # pop the object from the table dictionary
            processed_tokens.append(mo_name)

    for each in processed_tokens:
        table.pop(each)

    log.debug("Modified Tokens Count: %s Values: %s" % (len(table), table))

    # Send all the MOs with default properties in one shot
    handle.set_mo(bios_mo)

    # Send the rest of the MOs
    for mo_name, props in table.items():
        d = {}
        server_mo_props = server_mos[mo_name]
        filtered_props = {k: v for k, v in props.items()
                          if k in server_mo_props and server_mo_props[k]}

        # REALLY DIRTY HACK!!
        # C6 Non Retention - Works on M5, fails on M4
        # C6 non Retention - Works on M4, fails on M5
        if mo_name == "BiosVfPackageCStateLimit" and is_platform_m4(handle) and "vp_package_c_state_limit" in filtered_props:
            if filtered_props["vp_package_c_state_limit"] == "C6 Non Retention":
                filtered_props["vp_package_c_state_limit"] = "C6 non Retention"

        if len(filtered_props) != 0:
            mo_class = load_class(mo_name)
            filtered_props["_handle"] = handle
            try:
                mo_obj = mo_class(parent_mo_or_dn=bios_mo.dn, **filtered_props)

                # HACK for CIMC ISSUE. 'rn' is different for M4 and M5
                # rn for M5 for this token has been corrected in GP-MR2
                if mo_name == "BiosVfSataModeSelect" and \
                        is_platform_m5(handle) and \
                        handle.version < ImcVersion("3.1(3a)"):
                    mo_obj.rn = "SataModeSelect"
                    mo_obj.dn = bios_mo.dn + "/" + mo_obj.rn

                # HP and below only "Disabled" was supported for this token
                # In HP, "disabled" was also supported and hence need to send the older
                # version of this value for an older server
                if mo_name == "BiosVfCDNSupport" and \
                        mo_obj.vp_cdn_support == "disabled" and \
                        handle.version < ImcVersion("4.0(1a)"):
                    mo_obj.vp_cdn_support = "Disabled"

                handle.set_mo(mo_obj)
            except ImcException as e:
                d["Object"] = mo_name
                error = e.error_descr
                if e.error_code == "ERR-xml-parse-error":
                    error = sanitize_xml_parsing_error(e.error_descr)
                d["Error"] = error
                messages.append(d)
                continue
            except Exception as e:
                d["Object"] = mo_name
                d["Error"] = str(e)
                messages.append(d)
                continue

    message = ""

    if len(messages) != 0:
        message = "Following issues were seen during application of BIOS " \
                "tokens: \n"
        for m in messages:
            message += m["Object"] + ": " + m["Error"] + "\n"

    ret["msg"] = message
    ret["msg_params"] = messages
    ret["changed"] = True
    return ret


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
                            "baudRate": "19200",
                            "intelVtdatsSupport": "enabled",
                            "consoleRedirection": "com-1",
                            "flowControl": "rts-cts",
                            "sataModeSelect": "platform-default",
                            "txtSupport": "platform-default",
                            "packageCstateLimit": "C0 C1 State"},
                          server_id=2)
"""

    from imcsdk.imcexception import ImcException
    parent_dn = _get_bios_dn(handle, server_id) + "/bios-settings"
    mo_table = _get_bios_mo_table(handle, tokens, server_id)

    for mo_name, props in mo_table.items():
        try:
            cimc_mos = handle.query_classid(class_id=mo_name)
        except ImcException:
            log.debug("ManagedObject:%s not found on server! Skipping" %
                      mo_name)
            continue
        cimc_mo = None
        for mo in cimc_mos:
            if mo.dn.startswith(parent_dn):
                cimc_mo = mo
                break

        if cimc_mo is None:
            return False

        # Ideally construct a dictionary with only properties starting with 'vp'.
        # But, we have a ready-made dictionary available, hence just re-use it.
        cimc_props = cimc_mo.__dict__

        # Skip comparison when the value to be checked with is "platform-default" and if the token exists on cimc
        modified_props = {x: props[x] for x in props if props[x] != "platform-default" and cimc_props[x]}

        if modified_props:
            if not cimc_mo.check_prop_match(**modified_props):
                return False

    return True


def _get_bios_mo_table(handle, tokens={}, server_id=1):
    from imcsdk.imcbiostables import bios_tokens_table

    mo_table = {}

    bios_tokens_table_platform = bios_tokens_table.get(handle.platform,
                                                       bios_tokens_table[
                                                           'classic'])
    for token, value in tokens.items():
        entry = bios_tokens_table_platform.get(token)
        if entry is None:
            log.warning("Token not found: %s Platform: %s" % (token,
                        handle.platform))
            continue

        mo_props = mo_table.get(entry["mo_name"], {})
        mo_props[entry["prop_name"]] = value
        mo_table[entry["mo_name"]] = mo_props

    return mo_table


def _get_server_bios_mo_table(handle, dn):
    mos = handle.query_children(in_dn=dn)
    mo_table = {}

    for mo in mos:
        props = {k: v for k, v in mo.__dict__.items() if k.startswith('vp')}
        mo_table[mo._class_id] = props

    return mo_table
