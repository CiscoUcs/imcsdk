"""This module contains the general information for MoInvKv ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MoInvKvConsts:
    pass


class MoInvKv(ManagedObject):
    """This is MoInvKv class."""

    consts = MoInvKvConsts()
    naming_props = set(['key'])

    mo_meta = {
        "classic": MoMeta("MoInvKv", "moInvKv", "kv-[key]", VersionMeta.Version401a, "OutputOnly", 0xf, [], ["read-only"], ['moKvInvHolder'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "value": MoPropertyMeta("value", "value", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "key": "key", 
            "owner": "owner", 
            "rn": "rn", 
            "status": "status", 
            "type": "type", 
            "value": "value", 
        },

    }

    def __init__(self, parent_mo_or_dn, key, **kwargs):
        self._dirty_mask = 0
        self.key = key
        self.child_action = None
        self.owner = None
        self.status = None
        self.type = None
        self.value = None

        ManagedObject.__init__(self, "MoInvKv", parent_mo_or_dn, **kwargs)

