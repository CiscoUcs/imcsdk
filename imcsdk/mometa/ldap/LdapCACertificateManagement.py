"""This module contains the general information for LdapCACertificateManagement ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LdapCACertificateManagementConsts:
    pass


class LdapCACertificateManagement(ManagedObject):
    """This is LdapCACertificateManagement class."""

    consts = LdapCACertificateManagementConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("LdapCACertificateManagement", "ldapCACertificateManagement", "ldap-ca-cert-mgmt", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "user"], [u'aaaLdap'], [u'downloadLdapCACertificate', u'exportLdapCACertificate', u'ldapCACertificate'], ["Get", "Set"]),
        "modular": MoMeta("LdapCACertificateManagement", "ldapCACertificateManagement", "ldap-ca-cert-mgmt", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'aaaLdap'], [u'downloadLdapCACertificate', u'exportLdapCACertificate', u'ldapCACertificate'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "binding_certificate": MoPropertyMeta("binding_certificate", "bindingCertificate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

        "modular": {
            "binding_certificate": MoPropertyMeta("binding_certificate", "bindingCertificate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "classic": {
            "bindingCertificate": "binding_certificate", 
            "childAction": "child_action", 
            "description": "description", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "bindingCertificate": "binding_certificate", 
            "childAction": "child_action", 
            "description": "description", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.binding_certificate = None
        self.child_action = None
        self.description = None
        self.status = None

        ManagedObject.__init__(self, "LdapCACertificateManagement", parent_mo_or_dn, **kwargs)

