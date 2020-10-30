"""This module contains the general information for CertificateManagement ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CertificateManagementConsts:
    ADMIN_ACTION_ACTIVATE_EXTERNAL_CERT = "activate-external-cert"


class CertificateManagement(ManagedObject):
    """This is CertificateManagement class."""

    consts = CertificateManagementConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("CertificateManagement", "certificateManagement", "cert-mgmt", VersionMeta.Version209c, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['topSystem'], ['currentCertificate', 'generateCertificateSigningRequest', 'uploadCertificate', 'uploadExternalCertificate', 'uploadExternalPrivateKey'], ["Get"]),
        "modular": MoMeta("CertificateManagement", "certificateManagement", "cert-mgmt", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['topSystem'], ['currentCertificate', 'generateCertificateSigningRequest', 'uploadCertificate', 'uploadExternalCertificate', 'uploadExternalPrivateKey'], ["Get"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["activate-external-cert"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version209c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "external_certificate": MoPropertyMeta("external_certificate", "externalCertificate", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "external_private_key": MoPropertyMeta("external_private_key", "externalPrivateKey", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["activate-external-cert"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "external_certificate": MoPropertyMeta("external_certificate", "externalCertificate", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "external_private_key": MoPropertyMeta("external_private_key", "externalPrivateKey", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "description": "description", 
            "externalCertificate": "external_certificate", 
            "externalPrivateKey": "external_private_key", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "description": "description", 
            "externalCertificate": "external_certificate", 
            "externalPrivateKey": "external_private_key", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.status = None
        self.child_action = None
        self.description = None
        self.external_certificate = None
        self.external_private_key = None

        ManagedObject.__init__(self, "CertificateManagement", parent_mo_or_dn, **kwargs)

