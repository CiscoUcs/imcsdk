"""This module contains the general information for BiosVfCbsDbgCpuGenCpuWdt ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsDbgCpuGenCpuWdtConsts:
    VP_CBS_DBG_CPU_GEN_CPU_WDT_AUTO = "Auto"
    VP_CBS_DBG_CPU_GEN_CPU_WDT_DISABLED = "Disabled"
    VP_CBS_DBG_CPU_GEN_CPU_WDT_ENABLED = "Enabled"
    _VP_CBS_DBG_CPU_GEN_CPU_WDT_DISABLED = "disabled"
    _VP_CBS_DBG_CPU_GEN_CPU_WDT_ENABLED = "enabled"
    VP_CBS_DBG_CPU_GEN_CPU_WDT_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsDbgCpuGenCpuWdt(ManagedObject):
    """This is BiosVfCbsDbgCpuGenCpuWdt class."""

    consts = BiosVfCbsDbgCpuGenCpuWdtConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsDbgCpuGenCpuWdt", "biosVfCbsDbgCpuGenCpuWdt", "core-watchdog-timer-enable", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_dbg_cpu_gen_cpu_wdt": MoPropertyMeta("vp_cbs_dbg_cpu_gen_cpu_wdt", "vpCbsDbgCpuGenCpuWdt", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsDbgCpuGenCpuWdt": "vp_cbs_dbg_cpu_gen_cpu_wdt", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_dbg_cpu_gen_cpu_wdt = None

        ManagedObject.__init__(self, "BiosVfCbsDbgCpuGenCpuWdt", parent_mo_or_dn, **kwargs)

