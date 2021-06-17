"""This module contains the general information for BiosVfPciRomClp ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPciRomClpConsts:
    VP_PCI_ROM_CLP_DISABLED = "Disabled"
    VP_PCI_ROM_CLP_ENABLED = "Enabled"
    _VP_PCI_ROM_CLP_DISABLED = "disabled"
    _VP_PCI_ROM_CLP_ENABLED = "enabled"
    VP_PCI_ROM_CLP_PLATFORM_DEFAULT = "platform-default"


class BiosVfPciRomClp(ManagedObject):
    """This is BiosVfPciRomClp class."""

    consts = BiosVfPciRomClpConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPciRomClp", "biosVfPciRomClp", "pci-rom-clp", VersionMeta.Version204c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfPciRomClp", "biosVfPciRomClp", "pci-rom-clp", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pci_rom_clp": MoPropertyMeta("vp_pci_rom_clp", "vpPciRomClp", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pci_rom_clp": MoPropertyMeta("vp_pci_rom_clp", "vpPciRomClp", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPciRomClp": "vp_pci_rom_clp", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPciRomClp": "vp_pci_rom_clp", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_pci_rom_clp = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfPciRomClp", parent_mo_or_dn, **kwargs)

