"""This module contains the general information for BiosVfCiscoAdaptiveMemTraining ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCiscoAdaptiveMemTrainingConsts:
    VP_CISCO_ADAPTIVE_MEM_TRAINING_DISABLED = "Disabled"
    VP_CISCO_ADAPTIVE_MEM_TRAINING_ENABLED = "Enabled"
    _VP_CISCO_ADAPTIVE_MEM_TRAINING_DISABLED = "disabled"
    _VP_CISCO_ADAPTIVE_MEM_TRAINING_ENABLED = "enabled"
    VP_CISCO_ADAPTIVE_MEM_TRAINING_PLATFORM_DEFAULT = "platform-default"


class BiosVfCiscoAdaptiveMemTraining(ManagedObject):
    """This is BiosVfCiscoAdaptiveMemTraining class."""

    consts = BiosVfCiscoAdaptiveMemTrainingConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCiscoAdaptiveMemTraining", "biosVfCiscoAdaptiveMemTraining", "Cisco-Adap-Mem", VersionMeta.Version402c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfCiscoAdaptiveMemTraining", "biosVfCiscoAdaptiveMemTraining", "Cisco-Adap-Mem", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cisco_adaptive_mem_training": MoPropertyMeta("vp_cisco_adaptive_mem_training", "vpCiscoAdaptiveMemTraining", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version402c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cisco_adaptive_mem_training": MoPropertyMeta("vp_cisco_adaptive_mem_training", "vpCiscoAdaptiveMemTraining", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCiscoAdaptiveMemTraining": "vp_cisco_adaptive_mem_training", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCiscoAdaptiveMemTraining": "vp_cisco_adaptive_mem_training", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_cisco_adaptive_mem_training = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfCiscoAdaptiveMemTraining", parent_mo_or_dn, **kwargs)

