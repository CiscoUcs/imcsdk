"""This module contains the general information for BiosVfCbsCmnGnbSMUCPPC ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnGnbSMUCPPCConsts:
    VP_CBS_CMN_GNB_SMUCPPC_AUTO = "Auto"
    VP_CBS_CMN_GNB_SMUCPPC_DISABLED = "Disabled"
    VP_CBS_CMN_GNB_SMUCPPC_ENABLED = "Enabled"
    _VP_CBS_CMN_GNB_SMUCPPC_DISABLED = "disabled"
    _VP_CBS_CMN_GNB_SMUCPPC_ENABLED = "enabled"
    VP_CBS_CMN_GNB_SMUCPPC_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnGnbSMUCPPC(ManagedObject):
    """This is BiosVfCbsCmnGnbSMUCPPC class."""

    consts = BiosVfCbsCmnGnbSMUCPPCConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnGnbSMUCPPC", "biosVfCbsCmnGnbSMUCPPC", "Smu-Cppc", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_gnb_smucppc": MoPropertyMeta("vp_cbs_cmn_gnb_smucppc", "vpCbsCmnGnbSMUCPPC", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnGnbSMUCPPC": "vp_cbs_cmn_gnb_smucppc", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_gnb_smucppc = None

        ManagedObject.__init__(self, "BiosVfCbsCmnGnbSMUCPPC", parent_mo_or_dn, **kwargs)

