"""This module contains the general information for BiosVfMemoryInterleave ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfMemoryInterleaveConsts:
    VP_CHANNEL_INTER_LEAVE_1_WAY = "1-way"
    VP_CHANNEL_INTER_LEAVE_2_WAY = "2-way"
    VP_CHANNEL_INTER_LEAVE_3_WAY = "3-way"
    VP_CHANNEL_INTER_LEAVE_4_WAY = "4-way"
    VP_CHANNEL_INTER_LEAVE_AUTO = "auto"
    VP_CHANNEL_INTER_LEAVE_PLATFORM_DEFAULT = "platform-default"
    VP_MEMORY_INTER_LEAVE_1_WAY_NODE_INTERLEAVE = "1 Way Node Interleave"
    VP_MEMORY_INTER_LEAVE_2_WAY_NODE_INTERLEAVE = "2 Way Node Interleave"
    VP_MEMORY_INTER_LEAVE_4_WAY_NODE_INTERLEAVE = "4 Way Node Interleave"
    VP_MEMORY_INTER_LEAVE_8_WAY_NODE_INTERLEAVE = "8 Way Node Interleave"
    VP_MEMORY_INTER_LEAVE_DISABLED = "Disabled"
    VP_MEMORY_INTER_LEAVE_ENABLED = "Enabled"
    _VP_MEMORY_INTER_LEAVE_DISABLED = "disabled"
    _VP_MEMORY_INTER_LEAVE_ENABLED = "enabled"
    VP_MEMORY_INTER_LEAVE_PLATFORM_DEFAULT = "platform-default"
    VP_RANK_INTER_LEAVE_1_WAY = "1-way"
    VP_RANK_INTER_LEAVE_2_WAY = "2-way"
    VP_RANK_INTER_LEAVE_4_WAY = "4-way"
    VP_RANK_INTER_LEAVE_8_WAY = "8-way"
    VP_RANK_INTER_LEAVE_AUTO = "auto"
    VP_RANK_INTER_LEAVE_PLATFORM_DEFAULT = "platform-default"


class BiosVfMemoryInterleave(ManagedObject):
    """This is BiosVfMemoryInterleave class."""

    consts = BiosVfMemoryInterleaveConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfMemoryInterleave", "biosVfMemoryInterleave", "Memory-Interleave", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfMemoryInterleave", "biosVfMemoryInterleave", "Memory-Interleave", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_channel_inter_leave": MoPropertyMeta("vp_channel_inter_leave", "vpChannelInterLeave", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1-way", "2-way", "3-way", "4-way", "auto", "platform-default"], []),
            "vp_memory_inter_leave": MoPropertyMeta("vp_memory_inter_leave", "vpMemoryInterLeave", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["1 Way Node Interleave", "2 Way Node Interleave", "4 Way Node Interleave", "8 Way Node Interleave", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_rank_inter_leave": MoPropertyMeta("vp_rank_inter_leave", "vpRankInterLeave", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["1-way", "2-way", "4-way", "8-way", "auto", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_channel_inter_leave": MoPropertyMeta("vp_channel_inter_leave", "vpChannelInterLeave", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1-way", "2-way", "3-way", "4-way", "auto", "platform-default"], []),
            "vp_memory_inter_leave": MoPropertyMeta("vp_memory_inter_leave", "vpMemoryInterLeave", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["1 Way Node Interleave", "2 Way Node Interleave", "4 Way Node Interleave", "8 Way Node Interleave", "Disabled", "Enabled", "platform-default"], []),
            "vp_rank_inter_leave": MoPropertyMeta("vp_rank_inter_leave", "vpRankInterLeave", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["1-way", "2-way", "4-way", "8-way", "auto", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpChannelInterLeave": "vp_channel_inter_leave", 
            "vpMemoryInterLeave": "vp_memory_inter_leave", 
            "vpRankInterLeave": "vp_rank_inter_leave", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpChannelInterLeave": "vp_channel_inter_leave", 
            "vpMemoryInterLeave": "vp_memory_inter_leave", 
            "vpRankInterLeave": "vp_rank_inter_leave", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_channel_inter_leave = None
        self.vp_memory_inter_leave = None
        self.vp_rank_inter_leave = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfMemoryInterleave", parent_mo_or_dn, **kwargs)

