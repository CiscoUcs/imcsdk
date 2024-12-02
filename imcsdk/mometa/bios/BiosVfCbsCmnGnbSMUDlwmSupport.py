"""This module contains the general information for BiosVfCbsCmnGnbSMUDlwmSupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnGnbSMUDlwmSupportConsts:
    VP_CBS_CMN_GNB_SMUDLWM_SUPPORT_AUTO = "Auto"
    VP_CBS_CMN_GNB_SMUDLWM_SUPPORT_DISABLED = "Disabled"
    VP_CBS_CMN_GNB_SMUDLWM_SUPPORT_ENABLED = "Enabled"
    _VP_CBS_CMN_GNB_SMUDLWM_SUPPORT_DISABLED = "disabled"
    _VP_CBS_CMN_GNB_SMUDLWM_SUPPORT_ENABLED = "enabled"
    VP_CBS_CMN_GNB_SMUDLWM_SUPPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnGnbSMUDlwmSupport(ManagedObject):
    """This is BiosVfCbsCmnGnbSMUDlwmSupport class."""

    consts = BiosVfCbsCmnGnbSMUDlwmSupportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnGnbSMUDlwmSupport", "biosVfCbsCmnGnbSMUDlwmSupport", "dlwm-support", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_gnb_smu_dlwm_support": MoPropertyMeta("vp_cbs_cmn_gnb_smu_dlwm_support", "vpCbsCmnGnbSMUDlwmSupport", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnGnbSMUDlwmSupport": "vp_cbs_cmn_gnb_smu_dlwm_support", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_gnb_smu_dlwm_support = None

        ManagedObject.__init__(self, "BiosVfCbsCmnGnbSMUDlwmSupport", parent_mo_or_dn, **kwargs)

