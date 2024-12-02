"""This module contains the general information for NvmeHybridSlotConfig ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class NvmeHybridSlotConfigConsts:
    pass


class NvmeHybridSlotConfig(ManagedObject):
    """This is NvmeHybridSlotConfig class."""

    consts = NvmeHybridSlotConfigConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("NvmeHybridSlotConfig", "nvmeHybridSlotConfig", "nvmeHybridSlotConfig", VersionMeta.Version432_230190, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['topSystem'], ['slotConfig'], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version432_230190, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "config_status": MoPropertyMeta("config_status", "configStatus", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "last_update_status": MoPropertyMeta("last_update_status", "lastUpdateStatus", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "configStatus": "config_status", 
            "dn": "dn", 
            "lastUpdateStatus": "last_update_status", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_status = None
        self.last_update_status = None
        self.status = None

        ManagedObject.__init__(self, "NvmeHybridSlotConfig", parent_mo_or_dn, **kwargs)

