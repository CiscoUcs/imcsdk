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
        "classic": MoMeta("BiosVfPSata", "biosVfPSata", "PSata", VersionMeta.Version311d, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version311d, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_p_sata": MoPropertyMeta("vp_p_sata", "vpPSata", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["AHCI", "Disabled", "LSI SW RAID", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPSata": "vp_p_sata", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_p_sata = None

        ManagedObject.__init__(self, "BiosVfPSata", parent_mo_or_dn, **kwargs)

