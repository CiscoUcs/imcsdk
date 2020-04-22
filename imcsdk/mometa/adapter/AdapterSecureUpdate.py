"""This module contains the general information for AdapterSecureUpdate ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdapterSecureUpdateConsts:
    pass


class AdapterSecureUpdate(ManagedObject):
    """This is AdapterSecureUpdate class."""

    consts = AdapterSecureUpdateConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("AdapterSecureUpdate", "adapterSecureUpdate", "adapter-secure-update", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['computeServerNode'], [], [None])
    }


    prop_meta = {

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "secure_update": MoPropertyMeta("secure_update", "secureUpdate", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "secureUpdate": "secure_update", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.secure_update = None
        self.status = None

        ManagedObject.__init__(self, "AdapterSecureUpdate", parent_mo_or_dn, **kwargs)

