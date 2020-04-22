"""This module contains the general information for EquipmentChassisLocatorLed ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class EquipmentChassisLocatorLedConsts:
    ADMIN_STATE_INACTIVE = "inactive"
    ADMIN_STATE_OFF = "off"
    ADMIN_STATE_ON = "on"
    COLOR_AMBER = "amber"
    COLOR_BLUE = "blue"
    COLOR_GREEN = "green"
    COLOR_RED = "red"
    COLOR_UNKNOWN = "unknown"
    OPER_STATE_BLINKING = "blinking"
    OPER_STATE_ETH = "eth"
    OPER_STATE_FC = "fc"
    OPER_STATE_OFF = "off"
    OPER_STATE_ON = "on"
    OPER_STATE_UNKNOWN = "unknown"


class EquipmentChassisLocatorLed(ManagedObject):
    """This is EquipmentChassisLocatorLed class."""

    consts = EquipmentChassisLocatorLedConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("EquipmentChassisLocatorLed", "equipmentChassisLocatorLed", "chassis-locator-led", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['equipmentChassis'], [], ["Get", "Set"])
    }


    prop_meta = {

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["inactive", "off", "on"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "color": MoPropertyMeta("color", "color", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["amber", "blue", "green", "red", "unknown"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 512, None, [], []),
            "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["blinking", "eth", "fc", "off", "on", "unknown"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "modular": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "color": "color", 
            "dn": "dn", 
            "id": "id", 
            "name": "name", 
            "operState": "oper_state", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.color = None
        self.id = None
        self.name = None
        self.oper_state = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentChassisLocatorLed", parent_mo_or_dn, **kwargs)

