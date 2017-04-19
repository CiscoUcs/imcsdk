# Copyright 2016 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains the APIs used to launch IMC kvm.
"""

try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode

import subprocess
import logging

from .. import imcgenutils
from ..imcexception import ImcWarning, ImcValidationException, ImcException
from ..imccoremeta import ImcVersion

log = logging.getLogger('imc')


class _ParamKvm(object):
    # Internal class to act as enum to support imc_kvm_launch utility.

    KVM_IP_ADDR = "cimcAddr"
    TOKEN_ONE = "tkn1"
    TOKEN_TWO = "tkn2"


def imc_kvm_launch(handle, need_url=False):
    """
    imc_kvm_launch launches the kvm session for a specified server.

    Args:
        handle (ImcHandle)
        need_url (bool): True/False,
                         Returns URL to launch kvm, if True

    Example:
        imc_kvm_launch(handle, need_url=False)
        imc_kvm_launch(handle, need_url=True)
    """

    from ..imcmethodfactory import config_resolve_class
    from ..imcmethodfactory import aaa_get_compute_auth_tokens

    min_version = ImcVersion('1.5(2)')
    if handle.version < min_version:
        raise ImcValidationException(
            "start_kvm_session not supported for Imc version older than %s. "
            "You are connected to Imc Version %s" % (min_version,
                                                     handle.version))

    nvc = {}
    ip_address = None

    elem = config_resolve_class(cookie=handle.cookie, class_id="MgmtIf")

    response = handle.post_elem(elem)
    if response.error_code == 0:
        for mgmt_if in response.out_configs.child:
            if mgmt_if.subject == "blade" and mgmt_if.ext_enabled == "yes":
                ip_address = mgmt_if.ext_ip
    else:
        raise ImcException(response.error_code, response.error_descr)

    if ip_address is None or ip_address == '0.0.0.0':
        raise ImcValidationException("No assigned IP address to use.")

    nvc[_ParamKvm.KVM_IP_ADDR] = ip_address
    elem = aaa_get_compute_auth_tokens(cookie=handle.cookie)
    response = handle.post_elem(elem)

    if response.error_code == 0:
        nvc[_ParamKvm.TOKEN_ONE] = response.out_tokens.split(',')[0]
        nvc[_ParamKvm.TOKEN_TWO] = response.out_tokens.split(',')[1]
    else:
        raise ImcException(response.error_code, response.error_descr)

    uri = handle.uri
    kvm_url = '%s/kvm.jnlp?%s' % (uri, urlencode(nvc))

    if need_url:
        return kvm_url
    else:
        install_path = imcgenutils.get_java_installation_path()
        if install_path is not None:
            subprocess.call([install_path, kvm_url])
        else:
            ImcWarning("Java is not installed on System.")
            subprocess.Popen(kvm_url)
