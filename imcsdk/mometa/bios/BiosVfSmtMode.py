"""This module contains the general information for BiosVfSmtMode ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSmtModeConsts:
    VP_SMT_MODE_AUTO = "Auto"
    VP_SMT_MODE_OFF = "Off"
    VP_SMT_MODE_PLATFORM_DEFAULT = "platform-default"


class BiosVfSmtMode(ManagedObject):
    """This is BiosVfSmtMode class."""

    consts = BiosVfSmtModeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSmtMode", "biosVfSmtMode", "smt-mode", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_smt_mode": MoPropertyMeta("vp_smt_mode", "vpSmtMode", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Off", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSmtMode": "vp_smt_mode", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_smt_mode = None

        ManagedObject.__init__(self, "BiosVfSmtMode", parent_mo_or_dn, **kwargs)

