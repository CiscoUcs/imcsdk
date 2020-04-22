"""This module contains the general information for BiosVfMMCFGBase ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfMMCFGBaseConsts:
    VP_MMCFGBASE_1_GB = "1 GB"
    VP_MMCFGBASE_2_GB = "2 GB"
    VP_MMCFGBASE_2_5_GB = "2.5 GB"
    VP_MMCFGBASE_3_GB = "3 GB"
    VP_MMCFGBASE_AUTO = "Auto"
    VP_MMCFGBASE_PLATFORM_DEFAULT = "platform-default"


class BiosVfMMCFGBase(ManagedObject):
    """This is BiosVfMMCFGBase class."""

    consts = BiosVfMMCFGBaseConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfMMCFGBase", "biosVfMMCFGBase", "MMCFG-Base", VersionMeta.Version201a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfMMCFGBase", "biosVfMMCFGBase", "MMCFG-Base", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_mmcfg_base": MoPropertyMeta("vp_mmcfg_base", "vpMMCFGBase", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1 GB", "2 GB", "2.5 GB", "3 GB", "Auto", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_mmcfg_base": MoPropertyMeta("vp_mmcfg_base", "vpMMCFGBase", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1 GB", "2 GB", "2.5 GB", "3 GB", "Auto", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpMMCFGBase": "vp_mmcfg_base", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpMMCFGBase": "vp_mmcfg_base", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_mmcfg_base = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfMMCFGBase", parent_mo_or_dn, **kwargs)

