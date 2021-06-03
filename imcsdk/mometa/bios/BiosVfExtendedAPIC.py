"""This module contains the general information for BiosVfExtendedAPIC ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfExtendedAPICConsts:
    VP_EXTENDED_APIC_DISABLED = "Disabled"
    VP_EXTENDED_APIC_ENABLED = "Enabled"
    VP_EXTENDED_APIC_X2_APIC = "X2APIC"
    VP_EXTENDED_APIC_XAPIC = "XAPIC"
    _VP_EXTENDED_APIC_DISABLED = "disabled"
    _VP_EXTENDED_APIC_ENABLED = "enabled"
    VP_EXTENDED_APIC_PLATFORM_DEFAULT = "platform-default"


class BiosVfExtendedAPIC(ManagedObject):
    """This is BiosVfExtendedAPIC class."""

    consts = BiosVfExtendedAPICConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfExtendedAPIC", "biosVfExtendedAPIC", "Extended-APIC", VersionMeta.Version201a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfExtendedAPIC", "biosVfExtendedAPIC", "Extended-APIC", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_extended_apic": MoPropertyMeta("vp_extended_apic", "vpExtendedAPIC", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "X2APIC", "XAPIC", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_extended_apic": MoPropertyMeta("vp_extended_apic", "vpExtendedAPIC", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "X2APIC", "XAPIC", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpExtendedAPIC": "vp_extended_apic", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpExtendedAPIC": "vp_extended_apic", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_extended_apic = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfExtendedAPIC", parent_mo_or_dn, **kwargs)

