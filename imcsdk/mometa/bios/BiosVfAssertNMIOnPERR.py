"""This module contains the general information for BiosVfAssertNMIOnPERR ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfAssertNMIOnPERRConsts:
    VP_ASSERT_NMION_PERR_DISABLED = "Disabled"
    VP_ASSERT_NMION_PERR_ENABLED = "Enabled"
    _VP_ASSERT_NMION_PERR_DISABLED = "disabled"
    _VP_ASSERT_NMION_PERR_ENABLED = "enabled"
    VP_ASSERT_NMION_PERR_PLATFORM_DEFAULT = "platform-default"


class BiosVfAssertNMIOnPERR(ManagedObject):
    """This is BiosVfAssertNMIOnPERR class."""

    consts = BiosVfAssertNMIOnPERRConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfAssertNMIOnPERR", "biosVfAssertNMIOnPERR", "Assert-NMI-on-PERR", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfAssertNMIOnPERR", "biosVfAssertNMIOnPERR", "Assert-NMI-on-PERR", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_assert_nmi_on_perr": MoPropertyMeta("vp_assert_nmi_on_perr", "vpAssertNMIOnPERR", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_assert_nmi_on_perr": MoPropertyMeta("vp_assert_nmi_on_perr", "vpAssertNMIOnPERR", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpAssertNMIOnPERR": "vp_assert_nmi_on_perr", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpAssertNMIOnPERR": "vp_assert_nmi_on_perr", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_assert_nmi_on_perr = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfAssertNMIOnPERR", parent_mo_or_dn, **kwargs)

