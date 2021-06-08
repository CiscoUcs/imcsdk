"""This module contains the general information for ComputeRackUnit ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class ComputeRackUnitConsts:
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


class ComputeRackUnit(ManagedObject):
    """This is ComputeRackUnit class."""

    consts = ComputeRackUnitConsts()
    naming_props = set(['serverId'])

    mo_meta = {
        "classic": MoMeta("ComputeRackUnit", "computeRackUnit", "rack-unit-[server_id]", VersionMeta.Version151f, "InputOutput", 0x3ff, [], ["admin", "user"], ['topSystem'], ['adaptorUnit', 'biosUnit', 'computeBoard', 'equipmentFanModule', 'equipmentIndicatorLed', 'equipmentLocatorLed', 'equipmentPsu', 'equipmentPsuColdRedundancy', 'eventManagement', 'faultInst', 'lsbootDef', 'lsbootDevPrecision', 'mgmtController', 'moKvInvHolder', 'networkAdapterUnit', 'oneTimeBootDevice', 'oneTimePrecisionBootDevice', 'pciEquipSlot', 'powerBudget', 'powerMonitor', 'rackUnitPersonality', 'serverUtilization', 'solIf', 'sysdebugTechSupportExport', 'systemIOController', 'x86LiveDebug'], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "adaptor_secure_update": MoPropertyMeta("adaptor_secure_update", "adaptorSecureUpdate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "admin_power": MoPropertyMeta("admin_power", "adminPower", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["bmc-reset-default", "bmc-reset-immediate", "cmos-reset-immediate", "cycle-immediate", "diagnostic-interrupt", "down", "hard-reset-immediate", "policy", "soft-shut-down", "up"], []),
            "asset_tag": MoPropertyMeta("asset_tag", "assetTag", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 32, r"""[^!|&]{0,32}""", [], []),
            "available_memory": MoPropertyMeta("available_memory", "availableMemory", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "bios_post_state": MoPropertyMeta("bios_post_state", "biosPostState", "string", VersionMeta.Version411c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["completed", "pending", "unknown"], []),
            "bmc_reset_status": MoPropertyMeta("bmc_reset_status", "bmcResetStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "chassis_serial": MoPropertyMeta("chassis_serial", "chassisSerial", "string", VersionMeta.Version204c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "cimc_reset_reason": MoPropertyMeta("cimc_reset_reason", "cimcResetReason", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "memory_speed": MoPropertyMeta("memory_speed", "memorySpeed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "unspecified"], ["0-4294967295"]),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_adaptors": MoPropertyMeta("num_of_adaptors", "numOfAdaptors", "byte", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_cores": MoPropertyMeta("num_of_cores", "numOfCores", "ulong", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_cores_enabled": MoPropertyMeta("num_of_cores_enabled", "numOfCoresEnabled", "ulong", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_cpus": MoPropertyMeta("num_of_cpus", "numOfCpus", "byte", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_eth_host_ifs": MoPropertyMeta("num_of_eth_host_ifs", "numOfEthHostIfs", "ushort", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_fc_host_ifs": MoPropertyMeta("num_of_fc_host_ifs", "numOfFcHostIfs", "ushort", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "num_of_threads": MoPropertyMeta("num_of_threads", "numOfThreads", "ulong", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "oper_power": MoPropertyMeta("oper_power", "operPower", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "not-supported", "off", "offduty", "offline", "on", "online", "power-save", "test", "unknown"], []),
            "original_uuid": MoPropertyMeta("original_uuid", "originalUuid", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "unauthorized", "unknown"], []),
            "reset_components": MoPropertyMeta("reset_components", "resetComponents", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "server_id": MoPropertyMeta("server_id", "serverId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "slot_id": MoPropertyMeta("slot_id", "slotId", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "smart_usb_access": MoPropertyMeta("smart_usb_access", "smartUsbAccess", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "smart_usb_status": MoPropertyMeta("smart_usb_status", "smartUsbStatus", "string", VersionMeta.Version311d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "storage_reset_status": MoPropertyMeta("storage_reset_status", "storageResetStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "total_memory": MoPropertyMeta("total_memory", "totalMemory", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, 0, 64, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,64}""", [], []),
            "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vic_reset_status": MoPropertyMeta("vic_reset_status", "vicResetStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adaptorSecureUpdate": "adaptor_secure_update", 
            "adminPower": "admin_power", 
            "assetTag": "asset_tag", 
            "availableMemory": "available_memory", 
            "biosPostState": "bios_post_state", 
            "bmcResetStatus": "bmc_reset_status", 
            "chassisSerial": "chassis_serial", 
            "childAction": "child_action", 
            "cimcResetReason": "cimc_reset_reason", 
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
            "resetComponents": "reset_components", 
            "rn": "rn", 
            "serial": "serial", 
            "serverId": "server_id", 
            "slotId": "slot_id", 
            "smartUsbAccess": "smart_usb_access", 
            "smartUsbStatus": "smart_usb_status", 
            "status": "status", 
            "storageResetStatus": "storage_reset_status", 
            "totalMemory": "total_memory", 
            "usrLbl": "usr_lbl", 
            "uuid": "uuid", 
            "vendor": "vendor", 
            "vicResetStatus": "vic_reset_status", 
        },

    }

    def __init__(self, parent_mo_or_dn, server_id, **kwargs):
        self._dirty_mask = 0
        self.server_id = server_id
        self.adaptor_secure_update = None
        self.admin_power = None
        self.asset_tag = None
        self.available_memory = None
        self.bios_post_state = None
        self.bmc_reset_status = None
        self.chassis_serial = None
        self.child_action = None
        self.cimc_reset_reason = None
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
        self.reset_components = None
        self.serial = None
        self.slot_id = None
        self.smart_usb_access = None
        self.smart_usb_status = None
        self.status = None
        self.storage_reset_status = None
        self.total_memory = None
        self.usr_lbl = None
        self.uuid = None
        self.vendor = None
        self.vic_reset_status = None

        ManagedObject.__init__(self, "ComputeRackUnit", parent_mo_or_dn, **kwargs)

