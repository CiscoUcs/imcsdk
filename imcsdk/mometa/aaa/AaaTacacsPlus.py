"""This module contains the general information for AaaTacacsPlus ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AaaTacacsPlusConsts:
    pass


class AaaTacacsPlus(ManagedObject):
    """This is AaaTacacsPlus class."""

    consts = AaaTacacsPlusConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AaaTacacsPlus", "aaaTacacsPlus", "tacacs-ext", VersionMeta.Version413a, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['topSystem'], ['aaaTacacsPlusServer'], [None]),
        "modular": MoMeta("AaaTacacsPlus", "aaaTacacsPlus", "tacacs-ext", VersionMeta.Version413a, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['topSystem'], ['aaaTacacsPlusServer'], [None])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "fallback_authentication": MoPropertyMeta("fallback_authentication", "fallbackAuthentication", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["5-30"]),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "fallback_authentication": MoPropertyMeta("fallback_authentication", "fallbackAuthentication", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["5-30"]),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "fallbackAuthentication": "fallback_authentication", 
            "rn": "rn", 
            "status": "status", 
            "timeout": "timeout", 
        },

        "modular": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "fallbackAuthentication": "fallback_authentication", 
            "rn": "rn", 
            "status": "status", 
            "timeout": "timeout", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.fallback_authentication = None
        self.status = None
        self.timeout = None

        ManagedObject.__init__(self, "AaaTacacsPlus", parent_mo_or_dn, **kwargs)

