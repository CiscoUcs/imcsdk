"""This module contains the general information for BiosVfVMDEnable ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfVMDEnableConsts:
    VP_VMDENABLE_DISABLED = "Disabled"
    VP_VMDENABLE_ENABLED = "Enabled"
    _VP_VMDENABLE_DISABLED = "disabled"
    _VP_VMDENABLE_ENABLED = "enabled"
    VP_VMDENABLE_PLATFORM_DEFAULT = "platform-default"


class BiosVfVMDEnable(ManagedObject):
    """This is BiosVfVMDEnable class."""

    consts = BiosVfVMDEnableConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfVMDEnable", "biosVfVMDEnable", "VMDEnable", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_vmd_enable": MoPropertyMeta("vp_vmd_enable", "vpVMDEnable", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpVMDEnable": "vp_vmd_enable", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_vmd_enable = None

        ManagedObject.__init__(self, "BiosVfVMDEnable", parent_mo_or_dn, **kwargs)

