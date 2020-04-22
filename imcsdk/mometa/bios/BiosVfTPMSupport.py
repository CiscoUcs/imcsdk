"""This module contains the general information for BiosVfTPMSupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfTPMSupportConsts:
    VP_TPMSUPPORT_DISABLED = "Disabled"
    VP_TPMSUPPORT_ENABLED = "Enabled"
    _VP_TPMSUPPORT_DISABLED = "disabled"
    _VP_TPMSUPPORT_ENABLED = "enabled"
    VP_TPMSUPPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfTPMSupport(ManagedObject):
    """This is BiosVfTPMSupport class."""

    consts = BiosVfTPMSupportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfTPMSupport", "biosVfTPMSupport", "TPM-Support", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfTPMSupport", "biosVfTPMSupport", "TPM-Support", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_tpm_support": MoPropertyMeta("vp_tpm_support", "vpTPMSupport", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_tpm_support": MoPropertyMeta("vp_tpm_support", "vpTPMSupport", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpTPMSupport": "vp_tpm_support", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpTPMSupport": "vp_tpm_support", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_tpm_support = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfTPMSupport", parent_mo_or_dn, **kwargs)

