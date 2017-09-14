"""This module contains the general information for StorageNVMePhysicalDrive ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageNVMePhysicalDriveConsts:
    pass


class StorageNVMePhysicalDrive(ManagedObject):
    """This is StorageNVMePhysicalDrive class."""

    consts = StorageNVMePhysicalDriveConsts()
    naming_props = set([u'id'])

    mo_meta = {
        "classic": MoMeta("StorageNVMePhysicalDrive", "storageNVMePhysicalDrive", "pd-[id]", VersionMeta.Version311d, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'storageControllerNVMe'], [], ["Get"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version311d, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
            "drive_life_used": MoPropertyMeta("drive_life_used", "driveLifeUsed", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "led_fault_status": MoPropertyMeta("led_fault_status", "ledFaultStatus", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "pd_chip_temp_celsius": MoPropertyMeta("pd_chip_temp_celsius", "pdChipTempCelsius", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "pd_status": MoPropertyMeta("pd_status", "pdStatus", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "percentage_total_power_on_hour": MoPropertyMeta("percentage_total_power_on_hour", "percentageTotalPowerOnHour", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "performance_level": MoPropertyMeta("performance_level", "performanceLevel", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "driveLifeUsed": "drive_life_used", 
            "firmwareVersion": "firmware_version", 
            "id": "id", 
            "ledFaultStatus": "led_fault_status", 
            "model": "model", 
            "pdChipTempCelsius": "pd_chip_temp_celsius", 
            "pdStatus": "pd_status", 
            "percentageTotalPowerOnHour": "percentage_total_power_on_hour", 
            "performanceLevel": "performance_level", 
            "rn": "rn", 
            "serial": "serial", 
            "status": "status", 
            "vendor": "vendor", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.drive_life_used = None
        self.firmware_version = None
        self.led_fault_status = None
        self.model = None
        self.pd_chip_temp_celsius = None
        self.pd_status = None
        self.percentage_total_power_on_hour = None
        self.performance_level = None
        self.serial = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "StorageNVMePhysicalDrive", parent_mo_or_dn, **kwargs)

