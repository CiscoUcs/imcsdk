"""This module contains the general information for ComputeServerNode ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class ComputeServerNodeConsts:
    ADMIN_POWER_BMC_RESET_DEFAULT = "bmc-reset-default"
    ADMIN_POWER_BMC_RESET_IMMEDIATE = "bmc-reset-immediate"
    ADMIN_POWER_CMOS_RESET_IMMEDIATE = "cmos-reset-immediate"
    ADMIN_POWER_CYCLE_IMMEDIATE = "cycle-immediate"
    ADMIN_POWER_DIAGNOSTIC_INTERRUPT = "diagnostic-interrupt"
    ADMIN_POWER_DOWN = "down"
    ADMIN_POWER_HARD_RESET_IMMEDIATE = "hard-reset-immediate"
    ADMIN_POWER_POLICY = "policy"
    ADMIN_POWER_SOFT_SHUT_DOWN = "soft-shut-down"
    ADMIN_POWER_UP = "up"
    AVAILABLE_MEMORY_ = ""
    BIOS_POST_STATE_COMPLETED = "completed"
    BIOS_POST_STATE_PENDING = "pending"
    BIOS_POST_STATE_UNKNOWN = "unknown"
    MEMORY_SPEED_ = ""
    MEMORY_SPEED_UNSPECIFIED = "unspecified"
    OPER_POWER_DEGRADED = "degraded"
    OPER_POWER_ERROR = "error"
    OPER_POWER_NOT_SUPPORTED = "not-supported"
    OPER_POWER_OFF = "off"
    OPER_POWER_OFFDUTY = "offduty"
    OPER_POWER_OFFLINE = "offline"
    OPER_POWER_ON = "on"
    OPER_POWER_ONLINE = "online"
    OPER_POWER_POWER_SAVE = "power-save"
    OPER_POWER_TEST = "test"
    OPER_POWER_UNKNOWN = "unknown"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    PRESENCE_INACCESSIBLE = "inaccessible"
    PRESENCE_MISMATCH = "mismatch"
    PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    PRESENCE_MISSING = "missing"
    PRESENCE_UNAUTHORIZED = "unauthorized"
    PRESENCE_UNKNOWN = "unknown"
    TOTAL_MEMORY_ = ""


class ComputeServerNode(ManagedObject):
    """This is ComputeServerNode class."""

    consts = ComputeServerNodeConsts()
    naming_props = set(['serverId'])

    mo_meta = {
        "modular": MoMeta("ComputeServerNode", "computeServerNode", "server-[server_id]", VersionMeta.Version2013e, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['equipmentChassis'], ['adapterSecureUpdate', 'adaptorUnit', 'biosUnit', 'bmcResetReason', 'commSvcRack', 'computeBoard', 'equipmentFanModule', 'equipmentIndicatorLed', 'equipmentLocatorLed', 'equipmentPsu', 'faultInst', 'huuController', 'ioExpander', 'iodController', 'kmipManagement', 'lsbootDef', 'lsbootDevPrecision', 'mgmtBackupServer', 'mgmtController', 'mgmtImporterServer', 'networkAdapterUnit', 'oneTimeBootDevice', 'oneTimePrecisionBootDevice', 'osiController', 'pciEquipSlot', 'powerBudget', 'powerMonitor', 'serverUtilization', 'solIf'], ["Get", "Set"])
    }


    prop_meta = {

        "modular": {
            "admin_power": MoPropertyMeta("admin_power", "adminPower", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["bmc-reset-default", "bmc-reset-immediate", "cmos-reset-immediate", "cycle-immediate", "diagnostic-interrupt", "down", "hard-reset-immediate", "policy", "soft-shut-down", "up"], []),
            "available_memory": MoPropertyMeta("available_memory", "availableMemory", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [""], ["0-4294967295"]),
            "bios_post_state": MoPropertyMeta("bios_post_state", "biosPostState", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["completed", "pending", "unknown"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "memory_speed": MoPropertyMeta("memory_speed", "memorySpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "unspecified"], ["0-4294967295"]),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_adaptors": MoPropertyMeta("num_of_adaptors", "numOfAdaptors", "byte", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_cores": MoPropertyMeta("num_of_cores", "numOfCores", "ulong", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_cores_enabled": MoPropertyMeta("num_of_cores_enabled", "numOfCoresEnabled", "ulong", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_cpus": MoPropertyMeta("num_of_cpus", "numOfCpus", "byte", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_eth_host_ifs": MoPropertyMeta("num_of_eth_host_ifs", "numOfEthHostIfs", "ushort", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_fc_host_ifs": MoPropertyMeta("num_of_fc_host_ifs", "numOfFcHostIfs", "ushort", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_threads": MoPropertyMeta("num_of_threads", "numOfThreads", "ulong", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "oper_power": MoPropertyMeta("oper_power", "operPower", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "not-supported", "off", "offduty", "offline", "on", "online", "power-save", "test", "unknown"], []),
            "original_uuid": MoPropertyMeta("original_uuid", "originalUuid", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "unauthorized", "unknown"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "server_id": MoPropertyMeta("server_id", "serverId", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "total_memory": MoPropertyMeta("total_memory", "totalMemory", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [""], ["0-4294967295"]),
            "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 64, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,64}""", [], []),
            "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "modular": {
            "adminPower": "admin_power", 
            "availableMemory": "available_memory", 
            "biosPostState": "bios_post_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "memorySpeed": "memory_speed", 
            "model": "model", 
            "name": "name", 
            "numOfAdaptors": "num_of_adaptors", 
            "numOfCores": "num_of_cores", 
            "numOfCoresEnabled": "num_of_cores_enabled", 
            "numOfCpus": "num_of_cpus", 
            "numOfEthHostIfs": "num_of_eth_host_ifs", 
            "numOfFcHostIfs": "num_of_fc_host_ifs", 
            "numOfThreads": "num_of_threads", 
            "operPower": "oper_power", 
            "originalUuid": "original_uuid", 
            "presence": "presence", 
            "rn": "rn", 
            "serial": "serial", 
            "serverId": "server_id", 
            "status": "status", 
            "totalMemory": "total_memory", 
            "usrLbl": "usr_lbl", 
            "uuid": "uuid", 
            "vendor": "vendor", 
        },

    }

    def __init__(self, parent_mo_or_dn, server_id, **kwargs):
        self._dirty_mask = 0
        self.server_id = server_id
        self.admin_power = None
        self.available_memory = None
        self.bios_post_state = None
        self.child_action = None
        self.memory_speed = None
        self.model = None
        self.name = None
        self.num_of_adaptors = None
        self.num_of_cores = None
        self.num_of_cores_enabled = None
        self.num_of_cpus = None
        self.num_of_eth_host_ifs = None
        self.num_of_fc_host_ifs = None
        self.num_of_threads = None
        self.oper_power = None
        self.original_uuid = None
        self.presence = None
        self.serial = None
        self.status = None
        self.total_memory = None
        self.usr_lbl = None
        self.uuid = None
        self.vendor = None

        ManagedObject.__init__(self, "ComputeServerNode", parent_mo_or_dn, **kwargs)

