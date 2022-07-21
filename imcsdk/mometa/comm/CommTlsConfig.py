"""This module contains the general information for CommTlsConfig ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommTlsConfigConsts:
    TLSV2_CIPHER_MODE_CUSTOM = "Custom"
    TLSV2_CIPHER_MODE_HIGH = "High"
    TLSV2_CIPHER_MODE_LOW = "Low"
    TLSV2_CIPHER_MODE_MEDIUM = "Medium"
    TLSV2_CIPHER_MODE_NA = "NA"


class CommTlsConfig(ManagedObject):
    """This is CommTlsConfig class."""

    consts = CommTlsConfigConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("CommTlsConfig", "commTlsConfig", "tls-svc", VersionMeta.Version422a, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['commSvcEp'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version422a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "tls_config_supported": MoPropertyMeta("tls_config_supported", "tlsConfigSupported", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "tlsv2_cipher_list": MoPropertyMeta("tlsv2_cipher_list", "tlsv2CipherList", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[0-9a-zA-Z\.\+!_:-]{0,256}""", [], []),
            "tlsv2_cipher_mode": MoPropertyMeta("tlsv2_cipher_mode", "tlsv2CipherMode", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Custom", "High", "Low", "Medium", "NA"], []),
            "tlsv2_cipher_status": MoPropertyMeta("tlsv2_cipher_status", "tlsv2CipherStatus", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "tlsv2_enabled": MoPropertyMeta("tlsv2_enabled", "tlsv2Enabled", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "tlsv3_cipher_suite": MoPropertyMeta("tlsv3_cipher_suite", "tlsv3CipherSuite", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[0-9a-zA-Z\._:-]{0,125}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "tlsConfigSupported": "tls_config_supported", 
            "tlsv2CipherList": "tlsv2_cipher_list", 
            "tlsv2CipherMode": "tlsv2_cipher_mode", 
            "tlsv2CipherStatus": "tlsv2_cipher_status", 
            "tlsv2Enabled": "tlsv2_enabled", 
            "tlsv3CipherSuite": "tlsv3_cipher_suite", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.tls_config_supported = None
        self.tlsv2_cipher_list = None
        self.tlsv2_cipher_mode = None
        self.tlsv2_cipher_status = None
        self.tlsv2_enabled = None
        self.tlsv3_cipher_suite = None

        ManagedObject.__init__(self, "CommTlsConfig", parent_mo_or_dn, **kwargs)

