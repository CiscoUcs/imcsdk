"""This module contains the general information for BiosVfDmaCtrlOptIn ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfDmaCtrlOptInConsts:
    VP_DMA_CTRL_OPT_IN_DISABLED = "Disabled"
    VP_DMA_CTRL_OPT_IN_ENABLED = "Enabled"
    _VP_DMA_CTRL_OPT_IN_DISABLED = "disabled"
    _VP_DMA_CTRL_OPT_IN_ENABLED = "enabled"
    VP_DMA_CTRL_OPT_IN_PLATFORM_DEFAULT = "platform-default"


class BiosVfDmaCtrlOptIn(ManagedObject):
    """This is BiosVfDmaCtrlOptIn class."""

    consts = BiosVfDmaCtrlOptInConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfDmaCtrlOptIn", "biosVfDmaCtrlOptIn", "Dma-Control", VersionMeta.Version423a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version423a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_dma_ctrl_opt_in": MoPropertyMeta("vp_dma_ctrl_opt_in", "vpDmaCtrlOptIn", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpDmaCtrlOptIn": "vp_dma_ctrl_opt_in", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_dma_ctrl_opt_in = None

        ManagedObject.__init__(self, "BiosVfDmaCtrlOptIn", parent_mo_or_dn, **kwargs)

