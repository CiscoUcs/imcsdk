"""This module contains the general information for BiosVfTPMControl ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfTPMControlConsts:
    VP_TPMCONTROL_DISABLED = "Disabled"
    VP_TPMCONTROL_ENABLED = "Enabled"
    _VP_TPMCONTROL_DISABLED = "disabled"
    _VP_TPMCONTROL_ENABLED = "enabled"
    VP_TPMCONTROL_PLATFORM_DEFAULT = "platform-default"


class BiosVfTPMControl(ManagedObject):
    """This is BiosVfTPMControl class."""

    consts = BiosVfTPMControlConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfTPMControl", "biosVfTPMControl", "TPM-Control", VersionMeta.Version311d, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version311d, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_tpm_control": MoPropertyMeta("vp_tpm_control", "vpTPMControl", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpTPMControl": "vp_tpm_control", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_tpm_control = None

        ManagedObject.__init__(self, "BiosVfTPMControl", parent_mo_or_dn, **kwargs)

