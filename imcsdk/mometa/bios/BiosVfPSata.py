"""This module contains the general information for BiosVfPSata ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPSataConsts:
    VP_PSATA_AHCI = "AHCI"
    VP_PSATA_DISABLED = "Disabled"
    VP_PSATA_LSI_SW_RAID = "LSI SW RAID"
    VP_PSATA_PLATFORM_DEFAULT = "platform-default"


class BiosVfPSata(ManagedObject):
    """This is BiosVfPSata class."""

    consts = BiosVfPSataConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPSata", "biosVfPSata", "PSata", VersionMeta.Version304a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfPSata", "biosVfPSata", "PSata", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_p_sata": MoPropertyMeta("vp_p_sata", "vpPSata", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["AHCI", "Disabled", "LSI SW RAID", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version304a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_p_sata": MoPropertyMeta("vp_p_sata", "vpPSata", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["AHCI", "Disabled", "LSI SW RAID", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPSata": "vp_p_sata", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPSata": "vp_p_sata", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_p_sata = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfPSata", parent_mo_or_dn, **kwargs)

