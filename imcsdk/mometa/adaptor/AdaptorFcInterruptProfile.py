"""This module contains the general information for AdaptorFcInterruptProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorFcInterruptProfileConsts:
    MODE_INTX = "INTx"
    MODE_MSI = "MSI"
    MODE_MSIX = "MSIx"


class AdaptorFcInterruptProfile(ManagedObject):
    """This is AdaptorFcInterruptProfile class."""

    consts = AdaptorFcInterruptProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorFcInterruptProfile", "adaptorFcInterruptProfile", "fc-int", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'adaptorHostFcIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorFcInterruptProfile", "adaptorFcInterruptProfile", "fc-int", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'adaptorHostFcIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["INTx", "MSI", "MSIx"], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["INTx", "MSI", "MSIx"], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "mode": "mode", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "mode": "mode", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.mode = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorFcInterruptProfile", parent_mo_or_dn, **kwargs)

