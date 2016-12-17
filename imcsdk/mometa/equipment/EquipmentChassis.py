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
        "modular": MoMeta("EquipmentChassis", "equipmentChassis", "chassis-1", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], [u'topSystem'], [u'chassisPIDCatalog', u'chassisPowerBudget', u'chassisPowerMonitor', u'chassisPowerUtilization', u'computeServerNode', u'equipmentChassisLocatorLed', u'equipmentFanModule', u'equipmentIndicatorLed', u'equipmentPsu', u'equipmentSystemIOController', u'eventManagement', u'faultInst', u'mgmtBackup', u'mgmtIf', u'mgmtImporter', u'mgmtInventory', u'storageEnclosure', u'storageSasExpander', u'sysdebugTechSupportExport'], ["Get"])
    }


    prop_meta = {

        "modular": {
            "asset_tag": MoPropertyMeta("asset_tag", "assetTag", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 32, r"""[^!|&]{0,32}""", [], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, 0, 64, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,64}""", [], []), 
        },

    }

    prop_map = {

        "modular": {
            "assetTag": "asset_tag", 
            "childAction": "child_action", 
            "dn": "dn", 
            "model": "model", 
            "name": "name", 
            "rn": "rn", 
            "serial": "serial", 
            "status": "status", 
            "usrLbl": "usr_lbl", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.asset_tag = None
        self.child_action = None
        self.model = None
        self.name = None
        self.serial = None
        self.status = None
        self.usr_lbl = None

        ManagedObject.__init__(self, "EquipmentChassis", parent_mo_or_dn, **kwargs)

