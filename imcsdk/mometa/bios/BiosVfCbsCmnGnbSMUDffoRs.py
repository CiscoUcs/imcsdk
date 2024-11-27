"""This module contains the general information for BiosVfCbsCmnGnbSMUDffoRs ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnGnbSMUDffoRsConsts:
    VP_CBS_CMN_GNB_SMUDFFO_RS_AUTO = "Auto"
    VP_CBS_CMN_GNB_SMUDFFO_RS_DISABLED = "Disabled"
    VP_CBS_CMN_GNB_SMUDFFO_RS_ENABLED = "Enabled"
    _VP_CBS_CMN_GNB_SMUDFFO_RS_DISABLED = "disabled"
    _VP_CBS_CMN_GNB_SMUDFFO_RS_ENABLED = "enabled"
    VP_CBS_CMN_GNB_SMUDFFO_RS_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnGnbSMUDffoRs(ManagedObject):
    """This is BiosVfCbsCmnGnbSMUDffoRs class."""

    consts = BiosVfCbsCmnGnbSMUDffoRsConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnGnbSMUDffoRs", "biosVfCbsCmnGnbSMUDffoRs", "DF_PState_Frequency_Optimizer", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_gnb_smu_dffo_rs": MoPropertyMeta("vp_cbs_cmn_gnb_smu_dffo_rs", "vpCbsCmnGnbSMUDffoRs", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnGnbSMUDffoRs": "vp_cbs_cmn_gnb_smu_dffo_rs", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_gnb_smu_dffo_rs = None

        ManagedObject.__init__(self, "BiosVfCbsCmnGnbSMUDffoRs", parent_mo_or_dn, **kwargs)

