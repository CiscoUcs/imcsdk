"""This module contains the general information for PsuRedundancyPolicy ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PsuRedundancyPolicyConsts:
    REDUNDANCY_POLICY_GRID = "grid"
    REDUNDANCY_POLICY_N_PLUS_ONE = "n-plus-one"
    REDUNDANCY_POLICY_NON_REDUNDANT = "non-redundant"


class PsuRedundancyPolicy(ManagedObject):
    """This is PsuRedundancyPolicy class."""

    consts = PsuRedundancyPolicyConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("PsuRedundancyPolicy", "psuRedundancyPolicy", "psu-redundancy-policy", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['computeBoard'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "redundancy_policy": MoPropertyMeta("redundancy_policy", "redundancyPolicy", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["grid", "n-plus-one", "non-redundant"], []),
            "redundancy_status": MoPropertyMeta("redundancy_status", "redundancyStatus", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "redundancyPolicy": "redundancy_policy", 
            "redundancyStatus": "redundancy_status", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.redundancy_policy = None
        self.redundancy_status = None
        self.status = None

        ManagedObject.__init__(self, "PsuRedundancyPolicy", parent_mo_or_dn, **kwargs)

