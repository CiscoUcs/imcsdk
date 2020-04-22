"""This module contains the general information for StorageControllerProps ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageControllerPropsConsts:
    pass


class StorageControllerProps(ManagedObject):
    """This is StorageControllerProps class."""

    consts = StorageControllerPropsConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StorageControllerProps", "storageControllerProps", "controller-props", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageController'], [], ["Get"]),
        "modular": MoMeta("StorageControllerProps", "storageControllerProps", "controller-props", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageController'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "backend_port_count": MoPropertyMeta("backend_port_count", "backendPortCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "battery_status": MoPropertyMeta("battery_status", "batteryStatus", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "bbu_present": MoPropertyMeta("bbu_present", "bbuPresent", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "boot_block_version": MoPropertyMeta("boot_block_version", "bootBlockVersion", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "boot_drive": MoPropertyMeta("boot_drive", "bootDrive", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "boot_drive_is_physical_drive": MoPropertyMeta("boot_drive_is_physical_drive", "bootDriveIsPhysicalDrive", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "boot_version": MoPropertyMeta("boot_version", "bootVersion", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "cache_memory_size": MoPropertyMeta("cache_memory_size", "cacheMemorySize", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "controller_status": MoPropertyMeta("controller_status", "controllerStatus", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "critical_physical_drive_count": MoPropertyMeta("critical_physical_drive_count", "criticalPhysicalDriveCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "date_of_manufacture": MoPropertyMeta("date_of_manufacture", "dateOfManufacture", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "degraded_virtual_drive_count": MoPropertyMeta("degraded_virtual_drive_count", "degradedVirtualDriveCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "failed_physical_drive_count": MoPropertyMeta("failed_physical_drive_count", "failedPhysicalDriveCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "firmware_package_build": MoPropertyMeta("firmware_package_build", "firmwarePackageBuild", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "flash_present": MoPropertyMeta("flash_present", "flashPresent", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "memory_correctable_errors": MoPropertyMeta("memory_correctable_errors", "memoryCorrectableErrors", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "memory_present": MoPropertyMeta("memory_present", "memoryPresent", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "memory_size": MoPropertyMeta("memory_size", "memorySize", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "memory_uncorrectable_errors": MoPropertyMeta("memory_uncorrectable_errors", "memoryUncorrectableErrors", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "nvdata_version": MoPropertyMeta("nvdata_version", "nvdataVersion", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "nvram_present": MoPropertyMeta("nvram_present", "nvramPresent", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "offline_virtual_drive_count": MoPropertyMeta("offline_virtual_drive_count", "offlineVirtualDriveCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "physical_drive_count": MoPropertyMeta("physical_drive_count", "physicalDriveCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "preboot_cli_version": MoPropertyMeta("preboot_cli_version", "prebootCliVersion", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "raid_chip_temp_centigrade": MoPropertyMeta("raid_chip_temp_centigrade", "raidChipTempCentigrade", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "sas_address0": MoPropertyMeta("sas_address0", "sasAddress0", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sas_address1": MoPropertyMeta("sas_address1", "sasAddress1", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sas_address2": MoPropertyMeta("sas_address2", "sasAddress2", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sas_address3": MoPropertyMeta("sas_address3", "sasAddress3", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sas_address4": MoPropertyMeta("sas_address4", "sasAddress4", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sas_address5": MoPropertyMeta("sas_address5", "sasAddress5", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sas_address6": MoPropertyMeta("sas_address6", "sasAddress6", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sas_address7": MoPropertyMeta("sas_address7", "sasAddress7", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "serial_debugger_present": MoPropertyMeta("serial_debugger_present", "serialDebuggerPresent", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "supports_raid0": MoPropertyMeta("supports_raid0", "supportsRaid0", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid00": MoPropertyMeta("supports_raid00", "supportsRaid00", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid1": MoPropertyMeta("supports_raid1", "supportsRaid1", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid10": MoPropertyMeta("supports_raid10", "supportsRaid10", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid10_with_more_than2_drives": MoPropertyMeta("supports_raid10_with_more_than2_drives", "supportsRaid10WithMoreThan2Drives", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid1_with_more_than2_drives": MoPropertyMeta("supports_raid1_with_more_than2_drives", "supportsRaid1WithMoreThan2Drives", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid1e": MoPropertyMeta("supports_raid1e", "supportsRaid1e", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid1e0rlq0": MoPropertyMeta("supports_raid1e0rlq0", "supportsRaid1e0rlq0", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid1erlq0": MoPropertyMeta("supports_raid1erlq0", "supportsRaid1erlq0", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid5": MoPropertyMeta("supports_raid5", "supportsRaid5", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid50": MoPropertyMeta("supports_raid50", "supportsRaid50", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid6": MoPropertyMeta("supports_raid6", "supportsRaid6", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid60": MoPropertyMeta("supports_raid60", "supportsRaid60", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raidsrl03": MoPropertyMeta("supports_raidsrl03", "supportsRaidsrl03", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "tty_log_status": MoPropertyMeta("tty_log_status", "ttyLogStatus", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "virtual_drive_count": MoPropertyMeta("virtual_drive_count", "virtualDriveCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "web_bios_version": MoPropertyMeta("web_bios_version", "webBiosVersion", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "backend_port_count": MoPropertyMeta("backend_port_count", "backendPortCount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "battery_status": MoPropertyMeta("battery_status", "batteryStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "bbu_present": MoPropertyMeta("bbu_present", "bbuPresent", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "boot_block_version": MoPropertyMeta("boot_block_version", "bootBlockVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "boot_drive": MoPropertyMeta("boot_drive", "bootDrive", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "boot_drive_is_physical_drive": MoPropertyMeta("boot_drive_is_physical_drive", "bootDriveIsPhysicalDrive", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "boot_version": MoPropertyMeta("boot_version", "bootVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "cache_memory_size": MoPropertyMeta("cache_memory_size", "cacheMemorySize", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "controller_status": MoPropertyMeta("controller_status", "controllerStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "critical_physical_drive_count": MoPropertyMeta("critical_physical_drive_count", "criticalPhysicalDriveCount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "date_of_manufacture": MoPropertyMeta("date_of_manufacture", "dateOfManufacture", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "degraded_virtual_drive_count": MoPropertyMeta("degraded_virtual_drive_count", "degradedVirtualDriveCount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "failed_physical_drive_count": MoPropertyMeta("failed_physical_drive_count", "failedPhysicalDriveCount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "firmware_package_build": MoPropertyMeta("firmware_package_build", "firmwarePackageBuild", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "flash_present": MoPropertyMeta("flash_present", "flashPresent", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "memory_correctable_errors": MoPropertyMeta("memory_correctable_errors", "memoryCorrectableErrors", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "memory_present": MoPropertyMeta("memory_present", "memoryPresent", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "memory_size": MoPropertyMeta("memory_size", "memorySize", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "memory_uncorrectable_errors": MoPropertyMeta("memory_uncorrectable_errors", "memoryUncorrectableErrors", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "nvdata_version": MoPropertyMeta("nvdata_version", "nvdataVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "nvram_present": MoPropertyMeta("nvram_present", "nvramPresent", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "offline_virtual_drive_count": MoPropertyMeta("offline_virtual_drive_count", "offlineVirtualDriveCount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "physical_drive_count": MoPropertyMeta("physical_drive_count", "physicalDriveCount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "preboot_cli_version": MoPropertyMeta("preboot_cli_version", "prebootCliVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "raid_chip_temp_centigrade": MoPropertyMeta("raid_chip_temp_centigrade", "raidChipTempCentigrade", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "sas_address0": MoPropertyMeta("sas_address0", "sasAddress0", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sas_address1": MoPropertyMeta("sas_address1", "sasAddress1", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sas_address2": MoPropertyMeta("sas_address2", "sasAddress2", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sas_address3": MoPropertyMeta("sas_address3", "sasAddress3", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sas_address4": MoPropertyMeta("sas_address4", "sasAddress4", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sas_address5": MoPropertyMeta("sas_address5", "sasAddress5", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sas_address6": MoPropertyMeta("sas_address6", "sasAddress6", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sas_address7": MoPropertyMeta("sas_address7", "sasAddress7", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "serial_debugger_present": MoPropertyMeta("serial_debugger_present", "serialDebuggerPresent", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "supports_raid0": MoPropertyMeta("supports_raid0", "supportsRaid0", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid00": MoPropertyMeta("supports_raid00", "supportsRaid00", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid1": MoPropertyMeta("supports_raid1", "supportsRaid1", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid10": MoPropertyMeta("supports_raid10", "supportsRaid10", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid10_with_more_than2_drives": MoPropertyMeta("supports_raid10_with_more_than2_drives", "supportsRaid10WithMoreThan2Drives", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid1_with_more_than2_drives": MoPropertyMeta("supports_raid1_with_more_than2_drives", "supportsRaid1WithMoreThan2Drives", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid1e": MoPropertyMeta("supports_raid1e", "supportsRaid1e", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid1e0rlq0": MoPropertyMeta("supports_raid1e0rlq0", "supportsRaid1e0rlq0", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid1erlq0": MoPropertyMeta("supports_raid1erlq0", "supportsRaid1erlq0", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid5": MoPropertyMeta("supports_raid5", "supportsRaid5", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid50": MoPropertyMeta("supports_raid50", "supportsRaid50", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid6": MoPropertyMeta("supports_raid6", "supportsRaid6", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raid60": MoPropertyMeta("supports_raid60", "supportsRaid60", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "supports_raidsrl03": MoPropertyMeta("supports_raidsrl03", "supportsRaidsrl03", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "tty_log_status": MoPropertyMeta("tty_log_status", "ttyLogStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "virtual_drive_count": MoPropertyMeta("virtual_drive_count", "virtualDriveCount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "web_bios_version": MoPropertyMeta("web_bios_version", "webBiosVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "backendPortCount": "backend_port_count", 
            "batteryStatus": "battery_status", 
            "bbuPresent": "bbu_present", 
            "bootBlockVersion": "boot_block_version", 
            "bootDrive": "boot_drive", 
            "bootDriveIsPhysicalDrive": "boot_drive_is_physical_drive", 
            "bootVersion": "boot_version", 
            "cacheMemorySize": "cache_memory_size", 
            "childAction": "child_action", 
            "controllerStatus": "controller_status", 
            "criticalPhysicalDriveCount": "critical_physical_drive_count", 
            "dateOfManufacture": "date_of_manufacture", 
            "degradedVirtualDriveCount": "degraded_virtual_drive_count", 
            "dn": "dn", 
            "failedPhysicalDriveCount": "failed_physical_drive_count", 
            "firmwarePackageBuild": "firmware_package_build", 
            "flashPresent": "flash_present", 
            "health": "health", 
            "memoryCorrectableErrors": "memory_correctable_errors", 
            "memoryPresent": "memory_present", 
            "memorySize": "memory_size", 
            "memoryUncorrectableErrors": "memory_uncorrectable_errors", 
            "nvdataVersion": "nvdata_version", 
            "nvramPresent": "nvram_present", 
            "offlineVirtualDriveCount": "offline_virtual_drive_count", 
            "pciSlot": "pci_slot", 
            "physicalDriveCount": "physical_drive_count", 
            "prebootCliVersion": "preboot_cli_version", 
            "raidChipTempCentigrade": "raid_chip_temp_centigrade", 
            "revision": "revision", 
            "rn": "rn", 
            "sasAddress0": "sas_address0", 
            "sasAddress1": "sas_address1", 
            "sasAddress2": "sas_address2", 
            "sasAddress3": "sas_address3", 
            "sasAddress4": "sas_address4", 
            "sasAddress5": "sas_address5", 
            "sasAddress6": "sas_address6", 
            "sasAddress7": "sas_address7", 
            "serial": "serial", 
            "serialDebuggerPresent": "serial_debugger_present", 
            "status": "status", 
            "supportsRaid0": "supports_raid0", 
            "supportsRaid00": "supports_raid00", 
            "supportsRaid1": "supports_raid1", 
            "supportsRaid10": "supports_raid10", 
            "supportsRaid10WithMoreThan2Drives": "supports_raid10_with_more_than2_drives", 
            "supportsRaid1WithMoreThan2Drives": "supports_raid1_with_more_than2_drives", 
            "supportsRaid1e": "supports_raid1e", 
            "supportsRaid1e0rlq0": "supports_raid1e0rlq0", 
            "supportsRaid1erlq0": "supports_raid1erlq0", 
            "supportsRaid5": "supports_raid5", 
            "supportsRaid50": "supports_raid50", 
            "supportsRaid6": "supports_raid6", 
            "supportsRaid60": "supports_raid60", 
            "supportsRaidsrl03": "supports_raidsrl03", 
            "ttyLogStatus": "tty_log_status", 
            "virtualDriveCount": "virtual_drive_count", 
            "webBiosVersion": "web_bios_version", 
        },

        "modular": {
            "backendPortCount": "backend_port_count", 
            "batteryStatus": "battery_status", 
            "bbuPresent": "bbu_present", 
            "bootBlockVersion": "boot_block_version", 
            "bootDrive": "boot_drive", 
            "bootDriveIsPhysicalDrive": "boot_drive_is_physical_drive", 
            "bootVersion": "boot_version", 
            "cacheMemorySize": "cache_memory_size", 
            "childAction": "child_action", 
            "controllerStatus": "controller_status", 
            "criticalPhysicalDriveCount": "critical_physical_drive_count", 
            "dateOfManufacture": "date_of_manufacture", 
            "degradedVirtualDriveCount": "degraded_virtual_drive_count", 
            "dn": "dn", 
            "failedPhysicalDriveCount": "failed_physical_drive_count", 
            "firmwarePackageBuild": "firmware_package_build", 
            "flashPresent": "flash_present", 
            "health": "health", 
            "memoryCorrectableErrors": "memory_correctable_errors", 
            "memoryPresent": "memory_present", 
            "memorySize": "memory_size", 
            "memoryUncorrectableErrors": "memory_uncorrectable_errors", 
            "nvdataVersion": "nvdata_version", 
            "nvramPresent": "nvram_present", 
            "offlineVirtualDriveCount": "offline_virtual_drive_count", 
            "pciSlot": "pci_slot", 
            "physicalDriveCount": "physical_drive_count", 
            "prebootCliVersion": "preboot_cli_version", 
            "raidChipTempCentigrade": "raid_chip_temp_centigrade", 
            "revision": "revision", 
            "rn": "rn", 
            "sasAddress0": "sas_address0", 
            "sasAddress1": "sas_address1", 
            "sasAddress2": "sas_address2", 
            "sasAddress3": "sas_address3", 
            "sasAddress4": "sas_address4", 
            "sasAddress5": "sas_address5", 
            "sasAddress6": "sas_address6", 
            "sasAddress7": "sas_address7", 
            "serial": "serial", 
            "serialDebuggerPresent": "serial_debugger_present", 
            "status": "status", 
            "supportsRaid0": "supports_raid0", 
            "supportsRaid00": "supports_raid00", 
            "supportsRaid1": "supports_raid1", 
            "supportsRaid10": "supports_raid10", 
            "supportsRaid10WithMoreThan2Drives": "supports_raid10_with_more_than2_drives", 
            "supportsRaid1WithMoreThan2Drives": "supports_raid1_with_more_than2_drives", 
            "supportsRaid1e": "supports_raid1e", 
            "supportsRaid1e0rlq0": "supports_raid1e0rlq0", 
            "supportsRaid1erlq0": "supports_raid1erlq0", 
            "supportsRaid5": "supports_raid5", 
            "supportsRaid50": "supports_raid50", 
            "supportsRaid6": "supports_raid6", 
            "supportsRaid60": "supports_raid60", 
            "supportsRaidsrl03": "supports_raidsrl03", 
            "ttyLogStatus": "tty_log_status", 
            "virtualDriveCount": "virtual_drive_count", 
            "webBiosVersion": "web_bios_version", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.backend_port_count = None
        self.battery_status = None
        self.bbu_present = None
        self.boot_block_version = None
        self.boot_drive = None
        self.boot_drive_is_physical_drive = None
        self.boot_version = None
        self.cache_memory_size = None
        self.child_action = None
        self.controller_status = None
        self.critical_physical_drive_count = None
        self.date_of_manufacture = None
        self.degraded_virtual_drive_count = None
        self.failed_physical_drive_count = None
        self.firmware_package_build = None
        self.flash_present = None
        self.health = None
        self.memory_correctable_errors = None
        self.memory_present = None
        self.memory_size = None
        self.memory_uncorrectable_errors = None
        self.nvdata_version = None
        self.nvram_present = None
        self.offline_virtual_drive_count = None
        self.pci_slot = None
        self.physical_drive_count = None
        self.preboot_cli_version = None
        self.raid_chip_temp_centigrade = None
        self.revision = None
        self.sas_address0 = None
        self.sas_address1 = None
        self.sas_address2 = None
        self.sas_address3 = None
        self.sas_address4 = None
        self.sas_address5 = None
        self.sas_address6 = None
        self.sas_address7 = None
        self.serial = None
        self.serial_debugger_present = None
        self.status = None
        self.supports_raid0 = None
        self.supports_raid00 = None
        self.supports_raid1 = None
        self.supports_raid10 = None
        self.supports_raid10_with_more_than2_drives = None
        self.supports_raid1_with_more_than2_drives = None
        self.supports_raid1e = None
        self.supports_raid1e0rlq0 = None
        self.supports_raid1erlq0 = None
        self.supports_raid5 = None
        self.supports_raid50 = None
        self.supports_raid6 = None
        self.supports_raid60 = None
        self.supports_raidsrl03 = None
        self.tty_log_status = None
        self.virtual_drive_count = None
        self.web_bios_version = None

        ManagedObject.__init__(self, "StorageControllerProps", parent_mo_or_dn, **kwargs)

