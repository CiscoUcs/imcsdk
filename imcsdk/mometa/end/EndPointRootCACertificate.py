"""This module contains the general information for EndPointRootCACertificate ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class EndPointRootCACertificateConsts:
    USER_UPLOADABLE_NO = "no"
    USER_UPLOADABLE_YES = "yes"


class EndPointRootCACertificate(ManagedObject):
    """This is EndPointRootCACertificate class."""

    consts = EndPointRootCACertificateConsts()
    naming_props = set(['certificateId'])

    mo_meta = {
        "classic": MoMeta("EndPointRootCACertificate", "endPointRootCACertificate", "end-point-cert-[certificate_id]", VersionMeta.Version421a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['mctpCertificateManagement'], ['endPointRootCACertificateInfo'], [None]),
    }


    prop_meta = {

        "classic": {
            "certificate_id": MoPropertyMeta("certificate_id", "certificateId", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "issuer_common_name": MoPropertyMeta("issuer_common_name", "issuerCommonName", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 64, None, [], []),
            "issuer_organization": MoPropertyMeta("issuer_organization", "issuerOrganization", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 64, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "user_uploadable": MoPropertyMeta("user_uploadable", "userUploadable", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
            "valid_to": MoPropertyMeta("valid_to", "validTo", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "certificateId": "certificate_id", 
            "childAction": "child_action", 
            "dn": "dn", 
            "issuerCommonName": "issuer_common_name", 
            "issuerOrganization": "issuer_organization", 
            "rn": "rn", 
            "status": "status", 
            "userUploadable": "user_uploadable", 
            "validTo": "valid_to", 
        },

    }

    def __init__(self, parent_mo_or_dn, certificate_id, **kwargs):
        self._dirty_mask = 0
        self.certificate_id = certificate_id
        self.child_action = None
        self.issuer_common_name = None
        self.issuer_organization = None
        self.status = None
        self.user_uploadable = None
        self.valid_to = None

        ManagedObject.__init__(self, "EndPointRootCACertificate", parent_mo_or_dn, **kwargs)

