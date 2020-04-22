"""This module contains the general information for BiosBootMode ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosBootModeConsts:
    ACTUAL_BOOT_MODE_LEGACY = "Legacy"
    ACTUAL_BOOT_MODE_UEFI = "Uefi"
    ACTUAL_BOOT_MODE_UNKNOWN = "Unknown"


class BiosBootMode(ManagedObject):
    """This is BiosBootMode class."""

    consts = BiosBootModeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosBootMode", "biosBootMode", "boot-mode", VersionMeta.Version201a, "OutputOnly", 0xf, [], ["admin", "user"], ['biosBOT'], [], ["Get"]),
        "modular": MoMeta("BiosBootMode", "biosBootMode", "boot-mode", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "user"], ['biosBOT'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "actual_boot_mode": MoPropertyMeta("actual_boot_mode", "actualBootMode", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Legacy", "Uefi", "Unknown"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

        "modular": {
            "actual_boot_mode": MoPropertyMeta("actual_boot_mode", "actualBootMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Legacy", "Uefi", "Unknown"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "actualBootMode": "actual_boot_mode", 
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "actualBootMode": "actual_boot_mode", 
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.actual_boot_mode = None
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "BiosBootMode", parent_mo_or_dn, **kwargs)

