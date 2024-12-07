"""This module contains the general information for BiosVfTpmSupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfTpmSupportConsts:
    VP_TPM_SUPPORT_DISABLED = "Disabled"
    VP_TPM_SUPPORT_ENABLED = "Enabled"
    _VP_TPM_SUPPORT_DISABLED = "disabled"
    _VP_TPM_SUPPORT_ENABLED = "enabled"
    VP_TPM_SUPPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfTpmSupport(ManagedObject):
    """This is BiosVfTpmSupport class."""

    consts = BiosVfTpmSupportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfTpmSupport", "biosVfTpmSupport", "TPM-Support", VersionMeta.Version423a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version423a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_tpm_support": MoPropertyMeta("vp_tpm_support", "vpTpmSupport", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpTpmSupport": "vp_tpm_support", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_tpm_support = None

        ManagedObject.__init__(self, "BiosVfTpmSupport", parent_mo_or_dn, **kwargs)

