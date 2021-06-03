"""This module contains the general information for BiosVfWorkLoadConfig ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfWorkLoadConfigConsts:
    VP_WORK_LOAD_CONFIG_BALANCED = "Balanced"
    VP_WORK_LOAD_CONFIG_I_O_SENSITIVE = "I/O Sensitive"
    VP_WORK_LOAD_CONFIG_NUMA = "NUMA"
    VP_WORK_LOAD_CONFIG_UMA = "UMA"
    VP_WORK_LOAD_CONFIG_PLATFORM_DEFAULT = "platform-default"


class BiosVfWorkLoadConfig(ManagedObject):
    """This is BiosVfWorkLoadConfig class."""

    consts = BiosVfWorkLoadConfigConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfWorkLoadConfig", "biosVfWorkLoadConfig", "work-load-config", VersionMeta.Version204c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfWorkLoadConfig", "biosVfWorkLoadConfig", "work-load-config", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_work_load_config": MoPropertyMeta("vp_work_load_config", "vpWorkLoadConfig", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Balanced", "I/O Sensitive", "NUMA", "UMA", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_work_load_config": MoPropertyMeta("vp_work_load_config", "vpWorkLoadConfig", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Balanced", "I/O Sensitive", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpWorkLoadConfig": "vp_work_load_config", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpWorkLoadConfig": "vp_work_load_config", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_work_load_config = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfWorkLoadConfig", parent_mo_or_dn, **kwargs)

