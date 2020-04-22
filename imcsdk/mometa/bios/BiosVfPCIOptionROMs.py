"""This module contains the general information for BiosVfPCIOptionROMs ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPCIOptionROMsConsts:
    VP_PCIOPTION_ROMS_DISABLED = "Disabled"
    VP_PCIOPTION_ROMS_ENABLED = "Enabled"
    VP_PCIOPTION_ROMS_LEGACY_ONLY = "Legacy Only"
    VP_PCIOPTION_ROMS_UEFI_ONLY = "UEFI Only"
    _VP_PCIOPTION_ROMS_DISABLED = "disabled"
    _VP_PCIOPTION_ROMS_ENABLED = "enabled"
    VP_PCIOPTION_ROMS_PLATFORM_DEFAULT = "platform-default"


class BiosVfPCIOptionROMs(ManagedObject):
    """This is BiosVfPCIOptionROMs class."""

    consts = BiosVfPCIOptionROMsConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPCIOptionROMs", "biosVfPCIOptionROMs", "PCI-OptionROMs", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfPCIOptionROMs", "biosVfPCIOptionROMs", "PCI-OptionROMs", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pci_option_ro_ms": MoPropertyMeta("vp_pci_option_ro_ms", "vpPCIOptionROMs", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pci_option_ro_ms": MoPropertyMeta("vp_pci_option_ro_ms", "vpPCIOptionROMs", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPCIOptionROMs": "vp_pci_option_ro_ms", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPCIOptionROMs": "vp_pci_option_ro_ms", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_pci_option_ro_ms = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfPCIOptionROMs", parent_mo_or_dn, **kwargs)

