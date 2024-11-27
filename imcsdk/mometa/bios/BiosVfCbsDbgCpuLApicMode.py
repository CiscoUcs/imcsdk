"""This module contains the general information for BiosVfCbsDbgCpuLApicMode ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsDbgCpuLApicModeConsts:
    VP_CBS_DBG_CPU_LAPIC_MODE_AUTO = "Auto"
    VP_CBS_DBG_CPU_LAPIC_MODE_COMPATIBILITY = "Compatibility"
    VP_CBS_DBG_CPU_LAPIC_MODE_X2_APIC = "X2APIC"
    VP_CBS_DBG_CPU_LAPIC_MODE_XAPIC = "XAPIC"
    VP_CBS_DBG_CPU_LAPIC_MODE_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsDbgCpuLApicMode(ManagedObject):
    """This is BiosVfCbsDbgCpuLApicMode class."""

    consts = BiosVfCbsDbgCpuLApicModeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsDbgCpuLApicMode", "biosVfCbsDbgCpuLApicMode", "local-apci-mode", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_dbg_cpu_l_apic_mode": MoPropertyMeta("vp_cbs_dbg_cpu_l_apic_mode", "vpCbsDbgCpuLApicMode", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Compatibility", "X2APIC", "XAPIC", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsDbgCpuLApicMode": "vp_cbs_dbg_cpu_l_apic_mode", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_dbg_cpu_l_apic_mode = None

        ManagedObject.__init__(self, "BiosVfCbsDbgCpuLApicMode", parent_mo_or_dn, **kwargs)

