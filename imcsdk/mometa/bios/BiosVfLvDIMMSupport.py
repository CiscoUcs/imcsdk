"""This module contains the general information for BiosVfLvDIMMSupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfLvDIMMSupportConsts:
    VP_LV_DDRMODE_AUTO = "auto"
    VP_LV_DDRMODE_PERFORMANCE_MODE = "performance-mode"
    VP_LV_DDRMODE_PLATFORM_DEFAULT = "platform-default"
    VP_LV_DDRMODE_POWER_SAVING_MODE = "power-saving-mode"


class BiosVfLvDIMMSupport(ManagedObject):
    """This is BiosVfLvDIMMSupport class."""

    consts = BiosVfLvDIMMSupportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfLvDIMMSupport", "biosVfLvDIMMSupport", "LvDIMM-Support", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfLvDIMMSupport", "biosVfLvDIMMSupport", "LvDIMM-Support", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_lv_ddr_mode": MoPropertyMeta("vp_lv_ddr_mode", "vpLvDDRMode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["auto", "performance-mode", "platform-default", "power-saving-mode"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_lv_ddr_mode": MoPropertyMeta("vp_lv_ddr_mode", "vpLvDDRMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["auto", "performance-mode", "platform-default", "power-saving-mode"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpLvDDRMode": "vp_lv_ddr_mode", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpLvDDRMode": "vp_lv_ddr_mode", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_lv_ddr_mode = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfLvDIMMSupport", parent_mo_or_dn, **kwargs)

