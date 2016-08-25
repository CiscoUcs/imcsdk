"""This module contains the general information for BiosPassword ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosPasswordConsts:
    pass


class BiosPassword(ManagedObject):
    """This is BiosPassword class."""

    consts = BiosPasswordConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosPassword", "biosPassword", "bios-pw", None, "InputOutput", 0x1f, [], ["admin"], [], [], [None])

    prop_meta = {
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
        "password": MoPropertyMeta("password", "password", "string", None, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\S+]{0,20}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
    }

    prop_map = {
        "dn": "dn", 
        "password": "password", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.password = None
        self.status = None

        ManagedObject.__init__(self, "BiosPassword", parent_mo_or_dn, **kwargs)

