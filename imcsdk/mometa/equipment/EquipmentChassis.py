"""This module contains the general information for EquipmentChassis ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class EquipmentChassisConsts:
    pass


class EquipmentChassis(ManagedObject):
    """This is EquipmentChassis class."""

    consts = EquipmentChassisConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("EquipmentChassis", "equipmentChassis", "chassis-1", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'topSystem'], [u'chassisPIDCatalog', u'chassisPowerBudget', u'chassisPowerMonitor', u'chassisPowerUtilization', u'computeServerNode', u'equipmentChassisLocatorLed', u'equipmentFanModule', u'equipmentIndicatorLed', u'equipmentPsu', u'equipmentSystemIOController', u'mgmtBackup', u'mgmtIf', u'mgmtImporter', u'storageEnclosure', u'storageSasExpander', u'sysdebugTechSupportExport'], [None])
    }


    prop_meta = {

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        },

    }

    prop_map = {

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "model": "model", 
            "name": "name", 
            "rn": "rn", 
            "serial": "serial", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.model = None
        self.name = None
        self.serial = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentChassis", parent_mo_or_dn, **kwargs)

