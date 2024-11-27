"""This module contains the general information for SlotConfig ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class SlotConfigConsts:
    DESIRED_MODE_CONTROLLER = "controller"
    DESIRED_MODE_DIRECT = "direct"
    DESIRED_MODE_RAID = "raid"


class SlotConfig(ManagedObject):
    """This is SlotConfig class."""

    consts = SlotConfigConsts()
    naming_props = set(['slot'])

    mo_meta = {
        "classic": MoMeta("SlotConfig", "slotConfig", "slot-config-[slot]", VersionMeta.Version432_230190, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['nvmeHybridSlotConfig'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version432_230190, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_mode": MoPropertyMeta("current_mode", "currentMode", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "desired_mode": MoPropertyMeta("desired_mode", "desiredMode", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["controller", "direct", "raid"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_WRITE, 0x10, 1, 512, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version432_230190, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "currentMode": "current_mode", 
            "desiredMode": "desired_mode", 
            "dn": "dn", 
            "rn": "rn", 
            "slot": "slot", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, slot, **kwargs):
        self._dirty_mask = 0
        self.slot = slot
        self.child_action = None
        self.current_mode = None
        self.desired_mode = None
        self.status = None

        ManagedObject.__init__(self, "SlotConfig", parent_mo_or_dn, **kwargs)

