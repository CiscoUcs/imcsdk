"""This module contains the general information for BiosVfPreBootDMAProtection ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPreBootDMAProtectionConsts:
    VP_PRE_BOOT_DMAPROTECTION_DISABLED = "Disabled"
    VP_PRE_BOOT_DMAPROTECTION_ENABLED = "Enabled"
    _VP_PRE_BOOT_DMAPROTECTION_DISABLED = "disabled"
    _VP_PRE_BOOT_DMAPROTECTION_ENABLED = "enabled"
    VP_PRE_BOOT_DMAPROTECTION_PLATFORM_DEFAULT = "platform-default"


class BiosVfPreBootDMAProtection(ManagedObject):
    """This is BiosVfPreBootDMAProtection class."""

    consts = BiosVfPreBootDMAProtectionConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPreBootDMAProtection", "biosVfPreBootDMAProtection", "PreBootDMAProtection", VersionMeta.Version435_240045, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version435_240045, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version435_240045, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version435_240045, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version435_240045, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pre_boot_dma_protection": MoPropertyMeta("vp_pre_boot_dma_protection", "vpPreBootDMAProtection", "string", VersionMeta.Version435_240045, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPreBootDMAProtection": "vp_pre_boot_dma_protection", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_pre_boot_dma_protection = None

        ManagedObject.__init__(self, "BiosVfPreBootDMAProtection", parent_mo_or_dn, **kwargs)

