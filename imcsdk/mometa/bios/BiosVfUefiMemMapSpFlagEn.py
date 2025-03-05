"""This module contains the general information for BiosVfUefiMemMapSpFlagEn ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfUefiMemMapSpFlagEnConsts:
    VP_UEFI_MEM_MAP_SP_FLAG_EN_DISABLED = "Disabled"
    VP_UEFI_MEM_MAP_SP_FLAG_EN_ENABLED = "Enabled"
    _VP_UEFI_MEM_MAP_SP_FLAG_EN_DISABLED = "disabled"
    _VP_UEFI_MEM_MAP_SP_FLAG_EN_ENABLED = "enabled"
    VP_UEFI_MEM_MAP_SP_FLAG_EN_PLATFORM_DEFAULT = "platform-default"


class BiosVfUefiMemMapSpFlagEn(ManagedObject):
    """This is BiosVfUefiMemMapSpFlagEn class."""

    consts = BiosVfUefiMemMapSpFlagEnConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfUefiMemMapSpFlagEn", "biosVfUefiMemMapSpFlagEn", "Special-Purpose-Memory-Flag", VersionMeta.Version435_240037, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version435_240037, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version435_240037, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version435_240037, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version435_240037, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_uefi_mem_map_sp_flag_en": MoPropertyMeta("vp_uefi_mem_map_sp_flag_en", "vpUefiMemMapSpFlagEn", "string", VersionMeta.Version435_240037, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpUefiMemMapSpFlagEn": "vp_uefi_mem_map_sp_flag_en", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_uefi_mem_map_sp_flag_en = None

        ManagedObject.__init__(self, "BiosVfUefiMemMapSpFlagEn", parent_mo_or_dn, **kwargs)

