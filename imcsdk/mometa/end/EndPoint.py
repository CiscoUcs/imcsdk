"""This module contains the general information for EndPoint ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class EndPointConsts:
    pass


class EndPoint(ManagedObject):
    """This is EndPoint class."""

    consts = EndPointConsts()
    naming_props = set(['slotId'])

    mo_meta = {
        "classic": MoMeta("EndPoint", "endPoint", "ep-[slot_id]", VersionMeta.Version421a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['mctpCertificateManagement'], ['endPointCertificateChain'], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "slot_id": MoPropertyMeta("slot_id", "slotId", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "spdm_status": MoPropertyMeta("spdm_status", "spdmStatus", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "name": "name", 
            "rn": "rn", 
            "slotId": "slot_id", 
            "spdmStatus": "spdm_status", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, slot_id, **kwargs):
        self._dirty_mask = 0
        self.slot_id = slot_id
        self.child_action = None
        self.name = None
        self.spdm_status = None
        self.status = None

        ManagedObject.__init__(self, "EndPoint", parent_mo_or_dn, **kwargs)

