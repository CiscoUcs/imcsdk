"""This module contains the general information for SecureBootCertificateManagement ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class SecureBootCertificateManagementConsts:
    pass


class SecureBootCertificateManagement(ManagedObject):
    """This is SecureBootCertificateManagement class."""

    consts = SecureBootCertificateManagementConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("SecureBootCertificateManagement", "secureBootCertificateManagement", "secure-boot-cert-mgmt", VersionMeta.Version422a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosUnit'], ['deleteSecureBootCertificate', 'secureBootCACertificateInfo', 'uploadSecureBootCertificate'], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version422a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "error_description": MoPropertyMeta("error_description", "errorDescription", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "upload_progress": MoPropertyMeta("upload_progress", "uploadProgress", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "upload_status": MoPropertyMeta("upload_status", "uploadStatus", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "errorDescription": "error_description", 
            "rn": "rn", 
            "status": "status", 
            "uploadProgress": "upload_progress", 
            "uploadStatus": "upload_status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.error_description = None
        self.status = None
        self.upload_progress = None
        self.upload_status = None

        ManagedObject.__init__(self, "SecureBootCertificateManagement", parent_mo_or_dn, **kwargs)

