"""This module contains the general information for SystemBoardUnit ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class SystemBoardUnitConsts:
    pass


class SystemBoardUnit(ManagedObject):
    """This is SystemBoardUnit class."""

    consts = SystemBoardUnitConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("SystemBoardUnit", "systemBoardUnit", "sys-board-unit", VersionMeta.Version311d, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['topSystem'], [], ["Get"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version311d, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "cpu1_pkg_id": MoPropertyMeta("cpu1_pkg_id", "cpu1PkgId", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "cpu2_pkg_id": MoPropertyMeta("cpu2_pkg_id", "cpu2PkgId", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "cpu3_pkg_id": MoPropertyMeta("cpu3_pkg_id", "cpu3PkgId", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "cpu4_pkg_id": MoPropertyMeta("cpu4_pkg_id", "cpu4PkgId", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "cpu_module1": MoPropertyMeta("cpu_module1", "cpuModule1", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "cpu_module2": MoPropertyMeta("cpu_module2", "cpuModule2", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "cpu_type": MoPropertyMeta("cpu_type", "cpuType", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "hdd_backplane": MoPropertyMeta("hdd_backplane", "hddBackplane", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "hdd_module1": MoPropertyMeta("hdd_module1", "hddModule1", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "hdd_module2": MoPropertyMeta("hdd_module2", "hddModule2", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "hdd_module3": MoPropertyMeta("hdd_module3", "hddModule3", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "hdd_module4": MoPropertyMeta("hdd_module4", "hddModule4", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "intrusion_sensor": MoPropertyMeta("intrusion_sensor", "intrusionSensor", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "rear_bp_sku_type": MoPropertyMeta("rear_bp_sku_type", "rearBpSkuType", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "riser1": MoPropertyMeta("riser1", "riser1", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "riser2": MoPropertyMeta("riser2", "riser2", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "riser3": MoPropertyMeta("riser3", "riser3", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "sas_expander": MoPropertyMeta("sas_expander", "sasExpander", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "sata_nv_me": MoPropertyMeta("sata_nv_me", "sataNVMe", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "sd_controller": MoPropertyMeta("sd_controller", "sdController", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "cpu1PkgId": "cpu1_pkg_id", 
            "cpu2PkgId": "cpu2_pkg_id", 
            "cpu3PkgId": "cpu3_pkg_id", 
            "cpu4PkgId": "cpu4_pkg_id", 
            "cpuModule1": "cpu_module1", 
            "cpuModule2": "cpu_module2", 
            "cpuType": "cpu_type", 
            "dn": "dn", 
            "hddBackplane": "hdd_backplane", 
            "hddModule1": "hdd_module1", 
            "hddModule2": "hdd_module2", 
            "hddModule3": "hdd_module3", 
            "hddModule4": "hdd_module4", 
            "intrusionSensor": "intrusion_sensor", 
            "rearBpSkuType": "rear_bp_sku_type", 
            "riser1": "riser1", 
            "riser2": "riser2", 
            "riser3": "riser3", 
            "rn": "rn", 
            "sasExpander": "sas_expander", 
            "sataNVMe": "sata_nv_me", 
            "sdController": "sd_controller", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.cpu1_pkg_id = None
        self.cpu2_pkg_id = None
        self.cpu3_pkg_id = None
        self.cpu4_pkg_id = None
        self.cpu_module1 = None
        self.cpu_module2 = None
        self.cpu_type = None
        self.hdd_backplane = None
        self.hdd_module1 = None
        self.hdd_module2 = None
        self.hdd_module3 = None
        self.hdd_module4 = None
        self.intrusion_sensor = None
        self.rear_bp_sku_type = None
        self.riser1 = None
        self.riser2 = None
        self.riser3 = None
        self.sas_expander = None
        self.sata_nv_me = None
        self.sd_controller = None
        self.status = None

        ManagedObject.__init__(self, "SystemBoardUnit", parent_mo_or_dn, **kwargs)

