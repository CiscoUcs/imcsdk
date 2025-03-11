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
        "classic": MoMeta("BiosPlatformDefaults", "biosPlatformDefaults", "bios-defaults", VersionMeta.Version151x, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosUnit'], ['biosVfASPMSupport', 'biosVfAcpiSratSpFlagEn', 'biosVfAdaptiveRefreshMgmtLevel', 'biosVfAdjacentCacheLinePrefetch', 'biosVfAdvancedMemTest', 'biosVfAltitude', 'biosVfAssertNMIOnPERR', 'biosVfAssertNMIOnSERR', 'biosVfAutoCCState', 'biosVfAutonumousCstateEnable', 'biosVfBmeDmaMitigation', 'biosVfBootOptionNumRetry', 'biosVfBootOptionReCoolDown', 'biosVfBootOptionRetry', 'biosVfBootPerformanceMode', 'biosVfBurstAndPostponedRefresh', 'biosVfC1AutoDemotion', 'biosVfC1AutoUnDemotion', 'biosVfCDNEnable', 'biosVfCDNSupport', 'biosVfCPUEnergyPerformance', 'biosVfCPUFrequencyFloor', 'biosVfCPUPerformance', 'biosVfCPUPowerManagement', 'biosVfCRQos', 'biosVfCbsCmnApbdis', 'biosVfCbsCmnApbdisDfPstateRs', 'biosVfCbsCmnCpuAvx512', 'biosVfCbsCmnCpuCpb', 'biosVfCbsCmnCpuGenDowncoreCtrl', 'biosVfCbsCmnCpuGlobalCstateCtrl', 'biosVfCbsCmnCpuL1StreamHwPrefetcher', 'biosVfCbsCmnCpuL2StreamHwPrefetcher', 'biosVfCbsCmnCpuSevAsidSpaceLimit', 'biosVfCbsCmnCpuSmee', 'biosVfCbsCmnCpuStreamingStoresCtrl', 'biosVfCbsCmnDeterminismSlider', 'biosVfCbsCmnEdcControlThrottle', 'biosVfCbsCmnEfficiencyModeEn', 'biosVfCbsCmnEfficiencyModeEnRs', 'biosVfCbsCmnFixedSocPstate', 'biosVfCbsCmnGnbNbIOMMU', 'biosVfCbsCmnGnbSMUCPPC', 'biosVfCbsCmnGnbSMUDfCstates', 'biosVfCbsCmnGnbSMUDffoRs', 'biosVfCbsCmnGnbSMUDlwmSupport', 'biosVfCbsCmnMemCtrlBankGroupSwapDdr4', 'biosVfCbsCmnMemCtrllerPwrDnEnDdr', 'biosVfCbsCmnMemMapBankInterleaveDdr4', 'biosVfCbsCmnMemSpeedDdr47xx2', 'biosVfCbsCmnMemSpeedDdr47xx3', 'biosVfCbsCmnPreferredIO7xx2', 'biosVfCbsCmnPreferredIO7xx3', 'biosVfCbsCmncTDPCtl', 'biosVfCbsCmnxGmiForceLinkWidthRs', 'biosVfCbsCpuCcdCtrlSsp', 'biosVfCbsCpuCoreCtrl', 'biosVfCbsCpuDownCoreCtrlBergamo', 'biosVfCbsCpuDownCoreCtrlGenoa', 'biosVfCbsCpuSmtCtrl', 'biosVfCbsDbgCpuGenCpuWdt', 'biosVfCbsDbgCpuLApicMode', 'biosVfCbsDbgCpuSnpMemCover', 'biosVfCbsDbgCpuSnpMemSizeCover', 'biosVfCbsDfCmn4LinkMaxXgmiSpeed', 'biosVfCbsDfCmnAcpiSratL3Numa', 'biosVfCbsDfCmnDramNps', 'biosVfCbsDfCmnDramScrubTime', 'biosVfCbsDfCmnMemIntlv', 'biosVfCbsDfCmnMemIntlvControl', 'biosVfCbsDfCmnMemIntlvSize', 'biosVfCbsDfDbgXgmiLinkCfg', 'biosVfCbsGnbDbgPcieTbtSupport', 'biosVfCbsSevSnpSupport', 'biosVfCiscoAdaptiveMemTraining', 'biosVfCiscoDebugLevel', 'biosVfCiscoOpromLaunchOptimization', 'biosVfCiscoXgmiMaxSpeed', 'biosVfCkeLowPolicy', 'biosVfClosedLoopThermThrotl', 'biosVfCmciEnable', 'biosVfConfigTDP', 'biosVfConfigTDPLevel', 'biosVfConsoleRedirection', 'biosVfCoreMultiProcessing', 'biosVfCpuPaLimit', 'biosVfCpuPerfEnhancement', 'biosVfCrfastgoConfig', 'biosVfDCPMMFirmwareDowngrade', 'biosVfDCUPrefetch', 'biosVfDRAMClockThrottling', 'biosVfDemandScrub', 'biosVfDfxOsbEn', 'biosVfDirectCacheAccess', 'biosVfDmaCtrlOptIn', 'biosVfDramRefreshRate', 'biosVfDramSwThermalThrottling', 'biosVfEPPEnable', 'biosVfEPPProfile', 'biosVfEadrSupport', 'biosVfEdpcEn', 'biosVfEnableClockSpreadSpec', 'biosVfEnableMktme', 'biosVfEnableRMT', 'biosVfEnableTdx', 'biosVfEnableTdxSeamldr', 'biosVfEnableTme', 'biosVfEnergyEfficientTurbo', 'biosVfEngPerfTuning', 'biosVfEnhancedIntelSpeedStepTech', 'biosVfEpochUpdate', 'biosVfErrorCheckScrub', 'biosVfExecuteDisableBit', 'biosVfExtendedAPIC', 'biosVfFRB2Enable', 'biosVfHWPMEnable', 'biosVfHardwarePrefetch', 'biosVfIMCInterleave', 'biosVfIOATConfigCpm', 'biosVfIOHResource', 'biosVfIPV4HTTP', 'biosVfIPV4PXE', 'biosVfIPV6HTTP', 'biosVfIPV6PXE', 'biosVfIntelDynamicSpeedSelect', 'biosVfIntelHyperThreadingTech', 'biosVfIntelSpeedSelect', 'biosVfIntelTurboBoostTech', 'biosVfIntelVTForDirectedIO', 'biosVfIntelVirtualizationTechnology', 'biosVfIohErrorEn', 'biosVfKTIPrefetch', 'biosVfLLCAlloc', 'biosVfLLCPrefetch', 'biosVfLOMPortOptionROM', 'biosVfLatencyOptimizedMode', 'biosVfLegacyUSBSupport', 'biosVfLvDIMMSupport', 'biosVfMMCFGBase', 'biosVfMemoryBandwidthBoost', 'biosVfMemoryInterleave', 'biosVfMemoryMappedIOAbove4GB', 'biosVfMemoryRefreshRate', 'biosVfMemorySizeLimit', 'biosVfMemoryThermalThrottling', 'biosVfMirroringMode', 'biosVfMmiohBase', 'biosVfMmiohSize', 'biosVfNUMAOptimized', 'biosVfNetworkStack', 'biosVfNvmdimmPerformConfig', 'biosVfOSBootWatchdogTimer', 'biosVfOSBootWatchdogTimerPolicy', 'biosVfOSBootWatchdogTimerTimeout', 'biosVfOnboardNIC', 'biosVfOnboardStorage', 'biosVfOnboardStorageSWStack', 'biosVfOperationMode', 'biosVfOptimizedPowerMode', 'biosVfOutOfBandMgmtPort', 'biosVfPCIOptionROMs', 'biosVfPCISlotOptionROMEnable', 'biosVfPCIeRASSupport', 'biosVfPCIeSSDHotPlugSupport', 'biosVfPOSTErrorPause', 'biosVfPSata', 'biosVfPStateCoordType', 'biosVfPackageCStateLimit', 'biosVfPanicHighWatermark', 'biosVfPartialCacheLineSparing', 'biosVfPartialMirrorModeConfig', 'biosVfPartialMirrorPercent', 'biosVfPartialMirrorValue1', 'biosVfPartialMirrorValue2', 'biosVfPartialMirrorValue3', 'biosVfPartialMirrorValue4', 'biosVfPatrolScrub', 'biosVfPatrolScrubDuration', 'biosVfPchPciePllSsc', 'biosVfPchUsb30Mode', 'biosVfPciRomClp', 'biosVfPcieARISupport', 'biosVfPciePllSsc', 'biosVfPcieSlotsCdnEnable', 'biosVfPostPackageRepair', 'biosVfPowerOnPasswordSupport', 'biosVfPreBootDMAProtection', 'biosVfPrmrrSize', 'biosVfProcessorC1E', 'biosVfProcessorC3Report', 'biosVfProcessorC6Report', 'biosVfProcessorCState', 'biosVfPwrPerfTuning', 'biosVfQPIConfig', 'biosVfQpiLinkSpeed', 'biosVfQpiSnoopMode', 'biosVfResizeBarSupport', 'biosVfRuntimePostPackageRepair', 'biosVfSEV', 'biosVfSHA1PCRBank', 'biosVfSHA256PCRBank', 'biosVfSHA384PCRBank', 'biosVfSMEE', 'biosVfSataModeSelect', 'biosVfSelectMemoryRASConfiguration', 'biosVfSelectPprType', 'biosVfSerialMux', 'biosVfSerialPortAEnable', 'biosVfSgx', 'biosVfSgxEpoch', 'biosVfSgxLePubKeyHash', 'biosVfSinglePCTLEnable', 'biosVfSmtMode', 'biosVfSnoopyModeFor2LM', 'biosVfSnoopyModeForAD', 'biosVfSparingMode', 'biosVfSrIov', 'biosVfSubNumaClustering', 'biosVfSvmMode', 'biosVfTPMControl', 'biosVfTSME', 'biosVfTXTSupport', 'biosVfTpmPpiRequired', 'biosVfTpmSupport', 'biosVfUCSMBootOrderRuleControl', 'biosVfUFSDisable', 'biosVfUPILinkEnablement', 'biosVfUPIPowerManagement', 'biosVfUSBBootConfig', 'biosVfUSBEmulation', 'biosVfUSBPortsConfig', 'biosVfUefiMemMapSpFlagEn', 'biosVfUmaBasedClustering', 'biosVfUsbXhciSupport', 'biosVfVMDEnable', 'biosVfVgaPriority', 'biosVfVirtualNuma', 'biosVfVolMemoryMode', 'biosVfWorkLoadConfig', 'biosVfX2ApicOptOut', 'biosVfXPTPrefetch', 'biosVfXPTRemotePrefetch'], ["Get"]),
        "modular": MoMeta("BiosPlatformDefaults", "biosPlatformDefaults", "bios-defaults", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosUnit'], ['biosVfASPMSupport', 'biosVfAdjacentCacheLinePrefetch', 'biosVfAdvancedMemTest', 'biosVfAltitude', 'biosVfAssertNMIOnPERR', 'biosVfAssertNMIOnSERR', 'biosVfAutoCCState', 'biosVfAutonumousCstateEnable', 'biosVfBmeDmaMitigation', 'biosVfBootOptionRetry', 'biosVfBootPerformanceMode', 'biosVfCDNEnable', 'biosVfCDNSupport', 'biosVfCPUEnergyPerformance', 'biosVfCPUFrequencyFloor', 'biosVfCPUPerformance', 'biosVfCPUPowerManagement', 'biosVfCRQos', 'biosVfCiscoAdaptiveMemTraining', 'biosVfCiscoDebugLevel', 'biosVfCiscoOpromLaunchOptimization', 'biosVfCkeLowPolicy', 'biosVfCmciEnable', 'biosVfConfigTDPLevel', 'biosVfConsoleRedirection', 'biosVfCoreMultiProcessing', 'biosVfCrfastgoConfig', 'biosVfDCPMMFirmwareDowngrade', 'biosVfDCUPrefetch', 'biosVfDRAMClockThrottling', 'biosVfDemandScrub', 'biosVfDirectCacheAccess', 'biosVfDramRefreshRate', 'biosVfEPPEnable', 'biosVfEPPProfile', 'biosVfEnableClockSpreadSpec', 'biosVfEnergyEfficientTurbo', 'biosVfEnhancedIntelSpeedStepTech', 'biosVfExecuteDisableBit', 'biosVfExtendedAPIC', 'biosVfFRB2Enable', 'biosVfHWPMEnable', 'biosVfHardwarePrefetch', 'biosVfIMCInterleave', 'biosVfIOHResource', 'biosVfIPV4HTTP', 'biosVfIPV4PXE', 'biosVfIPV6HTTP', 'biosVfIPV6PXE', 'biosVfIntelHyperThreadingTech', 'biosVfIntelSpeedSelect', 'biosVfIntelTurboBoostTech', 'biosVfIntelVTForDirectedIO', 'biosVfIntelVirtualizationTechnology', 'biosVfKTIPrefetch', 'biosVfLLCPrefetch', 'biosVfLOMPortOptionROM', 'biosVfLegacyUSBSupport', 'biosVfLvDIMMSupport', 'biosVfMMCFGBase', 'biosVfMemoryInterleave', 'biosVfMemoryMappedIOAbove4GB', 'biosVfMemoryRefreshRate', 'biosVfMemorySizeLimit', 'biosVfMemoryThermalThrottling', 'biosVfMirroringMode', 'biosVfNUMAOptimized', 'biosVfNetworkStack', 'biosVfNvmdimmPerformConfig', 'biosVfOSBootWatchdogTimer', 'biosVfOSBootWatchdogTimerPolicy', 'biosVfOSBootWatchdogTimerTimeout', 'biosVfOnboardNIC', 'biosVfOnboardStorage', 'biosVfOnboardStorageSWStack', 'biosVfOutOfBandMgmtPort', 'biosVfPCIOptionROMs', 'biosVfPCISlotOptionROMEnable', 'biosVfPCIeRASSupport', 'biosVfPOSTErrorPause', 'biosVfPSata', 'biosVfPStateCoordType', 'biosVfPackageCStateLimit', 'biosVfPanicHighWatermark', 'biosVfPartialMirrorModeConfig', 'biosVfPartialMirrorPercent', 'biosVfPartialMirrorValue1', 'biosVfPartialMirrorValue2', 'biosVfPartialMirrorValue3', 'biosVfPartialMirrorValue4', 'biosVfPatrolScrub', 'biosVfPatrolScrubDuration', 'biosVfPchUsb30Mode', 'biosVfPciRomClp', 'biosVfPciePllSsc', 'biosVfPowerOnPasswordSupport', 'biosVfProcessorC1E', 'biosVfProcessorC3Report', 'biosVfProcessorC6Report', 'biosVfProcessorCState', 'biosVfPwrPerfTuning', 'biosVfQPIConfig', 'biosVfQpiLinkSpeed', 'biosVfQpiSnoopMode', 'biosVfSataModeSelect', 'biosVfSelectMemoryRASConfiguration', 'biosVfSelectPprType', 'biosVfSerialPortAEnable', 'biosVfSnoopyModeFor2LM', 'biosVfSnoopyModeForAD', 'biosVfSparingMode', 'biosVfSrIov', 'biosVfSubNumaClustering', 'biosVfTPMControl', 'biosVfTPMSupport', 'biosVfTXTSupport', 'biosVfUCSMBootOrderRuleControl', 'biosVfUFSDisable', 'biosVfUSBBootConfig', 'biosVfUSBEmulation', 'biosVfUSBPortsConfig', 'biosVfUsbXhciSupport', 'biosVfVgaPriority', 'biosVfWorkLoadConfig', 'biosVfXPTPrefetch'], ["Get"])
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

