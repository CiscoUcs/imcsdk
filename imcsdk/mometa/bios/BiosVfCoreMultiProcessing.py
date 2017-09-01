"""This module contains the general information for BiosVfCoreMultiProcessing ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCoreMultiProcessingConsts:
    VP_CORE_MULTI_PROCESSING_1 = "1"
    VP_CORE_MULTI_PROCESSING_10 = "10"
    VP_CORE_MULTI_PROCESSING_11 = "11"
    VP_CORE_MULTI_PROCESSING_12 = "12"
    VP_CORE_MULTI_PROCESSING_13 = "13"
    VP_CORE_MULTI_PROCESSING_14 = "14"
    VP_CORE_MULTI_PROCESSING_15 = "15"
    VP_CORE_MULTI_PROCESSING_16 = "16"
    VP_CORE_MULTI_PROCESSING_17 = "17"
    VP_CORE_MULTI_PROCESSING_18 = "18"
    VP_CORE_MULTI_PROCESSING_19 = "19"
    VP_CORE_MULTI_PROCESSING_2 = "2"
    VP_CORE_MULTI_PROCESSING_20 = "20"
    VP_CORE_MULTI_PROCESSING_21 = "21"
    VP_CORE_MULTI_PROCESSING_22 = "22"
    VP_CORE_MULTI_PROCESSING_23 = "23"
    VP_CORE_MULTI_PROCESSING_24 = "24"
    VP_CORE_MULTI_PROCESSING_25 = "25"
    VP_CORE_MULTI_PROCESSING_26 = "26"
    VP_CORE_MULTI_PROCESSING_27 = "27"
    VP_CORE_MULTI_PROCESSING_28 = "28"
    VP_CORE_MULTI_PROCESSING_3 = "3"
    VP_CORE_MULTI_PROCESSING_4 = "4"
    VP_CORE_MULTI_PROCESSING_5 = "5"
    VP_CORE_MULTI_PROCESSING_6 = "6"
    VP_CORE_MULTI_PROCESSING_7 = "7"
    VP_CORE_MULTI_PROCESSING_8 = "8"
    VP_CORE_MULTI_PROCESSING_9 = "9"
    VP_CORE_MULTI_PROCESSING_ALL = "all"
    VP_CORE_MULTI_PROCESSING_PLATFORM_DEFAULT = "platform-default"


class BiosVfCoreMultiProcessing(ManagedObject):
    """This is BiosVfCoreMultiProcessing class."""

    consts = BiosVfCoreMultiProcessingConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCoreMultiProcessing", "biosVfCoreMultiProcessing", "Core-MultiProcessing", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfCoreMultiProcessing", "biosVfCoreMultiProcessing", "Core-MultiProcessing", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_core_multi_processing": MoPropertyMeta("vp_core_multi_processing", "vpCoreMultiProcessing", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "2", "20", "21", "22", "23", "24", "25", "26", "27", "28", "3", "4", "5", "6", "7", "8", "9", "all", "platform-default"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_core_multi_processing": MoPropertyMeta("vp_core_multi_processing", "vpCoreMultiProcessing", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1", "10", "11", "12", "13", "14", "15", "16", "17", "18", "2", "3", "4", "5", "6", "7", "8", "9", "all", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCoreMultiProcessing": "vp_core_multi_processing", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCoreMultiProcessing": "vp_core_multi_processing", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_core_multi_processing = None

        ManagedObject.__init__(self, "BiosVfCoreMultiProcessing", parent_mo_or_dn, **kwargs)

