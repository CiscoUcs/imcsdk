"""This module contains the general information for IoControllerNVMePhysicalDrive ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class IoControllerNVMePhysicalDriveConsts:
    pass


class IoControllerNVMePhysicalDrive(ManagedObject):
    """This is IoControllerNVMePhysicalDrive class."""

    consts = IoControllerNVMePhysicalDriveConsts()
    naming_props = set(['id'])

    mo_meta = {
        "modular": MoMeta("IoControllerNVMePhysicalDrive", "ioControllerNVMePhysicalDrive", "pd-[id]", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['systemIOControllerNVMe'], ['faultInst'], [None])
    }


    prop_meta = {

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
        self.firmware_version = None
        self.led_fault_status = None
        self.lifeleftin_days = None
        self.model = None
        self.pd_chip_temp_celsius = None
        self.pd_status = None
        self.percentage_total_power_on_hour = None
        self.performance_level = None
        self.serial = None
        self.shutdown_temperature = None
        self.status = None
        self.throttle_start_temperature = None
        self.vendor = None

        ManagedObject.__init__(self, "IoControllerNVMePhysicalDrive", parent_mo_or_dn, **kwargs)

