"""This module contains the general information for EquipmentIndicatorLed ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class EquipmentIndicatorLedConsts:
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


class EquipmentIndicatorLed(ManagedObject):
    """This is EquipmentIndicatorLed class."""

    consts = EquipmentIndicatorLedConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("EquipmentIndicatorLed", "equipmentIndicatorLed", "indicator-led-[id]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['computeRackUnit'], [], ["Get"]),
        "modular": MoMeta("EquipmentIndicatorLed", "equipmentIndicatorLed", "indicator-led-[id]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['computeServerNode', 'equipmentChassis'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "color": MoPropertyMeta("color", "color", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["amber", "blue", "green", "red", "unknown"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,25}""", [], []),
            "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["blinking", "eth", "fc", "off", "on", "unknown"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "color": MoPropertyMeta("color", "color", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["amber", "blue", "green", "red", "unknown"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,25}""", [], []),
            "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["blinking", "eth", "fc", "off", "on", "unknown"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "color": "color", 
            "dn": "dn", 
            "id": "id", 
            "name": "name", 
            "operState": "oper_state", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
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

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.color = None
        self.name = None
        self.oper_state = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentIndicatorLed", parent_mo_or_dn, **kwargs)

