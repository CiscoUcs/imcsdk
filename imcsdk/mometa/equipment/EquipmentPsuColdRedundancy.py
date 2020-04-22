"""This module contains the general information for EquipmentPsuColdRedundancy ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class EquipmentPsuColdRedundancyConsts:
    pass


class EquipmentPsuColdRedundancy(ManagedObject):
    """This is EquipmentPsuColdRedundancy class."""

    consts = EquipmentPsuColdRedundancyConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("EquipmentPsuColdRedundancy", "equipmentPsuColdRedundancy", "psu-cold-redundancy", VersionMeta.Version204c, "InputOutput", 0x1f, [], ["admin"], ['computeRackUnit'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "enabled": MoPropertyMeta("enabled", "enabled", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "overall_status": MoPropertyMeta("overall_status", "overallStatus", "string", VersionMeta.Version208d, MoPropertyMeta.READ_ONLY, None, 0, 710, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "enabled": "enabled", 
            "overallStatus": "overall_status", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.enabled = None
        self.overall_status = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPsuColdRedundancy", parent_mo_or_dn, **kwargs)

