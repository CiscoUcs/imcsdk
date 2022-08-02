"""This module contains the general information for DeleteSecureBootCertificate ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class DeleteSecureBootCertificateConsts:
    ADMIN_ACTION_DELETE_SECURE_BOOT_CERT = "delete-secure-boot-cert"


class DeleteSecureBootCertificate(ManagedObject):
    """This is DeleteSecureBootCertificate class."""

    consts = DeleteSecureBootCertificateConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("DeleteSecureBootCertificate", "deleteSecureBootCertificate", "delete-secure-boot-cert", VersionMeta.Version422a, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['secureBootCertificateManagement'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete-secure-boot-cert"], []),
            "certificate_id": MoPropertyMeta("certificate_id", "certificateId", "uint", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-10"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version422a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "certificateId": "certificate_id", 
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.certificate_id = None
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "DeleteSecureBootCertificate", parent_mo_or_dn, **kwargs)

