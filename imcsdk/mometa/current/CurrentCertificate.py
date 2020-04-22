"""This module contains the general information for CurrentCertificate ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CurrentCertificateConsts:
    pass


class CurrentCertificate(ManagedObject):
    """This is CurrentCertificate class."""

    consts = CurrentCertificateConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("CurrentCertificate", "currentCertificate", "curr-cert", VersionMeta.Version209c, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['certificateManagement'], [], [None]),
        "modular": MoMeta("CurrentCertificate", "currentCertificate", "curr-cert", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['certificateManagement'], [], [None])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version209c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "common_name": MoPropertyMeta("common_name", "commonName", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "country_code": MoPropertyMeta("country_code", "countryCode", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "issuer_common_name": MoPropertyMeta("issuer_common_name", "issuerCommonName", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_country_code": MoPropertyMeta("issuer_country_code", "issuerCountryCode", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_locality": MoPropertyMeta("issuer_locality", "issuerLocality", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_organization": MoPropertyMeta("issuer_organization", "issuerOrganization", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_organizational_unit": MoPropertyMeta("issuer_organizational_unit", "issuerOrganizationalUnit", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_state": MoPropertyMeta("issuer_state", "issuerState", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "locality": MoPropertyMeta("locality", "locality", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "organization": MoPropertyMeta("organization", "organization", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "organizational_unit": MoPropertyMeta("organizational_unit", "organizationalUnit", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "serial_number": MoPropertyMeta("serial_number", "serialNumber", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "valid_from": MoPropertyMeta("valid_from", "validFrom", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "valid_to": MoPropertyMeta("valid_to", "validTo", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "common_name": MoPropertyMeta("common_name", "commonName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "country_code": MoPropertyMeta("country_code", "countryCode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "issuer_common_name": MoPropertyMeta("issuer_common_name", "issuerCommonName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_country_code": MoPropertyMeta("issuer_country_code", "issuerCountryCode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_locality": MoPropertyMeta("issuer_locality", "issuerLocality", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_organization": MoPropertyMeta("issuer_organization", "issuerOrganization", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_organizational_unit": MoPropertyMeta("issuer_organizational_unit", "issuerOrganizationalUnit", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_state": MoPropertyMeta("issuer_state", "issuerState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "locality": MoPropertyMeta("locality", "locality", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "organization": MoPropertyMeta("organization", "organization", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "organizational_unit": MoPropertyMeta("organizational_unit", "organizationalUnit", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "serial_number": MoPropertyMeta("serial_number", "serialNumber", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "valid_from": MoPropertyMeta("valid_from", "validFrom", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "valid_to": MoPropertyMeta("valid_to", "validTo", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "commonName": "common_name", 
            "countryCode": "country_code", 
            "dn": "dn", 
            "issuerCommonName": "issuer_common_name", 
            "issuerCountryCode": "issuer_country_code", 
            "issuerLocality": "issuer_locality", 
            "issuerOrganization": "issuer_organization", 
            "issuerOrganizationalUnit": "issuer_organizational_unit", 
            "issuerState": "issuer_state", 
            "locality": "locality", 
            "organization": "organization", 
            "organizationalUnit": "organizational_unit", 
            "rn": "rn", 
            "serialNumber": "serial_number", 
            "state": "state", 
            "status": "status", 
            "validFrom": "valid_from", 
            "validTo": "valid_to", 
        },

        "modular": {
            "childAction": "child_action", 
            "commonName": "common_name", 
            "countryCode": "country_code", 
            "dn": "dn", 
            "issuerCommonName": "issuer_common_name", 
            "issuerCountryCode": "issuer_country_code", 
            "issuerLocality": "issuer_locality", 
            "issuerOrganization": "issuer_organization", 
            "issuerOrganizationalUnit": "issuer_organizational_unit", 
            "issuerState": "issuer_state", 
            "locality": "locality", 
            "organization": "organization", 
            "organizationalUnit": "organizational_unit", 
            "rn": "rn", 
            "serialNumber": "serial_number", 
            "state": "state", 
            "status": "status", 
            "validFrom": "valid_from", 
            "validTo": "valid_to", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.common_name = None
        self.country_code = None
        self.issuer_common_name = None
        self.issuer_country_code = None
        self.issuer_locality = None
        self.issuer_organization = None
        self.issuer_organizational_unit = None
        self.issuer_state = None
        self.locality = None
        self.organization = None
        self.organizational_unit = None
        self.serial_number = None
        self.state = None
        self.status = None
        self.valid_from = None
        self.valid_to = None

        ManagedObject.__init__(self, "CurrentCertificate", parent_mo_or_dn, **kwargs)

