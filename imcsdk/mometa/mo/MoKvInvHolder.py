"""This module contains the general information for MoKvInvHolder ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MoKvInvHolderConsts:
    pass


class MoKvInvHolder(ManagedObject):
    """This is MoKvInvHolder class."""

    consts = MoKvInvHolderConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("MoKvInvHolder", "moKvInvHolder", "inv-kv-hostOs", VersionMeta.Version401a, "OutputOnly", 0xf, [], ["read-only"], ['computeRackUnit'], ['moInvKv'], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "endpoint": MoPropertyMeta("endpoint", "endpoint", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "endpoint": "endpoint", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.endpoint = None
        self.status = None

        ManagedObject.__init__(self, "MoKvInvHolder", parent_mo_or_dn, **kwargs)

