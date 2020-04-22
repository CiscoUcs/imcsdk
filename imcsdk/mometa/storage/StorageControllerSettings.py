"""This module contains the general information for StorageControllerSettings ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageControllerSettingsConsts:
    pass


class StorageControllerSettings(ManagedObject):
    """This is StorageControllerSettings class."""

    consts = StorageControllerSettingsConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StorageControllerSettings", "storageControllerSettings", "controller-settings", VersionMeta.Version201a, "InputOutput", 0xf, [], ["admin", "read-only", "user"], ['storageController'], [], ["Get"]),
        "modular": MoMeta("StorageControllerSettings", "storageControllerSettings", "controller-settings", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageController'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "auto_enhanced_import": MoPropertyMeta("auto_enhanced_import", "autoEnhancedImport", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "battery_warning": MoPropertyMeta("battery_warning", "batteryWarning", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "cache_flush_interval": MoPropertyMeta("cache_flush_interval", "cacheFlushInterval", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "cluster_enable": MoPropertyMeta("cluster_enable", "clusterEnable", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "consistency_check_rate": MoPropertyMeta("consistency_check_rate", "consistencyCheckRate", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "ecc_bucket_leak_rate": MoPropertyMeta("ecc_bucket_leak_rate", "eccBucketLeakRate", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "enable_copyback_on_smart": MoPropertyMeta("enable_copyback_on_smart", "enableCopybackOnSmart", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "enable_copyback_to_ssd_on_smart_error": MoPropertyMeta("enable_copyback_to_ssd_on_smart_error", "enableCopybackToSsdOnSmartError", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "enable_jbod": MoPropertyMeta("enable_jbod", "enableJbod", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "enable_ssd_patrol_read": MoPropertyMeta("enable_ssd_patrol_read", "enableSsdPatrolRead", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "expose_enclosure_devices": MoPropertyMeta("expose_enclosure_devices", "exposeEnclosureDevices", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "maintain_pd_fail_history": MoPropertyMeta("maintain_pd_fail_history", "maintainPdFailHistory", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "ncq_status": MoPropertyMeta("ncq_status", "ncqStatus", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "patrol_read_rate": MoPropertyMeta("patrol_read_rate", "patrolReadRate", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "phys_drive_coercion_mode": MoPropertyMeta("phys_drive_coercion_mode", "physDriveCoercionMode", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "predictive_fail_poll_interval": MoPropertyMeta("predictive_fail_poll_interval", "predictiveFailPollInterval", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rebuild_rate": MoPropertyMeta("rebuild_rate", "rebuildRate", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "reconstruction_rate": MoPropertyMeta("reconstruction_rate", "reconstructionRate", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "spin_down_unconfigured": MoPropertyMeta("spin_down_unconfigured", "spinDownUnconfigured", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "spinup_delay": MoPropertyMeta("spinup_delay", "spinupDelay", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "spinup_drive_count": MoPropertyMeta("spinup_drive_count", "spinupDriveCount", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "auto_enhanced_import": MoPropertyMeta("auto_enhanced_import", "autoEnhancedImport", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "battery_warning": MoPropertyMeta("battery_warning", "batteryWarning", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "cache_flush_interval": MoPropertyMeta("cache_flush_interval", "cacheFlushInterval", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "cluster_enable": MoPropertyMeta("cluster_enable", "clusterEnable", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "consistency_check_rate": MoPropertyMeta("consistency_check_rate", "consistencyCheckRate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "ecc_bucket_leak_rate": MoPropertyMeta("ecc_bucket_leak_rate", "eccBucketLeakRate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "enable_copyback_on_smart": MoPropertyMeta("enable_copyback_on_smart", "enableCopybackOnSmart", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "enable_copyback_to_ssd_on_smart_error": MoPropertyMeta("enable_copyback_to_ssd_on_smart_error", "enableCopybackToSsdOnSmartError", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "enable_jbod": MoPropertyMeta("enable_jbod", "enableJbod", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "enable_ssd_patrol_read": MoPropertyMeta("enable_ssd_patrol_read", "enableSsdPatrolRead", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "expose_enclosure_devices": MoPropertyMeta("expose_enclosure_devices", "exposeEnclosureDevices", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "maintain_pd_fail_history": MoPropertyMeta("maintain_pd_fail_history", "maintainPdFailHistory", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "ncq_status": MoPropertyMeta("ncq_status", "ncqStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "patrol_read_rate": MoPropertyMeta("patrol_read_rate", "patrolReadRate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "phys_drive_coercion_mode": MoPropertyMeta("phys_drive_coercion_mode", "physDriveCoercionMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "predictive_fail_poll_interval": MoPropertyMeta("predictive_fail_poll_interval", "predictiveFailPollInterval", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rebuild_rate": MoPropertyMeta("rebuild_rate", "rebuildRate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "reconstruction_rate": MoPropertyMeta("reconstruction_rate", "reconstructionRate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "spin_down_unconfigured": MoPropertyMeta("spin_down_unconfigured", "spinDownUnconfigured", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "spinup_delay": MoPropertyMeta("spinup_delay", "spinupDelay", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "spinup_drive_count": MoPropertyMeta("spinup_drive_count", "spinupDriveCount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "autoEnhancedImport": "auto_enhanced_import", 
            "batteryWarning": "battery_warning", 
            "cacheFlushInterval": "cache_flush_interval", 
            "childAction": "child_action", 
            "clusterEnable": "cluster_enable", 
            "consistencyCheckRate": "consistency_check_rate", 
            "dn": "dn", 
            "eccBucketLeakRate": "ecc_bucket_leak_rate", 
            "enableCopybackOnSmart": "enable_copyback_on_smart", 
            "enableCopybackToSsdOnSmartError": "enable_copyback_to_ssd_on_smart_error", 
            "enableJbod": "enable_jbod", 
            "enableSsdPatrolRead": "enable_ssd_patrol_read", 
            "exposeEnclosureDevices": "expose_enclosure_devices", 
            "maintainPdFailHistory": "maintain_pd_fail_history", 
            "ncqStatus": "ncq_status", 
            "patrolReadRate": "patrol_read_rate", 
            "pciSlot": "pci_slot", 
            "physDriveCoercionMode": "phys_drive_coercion_mode", 
            "predictiveFailPollInterval": "predictive_fail_poll_interval", 
            "rebuildRate": "rebuild_rate", 
            "reconstructionRate": "reconstruction_rate", 
            "rn": "rn", 
            "spinDownUnconfigured": "spin_down_unconfigured", 
            "spinupDelay": "spinup_delay", 
            "spinupDriveCount": "spinup_drive_count", 
            "status": "status", 
        },

        "modular": {
            "autoEnhancedImport": "auto_enhanced_import", 
            "batteryWarning": "battery_warning", 
            "cacheFlushInterval": "cache_flush_interval", 
            "childAction": "child_action", 
            "clusterEnable": "cluster_enable", 
            "consistencyCheckRate": "consistency_check_rate", 
            "dn": "dn", 
            "eccBucketLeakRate": "ecc_bucket_leak_rate", 
            "enableCopybackOnSmart": "enable_copyback_on_smart", 
            "enableCopybackToSsdOnSmartError": "enable_copyback_to_ssd_on_smart_error", 
            "enableJbod": "enable_jbod", 
            "enableSsdPatrolRead": "enable_ssd_patrol_read", 
            "exposeEnclosureDevices": "expose_enclosure_devices", 
            "maintainPdFailHistory": "maintain_pd_fail_history", 
            "ncqStatus": "ncq_status", 
            "patrolReadRate": "patrol_read_rate", 
            "pciSlot": "pci_slot", 
            "physDriveCoercionMode": "phys_drive_coercion_mode", 
            "predictiveFailPollInterval": "predictive_fail_poll_interval", 
            "rebuildRate": "rebuild_rate", 
            "reconstructionRate": "reconstruction_rate", 
            "rn": "rn", 
            "spinDownUnconfigured": "spin_down_unconfigured", 
            "spinupDelay": "spinup_delay", 
            "spinupDriveCount": "spinup_drive_count", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.auto_enhanced_import = None
        self.battery_warning = None
        self.cache_flush_interval = None
        self.child_action = None
        self.cluster_enable = None
        self.consistency_check_rate = None
        self.ecc_bucket_leak_rate = None
        self.enable_copyback_on_smart = None
        self.enable_copyback_to_ssd_on_smart_error = None
        self.enable_jbod = None
        self.enable_ssd_patrol_read = None
        self.expose_enclosure_devices = None
        self.maintain_pd_fail_history = None
        self.ncq_status = None
        self.patrol_read_rate = None
        self.pci_slot = None
        self.phys_drive_coercion_mode = None
        self.predictive_fail_poll_interval = None
        self.rebuild_rate = None
        self.reconstruction_rate = None
        self.spin_down_unconfigured = None
        self.spinup_delay = None
        self.spinup_drive_count = None
        self.status = None

        ManagedObject.__init__(self, "StorageControllerSettings", parent_mo_or_dn, **kwargs)

