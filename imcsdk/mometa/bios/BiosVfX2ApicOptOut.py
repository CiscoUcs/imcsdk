"""This module contains the general information for BiosVfX2ApicOptOut ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfX2ApicOptOutConsts:
    VP_X2_APIC_OPT_OUT_DISABLED = "Disabled"
    VP_X2_APIC_OPT_OUT_ENABLED = "Enabled"
    _VP_X2_APIC_OPT_OUT_DISABLED = "disabled"
    _VP_X2_APIC_OPT_OUT_ENABLED = "enabled"
    VP_X2_APIC_OPT_OUT_PLATFORM_DEFAULT = "platform-default"


class BiosVfX2ApicOptOut(ManagedObject):
    """This is BiosVfX2ApicOptOut class."""

    consts = BiosVfX2ApicOptOutConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfX2ApicOptOut", "biosVfX2ApicOptOut", "X2APIC-Opt-Out", VersionMeta.Version423a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version423a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_x2_apic_opt_out": MoPropertyMeta("vp_x2_apic_opt_out", "vpX2ApicOptOut", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpX2ApicOptOut": "vp_x2_apic_opt_out", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_x2_apic_opt_out = None

        ManagedObject.__init__(self, "BiosVfX2ApicOptOut", parent_mo_or_dn, **kwargs)

