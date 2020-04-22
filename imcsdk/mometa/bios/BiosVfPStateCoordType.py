"""This module contains the general information for BiosVfPStateCoordType ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPStateCoordTypeConsts:
    VP_PSTATE_COORD_TYPE_HW_ALL = "HW ALL"
    VP_PSTATE_COORD_TYPE_SW_ALL = "SW ALL"
    VP_PSTATE_COORD_TYPE_SW_ANY = "SW ANY"
    VP_PSTATE_COORD_TYPE_PLATFORM_DEFAULT = "platform-default"


class BiosVfPStateCoordType(ManagedObject):
    """This is BiosVfPStateCoordType class."""

    consts = BiosVfPStateCoordTypeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPStateCoordType", "biosVfPStateCoordType", "p-state-coord", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfPStateCoordType", "biosVfPStateCoordType", "p-state-coord", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_p_state_coord_type": MoPropertyMeta("vp_p_state_coord_type", "vpPStateCoordType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["HW ALL", "SW ALL", "SW ANY", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_p_state_coord_type": MoPropertyMeta("vp_p_state_coord_type", "vpPStateCoordType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["HW ALL", "SW ALL", "SW ANY", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPStateCoordType": "vp_p_state_coord_type", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPStateCoordType": "vp_p_state_coord_type", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_p_state_coord_type = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfPStateCoordType", parent_mo_or_dn, **kwargs)

