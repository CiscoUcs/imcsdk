"""This module contains the general information for OneTimeBootDevice ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class OneTimeBootDeviceConsts:
    DEVICE_HUU = "huu"
    DEVICE_HV = "hv"
    DEVICE_NONE = "none"
    DEVICE_SCU = "scu"


class OneTimeBootDevice(ManagedObject):
    """This is OneTimeBootDevice class."""

    consts = OneTimeBootDeviceConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("OneTimeBootDevice", "oneTimeBootDevice", "boot-one-time", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['computeRackUnit'], [], ["Get", "Set"]),
        "modular": MoMeta("OneTimeBootDevice", "oneTimeBootDevice", "boot-one-time", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['computeServerNode'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "device": MoPropertyMeta("device", "device", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["huu", "hv", "none", "scu"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        },

        "modular": {
            "device": MoPropertyMeta("device", "device", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["huu", "hv", "none", "scu"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "device": "device", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "name": "name", 
        },

        "modular": {
            "device": "device", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "name": "name", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.device = None
        self.status = None
        self.child_action = None
        self.name = None

        ManagedObject.__init__(self, "OneTimeBootDevice", parent_mo_or_dn, **kwargs)

