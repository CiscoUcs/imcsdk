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


def get_current_certificate(handle):
    """
    This api gets the current certificate installed on the system

    Args:
        handle (ImcHandle)

    Returns:
        CurrentCertificate object
    """

    cert_mo = handle.query_classid("CurrentCertificate")
    return cert_mo[0]


def generate_certificate_signing_request(handle, name, org, org_unit, country,
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
    """

    from imcsdk.mometa.generate.GenerateCertificateSigningRequest import \
        GenerateCertificateSigningRequest

    mo = GenerateCertificateSigningRequest(parent_mo_or_dn="sys/cert-mgmt")

    mo.common_name = name
    mo.organization = org
    mo.organizational_unit = org_unit
    mo.country_code = country
    mo.state = state
    mo.locality = locality

    if self_signed:
        mo.self_signed = "yes"
    else:
        mo.user = username
        mo.pwd = password
        mo.remote_server = server
        mo.remote_file = file_name
        mo.protocol = protocol

    handle.add_mo(mo, modify_present=True)


def get_certificate_signing_status(handle):
    """
    This api checks the status of the certificate generation request
    submitted previously

    Args:
        handle (Imchandle)

    Returns:
        Status of the certificate generation activity (string)
    """

    mo = handle.query_classid("GenerateCertificateSigningRequest")
    return mo[0].csr_status


def upload_certificate(handle, username, password, server, file_name, protocol):
    """
    This api uploads the certificate generated using \
        generate_certificate_signing_request

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
    mo.admin_action = UploadCertificateConsts.ADMIN_ACTION_REMOTE_CERT_UPLOAD
    mo.username = username
    mo.pwd = password
    mo.remote_server = server
    mo.remote_file = file_name
    mo.protocol = protocol

    handle.add_mo(mo, modify_present=True)
