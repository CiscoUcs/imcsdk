"""This module contains the general information for Biosf2Password ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class Biosf2PasswordConsts:
    F2_PASSWORDOPT_IN_FALSE = "false"
    F2_PASSWORDOPT_IN_TRUE = "true"


class Biosf2Password(ManagedObject):
    """This is Biosf2Password class."""

    consts = Biosf2PasswordConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("Biosf2Password", "biosf2Password", "bios-f2-password", VersionMeta.Version431a, "InputOutput", 0x3f, [], ["admin"], ['biosUnit'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version431a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "f2_passwordopt_in": MoPropertyMeta("f2_passwordopt_in", "f2PasswordoptIn", "string", VersionMeta.Version431a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "true"], []),
            "new_bios_password": MoPropertyMeta("new_bios_password", "newBiosPassword", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x4, 8, 128, None, [], []),
            "old_bios_password": MoPropertyMeta("old_bios_password", "oldBiosPassword", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x8, 0, 128, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "f2PasswordoptIn": "f2_passwordopt_in", 
            "newBiosPassword": "new_bios_password", 
            "oldBiosPassword": "old_bios_password", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.f2_passwordopt_in = None
        self.new_bios_password = None
        self.old_bios_password = None
        self.status = None

        ManagedObject.__init__(self, "Biosf2Password", parent_mo_or_dn, **kwargs)

