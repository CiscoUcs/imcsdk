"""This module contains the general information for BiosVfSelectMemoryRASConfiguration ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSelectMemoryRASConfigurationConsts:
    VP_SELECT_MEMORY_RASCONFIGURATION_ADDDC_SPARING = "adddc-sparing"
    VP_SELECT_MEMORY_RASCONFIGURATION_LOCKSTEP = "lockstep"
    VP_SELECT_MEMORY_RASCONFIGURATION_MAXIMUM_PERFORMANCE = "maximum-performance"
    VP_SELECT_MEMORY_RASCONFIGURATION_MIRROR_MODE_1LM = "mirror-mode-1lm"
    VP_SELECT_MEMORY_RASCONFIGURATION_MIRRORING = "mirroring"
    VP_SELECT_MEMORY_RASCONFIGURATION_PARTIAL_MIRROR_MODE_1LM = "partial-mirror-mode-1lm"
    VP_SELECT_MEMORY_RASCONFIGURATION_PLATFORM_DEFAULT = "platform-default"
    VP_SELECT_MEMORY_RASCONFIGURATION_SPARING = "sparing"


class BiosVfSelectMemoryRASConfiguration(ManagedObject):
    """This is BiosVfSelectMemoryRASConfiguration class."""

    consts = BiosVfSelectMemoryRASConfigurationConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSelectMemoryRASConfiguration", "biosVfSelectMemoryRASConfiguration", "SelectMemory-RAS-configuration", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfSelectMemoryRASConfiguration", "biosVfSelectMemoryRASConfiguration", "SelectMemory-RAS-configuration", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_select_memory_ras_configuration": MoPropertyMeta("vp_select_memory_ras_configuration", "vpSelectMemoryRASConfiguration", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["adddc-sparing", "lockstep", "maximum-performance", "mirror-mode-1lm", "mirroring", "partial-mirror-mode-1lm", "platform-default", "sparing"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_select_memory_ras_configuration": MoPropertyMeta("vp_select_memory_ras_configuration", "vpSelectMemoryRASConfiguration", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["adddc-sparing", "lockstep", "maximum-performance", "mirror-mode-1lm", "mirroring", "partial-mirror-mode-1lm", "platform-default", "sparing"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSelectMemoryRASConfiguration": "vp_select_memory_ras_configuration", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSelectMemoryRASConfiguration": "vp_select_memory_ras_configuration", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_select_memory_ras_configuration = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfSelectMemoryRASConfiguration", parent_mo_or_dn, **kwargs)

