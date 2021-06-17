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
    VP_TPMPENDING_OPERATION_NONE = "None"
    VP_TPMPENDING_OPERATION_TPM_CLEAR = "TpmClear"
    VP_TPMPENDING_OPERATION_PLATFORM_DEFAULT = "platform-default"


class BiosVfTPMControl(ManagedObject):
    """This is BiosVfTPMControl class."""

    consts = BiosVfTPMControlConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfTPMControl", "biosVfTPMControl", "TPM-Control", VersionMeta.Version304a, "InputOutput", 0x3f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfTPMControl", "biosVfTPMControl", "TPM-Control", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_tpm_control": MoPropertyMeta("vp_tpm_control", "vpTPMControl", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version304a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "vp_tpm_pending_operation": MoPropertyMeta("vp_tpm_pending_operation", "vpTPMPendingOperation", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["None", "TpmClear", "platform-default"], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_tpm_control": MoPropertyMeta("vp_tpm_control", "vpTPMControl", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpTPMControl": "vp_tpm_control", 
            "childAction": "child_action", 
            "vpTPMPendingOperation": "vp_tpm_pending_operation", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpTPMControl": "vp_tpm_control", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_tpm_control = None
        self.child_action = None
        self.vp_tpm_pending_operation = None

        ManagedObject.__init__(self, "BiosVfTPMControl", parent_mo_or_dn, **kwargs)

