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
This module provides APIs for storage controller configuration.
"""

import logging

import imcsdk.imccoreutils as imccoreutils
from imcsdk.imcexception import ImcOperationError
from imcsdk.mometa.self.SelfEncryptStorageController import \
    SelfEncryptStorageController, SelfEncryptStorageControllerConsts
from imcsdk.mometa.storage.StorageController import StorageControllerConsts

log = logging.getLogger('imc')


def _get_controller_dn(handle, controller_type, controller_slot, server_id=1):
    dn = imccoreutils.get_server_dn(handle, server_id)
    return dn + "/board/storage-" + controller_type + "-" + controller_slot


def _get_controller(handle, controller_type, controller_slot, server_id=1):
    mo = handle.query_dn(_get_controller_dn(handle,
                                            controller_type,
                                            controller_slot,
                                            server_id))
    if mo is None:
        raise ImcOperationError("Get Controller Type:%s Slot:%s" %
                                (controller_type, controller_slot),
                                "Not found")
    return mo


def _controller_action_set(handle, controller_type, controller_slot, action,
                           server_id=1):
    mo = _get_controller(handle, controller_type, controller_slot, server_id)
    mo.admin_action = action
    handle.set_mo(mo)
    return mo


def controller_jbod_enable(handle, controller_type, controller_slot,
                           server_id=1):
    """
    Enables jbod mode on the controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        controller_jbod_enable(handle, controller_type='SAS',
                               controller_slot='HBA')

    """
    action = StorageControllerConsts.ADMIN_ACTION_ENABLE_JBOD
    return _controller_action_set(handle=handle,
                                  controller_type=controller_type,
                                  controller_slot=controller_slot,
                                  action=action,
                                  server_id=server_id)


def controller_jbod_exists(handle, controller_type, controller_slot,
                           server_id=1):
    """
    Checks if jbod mode is enabled on the controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        bool

    Examples:
        controller_jbod_exists(handle, controller_type='SAS',
                               controller_slot='HBA')
    """
    controller_dn = _get_controller_dn(handle, controller_type,
                                       controller_slot, server_id)
    dn = controller_dn + "/controller-settings"
    mo = handle.query_dn(dn)

    if mo.enable_jbod.lower() not in ['yes', 'true']:
        return False
    return True


def controller_jbod_disable(handle, controller_type, controller_slot,
                            server_id=1):
    """
    Disables jbod mode on the controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        controller_jbod_disable(handle, controller_type='SAS',
                                controller_slot='HBA')

    """
    action = StorageControllerConsts.ADMIN_ACTION_DISABLE_JBOD
    return _controller_action_set(handle=handle,
                                  controller_type=controller_type,
                                  controller_slot=controller_slot,
                                  action=action,
                                  server_id=server_id)


def controller_encryption_enable(handle, controller_type, controller_slot,
                                 security_key=None, key_id=None,
                                 existing_security_key=None,
                                 key_management="local",
                                 server_id=1, **kwargs):
    """
    Enables encryption on the controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                               "MEZZ","0"-"9"
        security_key (str): Security key used to enable controller security.
                            Max Length is 32 characters.
        key_id (str): Security Key Identifier.
                      Max Length is 256 characters.
        existing_security_key (str): Existing security key.
                            Max Length is 32 characters.
        key_management (str): "local" or "remote"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        controller_encryption_enable(handle, controller_type='SAS',
                                     controller_slot='HBA'',
                                     key_id='ABCD12345', security_key='12345')
    """
    from imcsdk.mometa.self.SelfEncryptStorageController import \
        SelfEncryptStorageController, SelfEncryptStorageControllerConsts

    controller_mo = _get_controller(handle, controller_type, controller_slot,
                                    server_id)

    enabled = controller_mo.self_encrypt_enabled.lower() in ['yes', 'true']
    if not enabled:
        action = \
            SelfEncryptStorageControllerConsts.ADMIN_ACTION_ENABLE_SELF_ENCRYPT
        existing_security_key = None
    else:
        action = \
            SelfEncryptStorageControllerConsts.ADMIN_ACTION_MODIFY_SELF_ENCRYPT

    if not enabled and key_management == "local" and security_key is None:
        raise ImcOperationError("Enable encryption on Controller: %s" % controller_slot,
                                "Missing param 'security_key'.")

    mo = SelfEncryptStorageController(parent_mo_or_dn=controller_mo.dn)
    params = {
        'key_id': key_id,
        'existing_security_key': existing_security_key,
        'security_key': security_key,
        'key_management': key_management,
        'admin_action': action,
    }

    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return handle.query_dn(controller_mo.dn)


def controller_encryption_exists(handle, controller_type, controller_slot,
                                 server_id=1, **kwargs):
    """
    Checks if encryption is enabled on the controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        True/False, MO

    Examples:
        controller_encryption_exists(handle, controller_type='SAS',
                                    controller_slot='HBA'')
    """
    try:
        mo = _get_controller(handle, controller_type, controller_slot,
                             server_id)
    except:
        return False, None

    existing_security_key = kwargs.pop('existing_security_key', None)
    if existing_security_key:
        return False, mo

    if mo.self_encrypt_enabled.lower() not in ['yes', 'true']:
        return False, mo

    kwargs.pop('security_key', None)
    kwargs.pop('key_management', None)
    dn = mo.dn + "/ctr-self-encrypt"
    encryption_mo = handle.query_dn(dn)
    return encryption_mo.check_prop_match(**kwargs), mo


def controller_encryption_disable(handle, controller_type,
                                  controller_slot, server_id=1):
    """
    Disables encryption on the controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        controller_encryption_disable(handle, controller_type='SAS',
                                      controller_slot='HBA'')
    """
    controller_dn = _get_controller_dn(handle, controller_type,
                                       controller_slot, server_id)

    mo = SelfEncryptStorageController(parent_mo_or_dn=controller_dn)
    mo.admin_action = \
        SelfEncryptStorageControllerConsts.ADMIN_ACTION_DISABLE_SELF_ENCRYPT
    handle.set_mo(mo)
    return handle.query_dn(controller_dn)


def controller_encryption_key_id_generate(handle, controller_type,
                                          controller_slot, server_id=1):
    """
    Generates a random key id for the given controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        Key-id string

    Examples:
        key_id = controller_encryption_key_id_generate(
                handle,
                controller_type='SAS',
                controller_slot='HBA'')
    """
    dn = _get_controller_dn(handle, controller_type, controller_slot,
                            server_id)
    mos = handle.query_children(
                in_dn=dn,
                class_id='GeneratedStorageControllerKeyId')
    return mos[0].generated_key_id if mos else ""


def controller_encryption_key_generate(handle, controller_type,
                                       controller_slot, server_id=1):
    """
    Generates a random security key for the given controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        Security Key string

    Examples:
        key = controller_encryption_key_generate(
                handle,
                controller_type='SAS',
                controller_slot='HBA'')
    """
    dn = _get_controller_dn(handle, controller_type, controller_slot,
                            server_id)
    mos = handle.query_children(
                in_dn=dn,
                class_id='SuggestedStorageControllerSecurityKey')
    return mos[0].suggested_security_key if mos else ""


def controller_unlock_foreign_drives(handle, controller_type,
                                     controller_slot, security_key,
                                     server_id=1):
    """
    Unlocks on the given controller, drives encrypted on another controller.

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        security_key (str): Security Key used to encrypt the foreign drive
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        key = controller_unlock_foreign_drives(
                handle,
                controller_type='SAS',
                controller_slot='HBA'',
                security_key='12345')
    """
    action = \
        SelfEncryptStorageControllerConsts.ADMIN_ACTION_UNLOCK_SECURED_DRIVES
    dn = _get_controller_dn(handle, controller_type, controller_slot,
                            server_id)
    mo = SelfEncryptStorageController(parent_mo_or_dn=dn)
    params = {
        'security_key': security_key,
        'admin_action': action
    }
    mo.set_prop_multiple(**params)
    return handle.query_dn(dn)


def controller_import_foreign_config(handle, controller_type,
                                     controller_slot, server_id=1):
    """
    Imports foreign configuration on the given controller

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        controller_import_foreign_config(handle,
                controller_type='SAS',
                controller_slot='HBA'')
    """
    action = StorageControllerConsts.ADMIN_ACTION_IMPORT_FOREIGN_CONFIG
    return _controller_action_set(
                handle,
                controller_type,
                controller_slot,
                action=action,
                server_id=server_id)


def controller_clear_boot_drive(handle, controller_type, controller_slot,
                                server_id=1):
    """
    Clears boot drive

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        controller_clear_boot_drive(handle, controller_type='SAS',
                                    controller_slot='HBA'')
    """
    action = StorageControllerConsts.ADMIN_ACTION_CLEAR_BOOT_DRIVE
    return _controller_action_set(
                handle,
                controller_type,
                controller_slot,
                action=action,
                server_id=server_id)


def controller_clear_boot_drive_exists(handle, controller_type,
                                       controller_slot, server_id=1):
    """
    checks if boot drive is already cleared.

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        controller_clear_boot_drive(handle, controller_type='SAS',
                                    controller_slot='HBA'')
    """
    controller_dn = _get_controller_dn(handle, controller_type,
                                       controller_slot, server_id)
    dn = controller_dn + "/controller-props"
    mo = handle.query_dn(dn)

    if mo.boot_drive.lower() != 'none':
        return False
    return True


def controller_action_apply(handle, controller_type, controller_slot,
                            action, server_id=1):
    """
    Applies the controller action.

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        action (str): ["clear_boot_drive"]
        server_id (int): server_id for UCS 3260 platform

    Returns:
        StorageController object

    Examples:
        controller_action_apply(handle, controller_type='SAS',
                                controller_slot='HBA',
                                action='clear_boot_drive')
    """
    api_map = {
        "clear_boot_drive": controller_clear_boot_drive,
    }

    if action not in api_map:
        raise ImcOperationError("Configure Controller: %s" % controller_slot,
                                "Invalid action. Valid values are  %s"
                                % str(", ".join(api_map.keys())))

    params = {
        'handle': handle,
        'controller_type': controller_type,
        'controller_slot': controller_slot,
        'server_id': server_id
    }

    execute_api = api_map[action]
    return execute_api(**params)


def controller_action_exists(handle, controller_type, controller_slot,
                             action, server_id=1):
    """
    Check if action is already applied on controller.

    Args:
        handle (ImcHandle)
        controller_type (str): Controller type
                               'SAS'
        controller_slot (str): Controller slot name/number
                                "MEZZ","0"-"9", "HBA"
        action (str): ["clear_boot_drive"]
        server_id (int): server_id for UCS 3260 platform

    Returns:
        True/False, MO/None

    Examples:
        controller_action_exists(handle, controller_type='SAS',
                                 controller_slot='HBA'',
                                 action='clear_boot_drive')
    """
    api_map = {
        "clear_boot_drive": controller_clear_boot_drive_exists,
    }

    if action not in api_map:
        raise ImcOperationError("Configure Controller: %s" % controller_slot,
                                "Invalid action. Valid values are  %s"
                                % str(", ".join(api_map.keys())))

    params = {
        'handle': handle,
        'controller_type': controller_type,
        'controller_slot': controller_slot,
        'server_id': server_id
    }

    execute_api = api_map[action]
    return execute_api(**params)
