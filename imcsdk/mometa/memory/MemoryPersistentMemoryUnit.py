"""This module contains the general information for MemoryPersistentMemoryUnit ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MemoryPersistentMemoryUnitConsts:
    CAPACITY_UNSPECIFIED = "unspecified"
    CLOCK_UNSPECIFIED = "unspecified"
    FORM_FACTOR_DIMM = "DIMM"
    FORM_FACTOR_FB_DIMM = "FB-DIMM"
    FORM_FACTOR_OTHER = "Other"
    FORM_FACTOR_RIMM = "RIMM"
    FORM_FACTOR_SIMM = "SIMM"
    FORM_FACTOR_SODIMM = "SODIMM"
    FORM_FACTOR_SRIMM = "SRIMM"
    FORM_FACTOR_TSOP = "TSOP"
    FORM_FACTOR_UNKNOWN = "Unknown"
    FORM_FACTOR_UNDISCOVERED = "undiscovered"
    HEALTH_STATE_CRITICAL_FAILURE = "CriticalFailure"
    HEALTH_STATE_FATAL_FAILURE = "FatalFailure"
    HEALTH_STATE_HEALTHY = "Healthy"
    HEALTH_STATE_MINOR_FAILURE = "MinorFailure"
    HEALTH_STATE_NON_FUNCTIONAL = "NonFunctional"
    HEALTH_STATE_UNKNOWN = "Unknown"
    HEALTH_STATE_UNMANAGABLE = "Unmanagable"
    HEALTH_STATE_UNRECOVERABLE_ERROR = "UnrecoverableError"
    OPER_STATE_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPER_STATE_AUTO_UPGRADE = "auto-upgrade"
    OPER_STATE_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPER_STATE_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPER_STATE_CONFIG = "config"
    OPER_STATE_DECOMISSIONING = "decomissioning"
    OPER_STATE_DEGRADED = "degraded"
    OPER_STATE_DISABLED = "disabled"
    OPER_STATE_DISCOVERY = "discovery"
    OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    OPER_STATE_EQUIPMENT_PROBLEM = "equipment-problem"
    OPER_STATE_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    OPER_STATE_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    OPER_STATE_IDENTIFY = "identify"
    OPER_STATE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    OPER_STATE_INOPERABLE = "inoperable"
    OPER_STATE_MALFORMED_FRU = "malformed-fru"
    OPER_STATE_NOT_SUPPORTED = "not-supported"
    OPER_STATE_OPERABLE = "operable"
    OPER_STATE_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPER_STATE_PERFORMANCE_PROBLEM = "performance-problem"
    OPER_STATE_POST_FAILURE = "post-failure"
    OPER_STATE_POWER_PROBLEM = "power-problem"
    OPER_STATE_POWERED_OFF = "powered-off"
    OPER_STATE_REMOVED = "removed"
    OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    OPER_STATE_UNKNOWN = "unknown"
    OPER_STATE_UPGRADE_PROBLEM = "upgrade-problem"
    OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
    OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPERABILITY_CONFIG = "config"
    OPERABILITY_DECOMISSIONING = "decomissioning"
    OPERABILITY_DEGRADED = "degraded"
    OPERABILITY_DISABLED = "disabled"
    OPERABILITY_DISCOVERY = "discovery"
    OPERABILITY_DISCOVERY_FAILED = "discovery-failed"
    OPERABILITY_EQUIPMENT_PROBLEM = "equipment-problem"
    OPERABILITY_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    OPERABILITY_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    OPERABILITY_IDENTIFY = "identify"
    OPERABILITY_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    OPERABILITY_INOPERABLE = "inoperable"
    OPERABILITY_MALFORMED_FRU = "malformed-fru"
    OPERABILITY_NOT_SUPPORTED = "not-supported"
    OPERABILITY_OPERABLE = "operable"
    OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    OPERABILITY_POST_FAILURE = "post-failure"
    OPERABILITY_POWER_PROBLEM = "power-problem"
    OPERABILITY_POWERED_OFF = "powered-off"
    OPERABILITY_REMOVED = "removed"
    OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    OPERABILITY_UNKNOWN = "unknown"
    OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    PRESENCE_INACCESSIBLE = "inaccessible"
    PRESENCE_MISMATCH = "mismatch"
    PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    PRESENCE_MISSING = "missing"
    PRESENCE_NOT_SUPPORTED = "not-supported"
    PRESENCE_UNAUTHORIZED = "unauthorized"
    PRESENCE_UNKNOWN = "unknown"
    SOCKET_ID_1 = "1"
    SOCKET_ID_2 = "2"
    SOCKET_ID_3 = "3"
    SOCKET_ID_4 = "4"
    SOCKET_LOCAL_DIMM_NUMBER_10 = "10"
    SOCKET_LOCAL_DIMM_NUMBER_11 = "11"
    SOCKET_LOCAL_DIMM_NUMBER_12 = "12"
    SOCKET_LOCAL_DIMM_NUMBER_14 = "14"
    SOCKET_LOCAL_DIMM_NUMBER_15 = "15"
    SOCKET_LOCAL_DIMM_NUMBER_16 = "16"
    SOCKET_LOCAL_DIMM_NUMBER_2 = "2"
    SOCKET_LOCAL_DIMM_NUMBER_3 = "3"
    SOCKET_LOCAL_DIMM_NUMBER_4 = "4"
    SOCKET_LOCAL_DIMM_NUMBER_6 = "6"
    SOCKET_LOCAL_DIMM_NUMBER_7 = "7"
    SOCKET_LOCAL_DIMM_NUMBER_8 = "8"
    TYPE_3_DRAM = "3DRAM"
    TYPE_CDRAM = "CDRAM"
    TYPE_DDR = "DDR"
    TYPE_DDR2 = "DDR2"
    TYPE_DDR2_FB_DIMM = "DDR2 FB-DIMM"
    TYPE_DDR3 = "DDR3"
    TYPE_DDR4 = "DDR4"
    TYPE_DRAM = "DRAM"
    TYPE_EDRAM = "EDRAM"
    TYPE_EEPROM = "EEPROM"
    TYPE_EPROM = "EPROM"
    TYPE_FBD2 = "FBD2"
    TYPE_FEPROM = "FEPROM"
    TYPE_FLASH = "FLASH"
    TYPE_LOGICAL_NON_VOLATILE_DEVICE = "Logical non-volatile device"
    TYPE_OTHER = "Other"
    TYPE_RAM = "RAM"
    TYPE_RDRAM = "RDRAM"
    TYPE_ROM = "ROM"
    TYPE_SDRAM = "SDRAM"
    TYPE_SGRAM = "SGRAM"
    TYPE_SRAM = "SRAM"
    TYPE_UNKNOWN = "Unknown"
    TYPE_VRAM = "VRAM"
    TYPE_UNDISCOVERED = "undiscovered"
    VISIBILITY_NO = "no"
    VISIBILITY_UNKNOWN = "unknown"
    VISIBILITY_YES = "yes"
    WIDTH_UNSPECIFIED = "unspecified"


class MemoryPersistentMemoryUnit(ManagedObject):
    """This is MemoryPersistentMemoryUnit class."""

    consts = MemoryPersistentMemoryUnitConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("MemoryPersistentMemoryUnit", "memoryPersistentMemoryUnit", "pmem-[id]", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['memoryArray'], [], [None]),
        "modular": MoMeta("MemoryPersistentMemoryUnit", "memoryPersistentMemoryUnit", "pmem-[id]", VersionMeta.Version404b, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['memoryArray'], [], [None])
    }


    prop_meta = {

        "classic": {
            "app_direct_capacity": MoPropertyMeta("app_direct_capacity", "appDirectCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "array": MoPropertyMeta("array", "array", "ushort", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "bank_locator": MoPropertyMeta("bank_locator", "bankLocator", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "capacity": MoPropertyMeta("capacity", "capacity", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "clock": MoPropertyMeta("clock", "clock", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "form_factor": MoPropertyMeta("form_factor", "formFactor", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["DIMM", "FB-DIMM", "Other", "RIMM", "SIMM", "SODIMM", "SRIMM", "TSOP", "Unknown", "undiscovered"], []),
            "health_state": MoPropertyMeta("health_state", "healthState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["CriticalFailure", "FatalFailure", "Healthy", "MinorFailure", "NonFunctional", "Unknown", "Unmanagable", "UnrecoverableError"], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version404b, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "last_security_oper_status": MoPropertyMeta("last_security_oper_status", "lastSecurityOperStatus", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "location": MoPropertyMeta("location", "location", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "memory_capacity": MoPropertyMeta("memory_capacity", "memoryCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "memory_type_detail": MoPropertyMeta("memory_type_detail", "memoryTypeDetail", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []),
            "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []),
            "persistent_memory_capacity": MoPropertyMeta("persistent_memory_capacity", "persistentMemoryCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], []),
            "reserved_capacity": MoPropertyMeta("reserved_capacity", "reservedCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "security_status": MoPropertyMeta("security_status", "securityStatus", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "3", "4"], []),
            "socket_local_dimm_number": MoPropertyMeta("socket_local_dimm_number", "socketLocalDimmNumber", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["10", "11", "12", "14", "15", "16", "2", "3", "4", "6", "7", "8"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "total_capacity": MoPropertyMeta("total_capacity", "totalCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["3DRAM", "CDRAM", "DDR", "DDR2", "DDR2 FB-DIMM", "DDR3", "DDR4", "DRAM", "EDRAM", "EEPROM", "EPROM", "FBD2", "FEPROM", "FLASH", "Logical non-volatile device", "Other", "RAM", "RDRAM", "ROM", "SDRAM", "SGRAM", "SRAM", "Unknown", "VRAM", "undiscovered"], []),
            "uid": MoPropertyMeta("uid", "uid", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "visibility": MoPropertyMeta("visibility", "visibility", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "unknown", "yes"], []),
            "width": MoPropertyMeta("width", "width", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
        },

        "modular": {
            "app_direct_capacity": MoPropertyMeta("app_direct_capacity", "appDirectCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "array": MoPropertyMeta("array", "array", "ushort", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "bank_locator": MoPropertyMeta("bank_locator", "bankLocator", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "capacity": MoPropertyMeta("capacity", "capacity", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "clock": MoPropertyMeta("clock", "clock", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "form_factor": MoPropertyMeta("form_factor", "formFactor", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["DIMM", "FB-DIMM", "Other", "RIMM", "SIMM", "SODIMM", "SRIMM", "TSOP", "Unknown", "undiscovered"], []),
            "health_state": MoPropertyMeta("health_state", "healthState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["CriticalFailure", "FatalFailure", "Healthy", "MinorFailure", "NonFunctional", "Unknown", "Unmanagable", "UnrecoverableError"], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version404b, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "last_security_oper_status": MoPropertyMeta("last_security_oper_status", "lastSecurityOperStatus", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "location": MoPropertyMeta("location", "location", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "memory_capacity": MoPropertyMeta("memory_capacity", "memoryCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "memory_type_detail": MoPropertyMeta("memory_type_detail", "memoryTypeDetail", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []),
            "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []),
            "persistent_memory_capacity": MoPropertyMeta("persistent_memory_capacity", "persistentMemoryCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], []),
            "reserved_capacity": MoPropertyMeta("reserved_capacity", "reservedCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "security_status": MoPropertyMeta("security_status", "securityStatus", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "3", "4"], []),
            "socket_local_dimm_number": MoPropertyMeta("socket_local_dimm_number", "socketLocalDimmNumber", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["10", "12", "2", "4", "6", "8"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "total_capacity": MoPropertyMeta("total_capacity", "totalCapacity", "long", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["3DRAM", "CDRAM", "DDR", "DDR2", "DDR2 FB-DIMM", "DDR3", "DDR4", "DRAM", "EDRAM", "EEPROM", "EPROM", "FBD2", "FEPROM", "FLASH", "Logical non-volatile device", "Other", "RAM", "RDRAM", "ROM", "SDRAM", "SGRAM", "SRAM", "Unknown", "VRAM", "undiscovered"], []),
            "uid": MoPropertyMeta("uid", "uid", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "visibility": MoPropertyMeta("visibility", "visibility", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "unknown", "yes"], []),
            "width": MoPropertyMeta("width", "width", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
        },

    }

    prop_map = {

        "classic": {
            "appDirectCapacity": "app_direct_capacity", 
            "array": "array", 
            "bankLocator": "bank_locator", 
            "capacity": "capacity", 
            "childAction": "child_action", 
            "clock": "clock", 
            "dn": "dn", 
            "firmwareVersion": "firmware_version", 
            "formFactor": "form_factor", 
            "healthState": "health_state", 
            "id": "id", 
            "lastSecurityOperStatus": "last_security_oper_status", 
            "location": "location", 
            "memoryCapacity": "memory_capacity", 
            "memoryTypeDetail": "memory_type_detail", 
            "model": "model", 
            "operState": "oper_state", 
            "operability": "operability", 
            "persistentMemoryCapacity": "persistent_memory_capacity", 
            "presence": "presence", 
            "reservedCapacity": "reserved_capacity", 
            "rn": "rn", 
            "securityStatus": "security_status", 
            "serial": "serial", 
            "socketId": "socket_id", 
            "socketLocalDimmNumber": "socket_local_dimm_number", 
            "status": "status", 
            "totalCapacity": "total_capacity", 
            "type": "type", 
            "uid": "uid", 
            "vendor": "vendor", 
            "visibility": "visibility", 
            "width": "width", 
        },

        "modular": {
            "appDirectCapacity": "app_direct_capacity", 
            "array": "array", 
            "bankLocator": "bank_locator", 
            "capacity": "capacity", 
            "childAction": "child_action", 
            "clock": "clock", 
            "dn": "dn", 
            "firmwareVersion": "firmware_version", 
            "formFactor": "form_factor", 
            "healthState": "health_state", 
            "id": "id", 
            "lastSecurityOperStatus": "last_security_oper_status", 
            "location": "location", 
            "memoryCapacity": "memory_capacity", 
            "memoryTypeDetail": "memory_type_detail", 
            "model": "model", 
            "operState": "oper_state", 
            "operability": "operability", 
            "persistentMemoryCapacity": "persistent_memory_capacity", 
            "presence": "presence", 
            "reservedCapacity": "reserved_capacity", 
            "rn": "rn", 
            "securityStatus": "security_status", 
            "serial": "serial", 
            "socketId": "socket_id", 
            "socketLocalDimmNumber": "socket_local_dimm_number", 
            "status": "status", 
            "totalCapacity": "total_capacity", 
            "type": "type", 
            "uid": "uid", 
            "vendor": "vendor", 
            "visibility": "visibility", 
            "width": "width", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.app_direct_capacity = None
        self.array = None
        self.bank_locator = None
        self.capacity = None
        self.child_action = None
        self.clock = None
        self.firmware_version = None
        self.form_factor = None
        self.health_state = None
        self.last_security_oper_status = None
        self.location = None
        self.memory_capacity = None
        self.memory_type_detail = None
        self.model = None
        self.oper_state = None
        self.operability = None
        self.persistent_memory_capacity = None
        self.presence = None
        self.reserved_capacity = None
        self.security_status = None
        self.serial = None
        self.socket_id = None
        self.socket_local_dimm_number = None
        self.status = None
        self.total_capacity = None
        self.type = None
        self.uid = None
        self.vendor = None
        self.visibility = None
        self.width = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryUnit", parent_mo_or_dn, **kwargs)

