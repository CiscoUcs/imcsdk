"""This module contains the general information for StorageNVMePhysicalDrive ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageNVMePhysicalDriveConsts:
    pass


class StorageNVMePhysicalDrive(ManagedObject):
    """This is StorageNVMePhysicalDrive class."""

    consts = StorageNVMePhysicalDriveConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("StorageNVMePhysicalDrive", "storageNVMePhysicalDrive", "pd-[id]", VersionMeta.Version401a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageControllerNVMe'], ['faultInst'], ["Get"]),
        "modular": MoMeta("StorageNVMePhysicalDrive", "storageNVMePhysicalDrive", "pd-[id]", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageControllerNVMe'], ['faultInst'], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "controller_temperature": MoPropertyMeta("controller_temperature", "controllerTemperature", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "drive_life_used": MoPropertyMeta("drive_life_used", "driveLifeUsed", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "drive_slot_status": MoPropertyMeta("drive_slot_status", "driveSlotStatus", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version401a, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "led_fault_status": MoPropertyMeta("led_fault_status", "ledFaultStatus", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "lifeleftin_days": MoPropertyMeta("lifeleftin_days", "lifeleftinDays", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pd_chip_temp_celsius": MoPropertyMeta("pd_chip_temp_celsius", "pdChipTempCelsius", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pd_status": MoPropertyMeta("pd_status", "pdStatus", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "percentage_total_power_on_hour": MoPropertyMeta("percentage_total_power_on_hour", "percentageTotalPowerOnHour", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "performance_level": MoPropertyMeta("performance_level", "performanceLevel", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "shutdown_temperature": MoPropertyMeta("shutdown_temperature", "shutdownTemperature", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "throttle_start_temperature": MoPropertyMeta("throttle_start_temperature", "throttleStartTemperature", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "controller_temperature": MoPropertyMeta("controller_temperature", "controllerTemperature", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "drive_life_used": MoPropertyMeta("drive_life_used", "driveLifeUsed", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version404b, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "led_fault_status": MoPropertyMeta("led_fault_status", "ledFaultStatus", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "lifeleftin_days": MoPropertyMeta("lifeleftin_days", "lifeleftinDays", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pd_chip_temp_celsius": MoPropertyMeta("pd_chip_temp_celsius", "pdChipTempCelsius", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pd_status": MoPropertyMeta("pd_status", "pdStatus", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "percentage_total_power_on_hour": MoPropertyMeta("percentage_total_power_on_hour", "percentageTotalPowerOnHour", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "performance_level": MoPropertyMeta("performance_level", "performanceLevel", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "shutdown_temperature": MoPropertyMeta("shutdown_temperature", "shutdownTemperature", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "throttle_start_temperature": MoPropertyMeta("throttle_start_temperature", "throttleStartTemperature", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "controllerTemperature": "controller_temperature", 
            "dn": "dn", 
            "driveLifeUsed": "drive_life_used", 
            "driveSlotStatus": "drive_slot_status", 
            "firmwareVersion": "firmware_version", 
            "id": "id", 
            "ledFaultStatus": "led_fault_status", 
            "lifeleftinDays": "lifeleftin_days", 
            "pdChipTempCelsius": "pd_chip_temp_celsius", 
            "pdStatus": "pd_status", 
            "percentageTotalPowerOnHour": "percentage_total_power_on_hour", 
            "performanceLevel": "performance_level", 
            "productName": "product_name", 
            "rn": "rn", 
            "serial": "serial", 
            "shutdownTemperature": "shutdown_temperature", 
            "status": "status", 
            "throttleStartTemperature": "throttle_start_temperature", 
            "vendor": "vendor", 
        },

        "modular": {
            "childAction": "child_action", 
            "controllerTemperature": "controller_temperature", 
            "dn": "dn", 
            "driveLifeUsed": "drive_life_used", 
            "firmwareVersion": "firmware_version", 
            "id": "id", 
            "ledFaultStatus": "led_fault_status", 
            "lifeleftinDays": "lifeleftin_days", 
            "model": "model", 
            "pdChipTempCelsius": "pd_chip_temp_celsius", 
            "pdStatus": "pd_status", 
            "percentageTotalPowerOnHour": "percentage_total_power_on_hour", 
            "performanceLevel": "performance_level", 
            "rn": "rn", 
            "serial": "serial", 
            "shutdownTemperature": "shutdown_temperature", 
            "status": "status", 
            "throttleStartTemperature": "throttle_start_temperature", 
            "vendor": "vendor", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.controller_temperature = None
        self.drive_life_used = None
        self.drive_slot_status = None
        self.firmware_version = None
        self.led_fault_status = None
        self.lifeleftin_days = None
        self.pd_chip_temp_celsius = None
        self.pd_status = None
        self.percentage_total_power_on_hour = None
        self.performance_level = None
        self.product_name = None
        self.serial = None
        self.shutdown_temperature = None
        self.status = None
        self.throttle_start_temperature = None
        self.vendor = None
        self.model = None

        ManagedObject.__init__(self, "StorageNVMePhysicalDrive", parent_mo_or_dn, **kwargs)

