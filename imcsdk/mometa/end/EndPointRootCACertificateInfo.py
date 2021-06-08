"""This module contains the general information for EndPointRootCACertificateInfo ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class EndPointRootCACertificateInfoConsts:
    ADMIN_ACTION_DELETE_END_POINT_ROOT_CA_CERTIFICATE = "delete-end-point-root-ca-certificate"


class EndPointRootCACertificateInfo(ManagedObject):
    """This is EndPointRootCACertificateInfo class."""

    consts = EndPointRootCACertificateInfoConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("EndPointRootCACertificateInfo", "endPointRootCACertificateInfo", "info", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['endPointRootCACertificate'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete-end-point-root-ca-certificate"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "common_name": MoPropertyMeta("common_name", "commonName", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "country_code": MoPropertyMeta("country_code", "countryCode", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "issuer_common_name": MoPropertyMeta("issuer_common_name", "issuerCommonName", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_country_code": MoPropertyMeta("issuer_country_code", "issuerCountryCode", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_locality": MoPropertyMeta("issuer_locality", "issuerLocality", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_organization": MoPropertyMeta("issuer_organization", "issuerOrganization", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_organizational_unit": MoPropertyMeta("issuer_organizational_unit", "issuerOrganizationalUnit", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "issuer_state": MoPropertyMeta("issuer_state", "issuerState", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "locality": MoPropertyMeta("locality", "locality", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "organization": MoPropertyMeta("organization", "organization", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "organizational_unit": MoPropertyMeta("organizational_unit", "organizationalUnit", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "serial_number": MoPropertyMeta("serial_number", "serialNumber", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 243, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "valid_from": MoPropertyMeta("valid_from", "validFrom", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "valid_to": MoPropertyMeta("valid_to", "validTo", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
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
        self.admin_action = None
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

        ManagedObject.__init__(self, "EndPointRootCACertificateInfo", parent_mo_or_dn, **kwargs)

