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
This module implements all the smtp related functionality
"""

from imcsdk.imcexception import ImcOperationError
from imcsdk.mometa.mail.MailRecipient import MailRecipientConsts
from imcsdk.mometa.comm.CommMailAlert import CommMailAlertConsts
from imcsdk.apis.v2.utils import _get_mo, _is_invalid_value

import logging

log = logging.getLogger('imc')

_SMTP_DN = 'sys/svc-ext/mail-alert-svc'

_MAIL_ALERT_SEVERITY_LEVELS = [
    CommMailAlertConsts.MIN_SEVERITY_LEVEL_CONDITION,
    CommMailAlertConsts.MIN_SEVERITY_LEVEL_CRITICAL,
    CommMailAlertConsts.MIN_SEVERITY_LEVEL_MAJOR,
    CommMailAlertConsts.MIN_SEVERITY_LEVEL_MINOR,
    CommMailAlertConsts.MIN_SEVERITY_LEVEL_WARNING]


def _is_valid_severity_level(min_severity_level):
    return min_severity_level in _MAIL_ALERT_SEVERITY_LEVELS


def smtp_enable(handle, ip_address=None, port=None, min_severity_level=None,
                from_address=None, **kwargs):
    """
    Enables SMTP Policy and sets the given properties

    Args:
        handle (ImcHandle)
        ip_address (str): Ip Address of the SMTP server
        port (int): Port number of the SMTP server
        min_severity_level (str): Minimum fault severity level
            Valid values: "condition", "critical", "major", "minor", "warning"
        from_address(str): Email id that will be displayed as the source in the mail alert
        kwargs: key-value paired arguments for future use

    Returns:
        CommMailAlert object

    Raises:
        ImcOperationError if the severity level is not correct

    Example:
        smtp_enable(handle, '10.105.110.219', 25, 'minor')
    """
    if min_severity_level and not _is_valid_severity_level(min_severity_level):
        raise ImcOperationError(
            'Configure SMTP Policy',
            'Invalid severity level %s ' % min_severity_level)

    mo = _get_mo(handle, dn=_SMTP_DN)
    params = {
        'admin_state': 'enabled',
        'ip_address': ip_address,
        'port': str(port) if port is not None else None,
        'min_severity_level': min_severity_level,
        'from_address': from_address
    }
    mo.set_prop_multiple(**params)
    mo.set_prop_multiple(**kwargs)
    handle.set_mo(mo)
    return mo


def smtp_exists(handle, **kwargs):
    """
    Check whether the specified SMTP settings already exist

    Args:
        handle (ImcHandle)
        kwargs: key-value paired arguments

    Returns:
        (True, CommMailAlert) if settings match, (False, None) otherwise
    """
    try:
        mo = _get_mo(handle, dn=_SMTP_DN)
    except:
        return False, None

    kwargs['admin_state'] = 'enabled'

    if not mo.check_prop_match(**kwargs):
        return False, mo
    return True, None


def smtp_disable(handle):
    """
    Disable SMTP Settings

    Args:
        handle (ImcHandle)

    Raises:
        ImcOperationError

    Returns:
         CommMailAlert object
    """
    mo = _get_mo(handle, dn=_SMTP_DN)
    mo.admin_state = 'disabled'
    handle.set_mo(mo)
    return mo


def _get_smtp_recipients(handle):
    mos = handle.query_children(in_dn=_SMTP_DN, class_id='MailRecipient')
    if mos is None:
        raise ImcOperationError("Add SMTP recipient",
                                "No recipient slot present.")
    return mos


def _get_smtp_recipient(handle, email):
    mos = handle.query_children(in_dn=_SMTP_DN, class_id='MailRecipient')
    if mos is None:
        raise ImcOperationError("Get SMTP recipient",
                                "No recipient slot present.")

    for mo in mos:
        if mo.email == email:
            return mo
    return None


def _get_free_smtp_recipient(handle):
    mos = _get_smtp_recipients(handle)
    for mo in mos:
        if _is_invalid_value(mo.email):
            return mo

    raise ImcOperationError("Add SMTP recipient",
                            "Max number of emails already added.")


def smtp_recipient_add(handle, email):
    """
    Adds the smtp recipient

    Args:
        handle (ImcHandle)
        email (str): email address

    Returns
        MailRecipient

    Raises:
        ImcOperationError if email cannot be added

    Example:
        smtp_recipient_add(handle, 'cec@cisco.com')
    """
    mo = _get_free_smtp_recipient(handle)
    mo.email = email
    handle.set_mo(mo)
    return mo


def smtp_recipient_exists(handle, email):
    """
    Checks whether the smtp recipient is already present

    Args:
        handle (ImcHandle)
        email (str): email address

    Returns:
        True/False, MO/None

    Example:
        smtp_recipient_exists(handle, 'cec@cisco.com')
    """
    try:
        mos = _get_smtp_recipients(handle)
    except:
        return False, None

    for mo in mos:
        if mo.email == email:
            return True, mo
    return False, mo


def smtp_recipient_remove(handle, email):
    """
    Clears the smtp recipient with given email address

    Args:
        handle (ImcHandle)
        email (int): SMTP recipient email address

    Returns:
        MailRecipient object

    Raises:
        ImcOperationError

    Example:
        smtp_recipient_remove(handle, 'mail1@cisco.com')
    """
    mo = _get_smtp_recipient(handle, email)
    if mo is None:
        raise ImcOperationError("smtp_recipient_remove",
                                "Recipient does not exist")
    mo.admin_action = MailRecipientConsts.ADMIN_ACTION_CLEAR
    handle.set_mo(mo)
    return mo


def smtp_recipient_remove_all(handle):
    """
    Clears the smtp recipient with given id

    Args:
        handle (ImcHandle)

    Returns:
        None

    Raises:
        ImcOperationError

    Example:
        smtp_recipient_remove(handle,1)
    """
    mos = _get_smtp_recipients(handle)
    if mos is None:
        raise ImcOperationError("smtp_recipient_remove_all",
                                "No Recipient exist")
    for mo in mos:
        if not mo.email:
            continue
        mo.admin_action = MailRecipientConsts.ADMIN_ACTION_CLEAR
        handle.set_mo(mo)


def smtp_recipient_exists_any(handle):
    """
    Checks if any SMTP recipient exists.

    Args:
        handle (ImcHandle)

    Returns:
        None

    Raises:
        ImcOperationError

    Example:
        smtp_recipient_exists_any(handle)
    """
    mos = _get_smtp_recipients(handle)
    if mos is None:
        raise ImcOperationError("smtp_recipient_remove_all",
                                "No Recipient exist")
    for mo in mos:
        if mo.email:
            return True
    return False
