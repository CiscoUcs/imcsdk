"""This module contains the general information for BiosVfBmeDmaMitigation ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfBmeDmaMitigationConsts:
    VP_BME_DMA_MITIGATION_DISABLED = "Disabled"
    VP_BME_DMA_MITIGATION_ENABLED = "Enabled"
    _VP_BME_DMA_MITIGATION_DISABLED = "disabled"
    _VP_BME_DMA_MITIGATION_ENABLED = "enabled"
    VP_BME_DMA_MITIGATION_PLATFORM_DEFAULT = "platform-default"


class BiosVfBmeDmaMitigation(ManagedObject):
    """This is BiosVfBmeDmaMitigation class."""

    consts = BiosVfBmeDmaMitigationConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfBmeDmaMitigation", "biosVfBmeDmaMitigation", "bme-dma-mitigation", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfBmeDmaMitigation", "biosVfBmeDmaMitigation", "bme-dma-mitigation", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_bme_dma_mitigation": MoPropertyMeta("vp_bme_dma_mitigation", "vpBmeDmaMitigation", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_bme_dma_mitigation": MoPropertyMeta("vp_bme_dma_mitigation", "vpBmeDmaMitigation", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpBmeDmaMitigation": "vp_bme_dma_mitigation", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpBmeDmaMitigation": "vp_bme_dma_mitigation", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_bme_dma_mitigation = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfBmeDmaMitigation", parent_mo_or_dn, **kwargs)

