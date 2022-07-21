"""This module contains the general information for AdaptorLinkTraining ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorLinkTrainingConsts:
    ADMIN_LINK_TRAINING_AUTO = "AUTO"
    _ADMIN_LINK_TRAINING_AUTO = "Auto"
    ADMIN_LINK_TRAINING_N_A = "N/A"
    ADMIN_LINK_TRAINING_NA = "NA"
    ADMIN_LINK_TRAINING_OFF = "OFF"
    ADMIN_LINK_TRAINING_ON = "ON"
    _ADMIN_LINK_TRAINING_OFF = "Off"
    _ADMIN_LINK_TRAINING_ON = "On"
    _ADMIN_LINK_TRAINING_AUTO = "auto"
    _ADMIN_LINK_TRAINING_N_A = "n/a"
    _ADMIN_LINK_TRAINING_NA = "na"
    _ADMIN_LINK_TRAINING_OFF = "off"
    _ADMIN_LINK_TRAINING_ON = "on"
    LINK_TRAINING_OFF = "OFF"
    LINK_TRAINING_ON = "ON"
    LINK_TRAINING_N_A = "n/a"
    _LINK_TRAINING_OFF = "off"
    _LINK_TRAINING_ON = "on"
    OPER_LINK_TRAINING_AUTO = "AUTO"
    _OPER_LINK_TRAINING_AUTO = "Auto"
    OPER_LINK_TRAINING_N_A = "N/A"
    OPER_LINK_TRAINING_NA = "NA"
    OPER_LINK_TRAINING_OFF = "OFF"
    OPER_LINK_TRAINING_ON = "ON"
    _OPER_LINK_TRAINING_OFF = "Off"
    _OPER_LINK_TRAINING_ON = "On"
    _OPER_LINK_TRAINING_AUTO = "auto"
    _OPER_LINK_TRAINING_N_A = "n/a"
    _OPER_LINK_TRAINING_NA = "na"
    _OPER_LINK_TRAINING_OFF = "off"
    _OPER_LINK_TRAINING_ON = "on"


class AdaptorLinkTraining(ManagedObject):
    """This is AdaptorLinkTraining class."""

    consts = AdaptorLinkTrainingConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorLinkTraining", "adaptorLinkTraining", "link-training", VersionMeta.Version204c, "InputOutput", 0x7f, [], ["admin", "user"], ['adaptorExtEthIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorLinkTraining", "adaptorLinkTraining", "link-training", VersionMeta.Version303a, "InputOutput", 0x3f, [], ["admin", "user"], ['adaptorExtEthIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version204c, MoPropertyMeta.INTERNAL, 0x2, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "link_training": MoPropertyMeta("link_training", "linkTraining", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["OFF", "ON", "n/a", "off", "on"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "admin_link_training": MoPropertyMeta("admin_link_training", "adminLinkTraining", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["AUTO", "Auto", "N/A", "NA", "OFF", "ON", "Off", "On", "auto", "n/a", "na", "off", "on"], []),
            "oper_link_training": MoPropertyMeta("oper_link_training", "operLinkTraining", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["AUTO", "Auto", "N/A", "NA", "OFF", "ON", "Off", "On", "auto", "n/a", "na", "off", "on"], []),
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
            "adminLinkTraining": "admin_link_training", 
            "operLinkTraining": "oper_link_training", 
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
        self.admin_link_training = None
        self.oper_link_training = None

        ManagedObject.__init__(self, "AdaptorLinkTraining", parent_mo_or_dn, **kwargs)

