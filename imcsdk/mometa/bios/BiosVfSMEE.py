"""This module contains the general information for BiosVfSMEE ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSMEEConsts:
    VP_SMEE_DISABLED = "Disabled"
    VP_SMEE_ENABLED = "Enabled"
    _VP_SMEE_DISABLED = "disabled"
    _VP_SMEE_ENABLED = "enabled"
    VP_SMEE_PLATFORM_DEFAULT = "platform-default"


class BiosVfSMEE(ManagedObject):
    """This is BiosVfSMEE class."""

    consts = BiosVfSMEEConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSMEE", "biosVfSMEE", "smee", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_smee": MoPropertyMeta("vp_smee", "vpSMEE", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSMEE": "vp_smee", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_smee = None

        ManagedObject.__init__(self, "BiosVfSMEE", parent_mo_or_dn, **kwargs)

