"""This module contains the general information for CertificateManagement ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CertificateManagementConsts:
    pass


class CertificateManagement(ManagedObject):
    """This is CertificateManagement class."""

    consts = CertificateManagementConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("CertificateManagement", "certificateManagement", "cert-mgmt", VersionMeta.Version209c, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'topSystem'], [u'currentCertificate', u'generateCertificateSigningRequest', u'uploadCertificate'], ["Get"]),
        "modular": MoMeta("CertificateManagement", "certificateManagement", "cert-mgmt", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'topSystem'], [u'currentCertificate', u'generateCertificateSigningRequest', u'uploadCertificate'], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version209c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "description": "description", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "description": "description", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.description = None
        self.status = None

        ManagedObject.__init__(self, "CertificateManagement", parent_mo_or_dn, **kwargs)

