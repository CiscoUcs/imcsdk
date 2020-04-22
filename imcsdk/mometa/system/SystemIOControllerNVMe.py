"""This module contains the general information for SystemIOControllerNVMe ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class SystemIOControllerNVMeConsts:
    pass


class SystemIOControllerNVMe(ManagedObject):
    """This is SystemIOControllerNVMe class."""

    consts = SystemIOControllerNVMeConsts()
    naming_props = set(['id'])

    mo_meta = {
        "modular": MoMeta("SystemIOControllerNVMe", "systemIOControllerNVMe", "sioc-NVMe-[id]", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['equipmentSystemIOController'], ['faultInst', 'ioControllerNVMePhysicalDrive'], [None])
    }


    prop_meta = {

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "component_id": MoPropertyMeta("component_id", "componentId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "controller_chip_temp_celsius": MoPropertyMeta("controller_chip_temp_celsius", "controllerChipTempCelsius", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "controller_status": MoPropertyMeta("controller_status", "controllerStatus", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "drive_count": MoPropertyMeta("drive_count", "driveCount", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "drive_life_used": MoPropertyMeta("drive_life_used", "driveLifeUsed", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version404b, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "led_fault_status": MoPropertyMeta("led_fault_status", "ledFaultStatus", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "link_status": MoPropertyMeta("link_status", "linkStatus", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "p2p_device_id": MoPropertyMeta("p2p_device_id", "p2pDeviceId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "p2p_vendor_id": MoPropertyMeta("p2p_vendor_id", "p2pVendorId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pending_firmware_version": MoPropertyMeta("pending_firmware_version", "pendingFirmwareVersion", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "percentage_total_power_on_hour": MoPropertyMeta("percentage_total_power_on_hour", "percentageTotalPowerOnHour", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "performance_level": MoPropertyMeta("performance_level", "performanceLevel", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_id": MoPropertyMeta("product_id", "productId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_revision": MoPropertyMeta("product_revision", "productRevision", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "running_firmware_version": MoPropertyMeta("running_firmware_version", "runningFirmwareVersion", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "shutdown_temperature": MoPropertyMeta("shutdown_temperature", "shutdownTemperature", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "switch_status": MoPropertyMeta("switch_status", "switchStatus", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "temperature": MoPropertyMeta("temperature", "temperature", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor_id": MoPropertyMeta("vendor_id", "vendorId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "modular": {
            "childAction": "child_action", 
            "componentId": "component_id", 
            "controllerChipTempCelsius": "controller_chip_temp_celsius", 
            "controllerStatus": "controller_status", 
            "dn": "dn", 
            "driveCount": "drive_count", 
            "driveLifeUsed": "drive_life_used", 
            "health": "health", 
            "id": "id", 
            "ledFaultStatus": "led_fault_status", 
            "linkStatus": "link_status", 
            "model": "model", 
            "p2pDeviceId": "p2p_device_id", 
            "p2pVendorId": "p2p_vendor_id", 
            "pendingFirmwareVersion": "pending_firmware_version", 
            "percentageTotalPowerOnHour": "percentage_total_power_on_hour", 
            "performanceLevel": "performance_level", 
            "productId": "product_id", 
            "productRevision": "product_revision", 
            "rn": "rn", 
            "runningFirmwareVersion": "running_firmware_version", 
            "serial": "serial", 
            "shutdownTemperature": "shutdown_temperature", 
            "status": "status", 
            "switchStatus": "switch_status", 
            "temperature": "temperature", 
            "vendor": "vendor", 
            "vendorId": "vendor_id", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.component_id = None
        self.controller_chip_temp_celsius = None
        self.controller_status = None
        self.drive_count = None
        self.drive_life_used = None
        self.health = None
        self.led_fault_status = None
        self.link_status = None
        self.model = None
        self.p2p_device_id = None
        self.p2p_vendor_id = None
        self.pending_firmware_version = None
        self.percentage_total_power_on_hour = None
        self.performance_level = None
        self.product_id = None
        self.product_revision = None
        self.running_firmware_version = None
        self.serial = None
        self.shutdown_temperature = None
        self.status = None
        self.switch_status = None
        self.temperature = None
        self.vendor = None
        self.vendor_id = None

        ManagedObject.__init__(self, "SystemIOControllerNVMe", parent_mo_or_dn, **kwargs)

