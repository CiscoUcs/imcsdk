"""This module contains the general information for ComputeServerRef ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class ComputeServerRefConsts:
    pass


class ComputeServerRef(ManagedObject):
    """This is ComputeServerRef class."""

    consts = ComputeServerRefConsts()
    naming_props = set([u'ownership'])

    mo_meta = {
        "modular": MoMeta("ComputeServerRef", "computeServerRef", "server-ref-[ownership]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'storageEnclosureDiskSlotEp'], [], ["Get"])
    }


    prop_meta = {

        "modular": {
            "diskstate": MoPropertyMeta("diskstate", "diskstate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
            "ownership": MoPropertyMeta("ownership", "ownership", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "modular": {
            "diskstate": "diskstate", 
            "dn": "dn", 
            "ownership": "ownership", 
            "rn": "rn", 
            "slot": "slot", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, ownership, **kwargs):
        self._dirty_mask = 0
        self.ownership = ownership
        self.diskstate = None
        self.slot = None
        self.status = None

        ManagedObject.__init__(self, "ComputeServerRef", parent_mo_or_dn, **kwargs)

