"""This module contains the general information for BmcResetReason ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BmcResetReasonConsts:
    pass


class BmcResetReason(ManagedObject):
    """This is BmcResetReason class."""

    consts = BmcResetReasonConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("BmcResetReason", "bmcResetReason", "bmc-reset-reason", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['computeServerNode'], [], ["Get"])
    }


    prop_meta = {

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "reset_reason": MoPropertyMeta("reset_reason", "resetReason", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "resetReason": "reset_reason", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.reset_reason = None
        self.status = None

        ManagedObject.__init__(self, "BmcResetReason", parent_mo_or_dn, **kwargs)

