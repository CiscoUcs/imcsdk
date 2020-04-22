"""This module contains the general information for BiosVfHWPMEnable ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfHWPMEnableConsts:
    VP_HWPMENABLE_DISABLED = "Disabled"
    VP_HWPMENABLE_HWPM_NATIVE_MODE = "HWPM Native Mode"
    VP_HWPMENABLE_HWPM_OOB_MODE = "HWPM OOB Mode"
    VP_HWPMENABLE_NATIVE_MODE = "NATIVE MODE"
    VP_HWPMENABLE_NATIVE_MODE_WITH_NO_LEGACY = "Native Mode with no Legacy"
    VP_HWPMENABLE_OOB_MODE = "OOB MODE"
    VP_HWPMENABLE_PLATFORM_DEFAULT = "platform-default"


class BiosVfHWPMEnable(ManagedObject):
    """This is BiosVfHWPMEnable class."""

    consts = BiosVfHWPMEnableConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfHWPMEnable", "biosVfHWPMEnable", "HWPM-Enable", VersionMeta.Version2010b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfHWPMEnable", "biosVfHWPMEnable", "HWPM-Enable", VersionMeta.Version303a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_hwpm_enable": MoPropertyMeta("vp_hwpm_enable", "vpHWPMEnable", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "HWPM Native Mode", "HWPM OOB Mode", "NATIVE MODE", "Native Mode with no Legacy", "OOB MODE", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2010b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_hwpm_enable": MoPropertyMeta("vp_hwpm_enable", "vpHWPMEnable", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "HWPM Native Mode", "HWPM OOB Mode", "NATIVE MODE", "Native Mode with no Legacy", "OOB MODE", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpHWPMEnable": "vp_hwpm_enable", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpHWPMEnable": "vp_hwpm_enable", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_hwpm_enable = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfHWPMEnable", parent_mo_or_dn, **kwargs)

