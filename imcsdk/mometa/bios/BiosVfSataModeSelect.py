"""This module contains the general information for BiosVfSataModeSelect ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSataModeSelectConsts:
    VP_SATA_MODE_SELECT_AHCI = "AHCI"
    VP_SATA_MODE_SELECT_DISABLED = "Disabled"
    VP_SATA_MODE_SELECT_LSI_SW_RAID = "LSI SW RAID"
    VP_SATA_MODE_SELECT_PLATFORM_DEFAULT = "platform-default"


class BiosVfSataModeSelect(ManagedObject):
    """This is BiosVfSataModeSelect class."""

    consts = BiosVfSataModeSelectConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSataModeSelect", "biosVfSataModeSelect", "Pch-Sata-Mode", VersionMeta.Version202c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfSataModeSelect", "biosVfSataModeSelect", "Pch-Sata-Mode", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_sata_mode_select": MoPropertyMeta("vp_sata_mode_select", "vpSataModeSelect", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["AHCI", "Disabled", "LSI SW RAID", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_sata_mode_select": MoPropertyMeta("vp_sata_mode_select", "vpSataModeSelect", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["AHCI", "Disabled", "LSI SW RAID", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSataModeSelect": "vp_sata_mode_select", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSataModeSelect": "vp_sata_mode_select", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_sata_mode_select = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfSataModeSelect", parent_mo_or_dn, **kwargs)

