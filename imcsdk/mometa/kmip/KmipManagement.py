"""This module contains the general information for KmipManagement ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class KmipManagementConsts:
    ADMIN_ACTION_DELETE_CLIENT_CERTIFICATE = "delete-client-certificate"
    ADMIN_ACTION_DELETE_CLIENT_PRIVATE_KEY = "delete-client-private-key"
    ADMIN_ACTION_DELETE_ROOT_CA_CERTIFICATE = "delete-root-ca-certificate"


class KmipManagement(ManagedObject):
    """This is KmipManagement class."""

    consts = KmipManagementConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("KmipManagement", "kmipManagement", "kmip-mgmt", VersionMeta.Version302b, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], [u'topSystem'], [u'downloadClientCertificate', u'downloadClientPrivateKey', u'downloadRootCACertificate', u'exportClientCertificate', u'exportClientPrivateKey', u'exportRootCACertificate', u'kmipServer', u'kmipServerLogin'], ["Get", "Set"]),
        "modular": MoMeta("KmipManagement", "kmipManagement", "kmip-mgmt", VersionMeta.Version303a, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], [u'computeServerNode'], [u'downloadClientCertificate', u'downloadClientPrivateKey', u'downloadRootCACertificate', u'exportClientCertificate', u'exportClientPrivateKey', u'exportRootCACertificate', u'kmipServer', u'kmipServerLogin'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete-client-certificate", "delete-client-private-key", "delete-root-ca-certificate"], []), 
            "client_certificate": MoPropertyMeta("client_certificate", "clientCertificate", "string", VersionMeta.Version302b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "client_private_key": MoPropertyMeta("client_private_key", "clientPrivateKey", "string", VersionMeta.Version302b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version302b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "secure_key_management": MoPropertyMeta("secure_key_management", "secureKeyManagement", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "server_root_ca_certificate": MoPropertyMeta("server_root_ca_certificate", "serverRootCACertificate", "string", VersionMeta.Version302b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete-client-certificate", "delete-client-private-key", "delete-root-ca-certificate"], []), 
            "client_certificate": MoPropertyMeta("client_certificate", "clientCertificate", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "client_private_key": MoPropertyMeta("client_private_key", "clientPrivateKey", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "secure_key_management": MoPropertyMeta("secure_key_management", "secureKeyManagement", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "server_root_ca_certificate": MoPropertyMeta("server_root_ca_certificate", "serverRootCACertificate", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "clientCertificate": "client_certificate", 
            "clientPrivateKey": "client_private_key", 
            "description": "description", 
            "dn": "dn", 
            "rn": "rn", 
            "secureKeyManagement": "secure_key_management", 
            "serverRootCACertificate": "server_root_ca_certificate", 
            "status": "status", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "clientCertificate": "client_certificate", 
            "clientPrivateKey": "client_private_key", 
            "description": "description", 
            "dn": "dn", 
            "rn": "rn", 
            "secureKeyManagement": "secure_key_management", 
            "serverRootCACertificate": "server_root_ca_certificate", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.client_certificate = None
        self.client_private_key = None
        self.description = None
        self.secure_key_management = None
        self.server_root_ca_certificate = None
        self.status = None

        ManagedObject.__init__(self, "KmipManagement", parent_mo_or_dn, **kwargs)

