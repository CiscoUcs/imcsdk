"""This module contains the general information for StorageControllerNVMe ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageControllerNVMeConsts:
    pass


class StorageControllerNVMe(ManagedObject):
    """This is StorageControllerNVMe class."""

    consts = StorageControllerNVMeConsts()
    naming_props = set([u'id'])

    mo_meta = {
        "classic": MoMeta("StorageControllerNVMe", "storageControllerNVMe", "storage-NVMe-[id]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'computeBoard'], [u'storageNVMePhysicalDrive'], ["Get"]),
        "modular": MoMeta("StorageControllerNVMe", "storageControllerNVMe", "storage-NVMe-[id]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'computeBoard'], [u'firmwareRunning'], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "controller_chip_temp_celsius": MoPropertyMeta("controller_chip_temp_celsius", "controllerChipTempCelsius", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "controller_status": MoPropertyMeta("controller_status", "controllerStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "drive_life_used": MoPropertyMeta("drive_life_used", "driveLifeUsed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "led_fault_status": MoPropertyMeta("led_fault_status", "ledFaultStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "percentage_total_power_on_hour": MoPropertyMeta("percentage_total_power_on_hour", "percentageTotalPowerOnHour", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "performance_level": MoPropertyMeta("performance_level", "performanceLevel", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
            "controllerChipTempCelsius": "controller_chip_temp_celsius", 
            "controllerStatus": "controller_status", 
            "driveLifeUsed": "drive_life_used", 
            "health": "health", 
            "ledFaultStatus": "led_fault_status", 
            "model": "model", 
            "percentageTotalPowerOnHour": "percentage_total_power_on_hour", 
            "performanceLevel": "performance_level", 
            "serial": "serial", 
            "vendor": "vendor", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.status = None
        self.controller_chip_temp_celsius = None
        self.controller_status = None
        self.drive_life_used = None
        self.health = None
        self.led_fault_status = None
        self.model = None
        self.percentage_total_power_on_hour = None
        self.performance_level = None
        self.serial = None
        self.vendor = None

        ManagedObject.__init__(self, "StorageControllerNVMe", parent_mo_or_dn, **kwargs)

