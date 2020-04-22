"""This module contains the general information for BiosVfSvmMode ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSvmModeConsts:
    VP_SVM_MODE_DISABLED = "Disabled"
    VP_SVM_MODE_ENABLED = "Enabled"
    _VP_SVM_MODE_DISABLED = "disabled"
    _VP_SVM_MODE_ENABLED = "enabled"
    VP_SVM_MODE_PLATFORM_DEFAULT = "platform-default"


class BiosVfSvmMode(ManagedObject):
    """This is BiosVfSvmMode class."""

    consts = BiosVfSvmModeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSvmMode", "biosVfSvmMode", "svm-mode", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_svm_mode": MoPropertyMeta("vp_svm_mode", "vpSvmMode", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSvmMode": "vp_svm_mode", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_svm_mode = None

        ManagedObject.__init__(self, "BiosVfSvmMode", parent_mo_or_dn, **kwargs)

