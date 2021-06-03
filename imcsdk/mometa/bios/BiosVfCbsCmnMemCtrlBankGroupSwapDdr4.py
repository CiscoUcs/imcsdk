"""This module contains the general information for BiosVfCbsCmnMemCtrlBankGroupSwapDdr4 ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnMemCtrlBankGroupSwapDdr4Consts:
    VP_CBS_CMN_MEM_CTRL_BANK_GROUP_SWAP_DDR4_AUTO = "Auto"
    VP_CBS_CMN_MEM_CTRL_BANK_GROUP_SWAP_DDR4_DISABLED = "Disabled"
    VP_CBS_CMN_MEM_CTRL_BANK_GROUP_SWAP_DDR4_ENABLED = "Enabled"
    _VP_CBS_CMN_MEM_CTRL_BANK_GROUP_SWAP_DDR4_DISABLED = "disabled"
    _VP_CBS_CMN_MEM_CTRL_BANK_GROUP_SWAP_DDR4_ENABLED = "enabled"
    VP_CBS_CMN_MEM_CTRL_BANK_GROUP_SWAP_DDR4_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnMemCtrlBankGroupSwapDdr4(ManagedObject):
    """This is BiosVfCbsCmnMemCtrlBankGroupSwapDdr4 class."""

    consts = BiosVfCbsCmnMemCtrlBankGroupSwapDdr4Consts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnMemCtrlBankGroupSwapDdr4", "biosVfCbsCmnMemCtrlBankGroupSwapDdr4", "bank-groupswap", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_mem_ctrl_bank_group_swap_ddr4": MoPropertyMeta("vp_cbs_cmn_mem_ctrl_bank_group_swap_ddr4", "vpCbsCmnMemCtrlBankGroupSwapDdr4", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnMemCtrlBankGroupSwapDdr4": "vp_cbs_cmn_mem_ctrl_bank_group_swap_ddr4", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_mem_ctrl_bank_group_swap_ddr4 = None

        ManagedObject.__init__(self, "BiosVfCbsCmnMemCtrlBankGroupSwapDdr4", parent_mo_or_dn, **kwargs)

