"""This module contains the general information for BiosVfSHA256PCRBank ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSHA256PCRBankConsts:
    VP_SHA256_PCRBANK_DISABLED = "Disabled"
    VP_SHA256_PCRBANK_ENABLED = "Enabled"
    _VP_SHA256_PCRBANK_DISABLED = "disabled"
    _VP_SHA256_PCRBANK_ENABLED = "enabled"
    VP_SHA256_PCRBANK_PLATFORM_DEFAULT = "platform-default"


class BiosVfSHA256PCRBank(ManagedObject):
    """This is BiosVfSHA256PCRBank class."""

    consts = BiosVfSHA256PCRBankConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSHA256PCRBank", "biosVfSHA256PCRBank", "SHA256-PCR-Bank", VersionMeta.Version413h, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413h, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413h, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413h, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413h, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_sh_a256_pcr_bank": MoPropertyMeta("vp_sh_a256_pcr_bank", "vpSHA256PCRBank", "string", VersionMeta.Version413h, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSHA256PCRBank": "vp_sh_a256_pcr_bank", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_sh_a256_pcr_bank = None

        ManagedObject.__init__(self, "BiosVfSHA256PCRBank", parent_mo_or_dn, **kwargs)

