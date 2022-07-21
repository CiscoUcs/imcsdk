"""This module contains the general information for BiosVfSHA1PCRBank ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSHA1PCRBankConsts:
    VP_SHA1_PCRBANK_DISABLED = "Disabled"
    VP_SHA1_PCRBANK_ENABLED = "Enabled"
    _VP_SHA1_PCRBANK_DISABLED = "disabled"
    _VP_SHA1_PCRBANK_ENABLED = "enabled"
    VP_SHA1_PCRBANK_PLATFORM_DEFAULT = "platform-default"


class BiosVfSHA1PCRBank(ManagedObject):
    """This is BiosVfSHA1PCRBank class."""

    consts = BiosVfSHA1PCRBankConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSHA1PCRBank", "biosVfSHA1PCRBank", "SHA1-PCR-Bank", VersionMeta.Version413h, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413h, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413h, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413h, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413h, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_sh_a1_pcr_bank": MoPropertyMeta("vp_sh_a1_pcr_bank", "vpSHA1PCRBank", "string", VersionMeta.Version413h, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSHA1PCRBank": "vp_sh_a1_pcr_bank", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_sh_a1_pcr_bank = None

        ManagedObject.__init__(self, "BiosVfSHA1PCRBank", parent_mo_or_dn, **kwargs)

