"""This module contains the general information for BiosVfPowerOnPasswordSupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPowerOnPasswordSupportConsts:
    VP_POPSUPPORT_DISABLED = "Disabled"
    VP_POPSUPPORT_ENABLED = "Enabled"
    _VP_POPSUPPORT_DISABLED = "disabled"
    _VP_POPSUPPORT_ENABLED = "enabled"
    VP_POPSUPPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfPowerOnPasswordSupport(ManagedObject):
    """This is BiosVfPowerOnPasswordSupport class."""

    consts = BiosVfPowerOnPasswordSupportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPowerOnPasswordSupport", "biosVfPowerOnPasswordSupport", "POP-Support", VersionMeta.Version301c, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfPowerOnPasswordSupport", "biosVfPowerOnPasswordSupport", "POP-Support", VersionMeta.Version301c, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_pop_support": MoPropertyMeta("vp_pop_support", "vpPOPSupport", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_pop_support": MoPropertyMeta("vp_pop_support", "vpPOPSupport", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPOPSupport": "vp_pop_support", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPOPSupport": "vp_pop_support", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_pop_support = None

        ManagedObject.__init__(self, "BiosVfPowerOnPasswordSupport", parent_mo_or_dn, **kwargs)

