"""This module contains the general information for FaultInst ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class FaultInstConsts:
    ACK_FALSE = "false"
    ACK_NO = "no"
    ACK_TRUE = "true"
    ACK_YES = "yes"
    HIGHEST_SEVERITY_CLEARED = "cleared"
    HIGHEST_SEVERITY_CONDITION = "condition"
    HIGHEST_SEVERITY_CRITICAL = "critical"
    HIGHEST_SEVERITY_INFO = "info"
    HIGHEST_SEVERITY_MAJOR = "major"
    HIGHEST_SEVERITY_MINOR = "minor"
    HIGHEST_SEVERITY_WARNING = "warning"
    ORIG_SEVERITY_CLEARED = "cleared"
    ORIG_SEVERITY_CONDITION = "condition"
    ORIG_SEVERITY_CRITICAL = "critical"
    ORIG_SEVERITY_INFO = "info"
    ORIG_SEVERITY_MAJOR = "major"
    ORIG_SEVERITY_MINOR = "minor"
    ORIG_SEVERITY_WARNING = "warning"
    PREV_SEVERITY_CLEARED = "cleared"
    PREV_SEVERITY_CONDITION = "condition"
    PREV_SEVERITY_CRITICAL = "critical"
    PREV_SEVERITY_INFO = "info"
    PREV_SEVERITY_MAJOR = "major"
    PREV_SEVERITY_MINOR = "minor"
    PREV_SEVERITY_WARNING = "warning"
    SEVERITY_CLEARED = "cleared"
    SEVERITY_CONDITION = "condition"
    SEVERITY_CRITICAL = "critical"
    SEVERITY_INFO = "info"
    SEVERITY_MAJOR = "major"
    SEVERITY_MINOR = "minor"
    SEVERITY_WARNING = "warning"
    TYPE_CONFIGURATION = "configuration"
    TYPE_CONNECTIVITY = "connectivity"
    TYPE_ENVIRONMENTAL = "environmental"
    TYPE_EQUIPMENT = "equipment"
    TYPE_FSM = "fsm"
    TYPE_GENERIC = "generic"
    TYPE_MANAGEMENT = "management"
    TYPE_NETWORK = "network"
    TYPE_OPERATIONAL = "operational"
    TYPE_SERVER = "server"
    TYPE_SYSDEBUG = "sysdebug"


class FaultInst(ManagedObject):
    """This is FaultInst class."""

    consts = FaultInstConsts()
    naming_props = set(['code'])

    mo_meta = {
        "classic": MoMeta("FaultInst", "faultInst", "fault-[code]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['adaptorUnit', 'cloudDeviceConnectorEp', 'computeBoard', 'computeRackUnit', 'equipmentFan', 'equipmentPsu', 'memoryArray', 'memoryUnit', 'mgmtIf', 'pciEquipSlot', 'pciSwitch', 'powerBudget', 'processorUnit', 'storageController', 'storageControllerNVMe', 'storageFlexFlashController', 'storageFlexFlashPhysicalDrive', 'storageFlexFlashVirtualDrive', 'storageFlexUtilController', 'storageFlexUtilPhysicalDrive', 'storageFlexUtilVirtualDrive', 'storageLocalDisk', 'storageNVMePhysicalDrive', 'storageRaidBattery', 'storageVirtualDrive', 'sysdebugMEpLog'], [], ["Get"]),
        "modular": MoMeta("FaultInst", "faultInst", "fault-[code]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['adaptorUnit', 'cloudDeviceConnectorEp', 'computeBoard', 'computeServerNode', 'equipmentChassis', 'equipmentFan', 'equipmentPsu', 'equipmentSystemIOController', 'ioControllerNVMePhysicalDrive', 'memoryArray', 'memoryUnit', 'pciEquipSlot', 'powerBudget', 'processorUnit', 'storageController', 'storageControllerNVMe', 'storageEnclosureDiskSlotEp', 'storageFlexFlashController', 'storageFlexFlashPhysicalDrive', 'storageFlexFlashVirtualDrive', 'storageLocalDisk', 'storageLocalDiskEp', 'storageNVMePhysicalDrive', 'storageRaidBattery', 'storageSasExpander', 'storageVirtualDrive', 'sysdebugMEpLog', 'systemIOControllerNVMe'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "ack": MoPropertyMeta("ack", "ack", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
            "affected_dn": MoPropertyMeta("affected_dn", "affectedDN", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "cause": MoPropertyMeta("cause", "cause", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "change_set": MoPropertyMeta("change_set", "changeSet", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 512, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "code": MoPropertyMeta("code", "code", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "created": MoPropertyMeta("created", "created", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 1024, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "highest_severity": MoPropertyMeta("highest_severity", "highestSeverity", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []),
            "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "last_transition": MoPropertyMeta("last_transition", "lastTransition", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|flapping|soaking-clear),){0,3}(defaultValue|none|flapping|soaking-clear){0,1}""", [], []),
            "occur": MoPropertyMeta("occur", "occur", "ushort", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "orig_severity": MoPropertyMeta("orig_severity", "origSeverity", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []),
            "prev_severity": MoPropertyMeta("prev_severity", "prevSeverity", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "rule": MoPropertyMeta("rule", "rule", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "severity": MoPropertyMeta("severity", "severity", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "tags": MoPropertyMeta("tags", "tags", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|generic|server|network|storage|pod|security|operations|fsmstagefail|fsmstageretry|fsmstageremoteinv|Intersight),){0,12}(defaultValue|generic|server|network|storage|pod|security|operations|fsmstagefail|fsmstageretry|fsmstageremoteinv|Intersight){0,1}""", [], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["configuration", "connectivity", "environmental", "equipment", "fsm", "generic", "management", "network", "operational", "server", "sysdebug"], []),
        },

        "modular": {
            "ack": MoPropertyMeta("ack", "ack", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
            "affected_dn": MoPropertyMeta("affected_dn", "affectedDN", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "cause": MoPropertyMeta("cause", "cause", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "change_set": MoPropertyMeta("change_set", "changeSet", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 512, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "code": MoPropertyMeta("code", "code", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "created": MoPropertyMeta("created", "created", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 384, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "highest_severity": MoPropertyMeta("highest_severity", "highestSeverity", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []),
            "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "last_transition": MoPropertyMeta("last_transition", "lastTransition", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|flapping|soaking-clear),){0,3}(defaultValue|none|flapping|soaking-clear){0,1}""", [], []),
            "occur": MoPropertyMeta("occur", "occur", "ushort", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "orig_severity": MoPropertyMeta("orig_severity", "origSeverity", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []),
            "prev_severity": MoPropertyMeta("prev_severity", "prevSeverity", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "rule": MoPropertyMeta("rule", "rule", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "severity": MoPropertyMeta("severity", "severity", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "tags": MoPropertyMeta("tags", "tags", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|generic|server|network|storage|pod|security|operations|fsmstagefail|fsmstageretry|fsmstageremoteinv),){0,10}(defaultValue|generic|server|network|storage|pod|security|operations|fsmstagefail|fsmstageretry|fsmstageremoteinv|Intersight){0,1}""", [], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["configuration", "connectivity", "environmental", "equipment", "fsm", "generic", "management", "network", "operational", "server", "sysdebug"], []),
        },

    }

    prop_map = {

        "classic": {
            "ack": "ack", 
            "affectedDN": "affected_dn", 
            "cause": "cause", 
            "changeSet": "change_set", 
            "childAction": "child_action", 
            "code": "code", 
            "created": "created", 
            "descr": "descr", 
            "dn": "dn", 
            "highestSeverity": "highest_severity", 
            "id": "id", 
            "lastTransition": "last_transition", 
            "lc": "lc", 
            "occur": "occur", 
            "origSeverity": "orig_severity", 
            "prevSeverity": "prev_severity", 
            "rn": "rn", 
            "rule": "rule", 
            "severity": "severity", 
            "status": "status", 
            "tags": "tags", 
            "type": "type", 
        },

        "modular": {
            "ack": "ack", 
            "affectedDN": "affected_dn", 
            "cause": "cause", 
            "changeSet": "change_set", 
            "childAction": "child_action", 
            "code": "code", 
            "created": "created", 
            "descr": "descr", 
            "dn": "dn", 
            "highestSeverity": "highest_severity", 
            "id": "id", 
            "lastTransition": "last_transition", 
            "lc": "lc", 
            "occur": "occur", 
            "origSeverity": "orig_severity", 
            "prevSeverity": "prev_severity", 
            "rn": "rn", 
            "rule": "rule", 
            "severity": "severity", 
            "status": "status", 
            "tags": "tags", 
            "type": "type", 
        },

    }

    def __init__(self, parent_mo_or_dn, code, **kwargs):
        self._dirty_mask = 0
        self.code = code
        self.ack = None
        self.affected_dn = None
        self.cause = None
        self.change_set = None
        self.child_action = None
        self.created = None
        self.descr = None
        self.highest_severity = None
        self.id = None
        self.last_transition = None
        self.lc = None
        self.occur = None
        self.orig_severity = None
        self.prev_severity = None
        self.rule = None
        self.severity = None
        self.status = None
        self.tags = None
        self.type = None

        ManagedObject.__init__(self, "FaultInst", parent_mo_or_dn, **kwargs)

