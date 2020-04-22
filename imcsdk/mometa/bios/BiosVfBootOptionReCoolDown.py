"""This module contains the general information for BiosVfBootOptionReCoolDown ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfBootOptionReCoolDownConsts:
    VP_BOOT_OPTION_RE_COOL_DOWN_15 = "15"
    VP_BOOT_OPTION_RE_COOL_DOWN_45 = "45"
    VP_BOOT_OPTION_RE_COOL_DOWN_90 = "90"
    VP_BOOT_OPTION_RE_COOL_DOWN_PLATFORM_DEFAULT = "platform-default"


class BiosVfBootOptionReCoolDown(ManagedObject):
    """This is BiosVfBootOptionReCoolDown class."""

    consts = BiosVfBootOptionReCoolDownConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfBootOptionReCoolDown", "biosVfBootOptionReCoolDown", "Boot-option-cool-down-retry", VersionMeta.Version304a, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version304a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_boot_option_re_cool_down": MoPropertyMeta("vp_boot_option_re_cool_down", "vpBootOptionReCoolDown", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["15", "45", "90", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpBootOptionReCoolDown": "vp_boot_option_re_cool_down", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_boot_option_re_cool_down = None

        ManagedObject.__init__(self, "BiosVfBootOptionReCoolDown", parent_mo_or_dn, **kwargs)

