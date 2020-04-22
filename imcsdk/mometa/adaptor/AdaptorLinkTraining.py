"""This module contains the general information for AdaptorLinkTraining ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorLinkTrainingConsts:
    LINK_TRAINING_OFF = "OFF"
    LINK_TRAINING_ON = "ON"
    LINK_TRAINING_N_A = "n/a"
    _LINK_TRAINING_OFF = "off"
    _LINK_TRAINING_ON = "on"


class AdaptorLinkTraining(ManagedObject):
    """This is AdaptorLinkTraining class."""

    consts = AdaptorLinkTrainingConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorLinkTraining", "adaptorLinkTraining", "link-training", VersionMeta.Version204c, "InputOutput", 0x3f, [], ["admin", "user"], ['adaptorExtEthIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorLinkTraining", "adaptorLinkTraining", "link-training", VersionMeta.Version303a, "InputOutput", 0x3f, [], ["admin", "user"], ['adaptorExtEthIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version204c, MoPropertyMeta.INTERNAL, 0x2, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "link_training": MoPropertyMeta("link_training", "linkTraining", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["OFF", "ON", "n/a", "off", "on"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, 0x2, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "link_training": MoPropertyMeta("link_training", "linkTraining", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["OFF", "ON", "n/a", "off", "on"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "linkTraining": "link_training", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "linkTraining": "link_training", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.link_training = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorLinkTraining", parent_mo_or_dn, **kwargs)

