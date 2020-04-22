"""This module contains the general information for GeneratedStorageControllerKeyId ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class GeneratedStorageControllerKeyIdConsts:
    pass


class GeneratedStorageControllerKeyId(ManagedObject):
    """This is GeneratedStorageControllerKeyId class."""

    consts = GeneratedStorageControllerKeyIdConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("GeneratedStorageControllerKeyId", "generatedStorageControllerKeyId", "gen-key-id", VersionMeta.Version209c, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageController'], [], ["Get"]),
        "modular": MoMeta("GeneratedStorageControllerKeyId", "generatedStorageControllerKeyId", "gen-key-id", VersionMeta.Version303a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['storageController'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version209c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "generated_key_id": MoPropertyMeta("generated_key_id", "generatedKeyId", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 1, 256, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "generated_key_id": MoPropertyMeta("generated_key_id", "generatedKeyId", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 1, 256, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "generatedKeyId": "generated_key_id", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "generatedKeyId": "generated_key_id", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.generated_key_id = None
        self.status = None

        ManagedObject.__init__(self, "GeneratedStorageControllerKeyId", parent_mo_or_dn, **kwargs)

