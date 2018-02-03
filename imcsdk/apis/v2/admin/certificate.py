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

country_codes = {
    "Albania": "AL",
    "Algeria": "DZ",
    "American Samoa": "AS",
    "Andorra": "AD",
    "Angola": "AO",
    "Anguilla": "AI",
    "Antarctica": "AQ",
    "Antigua and Barbuda": "AG",
    "Argentina": "AR",
    "Armenia": "AM",
    "Aruba": "AW",
    "Australia": "AU",
    "Austria": "AT",
    "Azerbaijan": "AZ",
    "Bahamas": "BS",
    "Bahrain": "BH",
    "Bangladesh": "BD",
    "Barbados": "BB",
    "Belarus": "BY",
    "Belgium": "BE",
    "Belize": "BZ",
    "Benin": "BJ",
    "Bermuda": "BM",
    "Bhutan": "BT",
    "Bolivia": "BO",
    "Bosnia and Herzegovina": "BA",
    "Botswana": "BW",
    "Bouvet Island": "BV",
    "Brazil": "BR",
    "British Indian Ocean Territory": "IO",
    "Brunei Darussalam": "BN",
    "Bulgaria": "BG",
    "Burkina Faso": "BF",
    "Burundi": "BI",
    "Cambodia": "KH",
    "Cameroon": "CM",
    "Canada": "CA",
    "Cape Verde": "CV",
    "Cayman Islands": "KY",
    "Central African Republic": "CF",
    "Chad": "TD",
    "Chile": "CL",
    "China": "CN",
    "Christmas Island": "CX",
    "Cocos (Keeling) Islands": "CC",
    "Colombia": "CO",
    "Comoros": "KM",
    "Congo": "CD",
    "Cook Islands": "CK",
    "Costa Rica": "CR",
    "Cote D'Ivoire (Ivory Coast)": "CI",
    "Croatia (Hrvatska)": "HR",
    "Cuba": "CU",
    "Cyprus": "CY",
    "Czech Republic": "CZ",
    "Czechoslovakia": "CZ",
    "Denmark": "DK",
    "Djibouti": "DJ",
    "Dominica": "DM",
    "Dominican Republic": "DO",
    "East Timor": "TL",
    "Ecuador": "EC",
    "Egypt": "EG",
    "El Salvador": "SV",
    "Equatorial Guinea": "GQ",
    "Eritrea": "ER",
    "Estonia": "EE",
    "Ethiopia": "ET",
    "Falkland Islands (Malvinas)": "FK",
    "Faroe Islands": "FO",
    "Fiji": "FJ",
    "Finland": "FI",
    "France": "FR",
    "France, Metropolitan": "FX",
    "French Guiana": "GF",
    "French Polynesia": "PF",
    "French Southern Territories": "TF",
    "Gabon": "GA",
    "Gambia": "GM",
    "Georgia": "GE",
    "Germany": "DE",
    "Ghana": "GH",
    "Gibraltar": "GI",
    "Great Britain (UK)": "UK",
    "Greece": "GR",
    "Greenland": "GL",
    "Grenada": "GD",
    "Guadeloupe": "GP",
    "Guam": "GU",
    "Guatemala": "GT",
    "Guinea": "GN",
    "Guinea-Bissau": "GW",
    "Guyana": "GY",
    "Haiti": "HT",
    "Heard and McDonald Islands": "HM",
    "Honduras": "HN",
    "Hong Kong": "HK",
    "Hungary": "HU",
    "Iceland": "IS",
    "India": "IN",
    "Indonesia": "ID",
    "Iran": "IR",
    "Iraq": "IQ",
    "Ireland": "IE",
    "Israel": "IL",
    "Italy": "IT",
    "Jamaica": "JM",
    "Japan": "JP",
    "Jordan": "JO",
    "Kazakhstan": "KZ",
    "Kenya": "KE",
    "Kiribati": "KI",
    "Korea (North)": "KP",
    "Korea (South)": "KR",
    "Kuwait": "KW",
    "Kyrgyzstan": "KG",
    "Laos": "LA",
    "Latvia": "LV",
    "Lebanon": "LB",
    "Lesotho": "LS",
    "Liberia": "LR",
    "Libya": "LY",
    "Liechtenstein": "LI",
    "Lithuania": "LT",
    "Luxembourg": "LU",
    "Macau": "MO",
    "Macedonia": "MK",
    "Madagascar": "MG",
    "Malawi": "MW",
    "Malaysia": "MY",
    "Maldives": "MV",
    "Mali": "ML",
    "Malta": "MT",
    "Marshall Islands": "MH",
    "Martinique": "MQ",
    "Mauritania": "MR",
    "Mauritius": "MU",
    "Mayotte": "YT",
    "Mexico": "MX",
    "Micronesia": "FM",
    "Moldova": "MD",
    "Monaco": "MC",
    "Mongolia": "MN",
    "Montserrat": "MS",
    "Morocco": "MA",
    "Mozambique": "MZ",
    "Myanmar": "MM",
    "Namibia": "NA",
    "Nauru": "NR",
    "Nepal": "NP",
    "Netherlands": "NL",
    "Netherlands Antilles": "AN",
    "Neutral Zone": "NT",
    "New Caledonia": "NC",
    "New Zealand (Aotearoa)": "NZ",
    "Nicaragua": "NI",
    "Niger": "NE",
    "Nigeria": "NG",
    "Niue": "NU",
    "Norfolk Island": "NF",
    "Northern Mariana Islands": "MP",
    "Norway": "NO",
    "Oman": "OM",
    "Pakistan": "PK",
    "Palau": "PW",
    "Panama": "PA",
    "Papua New Guinea": "PG",
    "Paraguay": "PY",
    "Peru": "PE",
    "Philippines": "PH",
    "Pitcairn": "PN",
    "Poland": "PL",
    "Portugal": "PT",
    "Puerto Rico": "PR",
    "Qatar": "QA",
    "Reunion": "RE",
    "Romania": "RO",
    "Russian Federation": "RU",
    "Rwanda": "RW",
    "S. Georgia and S. Sandwich Isls.": "GS",
    "Saint Kitts and Nevis": "KN",
    "Saint Lucia": "LC",
    "Saint Vincent and the Grenadines": "VC",
    "Samoa": "WS",
    "San Marino": "SM",
    "Sao Tome and Principe": "ST",
    "Saudi Arabia": "SA",
    "Senegal": "SN",
    "Seychelles": "SC",
    "Sierra Leone": "SL",
    "Singapore": "SG",
    "Slovak Republic": "SK",
    "Slovenia": "SI",
    "Solomon Islands": "SB",
    "Somalia": "SO",
    "South Africa": "ZA",
    "Spain": "ES",
    "Sri Lanka": "LK",
    "St. Helena": "SH",
    "St. Pierre and Miquelon": "PM",
    "Sudan": "SD",
    "Suriname": "SR",
    "Svalbard and Jan Mayen Islands": "SJ",
    "Swaziland": "SZ",
    "Sweden": "SE",
    "Switzerland": "CH",
    "Syria": "SY",
    "Taiwan": "TW",
    "Tajikistan": "TJ",
    "Tanzania": "TZ",
    "Thailand": "TH",
    "Togo": "TG",
    "Tokelau": "TK",
    "Tonga": "TO",
    "Trinidad and Tobago": "TT",
    "Tunisia": "TN",
    "Turkey": "TR",
    "Turkmenistan": "TM",
    "Turks and Caicos Islands": "TC",
    "Tuvalu": "TV",
    "US Minor Outlying Islands": "UM",
    "USSR (former)": "SU",
    "Uganda": "UG",
    "Ukraine": "UA",
    "United Arab Emirates": "AE",
    "United Kingdom": "GB",
    "United States": "US",
    "Uruguay": "UY",
    "Uzbekistan": "UZ",
    "Vanuatu": "VU",
    "Vatican City State (Holy See)": "VA",
    "Venezuela": "VE",
    "Viet Nam": "VN",
    "Virgin Islands (British)": "VG",
    "Virgin Islands (U.S.)": "VI",
    "Wallis and Futuna Islands": "WF",
    "Western Sahara": "EH",
    "Yemen": "YE",
    "Yugoslavia": "YU",
    "Zaire": "ZR",
    "Zambia": "ZM",
    "Zimbabwe": "ZW",
}


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


