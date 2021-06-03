"""This module contains the general information for BiosVfCbsCpuSmtCtrl ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCpuSmtCtrlConsts:
    VP_CBS_CPU_SMT_CTRL_AUTO = "Auto"
    VP_CBS_CPU_SMT_CTRL_DISABLED = "Disabled"
    VP_CBS_CPU_SMT_CTRL_ENABLED = "Enabled"
    _VP_CBS_CPU_SMT_CTRL_DISABLED = "disabled"
    _VP_CBS_CPU_SMT_CTRL_ENABLED = "enabled"
    VP_CBS_CPU_SMT_CTRL_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCpuSmtCtrl(ManagedObject):
    """This is BiosVfCbsCpuSmtCtrl class."""

    consts = BiosVfCbsCpuSmtCtrlConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCpuSmtCtrl", "biosVfCbsCpuSmtCtrl", "cpu-smt-mode", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cpu_smt_ctrl": MoPropertyMeta("vp_cbs_cpu_smt_ctrl", "vpCbsCpuSmtCtrl", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCpuSmtCtrl": "vp_cbs_cpu_smt_ctrl", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cpu_smt_ctrl = None

        ManagedObject.__init__(self, "BiosVfCbsCpuSmtCtrl", parent_mo_or_dn, **kwargs)

