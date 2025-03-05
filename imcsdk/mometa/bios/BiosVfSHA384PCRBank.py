"""This module contains the general information for BiosVfSHA384PCRBank ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSHA384PCRBankConsts:
    VP_SHA384_PCRBANK_DISABLED = "Disabled"
    VP_SHA384_PCRBANK_ENABLED = "Enabled"
    _VP_SHA384_PCRBANK_DISABLED = "disabled"
    _VP_SHA384_PCRBANK_ENABLED = "enabled"
    VP_SHA384_PCRBANK_PLATFORM_DEFAULT = "platform-default"


class BiosVfSHA384PCRBank(ManagedObject):
    """This is BiosVfSHA384PCRBank class."""

    consts = BiosVfSHA384PCRBankConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSHA384PCRBank", "biosVfSHA384PCRBank", "SHA384-PCR-Bank", VersionMeta.Version432_230285, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version432_230285, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version432_230285, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version432_230285, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version432_230285, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_sh_a384_pcr_bank": MoPropertyMeta("vp_sh_a384_pcr_bank", "vpSHA384PCRBank", "string", VersionMeta.Version432_230285, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSHA384PCRBank": "vp_sh_a384_pcr_bank", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_sh_a384_pcr_bank = None

        ManagedObject.__init__(self, "BiosVfSHA384PCRBank", parent_mo_or_dn, **kwargs)

