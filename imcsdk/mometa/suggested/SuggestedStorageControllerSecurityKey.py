"""This module contains the general information for SuggestedStorageControllerSecurityKey ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class SuggestedStorageControllerSecurityKeyConsts:
    pass


class SuggestedStorageControllerSecurityKey(ManagedObject):
    """This is SuggestedStorageControllerSecurityKey class."""

    consts = SuggestedStorageControllerSecurityKeyConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("SuggestedStorageControllerSecurityKey", "suggestedStorageControllerSecurityKey", "suggested-sec-key", VersionMeta.Version209c, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageController'], [], ["Get"]),
        "modular": MoMeta("SuggestedStorageControllerSecurityKey", "suggestedStorageControllerSecurityKey", "suggested-sec-key", VersionMeta.Version303a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageController'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version209c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "suggested_security_key": MoPropertyMeta("suggested_security_key", "suggestedSecurityKey", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 1, 33, None, [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "suggested_security_key": MoPropertyMeta("suggested_security_key", "suggestedSecurityKey", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 1, 33, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "suggestedSecurityKey": "suggested_security_key", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "suggestedSecurityKey": "suggested_security_key", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.suggested_security_key = None

        ManagedObject.__init__(self, "SuggestedStorageControllerSecurityKey", parent_mo_or_dn, **kwargs)

