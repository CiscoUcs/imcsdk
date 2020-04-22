"""This module contains the general information for OneTimePrecisionBootDevice ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class OneTimePrecisionBootDeviceConsts:
    ADMIN_ACTION_CLEAR_ONE_TIME_BOOT_DEVICE = "clear-one-time-boot-device"
    REBOOT_ON_UPDATE_FALSE = "false"
    REBOOT_ON_UPDATE_NO = "no"
    REBOOT_ON_UPDATE_TRUE = "true"
    REBOOT_ON_UPDATE_YES = "yes"


class OneTimePrecisionBootDevice(ManagedObject):
    """This is OneTimePrecisionBootDevice class."""

    consts = OneTimePrecisionBootDeviceConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("OneTimePrecisionBootDevice", "oneTimePrecisionBootDevice", "one-time-precision-boot", VersionMeta.Version301c, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['computeRackUnit'], [], ["Get", "Set"]),
        "modular": MoMeta("OneTimePrecisionBootDevice", "oneTimePrecisionBootDevice", "one-time-precision-boot", VersionMeta.Version301c, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['computeServerNode'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear-one-time-boot-device"], []),
            "device": MoPropertyMeta("device", "device", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "reboot_on_update": MoPropertyMeta("reboot_on_update", "rebootOnUpdate", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear-one-time-boot-device"], []),
            "device": MoPropertyMeta("device", "device", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "reboot_on_update": MoPropertyMeta("reboot_on_update", "rebootOnUpdate", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["No", "Yes", "no", "yes"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "device": "device", 
            "dn": "dn", 
            "rebootOnUpdate": "reboot_on_update", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "name": "name", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "device": "device", 
            "dn": "dn", 
            "rebootOnUpdate": "reboot_on_update", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "name": "name", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.device = None
        self.reboot_on_update = None
        self.status = None
        self.child_action = None
        self.name = None

        ManagedObject.__init__(self, "OneTimePrecisionBootDevice", parent_mo_or_dn, **kwargs)

