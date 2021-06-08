"""This module contains the general information for BiosVfSgxLePubKeyHash ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSgxLePubKeyHashConsts:
    VP_SGX_LE_PUB_KEY_HASH0_PLATFORM_DEFAULT = "platform-default"
    VP_SGX_LE_PUB_KEY_HASH1_PLATFORM_DEFAULT = "platform-default"
    VP_SGX_LE_PUB_KEY_HASH2_PLATFORM_DEFAULT = "platform-default"
    VP_SGX_LE_PUB_KEY_HASH3_PLATFORM_DEFAULT = "platform-default"


class BiosVfSgxLePubKeyHash(ManagedObject):
    """This is BiosVfSgxLePubKeyHash class."""

    consts = BiosVfSgxLePubKeyHashConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSgxLePubKeyHash", "biosVfSgxLePubKeyHash", "Sgx-Le-PubKeyHash", VersionMeta.Version421a, "InputOutput", 0xff, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_sgx_le_pub_key_hash0": MoPropertyMeta("vp_sgx_le_pub_key_hash0", "vpSgxLePubKeyHash0", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[0-9a-fA-F]{1,16}""", ["platform-default"], []),
            "vp_sgx_le_pub_key_hash1": MoPropertyMeta("vp_sgx_le_pub_key_hash1", "vpSgxLePubKeyHash1", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[0-9a-fA-F]{1,16}""", ["platform-default"], []),
            "vp_sgx_le_pub_key_hash2": MoPropertyMeta("vp_sgx_le_pub_key_hash2", "vpSgxLePubKeyHash2", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[0-9a-fA-F]{1,16}""", ["platform-default"], []),
            "vp_sgx_le_pub_key_hash3": MoPropertyMeta("vp_sgx_le_pub_key_hash3", "vpSgxLePubKeyHash3", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[0-9a-fA-F]{1,16}""", ["platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSgxLePubKeyHash0": "vp_sgx_le_pub_key_hash0", 
            "vpSgxLePubKeyHash1": "vp_sgx_le_pub_key_hash1", 
            "vpSgxLePubKeyHash2": "vp_sgx_le_pub_key_hash2", 
            "vpSgxLePubKeyHash3": "vp_sgx_le_pub_key_hash3", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_sgx_le_pub_key_hash0 = None
        self.vp_sgx_le_pub_key_hash1 = None
        self.vp_sgx_le_pub_key_hash2 = None
        self.vp_sgx_le_pub_key_hash3 = None

        ManagedObject.__init__(self, "BiosVfSgxLePubKeyHash", parent_mo_or_dn, **kwargs)

