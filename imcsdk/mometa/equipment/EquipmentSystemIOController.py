"""This module contains the general information for EquipmentSystemIOController ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class EquipmentSystemIOControllerConsts:
    ADMIN_POWER_CMC_REBOOT = "cmc-reboot"
    ADMIN_POWER_CMC_RESET_DEFAULT = "cmc-reset-default"
    ADMIN_POWER_POLICY = "policy"


class EquipmentSystemIOController(ManagedObject):
    """This is EquipmentSystemIOController class."""

    consts = EquipmentSystemIOControllerConsts()
    naming_props = set(['id'])

    mo_meta = {
        "modular": MoMeta("EquipmentSystemIOController", "equipmentSystemIOController", "slot-[id]", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['equipmentChassis'], ['commEpIpmiLan', 'equipmentSharedIOModule', 'faultInst', 'mgmtController', 'siocResetReason', 'systemIOControllerNVMe'], ["Get", "Set"])
    }


    prop_meta = {

        "modular": {
            "admin_power": MoPropertyMeta("admin_power", "adminPower", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["cmc-reboot", "cmc-reset-default", "policy"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], ["1-2"]),
            "pid": MoPropertyMeta("pid", "pid", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "modular": {
            "adminPower": "admin_power", 
            "childAction": "child_action", 
            "description": "description", 
            "dn": "dn", 
            "id": "id", 
            "pid": "pid", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_power = None
        self.child_action = None
        self.description = None
        self.pid = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentSystemIOController", parent_mo_or_dn, **kwargs)

