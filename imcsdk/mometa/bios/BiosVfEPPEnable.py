"""This module contains the general information for BiosVfEPPEnable ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfEPPEnableConsts:
    VP_EPPENABLE_DISABLED = "Disabled"
    VP_EPPENABLE_ENABLED = "Enabled"
    _VP_EPPENABLE_DISABLED = "disabled"
    _VP_EPPENABLE_ENABLED = "enabled"
    VP_EPPENABLE_PLATFORM_DEFAULT = "platform-default"


class BiosVfEPPEnable(ManagedObject):
    """This is BiosVfEPPEnable class."""

    consts = BiosVfEPPEnableConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfEPPEnable", "biosVfEPPEnable", "Processor-EPP-Enable", VersionMeta.Version413a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfEPPEnable", "biosVfEPPEnable", "Processor-EPP-Enable", VersionMeta.Version413a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_epp_enable": MoPropertyMeta("vp_epp_enable", "vpEPPEnable", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_epp_enable": MoPropertyMeta("vp_epp_enable", "vpEPPEnable", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEPPEnable": "vp_epp_enable", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEPPEnable": "vp_epp_enable", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_epp_enable = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfEPPEnable", parent_mo_or_dn, **kwargs)

