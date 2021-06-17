"""This module contains the general information for EquipmentChassis ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class EquipmentChassisConsts:
    REBOOT_HOST_FALSE = "false"
    REBOOT_HOST_NO = "no"
    REBOOT_HOST_TRUE = "true"
    REBOOT_HOST_YES = "yes"
    SERVER_SIOCCONNECTIVITY_SINGLE_SERVER_DUAL_SIOC = "single-server-dual-sioc"
    SERVER_SIOCCONNECTIVITY_SINGLE_SERVER_SINGLE_SIOC = "single-server-single-sioc"


class EquipmentChassis(ManagedObject):
    """This is EquipmentChassis class."""

    consts = EquipmentChassisConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("EquipmentChassis", "equipmentChassis", "chassis-1", VersionMeta.Version2013e, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['topSystem'], ['chassisPIDCatalog', 'chassisPowerBudget', 'chassisPowerMonitor', 'chassisPowerUtilization', 'computeServerNode', 'equipmentChassisLocatorLed', 'equipmentFanModule', 'equipmentIndicatorLed', 'equipmentPsu', 'equipmentSystemIOController', 'eventManagement', 'faultInst', 'mgmtBackup', 'mgmtIf', 'mgmtImporter', 'mgmtInventory', 'storageEnclosure', 'storageSasExpander', 'sysdebugTechSupportExport', 'vicBackupAll', 'vicImporterAll'], ["Get"])
    }


    prop_meta = {

        "modular": {
            "asset_tag": MoPropertyMeta("asset_tag", "assetTag", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 32, r"""[^!|&]{0,32}""", [], []),
            "bmc1_reset_status": MoPropertyMeta("bmc1_reset_status", "bmc1ResetStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "bmc2_reset_status": MoPropertyMeta("bmc2_reset_status", "bmc2ResetStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "cmc_reset_status": MoPropertyMeta("cmc_reset_status", "cmcResetStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "dual_enclosure_id_enable": MoPropertyMeta("dual_enclosure_id_enable", "dualEnclosureIdEnable", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["No", "Yes", "no", "yes"], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "reboot_host": MoPropertyMeta("reboot_host", "rebootHost", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["No", "Yes", "no", "yes"], []),
            "reset_components": MoPropertyMeta("reset_components", "resetComponents", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "server_sioc_connectivity": MoPropertyMeta("server_sioc_connectivity", "serverSIOCConnectivity", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["single-server-dual-sioc", "single-server-single-sioc"], []),
            "sioc_reset_status": MoPropertyMeta("sioc_reset_status", "siocResetStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "storage_reset_status": MoPropertyMeta("storage_reset_status", "storageResetStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x200, 0, 64, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,64}""", [], []),
        },

    }

    prop_map = {

        "modular": {
            "assetTag": "asset_tag", 
            "bmc1ResetStatus": "bmc1_reset_status", 
            "bmc2ResetStatus": "bmc2_reset_status", 
            "childAction": "child_action", 
            "cmcResetStatus": "cmc_reset_status", 
            "dn": "dn", 
            "dualEnclosureIdEnable": "dual_enclosure_id_enable", 
            "model": "model", 
            "name": "name", 
            "rebootHost": "reboot_host", 
            "resetComponents": "reset_components", 
            "rn": "rn", 
            "serial": "serial", 
            "serverSIOCConnectivity": "server_sioc_connectivity", 
            "siocResetStatus": "sioc_reset_status", 
            "status": "status", 
            "storageResetStatus": "storage_reset_status", 
            "usrLbl": "usr_lbl", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.asset_tag = None
        self.bmc1_reset_status = None
        self.bmc2_reset_status = None
        self.child_action = None
        self.cmc_reset_status = None
        self.dual_enclosure_id_enable = None
        self.model = None
        self.name = None
        self.reboot_host = None
        self.reset_components = None
        self.serial = None
        self.server_sioc_connectivity = None
        self.sioc_reset_status = None
        self.status = None
        self.storage_reset_status = None
        self.usr_lbl = None

        ManagedObject.__init__(self, "EquipmentChassis", parent_mo_or_dn, **kwargs)

