"""This module contains the general information for GenerateCertificateSigningRequest ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class GenerateCertificateSigningRequestConsts:
    COUNTRY_CODE_ALBANIA = "Albania"
    COUNTRY_CODE_ALGERIA = "Algeria"
    COUNTRY_CODE_AMERICAN_SAMOA = "American Samoa"
    COUNTRY_CODE_ANDORRA = "Andorra"
    COUNTRY_CODE_ANGOLA = "Angola"
    COUNTRY_CODE_ANGUILLA = "Anguilla"
    COUNTRY_CODE_ANTARCTICA = "Antarctica"
    COUNTRY_CODE_ANTIGUA_AND_BARBUDA = "Antigua and Barbuda"
    COUNTRY_CODE_ARGENTINA = "Argentina"
    COUNTRY_CODE_ARMENIA = "Armenia"
    COUNTRY_CODE_ARUBA = "Aruba"
    COUNTRY_CODE_AUSTRALIA = "Australia"
    COUNTRY_CODE_AUSTRIA = "Austria"
    COUNTRY_CODE_AZERBAIJAN = "Azerbaijan"
    COUNTRY_CODE_BAHAMAS = "Bahamas"
    COUNTRY_CODE_BAHRAIN = "Bahrain"
    COUNTRY_CODE_BANGLADESH = "Bangladesh"
    COUNTRY_CODE_BARBADOS = "Barbados"
    COUNTRY_CODE_BELARUS = "Belarus"
    COUNTRY_CODE_BELGIUM = "Belgium"
    COUNTRY_CODE_BELIZE = "Belize"
    COUNTRY_CODE_BENIN = "Benin"
    COUNTRY_CODE_BERMUDA = "Bermuda"
    COUNTRY_CODE_BHUTAN = "Bhutan"
    COUNTRY_CODE_BOLIVIA = "Bolivia"
    COUNTRY_CODE_BOSNIA_AND_HERZEGOVINA = "Bosnia and Herzegovina"
    COUNTRY_CODE_BOTSWANA = "Botswana"
    COUNTRY_CODE_BOUVET_ISLAND = "Bouvet Island"
    COUNTRY_CODE_BRAZIL = "Brazil"
    COUNTRY_CODE_BRITISH_INDIAN_OCEAN_TERRITORY = "British Indian Ocean Territory"
    COUNTRY_CODE_BRUNEI_DARUSSALAM = "Brunei Darussalam"
    COUNTRY_CODE_BULGARIA = "Bulgaria"
    COUNTRY_CODE_BURKINA_FASO = "Burkina Faso"
    COUNTRY_CODE_BURUNDI = "Burundi"
    COUNTRY_CODE_CAMBODIA = "Cambodia"
    COUNTRY_CODE_CAMEROON = "Cameroon"
    COUNTRY_CODE_CANADA = "Canada"
    COUNTRY_CODE_CAPE_VERDE = "Cape Verde"
    COUNTRY_CODE_CAYMAN_ISLANDS = "Cayman Islands"
    COUNTRY_CODE_CENTRAL_AFRICAN_REPUBLIC = "Central African Republic"
    COUNTRY_CODE_CHAD = "Chad"
    COUNTRY_CODE_CHILE = "Chile"
    COUNTRY_CODE_CHINA = "China"
    COUNTRY_CODE_CHRISTMAS_ISLAND = "Christmas Island"
    COUNTRY_CODE_COCOS_KEELING_ISLANDS = "Cocos (Keeling) Islands"
    COUNTRY_CODE_COLOMBIA = "Colombia"
    COUNTRY_CODE_COMOROS = "Comoros"
    COUNTRY_CODE_CONGO = "Congo"
    COUNTRY_CODE_COOK_ISLANDS = "Cook Islands"
    COUNTRY_CODE_COSTA_RICA = "Costa Rica"
    COUNTRY_CODE_COTE_D_IVOIRE_IVORY_COAST = "Cote D'Ivoire (Ivory Coast)"
    COUNTRY_CODE_CROATIA_HRVATSKA = "Croatia (Hrvatska)"
    COUNTRY_CODE_CUBA = "Cuba"
    COUNTRY_CODE_CYPRUS = "Cyprus"
    COUNTRY_CODE_CZECH_REPUBLIC = "Czech Republic"
    COUNTRY_CODE_CZECHOSLOVAKIA = "Czechoslovakia"
    COUNTRY_CODE_DENMARK = "Denmark"
    COUNTRY_CODE_DJIBOUTI = "Djibouti"
    COUNTRY_CODE_DOMINICA = "Dominica"
    COUNTRY_CODE_DOMINICAN_REPUBLIC = "Dominican Republic"
    COUNTRY_CODE_EAST_TIMOR = "East Timor"
    COUNTRY_CODE_ECUADOR = "Ecuador"
    COUNTRY_CODE_EGYPT = "Egypt"
    COUNTRY_CODE_EL_SALVADOR = "El Salvador"
    COUNTRY_CODE_EQUATORIAL_GUINEA = "Equatorial Guinea"
    COUNTRY_CODE_ERITREA = "Eritrea"
    COUNTRY_CODE_ESTONIA = "Estonia"
    COUNTRY_CODE_ETHIOPIA = "Ethiopia"
    COUNTRY_CODE_FALKLAND_ISLANDS_MALVINAS = "Falkland Islands (Malvinas)"
    COUNTRY_CODE_FAROE_ISLANDS = "Faroe Islands"
    COUNTRY_CODE_FIJI = "Fiji"
    COUNTRY_CODE_FINLAND = "Finland"
    COUNTRY_CODE_FRANCE = "France"
    COUNTRY_CODE_FRANCE_METROPOLITAN = "France, Metropolitan"
    COUNTRY_CODE_FRENCH_GUIANA = "French Guiana"
    COUNTRY_CODE_FRENCH_POLYNESIA = "French Polynesia"
    COUNTRY_CODE_FRENCH_SOUTHERN_TERRITORIES = "French Southern Territories"
    COUNTRY_CODE_GABON = "Gabon"
    COUNTRY_CODE_GAMBIA = "Gambia"
    COUNTRY_CODE_GEORGIA = "Georgia"
    COUNTRY_CODE_GERMANY = "Germany"
    COUNTRY_CODE_GHANA = "Ghana"
    COUNTRY_CODE_GIBRALTAR = "Gibraltar"
    COUNTRY_CODE_GREAT_BRITAIN_UK = "Great Britain (UK)"
    COUNTRY_CODE_GREECE = "Greece"
    COUNTRY_CODE_GREENLAND = "Greenland"
    COUNTRY_CODE_GRENADA = "Grenada"
    COUNTRY_CODE_GUADELOUPE = "Guadeloupe"
    COUNTRY_CODE_GUAM = "Guam"
    COUNTRY_CODE_GUATEMALA = "Guatemala"
    COUNTRY_CODE_GUINEA = "Guinea"
    COUNTRY_CODE_GUINEA_BISSAU = "Guinea-Bissau"
    COUNTRY_CODE_GUYANA = "Guyana"
    COUNTRY_CODE_HAITI = "Haiti"
    COUNTRY_CODE_HEARD_AND_MC_DONALD_ISLANDS = "Heard and McDonald Islands"
    COUNTRY_CODE_HONDURAS = "Honduras"
    COUNTRY_CODE_HONG_KONG = "Hong Kong"
    COUNTRY_CODE_HUNGARY = "Hungary"
    COUNTRY_CODE_ICELAND = "Iceland"
    COUNTRY_CODE_INDIA = "India"
    COUNTRY_CODE_INDONESIA = "Indonesia"
    COUNTRY_CODE_IRAN = "Iran"
    COUNTRY_CODE_IRAQ = "Iraq"
    COUNTRY_CODE_IRELAND = "Ireland"
    COUNTRY_CODE_ISRAEL = "Israel"
    COUNTRY_CODE_ITALY = "Italy"
    COUNTRY_CODE_JAMAICA = "Jamaica"
    COUNTRY_CODE_JAPAN = "Japan"
    COUNTRY_CODE_JORDAN = "Jordan"
    COUNTRY_CODE_KAZAKHSTAN = "Kazakhstan"
    COUNTRY_CODE_KENYA = "Kenya"
    COUNTRY_CODE_KIRIBATI = "Kiribati"
    COUNTRY_CODE_KOREA_NORTH = "Korea (North)"
    COUNTRY_CODE_KOREA_SOUTH = "Korea (South)"
    COUNTRY_CODE_KUWAIT = "Kuwait"
    COUNTRY_CODE_KYRGYZSTAN = "Kyrgyzstan"
    COUNTRY_CODE_LAOS = "Laos"
    COUNTRY_CODE_LATVIA = "Latvia"
    COUNTRY_CODE_LEBANON = "Lebanon"
    COUNTRY_CODE_LESOTHO = "Lesotho"
    COUNTRY_CODE_LIBERIA = "Liberia"
    COUNTRY_CODE_LIBYA = "Libya"
    COUNTRY_CODE_LIECHTENSTEIN = "Liechtenstein"
    COUNTRY_CODE_LITHUANIA = "Lithuania"
    COUNTRY_CODE_LUXEMBOURG = "Luxembourg"
    COUNTRY_CODE_MACAU = "Macau"
    COUNTRY_CODE_MACEDONIA = "Macedonia"
    COUNTRY_CODE_MADAGASCAR = "Madagascar"
    COUNTRY_CODE_MALAWI = "Malawi"
    COUNTRY_CODE_MALAYSIA = "Malaysia"
    COUNTRY_CODE_MALDIVES = "Maldives"
    COUNTRY_CODE_MALI = "Mali"
    COUNTRY_CODE_MALTA = "Malta"
    COUNTRY_CODE_MARSHALL_ISLANDS = "Marshall Islands"
    COUNTRY_CODE_MARTINIQUE = "Martinique"
    COUNTRY_CODE_MAURITANIA = "Mauritania"
    COUNTRY_CODE_MAURITIUS = "Mauritius"
    COUNTRY_CODE_MAYOTTE = "Mayotte"
    COUNTRY_CODE_MEXICO = "Mexico"
    COUNTRY_CODE_MICRONESIA = "Micronesia"
    COUNTRY_CODE_MOLDOVA = "Moldova"
    COUNTRY_CODE_MONACO = "Monaco"
    COUNTRY_CODE_MONGOLIA = "Mongolia"
    COUNTRY_CODE_MONTSERRAT = "Montserrat"
    COUNTRY_CODE_MOROCCO = "Morocco"
    COUNTRY_CODE_MOZAMBIQUE = "Mozambique"
    COUNTRY_CODE_MYANMAR = "Myanmar"
    COUNTRY_CODE_NAMIBIA = "Namibia"
    COUNTRY_CODE_NAURU = "Nauru"
    COUNTRY_CODE_NEPAL = "Nepal"
    COUNTRY_CODE_NETHERLANDS = "Netherlands"
    COUNTRY_CODE_NETHERLANDS_ANTILLES = "Netherlands Antilles"
    COUNTRY_CODE_NEUTRAL_ZONE = "Neutral Zone"
    COUNTRY_CODE_NEW_CALEDONIA = "New Caledonia"
    COUNTRY_CODE_NEW_ZEALAND_AOTEAROA = "New Zealand (Aotearoa)"
    COUNTRY_CODE_NICARAGUA = "Nicaragua"
    COUNTRY_CODE_NIGER = "Niger"
    COUNTRY_CODE_NIGERIA = "Nigeria"
    COUNTRY_CODE_NIUE = "Niue"
    COUNTRY_CODE_NORFOLK_ISLAND = "Norfolk Island"
    COUNTRY_CODE_NORTHERN_MARIANA_ISLANDS = "Northern Mariana Islands"
    COUNTRY_CODE_NORWAY = "Norway"
    COUNTRY_CODE_OMAN = "Oman"
    COUNTRY_CODE_PAKISTAN = "Pakistan"
    COUNTRY_CODE_PALAU = "Palau"
    COUNTRY_CODE_PANAMA = "Panama"
    COUNTRY_CODE_PAPUA_NEW_GUINEA = "Papua New Guinea"
    COUNTRY_CODE_PARAGUAY = "Paraguay"
    COUNTRY_CODE_PERU = "Peru"
    COUNTRY_CODE_PHILIPPINES = "Philippines"
    COUNTRY_CODE_PITCAIRN = "Pitcairn"
    COUNTRY_CODE_POLAND = "Poland"
    COUNTRY_CODE_PORTUGAL = "Portugal"
    COUNTRY_CODE_PUERTO_RICO = "Puerto Rico"
    COUNTRY_CODE_QATAR = "Qatar"
    COUNTRY_CODE_REUNION = "Reunion"
    COUNTRY_CODE_ROMANIA = "Romania"
    COUNTRY_CODE_RUSSIAN_FEDERATION = "Russian Federation"
    COUNTRY_CODE_RWANDA = "Rwanda"
    COUNTRY_CODE_S_GEORGIA_AND_S_SANDWICH_ISLS_ = "S. Georgia and S. Sandwich Isls."
    COUNTRY_CODE_SAINT_KITTS_AND_NEVIS = "Saint Kitts and Nevis"
    COUNTRY_CODE_SAINT_LUCIA = "Saint Lucia"
    COUNTRY_CODE_SAINT_VINCENT_AND_THE_GRENADINES = "Saint Vincent and the Grenadines"
    COUNTRY_CODE_SAMOA = "Samoa"
    COUNTRY_CODE_SAN_MARINO = "San Marino"
    COUNTRY_CODE_SAO_TOME_AND_PRINCIPE = "Sao Tome and Principe"
    COUNTRY_CODE_SAUDI_ARABIA = "Saudi Arabia"
    COUNTRY_CODE_SENEGAL = "Senegal"
    COUNTRY_CODE_SEYCHELLES = "Seychelles"
    COUNTRY_CODE_SIERRA_LEONE = "Sierra Leone"
    COUNTRY_CODE_SINGAPORE = "Singapore"
    COUNTRY_CODE_SLOVAK_REPUBLIC = "Slovak Republic"
    COUNTRY_CODE_SLOVENIA = "Slovenia"
    COUNTRY_CODE_SOLOMON_ISLANDS = "Solomon Islands"
    COUNTRY_CODE_SOMALIA = "Somalia"
    COUNTRY_CODE_SOUTH_AFRICA = "South Africa"
    COUNTRY_CODE_SPAIN = "Spain"
    COUNTRY_CODE_SRI_LANKA = "Sri Lanka"
    COUNTRY_CODE_ST_HELENA = "St. Helena"
    COUNTRY_CODE_ST_PIERRE_AND_MIQUELON = "St. Pierre and Miquelon"
    COUNTRY_CODE_SUDAN = "Sudan"
    COUNTRY_CODE_SURINAME = "Suriname"
    COUNTRY_CODE_SVALBARD_AND_JAN_MAYEN_ISLANDS = "Svalbard and Jan Mayen Islands"
    COUNTRY_CODE_SWAZILAND = "Swaziland"
    COUNTRY_CODE_SWEDEN = "Sweden"
    COUNTRY_CODE_SWITZERLAND = "Switzerland"
    COUNTRY_CODE_SYRIA = "Syria"
    COUNTRY_CODE_TAIWAN = "Taiwan"
    COUNTRY_CODE_TAJIKISTAN = "Tajikistan"
    COUNTRY_CODE_TANZANIA = "Tanzania"
    COUNTRY_CODE_THAILAND = "Thailand"
    COUNTRY_CODE_TOGO = "Togo"
    COUNTRY_CODE_TOKELAU = "Tokelau"
    COUNTRY_CODE_TONGA = "Tonga"
    COUNTRY_CODE_TRINIDAD_AND_TOBAGO = "Trinidad and Tobago"
    COUNTRY_CODE_TUNISIA = "Tunisia"
    COUNTRY_CODE_TURKEY = "Turkey"
    COUNTRY_CODE_TURKMENISTAN = "Turkmenistan"
    COUNTRY_CODE_TURKS_AND_CAICOS_ISLANDS = "Turks and Caicos Islands"
    COUNTRY_CODE_TUVALU = "Tuvalu"
    COUNTRY_CODE_US_MINOR_OUTLYING_ISLANDS = "US Minor Outlying Islands"
    COUNTRY_CODE_USSR_FORMER = "USSR (former)"
    COUNTRY_CODE_UGANDA = "Uganda"
    COUNTRY_CODE_UKRAINE = "Ukraine"
    COUNTRY_CODE_UNITED_ARAB_EMIRATES = "United Arab Emirates"
    COUNTRY_CODE_UNITED_KINGDOM = "United Kingdom"
    COUNTRY_CODE_UNITED_STATES = "United States"
    COUNTRY_CODE_URUGUAY = "Uruguay"
    COUNTRY_CODE_UZBEKISTAN = "Uzbekistan"
    COUNTRY_CODE_VANUATU = "Vanuatu"
    COUNTRY_CODE_VATICAN_CITY_STATE_HOLY_SEE = "Vatican City State (Holy See)"
    COUNTRY_CODE_VENEZUELA = "Venezuela"
    COUNTRY_CODE_VIET_NAM = "Viet Nam"
    COUNTRY_CODE_VIRGIN_ISLANDS_BRITISH = "Virgin Islands (British)"
    COUNTRY_CODE_VIRGIN_ISLANDS_U_S_ = "Virgin Islands (U.S.)"
    COUNTRY_CODE_WALLIS_AND_FUTUNA_ISLANDS = "Wallis and Futuna Islands"
    COUNTRY_CODE_WESTERN_SAHARA = "Western Sahara"
    COUNTRY_CODE_YEMEN = "Yemen"
    COUNTRY_CODE_YUGOSLAVIA = "Yugoslavia"
    COUNTRY_CODE_ZAIRE = "Zaire"
    COUNTRY_CODE_ZAMBIA = "Zambia"
    COUNTRY_CODE_ZIMBABWE = "Zimbabwe"
    PROTOCOL_FTP = "ftp"
    PROTOCOL_HTTP = "http"
    PROTOCOL_NONE = "none"
    PROTOCOL_SCP = "scp"
    PROTOCOL_SFTP = "sftp"
    PROTOCOL_TFTP = "tftp"
    SELF_SIGNED_NO = "No"
    SELF_SIGNED_YES = "Yes"
    _SELF_SIGNED_NO = "no"
    _SELF_SIGNED_YES = "yes"
    SIGNATURE_ALGORITHM_SHA1 = "sha1"
    SIGNATURE_ALGORITHM_SHA256 = "sha256"
    SIGNATURE_ALGORITHM_SHA384 = "sha384"
    SIGNATURE_ALGORITHM_SHA512 = "sha512"
    STRING_MASK_DEFAULT = "default"
    STRING_MASK_NOMBSTR = "nombstr"
    STRING_MASK_PKIX = "pkix"
    STRING_MASK_UTF8ONLY = "utf8only"
    SUBJECT_ALT_NAME_TYPE1_DNS = "DNS"
    SUBJECT_ALT_NAME_TYPE1_EMAIL = "EMAIL"
    SUBJECT_ALT_NAME_TYPE1_IP = "IP"
    SUBJECT_ALT_NAME_TYPE1_URI = "URI"
    _SUBJECT_ALT_NAME_TYPE1_DNS = "dns"
    _SUBJECT_ALT_NAME_TYPE1_EMAIL = "email"
    _SUBJECT_ALT_NAME_TYPE1_IP = "ip"
    _SUBJECT_ALT_NAME_TYPE1_URI = "uri"
    SUBJECT_ALT_NAME_TYPE10_DNS = "DNS"
    SUBJECT_ALT_NAME_TYPE10_EMAIL = "EMAIL"
    SUBJECT_ALT_NAME_TYPE10_IP = "IP"
    SUBJECT_ALT_NAME_TYPE10_URI = "URI"
    _SUBJECT_ALT_NAME_TYPE10_DNS = "dns"
    _SUBJECT_ALT_NAME_TYPE10_EMAIL = "email"
    _SUBJECT_ALT_NAME_TYPE10_IP = "ip"
    _SUBJECT_ALT_NAME_TYPE10_URI = "uri"
    SUBJECT_ALT_NAME_TYPE2_DNS = "DNS"
    SUBJECT_ALT_NAME_TYPE2_EMAIL = "EMAIL"
    SUBJECT_ALT_NAME_TYPE2_IP = "IP"
    SUBJECT_ALT_NAME_TYPE2_URI = "URI"
    _SUBJECT_ALT_NAME_TYPE2_DNS = "dns"
    _SUBJECT_ALT_NAME_TYPE2_EMAIL = "email"
    _SUBJECT_ALT_NAME_TYPE2_IP = "ip"
    _SUBJECT_ALT_NAME_TYPE2_URI = "uri"
    SUBJECT_ALT_NAME_TYPE3_DNS = "DNS"
    SUBJECT_ALT_NAME_TYPE3_EMAIL = "EMAIL"
    SUBJECT_ALT_NAME_TYPE3_IP = "IP"
    SUBJECT_ALT_NAME_TYPE3_URI = "URI"
    _SUBJECT_ALT_NAME_TYPE3_DNS = "dns"
    _SUBJECT_ALT_NAME_TYPE3_EMAIL = "email"
    _SUBJECT_ALT_NAME_TYPE3_IP = "ip"
    _SUBJECT_ALT_NAME_TYPE3_URI = "uri"
    SUBJECT_ALT_NAME_TYPE4_DNS = "DNS"
    SUBJECT_ALT_NAME_TYPE4_EMAIL = "EMAIL"
    SUBJECT_ALT_NAME_TYPE4_IP = "IP"
    SUBJECT_ALT_NAME_TYPE4_URI = "URI"
    _SUBJECT_ALT_NAME_TYPE4_DNS = "dns"
    _SUBJECT_ALT_NAME_TYPE4_EMAIL = "email"
    _SUBJECT_ALT_NAME_TYPE4_IP = "ip"
    _SUBJECT_ALT_NAME_TYPE4_URI = "uri"
    SUBJECT_ALT_NAME_TYPE5_DNS = "DNS"
    SUBJECT_ALT_NAME_TYPE5_EMAIL = "EMAIL"
    SUBJECT_ALT_NAME_TYPE5_IP = "IP"
    SUBJECT_ALT_NAME_TYPE5_URI = "URI"
    _SUBJECT_ALT_NAME_TYPE5_DNS = "dns"
    _SUBJECT_ALT_NAME_TYPE5_EMAIL = "email"
    _SUBJECT_ALT_NAME_TYPE5_IP = "ip"
    _SUBJECT_ALT_NAME_TYPE5_URI = "uri"
    SUBJECT_ALT_NAME_TYPE6_DNS = "DNS"
    SUBJECT_ALT_NAME_TYPE6_EMAIL = "EMAIL"
    SUBJECT_ALT_NAME_TYPE6_IP = "IP"
    SUBJECT_ALT_NAME_TYPE6_URI = "URI"
    _SUBJECT_ALT_NAME_TYPE6_DNS = "dns"
    _SUBJECT_ALT_NAME_TYPE6_EMAIL = "email"
    _SUBJECT_ALT_NAME_TYPE6_IP = "ip"
    _SUBJECT_ALT_NAME_TYPE6_URI = "uri"
    SUBJECT_ALT_NAME_TYPE7_DNS = "DNS"
    SUBJECT_ALT_NAME_TYPE7_EMAIL = "EMAIL"
    SUBJECT_ALT_NAME_TYPE7_IP = "IP"
    SUBJECT_ALT_NAME_TYPE7_URI = "URI"
    _SUBJECT_ALT_NAME_TYPE7_DNS = "dns"
    _SUBJECT_ALT_NAME_TYPE7_EMAIL = "email"
    _SUBJECT_ALT_NAME_TYPE7_IP = "ip"
    _SUBJECT_ALT_NAME_TYPE7_URI = "uri"
    SUBJECT_ALT_NAME_TYPE8_DNS = "DNS"
    SUBJECT_ALT_NAME_TYPE8_EMAIL = "EMAIL"
    SUBJECT_ALT_NAME_TYPE8_IP = "IP"
    SUBJECT_ALT_NAME_TYPE8_URI = "URI"
    _SUBJECT_ALT_NAME_TYPE8_DNS = "dns"
    _SUBJECT_ALT_NAME_TYPE8_EMAIL = "email"
    _SUBJECT_ALT_NAME_TYPE8_IP = "ip"
    _SUBJECT_ALT_NAME_TYPE8_URI = "uri"
    SUBJECT_ALT_NAME_TYPE9_DNS = "DNS"
    SUBJECT_ALT_NAME_TYPE9_EMAIL = "EMAIL"
    SUBJECT_ALT_NAME_TYPE9_IP = "IP"
    SUBJECT_ALT_NAME_TYPE9_URI = "URI"
    _SUBJECT_ALT_NAME_TYPE9_DNS = "dns"
    _SUBJECT_ALT_NAME_TYPE9_EMAIL = "email"
    _SUBJECT_ALT_NAME_TYPE9_IP = "ip"
    _SUBJECT_ALT_NAME_TYPE9_URI = "uri"
    COUNTRY_CODE_COCOS_KEELING_ISLANDS = "Cocos (Keeling) Islands"
    COUNTRY_CODE_COTE_D_IVOIRE_IVORY_COAST = "Cote D'Ivoire (Ivory Coast)"
    COUNTRY_CODE_CROATIA_HRVATSKA = "Croatia (Hrvatska)"
    COUNTRY_CODE_FALKLAND_ISLANDS_MALVINAS = "Falkland Islands (Malvinas)"
    COUNTRY_CODE_GREAT_BRITAIN_UK = "Great Britain (UK)"
    COUNTRY_CODE_KOREA_NORTH = "Korea (North)"
    COUNTRY_CODE_KOREA_SOUTH = "Korea (South)"
    COUNTRY_CODE_NEW_ZEALAND_AOTEAROA = "New Zealand (Aotearoa)"
    COUNTRY_CODE_USSR_FORMER = "USSR (former)"
    COUNTRY_CODE_VATICAN_CITY_STATE_HOLY_SEE = "Vatican City State (Holy See)"
    COUNTRY_CODE_VIRGIN_ISLANDS_BRITISH = "Virgin Islands (British)"
    COUNTRY_CODE_VIRGIN_ISLANDS_U_S_ = "Virgin Islands (U.S.)"


class GenerateCertificateSigningRequest(ManagedObject):
    """This is GenerateCertificateSigningRequest class."""

    consts = GenerateCertificateSigningRequestConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("GenerateCertificateSigningRequest", "generateCertificateSigningRequest", "gen-csr-req", VersionMeta.Version209c, "InputOutput", 0x1ffffffffff, [], ["admin", "read-only", "user"], ['certificateManagement'], [], [None]),
        "modular": MoMeta("GenerateCertificateSigningRequest", "generateCertificateSigningRequest", "gen-csr-req", VersionMeta.Version2013e, "InputOutput", 0x1ffffffffff, [], ["admin", "read-only", "user"], ['certificateManagement'], [], [None])
    }


    prop_meta = {

        "classic": {
            "add_challenge_password": MoPropertyMeta("add_challenge_password", "addChallengePassword", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "challenge_password": MoPropertyMeta("challenge_password", "challengePassword", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 20, r"""[^""#]{0,20}""", [], []),
            "common_name": MoPropertyMeta("common_name", "commonName", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x8, 1, 64, r"""[^""#]{1,64}""", [], []),
            "country_code": MoPropertyMeta("country_code", "countryCode", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x10, 1, 510, None, ["Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Cook Islands", "Costa Rica", "Cote D'Ivoire (Ivory Coast)", "Croatia (Hrvatska)", "Cuba", "Cyprus", "Czech Republic", "Czechoslovakia", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji", "Finland", "France", "France, Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Great Britain (UK)", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and McDonald Islands", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea (North)", "Korea (South)", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "Neutral Zone", "New Caledonia", "New Zealand (Aotearoa)", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "S. Georgia and S. Sandwich Isls.", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovak Republic", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "US Minor Outlying Islands", "USSR (former)", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City State (Holy See)", "Venezuela", "Viet Nam", "Virgin Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia", "Zaire", "Zambia", "Zimbabwe"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "email": MoPropertyMeta("email", "email", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x40, 0, 128, r"""[_\-a-zA-Z0-9\.\+]+@[a-zA-Z0-9](\.?[\-a-zA-Z0-9]*[a-zA-Z0-9])*""", [], []),
            "locality": MoPropertyMeta("locality", "locality", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x80, 1, 128, r"""[^""#]{1,128}""", [], []),
            "organization": MoPropertyMeta("organization", "organization", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x100, 1, 64, r"""[^""#]{1,64}""", [], []),
            "organizational_unit": MoPropertyMeta("organizational_unit", "organizationalUnit", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x200, 1, 64, r"""[^""#]{1,64}""", [], []),
            "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,255}""", [], []),
            "remote_server": MoPropertyMeta("remote_server", "remoteServer", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x2000, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x4000, 0, 255, None, [], []),
            "self_signed": MoPropertyMeta("self_signed", "selfSigned", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["No", "Yes", "no", "yes"], []),
            "signature_algorithm": MoPropertyMeta("signature_algorithm", "signatureAlgorithm", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10000, 0, 510, None, ["sha1", "sha256", "sha384", "sha512"], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x20000, 1, 128, r"""[^""#]{1,128}""", [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "string_mask": MoPropertyMeta("string_mask", "stringMask", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x80000, 0, 8, None, ["default", "nombstr", "pkix", "utf8only"], []),
            "subject_alt_name_type1": MoPropertyMeta("subject_alt_name_type1", "subjectAltNameType1", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x100000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type10": MoPropertyMeta("subject_alt_name_type10", "subjectAltNameType10", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x200000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type2": MoPropertyMeta("subject_alt_name_type2", "subjectAltNameType2", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x400000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type3": MoPropertyMeta("subject_alt_name_type3", "subjectAltNameType3", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x800000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type4": MoPropertyMeta("subject_alt_name_type4", "subjectAltNameType4", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x1000000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type5": MoPropertyMeta("subject_alt_name_type5", "subjectAltNameType5", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2000000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type6": MoPropertyMeta("subject_alt_name_type6", "subjectAltNameType6", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4000000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type7": MoPropertyMeta("subject_alt_name_type7", "subjectAltNameType7", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8000000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type8": MoPropertyMeta("subject_alt_name_type8", "subjectAltNameType8", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10000000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type9": MoPropertyMeta("subject_alt_name_type9", "subjectAltNameType9", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x20000000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_value1": MoPropertyMeta("subject_alt_name_value1", "subjectAltNameValue1", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x40000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value10": MoPropertyMeta("subject_alt_name_value10", "subjectAltNameValue10", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x80000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value2": MoPropertyMeta("subject_alt_name_value2", "subjectAltNameValue2", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x100000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value3": MoPropertyMeta("subject_alt_name_value3", "subjectAltNameValue3", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x200000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value4": MoPropertyMeta("subject_alt_name_value4", "subjectAltNameValue4", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x400000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value5": MoPropertyMeta("subject_alt_name_value5", "subjectAltNameValue5", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x800000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value6": MoPropertyMeta("subject_alt_name_value6", "subjectAltNameValue6", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x1000000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value7": MoPropertyMeta("subject_alt_name_value7", "subjectAltNameValue7", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2000000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value8": MoPropertyMeta("subject_alt_name_value8", "subjectAltNameValue8", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4000000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value9": MoPropertyMeta("subject_alt_name_value9", "subjectAltNameValue9", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8000000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x10000000000, 0, 255, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version209c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "csr_status": MoPropertyMeta("csr_status", "csrStatus", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "add_challenge_password": MoPropertyMeta("add_challenge_password", "addChallengePassword", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["No", "Yes", "no", "yes"], []),
            "challenge_password": MoPropertyMeta("challenge_password", "challengePassword", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 20, r"""[^""#]{0,20}""", [], []),
            "common_name": MoPropertyMeta("common_name", "commonName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 1, 64, r"""[^""#]{1,64}""", [], []),
            "country_code": MoPropertyMeta("country_code", "countryCode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 1, 510, None, ["Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Cook Islands", "Costa Rica", "Cote D'Ivoire (Ivory Coast)", "Croatia (Hrvatska)", "Cuba", "Cyprus", "Czech Republic", "Czechoslovakia", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji", "Finland", "France", "France, Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Great Britain (UK)", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and McDonald Islands", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea (North)", "Korea (South)", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "Neutral Zone", "New Caledonia", "New Zealand (Aotearoa)", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "S. Georgia and S. Sandwich Isls.", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovak Republic", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "US Minor Outlying Islands", "USSR (former)", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City State (Holy See)", "Venezuela", "Viet Nam", "Virgin Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia", "Zaire", "Zambia", "Zimbabwe"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "email": MoPropertyMeta("email", "email", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 128, r"""[_\-a-zA-Z0-9\.\+]+@[a-zA-Z0-9](\.?[\-a-zA-Z0-9]*[a-zA-Z0-9])*""", [], []),
            "locality": MoPropertyMeta("locality", "locality", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 1, 128, r"""[^""#]{1,128}""", [], []),
            "organization": MoPropertyMeta("organization", "organization", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 1, 64, r"""[^""#]{1,64}""", [], []),
            "organizational_unit": MoPropertyMeta("organizational_unit", "organizationalUnit", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, 1, 64, r"""[^""#]{1,64}""", [], []),
            "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,255}""", [], []),
            "remote_server": MoPropertyMeta("remote_server", "remoteServer", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000, 0, 255, None, [], []),
            "self_signed": MoPropertyMeta("self_signed", "selfSigned", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["No", "Yes", "no", "yes"], []),
            "signature_algorithm": MoPropertyMeta("signature_algorithm", "signatureAlgorithm", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10000, 0, 510, None, ["sha1", "sha256", "sha384", "sha512"], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20000, 1, 128, r"""[^""#]{1,128}""", [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "string_mask": MoPropertyMeta("string_mask", "stringMask", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x80000, 0, 8, None, ["default", "nombstr", "pkix", "utf8only"], []),
            "subject_alt_name_type1": MoPropertyMeta("subject_alt_name_type1", "subjectAltNameType1", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x100000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type10": MoPropertyMeta("subject_alt_name_type10", "subjectAltNameType10", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x200000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type2": MoPropertyMeta("subject_alt_name_type2", "subjectAltNameType2", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x400000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type3": MoPropertyMeta("subject_alt_name_type3", "subjectAltNameType3", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x800000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type4": MoPropertyMeta("subject_alt_name_type4", "subjectAltNameType4", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x1000000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type5": MoPropertyMeta("subject_alt_name_type5", "subjectAltNameType5", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2000000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type6": MoPropertyMeta("subject_alt_name_type6", "subjectAltNameType6", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4000000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type7": MoPropertyMeta("subject_alt_name_type7", "subjectAltNameType7", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8000000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type8": MoPropertyMeta("subject_alt_name_type8", "subjectAltNameType8", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10000000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_type9": MoPropertyMeta("subject_alt_name_type9", "subjectAltNameType9", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x20000000, 0, 10, None, ["DNS", "EMAIL", "IP", "URI", "dns", "email", "ip", "uri"], []),
            "subject_alt_name_value1": MoPropertyMeta("subject_alt_name_value1", "subjectAltNameValue1", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x40000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value10": MoPropertyMeta("subject_alt_name_value10", "subjectAltNameValue10", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x80000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value2": MoPropertyMeta("subject_alt_name_value2", "subjectAltNameValue2", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x100000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value3": MoPropertyMeta("subject_alt_name_value3", "subjectAltNameValue3", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x200000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value4": MoPropertyMeta("subject_alt_name_value4", "subjectAltNameValue4", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x400000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value5": MoPropertyMeta("subject_alt_name_value5", "subjectAltNameValue5", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x800000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value6": MoPropertyMeta("subject_alt_name_value6", "subjectAltNameValue6", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x1000000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value7": MoPropertyMeta("subject_alt_name_value7", "subjectAltNameValue7", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2000000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value8": MoPropertyMeta("subject_alt_name_value8", "subjectAltNameValue8", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4000000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "subject_alt_name_value9": MoPropertyMeta("subject_alt_name_value9", "subjectAltNameValue9", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8000000000, 0, 128, r"""[^""#]{0,128}""", [], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000000000, 0, 255, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "csr_status": MoPropertyMeta("csr_status", "csrStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "addChallengePassword": "add_challenge_password", 
            "challengePassword": "challenge_password", 
            "commonName": "common_name", 
            "countryCode": "country_code", 
            "dn": "dn", 
            "email": "email", 
            "locality": "locality", 
            "organization": "organization", 
            "organizationalUnit": "organizational_unit", 
            "protocol": "protocol", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "remoteServer": "remote_server", 
            "rn": "rn", 
            "selfSigned": "self_signed", 
            "signatureAlgorithm": "signature_algorithm", 
            "state": "state", 
            "status": "status", 
            "stringMask": "string_mask", 
            "subjectAltNameType1": "subject_alt_name_type1", 
            "subjectAltNameType10": "subject_alt_name_type10", 
            "subjectAltNameType2": "subject_alt_name_type2", 
            "subjectAltNameType3": "subject_alt_name_type3", 
            "subjectAltNameType4": "subject_alt_name_type4", 
            "subjectAltNameType5": "subject_alt_name_type5", 
            "subjectAltNameType6": "subject_alt_name_type6", 
            "subjectAltNameType7": "subject_alt_name_type7", 
            "subjectAltNameType8": "subject_alt_name_type8", 
            "subjectAltNameType9": "subject_alt_name_type9", 
            "subjectAltNameValue1": "subject_alt_name_value1", 
            "subjectAltNameValue10": "subject_alt_name_value10", 
            "subjectAltNameValue2": "subject_alt_name_value2", 
            "subjectAltNameValue3": "subject_alt_name_value3", 
            "subjectAltNameValue4": "subject_alt_name_value4", 
            "subjectAltNameValue5": "subject_alt_name_value5", 
            "subjectAltNameValue6": "subject_alt_name_value6", 
            "subjectAltNameValue7": "subject_alt_name_value7", 
            "subjectAltNameValue8": "subject_alt_name_value8", 
            "subjectAltNameValue9": "subject_alt_name_value9", 
            "user": "user", 
            "childAction": "child_action", 
            "csrStatus": "csr_status", 
        },

        "modular": {
            "addChallengePassword": "add_challenge_password", 
            "challengePassword": "challenge_password", 
            "commonName": "common_name", 
            "countryCode": "country_code", 
            "dn": "dn", 
            "email": "email", 
            "locality": "locality", 
            "organization": "organization", 
            "organizationalUnit": "organizational_unit", 
            "protocol": "protocol", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "remoteServer": "remote_server", 
            "rn": "rn", 
            "selfSigned": "self_signed", 
            "signatureAlgorithm": "signature_algorithm", 
            "state": "state", 
            "status": "status", 
            "stringMask": "string_mask", 
            "subjectAltNameType1": "subject_alt_name_type1", 
            "subjectAltNameType10": "subject_alt_name_type10", 
            "subjectAltNameType2": "subject_alt_name_type2", 
            "subjectAltNameType3": "subject_alt_name_type3", 
            "subjectAltNameType4": "subject_alt_name_type4", 
            "subjectAltNameType5": "subject_alt_name_type5", 
            "subjectAltNameType6": "subject_alt_name_type6", 
            "subjectAltNameType7": "subject_alt_name_type7", 
            "subjectAltNameType8": "subject_alt_name_type8", 
            "subjectAltNameType9": "subject_alt_name_type9", 
            "subjectAltNameValue1": "subject_alt_name_value1", 
            "subjectAltNameValue10": "subject_alt_name_value10", 
            "subjectAltNameValue2": "subject_alt_name_value2", 
            "subjectAltNameValue3": "subject_alt_name_value3", 
            "subjectAltNameValue4": "subject_alt_name_value4", 
            "subjectAltNameValue5": "subject_alt_name_value5", 
            "subjectAltNameValue6": "subject_alt_name_value6", 
            "subjectAltNameValue7": "subject_alt_name_value7", 
            "subjectAltNameValue8": "subject_alt_name_value8", 
            "subjectAltNameValue9": "subject_alt_name_value9", 
            "user": "user", 
            "childAction": "child_action", 
            "csrStatus": "csr_status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.add_challenge_password = None
        self.challenge_password = None
        self.common_name = None
        self.country_code = None
        self.email = None
        self.locality = None
        self.organization = None
        self.organizational_unit = None
        self.protocol = None
        self.pwd = None
        self.remote_file = None
        self.remote_server = None
        self.self_signed = None
        self.signature_algorithm = None
        self.state = None
        self.status = None
        self.string_mask = None
        self.subject_alt_name_type1 = None
        self.subject_alt_name_type10 = None
        self.subject_alt_name_type2 = None
        self.subject_alt_name_type3 = None
        self.subject_alt_name_type4 = None
        self.subject_alt_name_type5 = None
        self.subject_alt_name_type6 = None
        self.subject_alt_name_type7 = None
        self.subject_alt_name_type8 = None
        self.subject_alt_name_type9 = None
        self.subject_alt_name_value1 = None
        self.subject_alt_name_value10 = None
        self.subject_alt_name_value2 = None
        self.subject_alt_name_value3 = None
        self.subject_alt_name_value4 = None
        self.subject_alt_name_value5 = None
        self.subject_alt_name_value6 = None
        self.subject_alt_name_value7 = None
        self.subject_alt_name_value8 = None
        self.subject_alt_name_value9 = None
        self.user = None
        self.child_action = None
        self.csr_status = None

        ManagedObject.__init__(self, "GenerateCertificateSigningRequest", parent_mo_or_dn, **kwargs)

