"""This module contains the general information for LsbootBootSecurity ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LsbootBootSecurityConsts:
    SECURE_BOOT_DISABLED = "Disabled"
    SECURE_BOOT_ENABLED = "Enabled"
    SECURE_BOOT_DISABLE = "disable"
    _SECURE_BOOT_DISABLED = "disabled"
    SECURE_BOOT_ENABLE = "enable"
    _SECURE_BOOT_ENABLED = "enabled"


class LsbootBootSecurity(ManagedObject):
    """This is LsbootBootSecurity class."""

    consts = LsbootBootSecurityConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("LsbootBootSecurity", "lsbootBootSecurity", "boot-security", VersionMeta.Version201a, "InputOutput", 0x1f, [], ["admin", "user"], ['lsbootDef'], [], ["Get", "Set"]),
        "modular": MoMeta("LsbootBootSecurity", "lsbootBootSecurity", "boot-security", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "user"], ['lsbootDef'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "secure_boot": MoPropertyMeta("secure_boot", "secureBoot", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disable", "disabled", "enable", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "secure_boot": MoPropertyMeta("secure_boot", "secureBoot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disable", "disabled", "enable", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "secureBoot": "secure_boot", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "secureBoot": "secure_boot", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.secure_boot = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "LsbootBootSecurity", parent_mo_or_dn, **kwargs)

