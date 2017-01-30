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
This module provides apis for certificate related functionality
"""


def current_certificate_get(handle):
    """
    This api gets the current certificate installed on the system

    Args:
        handle (ImcHandle)

    Returns:
        CurrentCertificate object
    """

    cert_mo = handle.query_classid("CurrentCertificate")
    return cert_mo[0]


def certificate_signing_request_generate(handle, name, org, org_unit, country,
                                         state, locality, username=None,
                                         password=None, server=None,
                                         file_name=None, protocol=None,
                                         self_signed=False):
    """
    This api generates a new certificate signing request

    Args:
        handle (ImcHandle)
        name (string): Name for the Certificate
        org (string): Organization
        org_unit (string): Organizational Unit
        country (string): COUNTRY_CODE_* from \
                GenerateCertificateSigningRequestConsts
        state (string): State
        locality (string): Locality
        username (string): username
        password (string): password
        server (string): ip address of the remote server
        file_name (string): filename for the certificate file
        protocol (string): "ftp", "http", "none", "scp", "sftp", "tftp"
        self_signed (bool): if self-signed,
                (user, password, server, file, protocol) not required

    Returns:
        None

    Examples:
        certificate_signing_request_generate(
            handle, name="test-cert", org="test-org", org_unit="test-unit",
            country=GenerateCertificateSigningRequestConsts.COUNTRY_CODE_UNITED_STATES,
            state="California", locality="San Francisco", self_signed=True)

    """

    from imcsdk.mometa.generate.GenerateCertificateSigningRequest import \
        GenerateCertificateSigningRequest

    mo = GenerateCertificateSigningRequest(parent_mo_or_dn="sys/cert-mgmt")

    params = {
        "common_name": name,
        "organization": org,
        "organizational_unit": org_unit,
        "country_code": country,
        "state": state,
        "locality": locality
    }

    if self_signed:
        params["self_signed"] = "yes"
    else:
        params["user"] = username
        params["pwd"] = password
        params["remote_server"] = server
        params["remote_file"] = file_name
        params["protocol"] = protocol

    mo.set_prop_multiple(**params)
    handle.add_mo(mo, modify_present=True)


def certificate_signing_status_get(handle):
    """
    This api checks the status of the certificate generation request
    submitted previously

    Args:
        handle (Imchandle)

    Returns:
        Status of the certificate generation activity (string)
    """

    mo = handle.query_classid("GenerateCertificateSigningRequest")
    return mo[0].csr_status if mo else ""


def certificate_upload(handle, username, password, server, file_name, protocol):
    """
    This api uploads the certificate generated using \
        certificate_signing_request_generate

    Args:
        handle (ImcHandle)
        username (string): username
        password (string): password
        server (string): ip address of the remote server
        file_name (string): full path to the certificate file
        protocol (string): "ftp", "http", "none", "scp", "sftp", "tftp"

    Returns:
        None
    """

    from imcsdk.mometa.upload.UploadCertificate import UploadCertificate, \
        UploadCertificateConsts

    mo = UploadCertificate(parent_mo_or_dn="sys/cert-mgmt")
    params = {
        "admin_action": UploadCertificateConsts.ADMIN_ACTION_REMOTE_CERT_UPLOAD,
        "user": username,
        "pwd": password,
        "remote_server": server,
        "remote_file": file_name,
        "protocol": protocol,
    }

    mo.set_prop_multiple(**params)
    handle.add_mo(mo, modify_present=True)
