"""This module contains the general information for BiosPlatformDefaults ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosPlatformDefaultsConsts:
    pass


class BiosPlatformDefaults(ManagedObject):
    """This is BiosPlatformDefaults class."""

    consts = BiosPlatformDefaultsConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosPlatformDefaults", "biosPlatformDefaults", "bios-defaults", VersionMeta.Version151x, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'biosUnit'], [u'biosVfASPMSupport', u'biosVfAdjacentCacheLinePrefetch', u'biosVfAltitude', u'biosVfAssertNMIOnPERR', u'biosVfAssertNMIOnSERR', u'biosVfAutonumousCstateEnable', u'biosVfBootOptionRetry', u'biosVfCDNEnable', u'biosVfCDNSupport', u'biosVfCPUEnergyPerformance', u'biosVfCPUFrequencyFloor', u'biosVfCPUPerformance', u'biosVfCPUPowerManagement', u'biosVfCkeLowPolicy', u'biosVfCmciEnable', u'biosVfConsoleRedirection', u'biosVfCoreMultiProcessing', u'biosVfDCUPrefetch', u'biosVfDRAMClockThrottling', u'biosVfDemandScrub', u'biosVfDirectCacheAccess', u'biosVfDramRefreshRate', u'biosVfEnhancedIntelSpeedStepTech', u'biosVfExecuteDisableBit', u'biosVfExtendedAPIC', u'biosVfFRB2Enable', u'biosVfHWPMEnable', u'biosVfHardwarePrefetch', u'biosVfIOHResource', u'biosVfIntelHyperThreadingTech', u'biosVfIntelTurboBoostTech', u'biosVfIntelVTForDirectedIO', u'biosVfIntelVirtualizationTechnology', u'biosVfLOMPortOptionROM', u'biosVfLegacyUSBSupport', u'biosVfLvDIMMSupport', u'biosVfMMCFGBase', u'biosVfMemoryInterleave', u'biosVfMemoryMappedIOAbove4GB', u'biosVfMirroringMode', u'biosVfNUMAOptimized', u'biosVfOSBootWatchdogTimer', u'biosVfOSBootWatchdogTimerPolicy', u'biosVfOSBootWatchdogTimerTimeout', u'biosVfOnboardNIC', u'biosVfOnboardStorage', u'biosVfOnboardStorageSWStack', u'biosVfOutOfBandMgmtPort', u'biosVfPCIOptionROMs', u'biosVfPCISlotOptionROMEnable', u'biosVfPCIeSSDHotPlugSupport', u'biosVfPOSTErrorPause', u'biosVfPStateCoordType', u'biosVfPackageCStateLimit', u'biosVfPatrolScrub', u'biosVfPatrolScrubDuration', u'biosVfPchUsb30Mode', u'biosVfPciRomClp', u'biosVfPowerOnPasswordSupport', u'biosVfProcessorC1E', u'biosVfProcessorC3Report', u'biosVfProcessorC6Report', u'biosVfProcessorCState', u'biosVfPwrPerfTuning', u'biosVfQPIConfig', u'biosVfQpiSnoopMode', u'biosVfSataModeSelect', u'biosVfSelectMemoryRASConfiguration', u'biosVfSerialPortAEnable', u'biosVfSparingMode', u'biosVfSrIov', u'biosVfTPMSupport', u'biosVfUCSMBootOrderRuleControl', u'biosVfUSBBootConfig', u'biosVfUSBEmulation', u'biosVfUSBPortsConfig', u'biosVfVgaPriority', u'biosVfWorkLoadConfig'], ["Get"]),
        "modular": MoMeta("BiosPlatformDefaults", "biosPlatformDefaults", "bios-defaults", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'biosUnit'], [u'biosVfASPMSupport', u'biosVfAdjacentCacheLinePrefetch', u'biosVfAltitude', u'biosVfAssertNMIOnPERR', u'biosVfAssertNMIOnSERR', u'biosVfBootOptionRetry', u'biosVfCDNEnable', u'biosVfCDNSupport', u'biosVfCPUEnergyPerformance', u'biosVfCPUFrequencyFloor', u'biosVfCPUPerformance', u'biosVfCPUPowerManagement', u'biosVfCkeLowPolicy', u'biosVfCmciEnable', u'biosVfConsoleRedirection', u'biosVfCoreMultiProcessing', u'biosVfDCUPrefetch', u'biosVfDRAMClockThrottling', u'biosVfDemandScrub', u'biosVfDirectCacheAccess', u'biosVfDramRefreshRate', u'biosVfEnhancedIntelSpeedStepTech', u'biosVfExecuteDisableBit', u'biosVfExtendedAPIC', u'biosVfFRB2Enable', u'biosVfHardwarePrefetch', u'biosVfIOHResource', u'biosVfIntelHyperThreadingTech', u'biosVfIntelTurboBoostTech', u'biosVfIntelVTForDirectedIO', u'biosVfIntelVirtualizationTechnology', u'biosVfLOMPortOptionROM', u'biosVfLegacyUSBSupport', u'biosVfLvDIMMSupport', u'biosVfMMCFGBase', u'biosVfMemoryInterleave', u'biosVfMemoryMappedIOAbove4GB', u'biosVfMirroringMode', u'biosVfNUMAOptimized', u'biosVfOSBootWatchdogTimer', u'biosVfOSBootWatchdogTimerPolicy', u'biosVfOSBootWatchdogTimerTimeout', u'biosVfOnboardNIC', u'biosVfOnboardStorage', u'biosVfOnboardStorageSWStack', u'biosVfOutOfBandMgmtPort', u'biosVfPCIOptionROMs', u'biosVfPCISlotOptionROMEnable', u'biosVfPOSTErrorPause', u'biosVfPStateCoordType', u'biosVfPackageCStateLimit', u'biosVfPatrolScrub', u'biosVfPatrolScrubDuration', u'biosVfPchUsb30Mode', u'biosVfPciRomClp', u'biosVfPowerOnPasswordSupport', u'biosVfProcessorC1E', u'biosVfProcessorC3Report', u'biosVfProcessorC6Report', u'biosVfProcessorCState', u'biosVfPwrPerfTuning', u'biosVfQPIConfig', u'biosVfQpiSnoopMode', u'biosVfSataModeSelect', u'biosVfSelectMemoryRASConfiguration', u'biosVfSerialPortAEnable', u'biosVfSparingMode', u'biosVfSrIov', u'biosVfTPMSupport', u'biosVfUCSMBootOrderRuleControl', u'biosVfUSBBootConfig', u'biosVfUSBEmulation', u'biosVfUSBPortsConfig', u'biosVfVgaPriority', u'biosVfWorkLoadConfig'], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151x, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "BiosPlatformDefaults", parent_mo_or_dn, **kwargs)