def certificate_signing_request_generate(handle, name, org, locality, state,
                                         country, org_unit=None, email=None,
                                         server=None,
                                         username=None, password=None,
                                         file_name=None, protocol=None,
                                         self_signed=False):
    """
    This api generates a new certificate signing request

    Args:
        handle (ImcHandle)
        name (string): Name for the Certificate
        org (string): Organization
        locality (string): Locality
        state (string): State
        country (string): COUNTRY_CODE_* from \
                GenerateCertificateSigningRequestConsts
        org_unit (string): Organizational Unit
        email (string): Email
        server (string): ip address of the remote server
        username (string): username
        password (string): password
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
        "locality": locality,
        "state": state,
        "country_code": country,
        "organizational_unit": org_unit,
        "email": email
    }

    if self_signed:
        params["self_signed"] = "yes"
    else:
        params["self_signed"] = "no"
        params["remote_server"] = server
        params["user"] = username
        params["pwd"] = password
        params["remote_file"] = file_name
        params["protocol"] = protocol

    mo.set_prop_multiple(**params)
    handle.add_mo(mo, modify_present=True)


def certificate_exists(handle, **kwargs):
    """
    checks if certificate exists.

    Args:
        handle (ImcHandle)
        kwargs: Key-Value paired arguments relevant to CurrentCertificate mo

    Returns:
        True, CurrentCertificate MO if found, else False, None

    Example:
        certificate_exists(
    handle, name="test-cert", org="test-org", org_unit="test-unit",
    country=GenerateCertificateSigningRequestConsts.COUNTRY_CODE_UNITED_STATES,
    state="California", locality="San Francisco")
    """
    return False, None
   # TBD: How to handle self-signed vs ca-signed certificate?
   #  current_certificate = current_certificate_get(handle)
   #  if current_certificate is None:
   #      return False, None

   #  params = {
   #      "common_name": kwargs['name'],
   #      "organization": kwargs['org'],
   #      "locality": kwargs['locality'],
   #      "state": kwargs['state'],
   #      "country_code": country_codes[kwargs['country']]
   #  }

   #  if 'org_unit' in kwargs and kwargs['org_unit']:
   #      params['organizational_unit'] = kwargs['org_unit']

   #  if current_certificate.check_prop_match(**params):
   #      return True, current_certificate
   #  return False, None


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
