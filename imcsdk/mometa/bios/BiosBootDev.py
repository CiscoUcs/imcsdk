"""This module contains the general information for BiosBootDev ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosBootDevConsts:
    ORDER_1 = "1"
    ORDER_10 = "10"
    ORDER_11 = "11"
    ORDER_12 = "12"
    ORDER_13 = "13"
    ORDER_14 = "14"
    ORDER_15 = "15"
    ORDER_2 = "2"
    ORDER_3 = "3"
    ORDER_4 = "4"
    ORDER_5 = "5"
    ORDER_6 = "6"
    ORDER_7 = "7"
    ORDER_8 = "8"
    ORDER_9 = "9"


class BiosBootDev(ManagedObject):
    """This is BiosBootDev class."""

    consts = BiosBootDevConsts()
    naming_props = set(['order'])

    mo_meta = {
        "classic": MoMeta("BiosBootDev", "biosBootDev", "bdv-[order]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosBootDevGrp'], [], ["Get"]),
        "modular": MoMeta("BiosBootDev", "biosBootDev", "bdv-[order]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosBootDevGrp'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, None, ["1", "10", "11", "12", "13", "14", "15", "2", "3", "4", "5", "6", "7", "8", "9"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, ["1", "10", "11", "12", "13", "14", "15", "2", "3", "4", "5", "6", "7", "8", "9"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "descr": "descr", 
            "dn": "dn", 
            "order": "order", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "descr": "descr", 
            "dn": "dn", 
            "order": "order", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, order, **kwargs):
        self._dirty_mask = 0
        self.order = order
        self.child_action = None
        self.descr = None
        self.status = None

        ManagedObject.__init__(self, "BiosBootDev", parent_mo_or_dn, **kwargs)

