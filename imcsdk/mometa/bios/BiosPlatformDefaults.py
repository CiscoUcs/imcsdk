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
        "classic": MoMeta("BiosPlatformDefaults", "biosPlatformDefaults", "bios-defaults", VersionMeta.Version151x, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'biosUnit'], [u'biosVfASPMSupport', u'biosVfAdjacentCacheLinePrefetch', u'biosVfAltitude', u'biosVfAssertNMIOnPERR', u'biosVfAssertNMIOnSERR', u'biosVfAutoCCState', u'biosVfAutonumousCstateEnable', u'biosVfBmeDmaMitigation', u'biosVfBootOptionNumRetry', u'biosVfBootOptionReCoolDown', u'biosVfBootOptionRetry', u'biosVfBootPerformanceMode', u'biosVfCDNEnable', u'biosVfCDNSupport', u'biosVfCPUEnergyPerformance', u'biosVfCPUFrequencyFloor', u'biosVfCPUPerformance', u'biosVfCPUPowerManagement', u'biosVfCbsCmnCpuCpb', u'biosVfCbsCmnCpuGenDowncoreCtrl', u'biosVfCbsCmnCpuGlobalCstateCtrl', u'biosVfCbsCmnCpuL1StreamHwPrefetcher', u'biosVfCbsCmnCpuL2StreamHwPrefetcher', u'biosVfCbsCmnDeterminismSlider', u'biosVfCbsCmnGnbNbIOMMU', u'biosVfCbsCmnMemCtrlBankGroupSwapDdr4', u'biosVfCbsCmnMemMapBankInterleaveDdr4', u'biosVfCbsCmncTDPCtl', u'biosVfCbsDfCmnMemIntlv', u'biosVfCbsDfCmnMemIntlvSize', u'biosVfCiscoAdaptiveMemTraining', u'biosVfCiscoDebugLevel', u'biosVfCiscoOpromLaunchOptimization', u'biosVfCkeLowPolicy', u'biosVfClosedLoopThermThrotl', u'biosVfCmciEnable', u'biosVfConfigTDP', u'biosVfConsoleRedirection', u'biosVfCoreMultiProcessing', u'biosVfDCPMMFirmwareDowngrade', u'biosVfDCUPrefetch', u'biosVfDRAMClockThrottling', u'biosVfDemandScrub', u'biosVfDirectCacheAccess', u'biosVfDramRefreshRate', u'biosVfEPPProfile', u'biosVfEnergyEfficientTurbo', u'biosVfEngPerfTuning', u'biosVfEnhancedIntelSpeedStepTech', u'biosVfExecuteDisableBit', u'biosVfExtendedAPIC', u'biosVfFRB2Enable', u'biosVfHWPMEnable', u'biosVfHardwarePrefetch', u'biosVfIMCInterleave', u'biosVfIOHResource', u'biosVfIPV6PXE', u'biosVfIntelHyperThreadingTech', u'biosVfIntelSpeedSelect', u'biosVfIntelTurboBoostTech', u'biosVfIntelVTForDirectedIO', u'biosVfIntelVirtualizationTechnology', u'biosVfIohErrorEn', u'biosVfKTIPrefetch', u'biosVfLLCPrefetch', u'biosVfLOMPortOptionROM', u'biosVfLegacyUSBSupport', u'biosVfLvDIMMSupport', u'biosVfMMCFGBase', u'biosVfMemoryInterleave', u'biosVfMemoryMappedIOAbove4GB', u'biosVfMirroringMode', u'biosVfNUMAOptimized', u'biosVfOSBootWatchdogTimer', u'biosVfOSBootWatchdogTimerPolicy', u'biosVfOSBootWatchdogTimerTimeout', u'biosVfOnboardNIC', u'biosVfOnboardStorage', u'biosVfOnboardStorageSWStack', u'biosVfOutOfBandMgmtPort', u'biosVfPCIOptionROMs', u'biosVfPCISlotOptionROMEnable', u'biosVfPCIeSSDHotPlugSupport', u'biosVfPOSTErrorPause', u'biosVfPSata', u'biosVfPStateCoordType', u'biosVfPackageCStateLimit', u'biosVfPatrolScrub', u'biosVfPatrolScrubDuration', u'biosVfPchUsb30Mode', u'biosVfPciRomClp', u'biosVfPowerOnPasswordSupport', u'biosVfProcessorC1E', u'biosVfProcessorC3Report', u'biosVfProcessorC6Report', u'biosVfProcessorCState', u'biosVfPwrPerfTuning', u'biosVfQPIConfig', u'biosVfQpiSnoopMode', u'biosVfSMEE', u'biosVfSataModeSelect', u'biosVfSelectMemoryRASConfiguration', u'biosVfSerialPortAEnable', u'biosVfSinglePCTLEnable', u'biosVfSmtMode', u'biosVfSparingMode', u'biosVfSrIov', u'biosVfSubNumaClustering', u'biosVfSvmMode', u'biosVfTPMControl', u'biosVfTPMSupport', u'biosVfTXTSupport', u'biosVfUCSMBootOrderRuleControl', u'biosVfUSBBootConfig', u'biosVfUSBEmulation', u'biosVfUSBPortsConfig', u'biosVfUsbXhciSupport', u'biosVfVMDEnable', u'biosVfVgaPriority', u'biosVfWorkLoadConfig', u'biosVfXPTPrefetch'], ["Get"]),
        "modular": MoMeta("BiosPlatformDefaults", "biosPlatformDefaults", "bios-defaults", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'biosUnit'], [u'biosVfASPMSupport', u'biosVfAdjacentCacheLinePrefetch', u'biosVfAltitude', u'biosVfAssertNMIOnPERR', u'biosVfAssertNMIOnSERR', u'biosVfAutoCCState', u'biosVfAutonumousCstateEnable', u'biosVfBmeDmaMitigation', u'biosVfBootOptionRetry', u'biosVfBootPerformanceMode', u'biosVfCDNEnable', u'biosVfCDNSupport', u'biosVfCPUEnergyPerformance', u'biosVfCPUFrequencyFloor', u'biosVfCPUPerformance', u'biosVfCPUPowerManagement', u'biosVfCiscoAdaptiveMemTraining', u'biosVfCiscoDebugLevel', u'biosVfCiscoOpromLaunchOptimization', u'biosVfCkeLowPolicy', u'biosVfCmciEnable', u'biosVfConsoleRedirection', u'biosVfCoreMultiProcessing', u'biosVfDCPMMFirmwareDowngrade', u'biosVfDCUPrefetch', u'biosVfDRAMClockThrottling', u'biosVfDemandScrub', u'biosVfDirectCacheAccess', u'biosVfDramRefreshRate', u'biosVfEPPProfile', u'biosVfEnergyEfficientTurbo', u'biosVfEnhancedIntelSpeedStepTech', u'biosVfExecuteDisableBit', u'biosVfExtendedAPIC', u'biosVfFRB2Enable', u'biosVfHWPMEnable', u'biosVfHardwarePrefetch', u'biosVfIMCInterleave', u'biosVfIOHResource', u'biosVfIPV6PXE', u'biosVfIntelHyperThreadingTech', u'biosVfIntelSpeedSelect', u'biosVfIntelTurboBoostTech', u'biosVfIntelVTForDirectedIO', u'biosVfIntelVirtualizationTechnology', u'biosVfKTIPrefetch', u'biosVfLLCPrefetch', u'biosVfLOMPortOptionROM', u'biosVfLegacyUSBSupport', u'biosVfLvDIMMSupport', u'biosVfMMCFGBase', u'biosVfMemoryInterleave', u'biosVfMemoryMappedIOAbove4GB', u'biosVfMirroringMode', u'biosVfNUMAOptimized', u'biosVfOSBootWatchdogTimer', u'biosVfOSBootWatchdogTimerPolicy', u'biosVfOSBootWatchdogTimerTimeout', u'biosVfOnboardNIC', u'biosVfOnboardStorage', u'biosVfOnboardStorageSWStack', u'biosVfOutOfBandMgmtPort', u'biosVfPCIOptionROMs', u'biosVfPCISlotOptionROMEnable', u'biosVfPOSTErrorPause', u'biosVfPSata', u'biosVfPStateCoordType', u'biosVfPackageCStateLimit', u'biosVfPatrolScrub', u'biosVfPatrolScrubDuration', u'biosVfPchUsb30Mode', u'biosVfPciRomClp', u'biosVfPowerOnPasswordSupport', u'biosVfProcessorC1E', u'biosVfProcessorC3Report', u'biosVfProcessorC6Report', u'biosVfProcessorCState', u'biosVfPwrPerfTuning', u'biosVfQPIConfig', u'biosVfQpiSnoopMode', u'biosVfSataModeSelect', u'biosVfSelectMemoryRASConfiguration', u'biosVfSerialPortAEnable', u'biosVfSparingMode', u'biosVfSrIov', u'biosVfSubNumaClustering', u'biosVfTPMControl', u'biosVfTPMSupport', u'biosVfTXTSupport', u'biosVfUCSMBootOrderRuleControl', u'biosVfUSBBootConfig', u'biosVfUSBEmulation', u'biosVfUSBPortsConfig', u'biosVfUsbXhciSupport', u'biosVfVgaPriority', u'biosVfWorkLoadConfig', u'biosVfXPTPrefetch'], ["Get"])
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

