"""This module contains the general information for BiosVfClosedLoopThermThrotl ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfClosedLoopThermThrotlConsts:
    VP_CLOSED_LOOP_THERM_THROTL_DISABLED = "Disabled"
    VP_CLOSED_LOOP_THERM_THROTL_ENABLED = "Enabled"
    _VP_CLOSED_LOOP_THERM_THROTL_DISABLED = "disabled"
    _VP_CLOSED_LOOP_THERM_THROTL_ENABLED = "enabled"
    VP_CLOSED_LOOP_THERM_THROTL_PLATFORM_DEFAULT = "platform-default"


class BiosVfClosedLoopThermThrotl(ManagedObject):
    """This is BiosVfClosedLoopThermThrotl class."""

    consts = BiosVfClosedLoopThermThrotlConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfClosedLoopThermThrotl", "biosVfClosedLoopThermThrotl", "Closed-Loop-Therm-Throtl", VersionMeta.Version303a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_closed_loop_therm_throtl": MoPropertyMeta("vp_closed_loop_therm_throtl", "vpClosedLoopThermThrotl", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpClosedLoopThermThrotl": "vp_closed_loop_therm_throtl", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_closed_loop_therm_throtl = None

        ManagedObject.__init__(self, "BiosVfClosedLoopThermThrotl", parent_mo_or_dn, **kwargs)

