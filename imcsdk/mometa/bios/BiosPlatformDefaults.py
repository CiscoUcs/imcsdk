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
        "classic": MoMeta("BiosPlatformDefaults", "biosPlatformDefaults", "bios-defaults", VersionMeta.Version151x, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosUnit'], ['biosVfASPMSupport', 'biosVfAdjacentCacheLinePrefetch', 'biosVfAltitude', 'biosVfAssertNMIOnPERR', 'biosVfAssertNMIOnSERR', 'biosVfAutoCCState', 'biosVfAutonumousCstateEnable', 'biosVfBmeDmaMitigation', 'biosVfBootOptionNumRetry', 'biosVfBootOptionReCoolDown', 'biosVfBootOptionRetry', 'biosVfBootPerformanceMode', 'biosVfCDNEnable', 'biosVfCDNSupport', 'biosVfCPUEnergyPerformance', 'biosVfCPUFrequencyFloor', 'biosVfCPUPerformance', 'biosVfCPUPowerManagement', 'biosVfCbsCmnCpuCpb', 'biosVfCbsCmnCpuGenDowncoreCtrl', 'biosVfCbsCmnCpuGlobalCstateCtrl', 'biosVfCbsCmnCpuL1StreamHwPrefetcher', 'biosVfCbsCmnCpuL2StreamHwPrefetcher', 'biosVfCbsCmnDeterminismSlider', 'biosVfCbsCmnGnbNbIOMMU', 'biosVfCbsCmnMemCtrlBankGroupSwapDdr4', 'biosVfCbsCmnMemMapBankInterleaveDdr4', 'biosVfCbsCmncTDPCtl', 'biosVfCbsDfCmnMemIntlv', 'biosVfCbsDfCmnMemIntlvSize', 'biosVfCiscoAdaptiveMemTraining', 'biosVfCiscoDebugLevel', 'biosVfCiscoOpromLaunchOptimization', 'biosVfCkeLowPolicy', 'biosVfClosedLoopThermThrotl', 'biosVfCmciEnable', 'biosVfConfigTDP', 'biosVfConsoleRedirection', 'biosVfCoreMultiProcessing', 'biosVfDCPMMFirmwareDowngrade', 'biosVfDCUPrefetch', 'biosVfDRAMClockThrottling', 'biosVfDemandScrub', 'biosVfDirectCacheAccess', 'biosVfDramRefreshRate', 'biosVfEPPProfile', 'biosVfEnergyEfficientTurbo', 'biosVfEngPerfTuning', 'biosVfEnhancedIntelSpeedStepTech', 'biosVfExecuteDisableBit', 'biosVfExtendedAPIC', 'biosVfFRB2Enable', 'biosVfHWPMEnable', 'biosVfHardwarePrefetch', 'biosVfIMCInterleave', 'biosVfIOHResource', 'biosVfIPV4PXE', 'biosVfIPV6PXE', 'biosVfIntelHyperThreadingTech', 'biosVfIntelSpeedSelect', 'biosVfIntelTurboBoostTech', 'biosVfIntelVTForDirectedIO', 'biosVfIntelVirtualizationTechnology', 'biosVfIohErrorEn', 'biosVfKTIPrefetch', 'biosVfLLCPrefetch', 'biosVfLOMPortOptionROM', 'biosVfLegacyUSBSupport', 'biosVfLvDIMMSupport', 'biosVfMMCFGBase', 'biosVfMemoryInterleave', 'biosVfMemoryMappedIOAbove4GB', 'biosVfMemorySizeLimit', 'biosVfMirroringMode', 'biosVfNUMAOptimized', 'biosVfNetworkStack', 'biosVfOSBootWatchdogTimer', 'biosVfOSBootWatchdogTimerPolicy', 'biosVfOSBootWatchdogTimerTimeout', 'biosVfOnboardNIC', 'biosVfOnboardStorage', 'biosVfOnboardStorageSWStack', 'biosVfOutOfBandMgmtPort', 'biosVfPCIOptionROMs', 'biosVfPCISlotOptionROMEnable', 'biosVfPCIeRASSupport', 'biosVfPCIeSSDHotPlugSupport', 'biosVfPOSTErrorPause', 'biosVfPSata', 'biosVfPStateCoordType', 'biosVfPackageCStateLimit', 'biosVfPartialMirrorModeConfig', 'biosVfPartialMirrorPercent', 'biosVfPartialMirrorValue1', 'biosVfPartialMirrorValue2', 'biosVfPartialMirrorValue3', 'biosVfPartialMirrorValue4', 'biosVfPatrolScrub', 'biosVfPatrolScrubDuration', 'biosVfPchUsb30Mode', 'biosVfPciRomClp', 'biosVfPowerOnPasswordSupport', 'biosVfProcessorC1E', 'biosVfProcessorC3Report', 'biosVfProcessorC6Report', 'biosVfProcessorCState', 'biosVfPwrPerfTuning', 'biosVfQPIConfig', 'biosVfQpiSnoopMode', 'biosVfSMEE', 'biosVfSataModeSelect', 'biosVfSelectMemoryRASConfiguration', 'biosVfSelectPprType', 'biosVfSerialPortAEnable', 'biosVfSinglePCTLEnable', 'biosVfSmtMode', 'biosVfSparingMode', 'biosVfSrIov', 'biosVfSubNumaClustering', 'biosVfSvmMode', 'biosVfTPMControl', 'biosVfTPMSupport', 'biosVfTXTSupport', 'biosVfUCSMBootOrderRuleControl', 'biosVfUSBBootConfig', 'biosVfUSBEmulation', 'biosVfUSBPortsConfig', 'biosVfUsbXhciSupport', 'biosVfVMDEnable', 'biosVfVgaPriority', 'biosVfWorkLoadConfig', 'biosVfXPTPrefetch'], ["Get"]),
        "modular": MoMeta("BiosPlatformDefaults", "biosPlatformDefaults", "bios-defaults", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosUnit'], ['biosVfASPMSupport', 'biosVfAdjacentCacheLinePrefetch', 'biosVfAltitude', 'biosVfAssertNMIOnPERR', 'biosVfAssertNMIOnSERR', 'biosVfAutoCCState', 'biosVfAutonumousCstateEnable', 'biosVfBmeDmaMitigation', 'biosVfBootOptionRetry', 'biosVfBootPerformanceMode', 'biosVfCDNEnable', 'biosVfCDNSupport', 'biosVfCPUEnergyPerformance', 'biosVfCPUFrequencyFloor', 'biosVfCPUPerformance', 'biosVfCPUPowerManagement', 'biosVfCiscoAdaptiveMemTraining', 'biosVfCiscoDebugLevel', 'biosVfCiscoOpromLaunchOptimization', 'biosVfCkeLowPolicy', 'biosVfCmciEnable', 'biosVfConsoleRedirection', 'biosVfCoreMultiProcessing', 'biosVfDCPMMFirmwareDowngrade', 'biosVfDCUPrefetch', 'biosVfDRAMClockThrottling', 'biosVfDemandScrub', 'biosVfDirectCacheAccess', 'biosVfDramRefreshRate', 'biosVfEPPProfile', 'biosVfEnergyEfficientTurbo', 'biosVfEnhancedIntelSpeedStepTech', 'biosVfExecuteDisableBit', 'biosVfExtendedAPIC', 'biosVfFRB2Enable', 'biosVfHWPMEnable', 'biosVfHardwarePrefetch', 'biosVfIMCInterleave', 'biosVfIOHResource', 'biosVfIPV4PXE', 'biosVfIPV6PXE', 'biosVfIntelHyperThreadingTech', 'biosVfIntelSpeedSelect', 'biosVfIntelTurboBoostTech', 'biosVfIntelVTForDirectedIO', 'biosVfIntelVirtualizationTechnology', 'biosVfKTIPrefetch', 'biosVfLLCPrefetch', 'biosVfLOMPortOptionROM', 'biosVfLegacyUSBSupport', 'biosVfLvDIMMSupport', 'biosVfMMCFGBase', 'biosVfMemoryInterleave', 'biosVfMemoryMappedIOAbove4GB', 'biosVfMemorySizeLimit', 'biosVfMirroringMode', 'biosVfNUMAOptimized', 'biosVfNetworkStack', 'biosVfOSBootWatchdogTimer', 'biosVfOSBootWatchdogTimerPolicy', 'biosVfOSBootWatchdogTimerTimeout', 'biosVfOnboardNIC', 'biosVfOnboardStorage', 'biosVfOnboardStorageSWStack', 'biosVfOutOfBandMgmtPort', 'biosVfPCIOptionROMs', 'biosVfPCISlotOptionROMEnable', 'biosVfPCIeRASSupport', 'biosVfPOSTErrorPause', 'biosVfPSata', 'biosVfPStateCoordType', 'biosVfPackageCStateLimit', 'biosVfPartialMirrorModeConfig', 'biosVfPartialMirrorPercent', 'biosVfPartialMirrorValue1', 'biosVfPartialMirrorValue2', 'biosVfPartialMirrorValue3', 'biosVfPartialMirrorValue4', 'biosVfPatrolScrub', 'biosVfPatrolScrubDuration', 'biosVfPchUsb30Mode', 'biosVfPciRomClp', 'biosVfPowerOnPasswordSupport', 'biosVfProcessorC1E', 'biosVfProcessorC3Report', 'biosVfProcessorC6Report', 'biosVfProcessorCState', 'biosVfPwrPerfTuning', 'biosVfQPIConfig', 'biosVfQpiSnoopMode', 'biosVfSataModeSelect', 'biosVfSelectMemoryRASConfiguration', 'biosVfSelectPprType', 'biosVfSerialPortAEnable', 'biosVfSparingMode', 'biosVfSrIov', 'biosVfSubNumaClustering', 'biosVfTPMControl', 'biosVfTPMSupport', 'biosVfTXTSupport', 'biosVfUCSMBootOrderRuleControl', 'biosVfUSBBootConfig', 'biosVfUSBEmulation', 'biosVfUSBPortsConfig', 'biosVfUsbXhciSupport', 'biosVfVgaPriority', 'biosVfWorkLoadConfig', 'biosVfXPTPrefetch'], ["Get"])
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

