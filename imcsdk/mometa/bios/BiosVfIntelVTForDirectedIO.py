"""This module contains the general information for BiosVfIntelVTForDirectedIO ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfIntelVTForDirectedIOConsts:
    VP_INTEL_VTDATSSUPPORT_DISABLED = "Disabled"
    VP_INTEL_VTDATSSUPPORT_ENABLED = "Enabled"
    _VP_INTEL_VTDATSSUPPORT_DISABLED = "disabled"
    _VP_INTEL_VTDATSSUPPORT_ENABLED = "enabled"
    VP_INTEL_VTDATSSUPPORT_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_VTDCOHERENCY_SUPPORT_DISABLED = "Disabled"
    VP_INTEL_VTDCOHERENCY_SUPPORT_ENABLED = "Enabled"
    _VP_INTEL_VTDCOHERENCY_SUPPORT_DISABLED = "disabled"
    _VP_INTEL_VTDCOHERENCY_SUPPORT_ENABLED = "enabled"
    VP_INTEL_VTDCOHERENCY_SUPPORT_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_VTDINTERRUPT_REMAPPING_DISABLED = "Disabled"
    VP_INTEL_VTDINTERRUPT_REMAPPING_ENABLED = "Enabled"
    _VP_INTEL_VTDINTERRUPT_REMAPPING_DISABLED = "disabled"
    _VP_INTEL_VTDINTERRUPT_REMAPPING_ENABLED = "enabled"
    VP_INTEL_VTDINTERRUPT_REMAPPING_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_DISABLED = "Disabled"
    VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_ENABLED = "Enabled"
    _VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_DISABLED = "disabled"
    _VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_ENABLED = "enabled"
    VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_VTFOR_DIRECTED_IO_DISABLED = "Disabled"
    VP_INTEL_VTFOR_DIRECTED_IO_ENABLED = "Enabled"
    _VP_INTEL_VTFOR_DIRECTED_IO_DISABLED = "disabled"
    _VP_INTEL_VTFOR_DIRECTED_IO_ENABLED = "enabled"
    VP_INTEL_VTFOR_DIRECTED_IO_PLATFORM_DEFAULT = "platform-default"


class BiosVfIntelVTForDirectedIO(ManagedObject):
    """This is BiosVfIntelVTForDirectedIO class."""

    consts = BiosVfIntelVTForDirectedIOConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfIntelVTForDirectedIO", "biosVfIntelVTForDirectedIO", "Intel-VT-for-directed-IO", VersionMeta.Version151f, "InputOutput", 0x1ff, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfIntelVTForDirectedIO", "biosVfIntelVTForDirectedIO", "Intel-VT-for-directed-IO", VersionMeta.Version2013e, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_intel_vtdats_support": MoPropertyMeta("vp_intel_vtdats_support", "vpIntelVTDATSSupport", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_intel_vtd_coherency_support": MoPropertyMeta("vp_intel_vtd_coherency_support", "vpIntelVTDCoherencySupport", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_intel_vtd_interrupt_remapping": MoPropertyMeta("vp_intel_vtd_interrupt_remapping", "vpIntelVTDInterruptRemapping", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_intel_vtd_pass_through_dma_support": MoPropertyMeta("vp_intel_vtd_pass_through_dma_support", "vpIntelVTDPassThroughDMASupport", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_intel_vt_for_directed_io": MoPropertyMeta("vp_intel_vt_for_directed_io", "vpIntelVTForDirectedIO", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_intel_vtdats_support": MoPropertyMeta("vp_intel_vtdats_support", "vpIntelVTDATSSupport", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_intel_vtd_coherency_support": MoPropertyMeta("vp_intel_vtd_coherency_support", "vpIntelVTDCoherencySupport", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_intel_vtd_interrupt_remapping": MoPropertyMeta("vp_intel_vtd_interrupt_remapping", "vpIntelVTDInterruptRemapping", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_intel_vtd_pass_through_dma_support": MoPropertyMeta("vp_intel_vtd_pass_through_dma_support", "vpIntelVTDPassThroughDMASupport", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_intel_vt_for_directed_io": MoPropertyMeta("vp_intel_vt_for_directed_io", "vpIntelVTForDirectedIO", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIntelVTDATSSupport": "vp_intel_vtdats_support", 
            "vpIntelVTDCoherencySupport": "vp_intel_vtd_coherency_support", 
            "vpIntelVTDInterruptRemapping": "vp_intel_vtd_interrupt_remapping", 
            "vpIntelVTDPassThroughDMASupport": "vp_intel_vtd_pass_through_dma_support", 
            "vpIntelVTForDirectedIO": "vp_intel_vt_for_directed_io", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIntelVTDATSSupport": "vp_intel_vtdats_support", 
            "vpIntelVTDCoherencySupport": "vp_intel_vtd_coherency_support", 
            "vpIntelVTDInterruptRemapping": "vp_intel_vtd_interrupt_remapping", 
            "vpIntelVTDPassThroughDMASupport": "vp_intel_vtd_pass_through_dma_support", 
            "vpIntelVTForDirectedIO": "vp_intel_vt_for_directed_io", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_intel_vtdats_support = None
        self.vp_intel_vtd_coherency_support = None
        self.vp_intel_vtd_interrupt_remapping = None
        self.vp_intel_vtd_pass_through_dma_support = None
        self.vp_intel_vt_for_directed_io = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfIntelVTForDirectedIO", parent_mo_or_dn, **kwargs)

