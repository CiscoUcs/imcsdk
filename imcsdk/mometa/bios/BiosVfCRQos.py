"""This module contains the general information for BiosVfCRQos ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCRQosConsts:
    VP_CRQOS_DISABLED = "Disabled"
    VP_CRQOS_MODE_0_DISABLE_THE_PMEM_QO_S_FEATURE = "Mode 0 - Disable the PMem QoS Feature"
    VP_CRQOS_MODE_1_M2_M_QO_S_ENABLE_AND_CHA_QO_S_DISABLE = "Mode 1 - M2M QoS Enable and CHA QoS Disable"
    VP_CRQOS_MODE_2_M2_M_QO_S_ENABLE_AND_CHA_QO_S_ENABLE = "Mode 2 - M2M QoS Enable and CHA QoS Enable"
    VP_CRQOS_RECIPE_1 = "Recipe 1"
    VP_CRQOS_RECIPE_2 = "Recipe 2"
    VP_CRQOS_RECIPE_3 = "Recipe 3"
    VP_CRQOS_PLATFORM_DEFAULT = "platform-default"


class BiosVfCRQos(ManagedObject):
    """This is BiosVfCRQos class."""

    consts = BiosVfCRQosConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCRQos", "biosVfCRQos", "CR-Qos", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfCRQos", "biosVfCRQos", "CR-Qos", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cr_qos": MoPropertyMeta("vp_cr_qos", "vpCRQos", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Mode 0 - Disable the PMem QoS Feature", "Mode 1 - M2M QoS Enable and CHA QoS Disable", "Mode 2 - M2M QoS Enable and CHA QoS Enable", "Recipe 1", "Recipe 2", "Recipe 3", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cr_qos": MoPropertyMeta("vp_cr_qos", "vpCRQos", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Recipe 1", "Recipe 2", "Recipe 3", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCRQos": "vp_cr_qos", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCRQos": "vp_cr_qos", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_cr_qos = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfCRQos", parent_mo_or_dn, **kwargs)

