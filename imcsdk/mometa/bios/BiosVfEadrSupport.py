"""This module contains the general information for BiosVfEadrSupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfEadrSupportConsts:
    VP_EADR_SUPPORT_AUTO = "Auto"
    VP_EADR_SUPPORT_DISABLED = "Disabled"
    VP_EADR_SUPPORT_ENABLED = "Enabled"
    _VP_EADR_SUPPORT_DISABLED = "disabled"
    _VP_EADR_SUPPORT_ENABLED = "enabled"
    VP_EADR_SUPPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfEadrSupport(ManagedObject):
    """This is BiosVfEadrSupport class."""

    consts = BiosVfEadrSupportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfEadrSupport", "biosVfEadrSupport", "eADR-Support", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_eadr_support": MoPropertyMeta("vp_eadr_support", "vpEadrSupport", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEadrSupport": "vp_eadr_support", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_eadr_support = None

        ManagedObject.__init__(self, "BiosVfEadrSupport", parent_mo_or_dn, **kwargs)

