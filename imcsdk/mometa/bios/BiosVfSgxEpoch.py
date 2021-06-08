"""This module contains the general information for BiosVfSgxEpoch ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSgxEpochConsts:
    VP_SGX_EPOCH0_PLATFORM_DEFAULT = "platform-default"
    VP_SGX_EPOCH1_PLATFORM_DEFAULT = "platform-default"


class BiosVfSgxEpoch(ManagedObject):
    """This is BiosVfSgxEpoch class."""

    consts = BiosVfSgxEpochConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSgxEpoch", "biosVfSgxEpoch", "Sgx-Epoch", VersionMeta.Version421a, "InputOutput", 0x3f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_sgx_epoch0": MoPropertyMeta("vp_sgx_epoch0", "vpSgxEpoch0", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[0-9a-fA-F]{1,16}""", ["platform-default"], []),
            "vp_sgx_epoch1": MoPropertyMeta("vp_sgx_epoch1", "vpSgxEpoch1", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[0-9a-fA-F]{1,16}""", ["platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSgxEpoch0": "vp_sgx_epoch0", 
            "vpSgxEpoch1": "vp_sgx_epoch1", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_sgx_epoch0 = None
        self.vp_sgx_epoch1 = None

        ManagedObject.__init__(self, "BiosVfSgxEpoch", parent_mo_or_dn, **kwargs)

