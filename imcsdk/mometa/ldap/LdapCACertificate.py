"""This module contains the general information for LdapCACertificate ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LdapCACertificateConsts:
    ADMIN_ACTION_DELETE_CA_CERTIFICATE = "delete-ca-certificate"
    ADMIN_ACTION_TEST_LDAP_BINDING = "test-ldap-binding"


class LdapCACertificate(ManagedObject):
    """This is LdapCACertificate class."""

    consts = LdapCACertificateConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("LdapCACertificate", "ldapCACertificate", "ldap-ca-cert", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "user"], ['ldapCACertificateManagement'], [], ["Get", "Set"]),
        "modular": MoMeta("LdapCACertificate", "ldapCACertificate", "ldap-ca-cert", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['ldapCACertificateManagement'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete-ca-certificate", "test-ldap-binding"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete-ca-certificate", "test-ldap-binding"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "pwd": "pwd", 
            "rn": "rn", 
            "status": "status", 
            "user": "user", 
            "childAction": "child_action", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "pwd": "pwd", 
            "rn": "rn", 
            "status": "status", 
            "user": "user", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.pwd = None
        self.status = None
        self.user = None
        self.child_action = None

        ManagedObject.__init__(self, "LdapCACertificate", parent_mo_or_dn, **kwargs)

