"""This module contains the general information for StorageRaidBattery ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageRaidBatteryConsts:
    ADMIN_ACTION_DISABLE_AUTO_LEARN = "disable-auto-learn"
    ADMIN_ACTION_ENABLE_AUTO_LEARN = "enable-auto-learn"
    ADMIN_ACTION_START_LEARN_CYCLE = "start-learn-cycle"


class StorageRaidBattery(ManagedObject):
    """This is StorageRaidBattery class."""

    consts = StorageRaidBatteryConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StorageRaidBattery", "storageRaidBattery", "raid-battery", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['storageController'], ['faultInst'], ["Get", "Set"]),
        "modular": MoMeta("StorageRaidBattery", "storageRaidBattery", "raid-battery", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['storageController'], ['faultInst'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["disable-auto-learn", "enable-auto-learn", "start-learn-cycle"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "absolute_state_of_charge": MoPropertyMeta("absolute_state_of_charge", "absoluteStateOfCharge", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "battery_present": MoPropertyMeta("battery_present", "batteryPresent", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "battery_status": MoPropertyMeta("battery_status", "batteryStatus", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "battery_type": MoPropertyMeta("battery_type", "batteryType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "charging_state": MoPropertyMeta("charging_state", "chargingState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "completed_charge_cycles": MoPropertyMeta("completed_charge_cycles", "completedChargeCycles", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "current": MoPropertyMeta("current", "current", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "date_of_manufacture": MoPropertyMeta("date_of_manufacture", "dateOfManufacture", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "design_capacity": MoPropertyMeta("design_capacity", "designCapacity", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "design_voltage": MoPropertyMeta("design_voltage", "designVoltage", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "expected_margin_of_error": MoPropertyMeta("expected_margin_of_error", "expectedMarginOfError", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "full_capacity": MoPropertyMeta("full_capacity", "fullCapacity", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "learn_cycle_requested": MoPropertyMeta("learn_cycle_requested", "learnCycleRequested", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "learn_cycle_status": MoPropertyMeta("learn_cycle_status", "learnCycleStatus", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "learn_mode": MoPropertyMeta("learn_mode", "learnMode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "manufacturer": MoPropertyMeta("manufacturer", "manufacturer", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "next_learn_cycle": MoPropertyMeta("next_learn_cycle", "nextLearnCycle", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "relative_state_of_charge": MoPropertyMeta("relative_state_of_charge", "relativeStateOfCharge", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "remaining_capacity": MoPropertyMeta("remaining_capacity", "remainingCapacity", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "retention_time": MoPropertyMeta("retention_time", "retentionTime", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "serial_number": MoPropertyMeta("serial_number", "serialNumber", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "temperature": MoPropertyMeta("temperature", "temperature", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "temperature_high": MoPropertyMeta("temperature_high", "temperatureHigh", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "voltage": MoPropertyMeta("voltage", "voltage", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["disable-auto-learn", "enable-auto-learn", "start-learn-cycle"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "absolute_state_of_charge": MoPropertyMeta("absolute_state_of_charge", "absoluteStateOfCharge", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "battery_present": MoPropertyMeta("battery_present", "batteryPresent", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "battery_status": MoPropertyMeta("battery_status", "batteryStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "battery_type": MoPropertyMeta("battery_type", "batteryType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "charging_state": MoPropertyMeta("charging_state", "chargingState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "completed_charge_cycles": MoPropertyMeta("completed_charge_cycles", "completedChargeCycles", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "current": MoPropertyMeta("current", "current", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "date_of_manufacture": MoPropertyMeta("date_of_manufacture", "dateOfManufacture", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "design_capacity": MoPropertyMeta("design_capacity", "designCapacity", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "design_voltage": MoPropertyMeta("design_voltage", "designVoltage", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "expected_margin_of_error": MoPropertyMeta("expected_margin_of_error", "expectedMarginOfError", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "full_capacity": MoPropertyMeta("full_capacity", "fullCapacity", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "learn_cycle_requested": MoPropertyMeta("learn_cycle_requested", "learnCycleRequested", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "learn_cycle_status": MoPropertyMeta("learn_cycle_status", "learnCycleStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "learn_mode": MoPropertyMeta("learn_mode", "learnMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "manufacturer": MoPropertyMeta("manufacturer", "manufacturer", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "next_learn_cycle": MoPropertyMeta("next_learn_cycle", "nextLearnCycle", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "relative_state_of_charge": MoPropertyMeta("relative_state_of_charge", "relativeStateOfCharge", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "remaining_capacity": MoPropertyMeta("remaining_capacity", "remainingCapacity", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "retention_time": MoPropertyMeta("retention_time", "retentionTime", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "serial_number": MoPropertyMeta("serial_number", "serialNumber", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "temperature": MoPropertyMeta("temperature", "temperature", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "temperature_high": MoPropertyMeta("temperature_high", "temperatureHigh", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "voltage": MoPropertyMeta("voltage", "voltage", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "absoluteStateOfCharge": "absolute_state_of_charge", 
            "batteryPresent": "battery_present", 
            "batteryStatus": "battery_status", 
            "batteryType": "battery_type", 
            "chargingState": "charging_state", 
            "childAction": "child_action", 
            "completedChargeCycles": "completed_charge_cycles", 
            "current": "current", 
            "dateOfManufacture": "date_of_manufacture", 
            "designCapacity": "design_capacity", 
            "designVoltage": "design_voltage", 
            "expectedMarginOfError": "expected_margin_of_error", 
            "firmwareVersion": "firmware_version", 
            "fullCapacity": "full_capacity", 
            "health": "health", 
            "learnCycleRequested": "learn_cycle_requested", 
            "learnCycleStatus": "learn_cycle_status", 
            "learnMode": "learn_mode", 
            "manufacturer": "manufacturer", 
            "nextLearnCycle": "next_learn_cycle", 
            "relativeStateOfCharge": "relative_state_of_charge", 
            "remainingCapacity": "remaining_capacity", 
            "retentionTime": "retention_time", 
            "serialNumber": "serial_number", 
            "temperature": "temperature", 
            "temperatureHigh": "temperature_high", 
            "voltage": "voltage", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "absoluteStateOfCharge": "absolute_state_of_charge", 
            "batteryPresent": "battery_present", 
            "batteryStatus": "battery_status", 
            "batteryType": "battery_type", 
            "chargingState": "charging_state", 
            "childAction": "child_action", 
            "completedChargeCycles": "completed_charge_cycles", 
            "current": "current", 
            "dateOfManufacture": "date_of_manufacture", 
            "designCapacity": "design_capacity", 
            "designVoltage": "design_voltage", 
            "expectedMarginOfError": "expected_margin_of_error", 
            "firmwareVersion": "firmware_version", 
            "fullCapacity": "full_capacity", 
            "health": "health", 
            "learnCycleRequested": "learn_cycle_requested", 
            "learnCycleStatus": "learn_cycle_status", 
            "learnMode": "learn_mode", 
            "manufacturer": "manufacturer", 
            "nextLearnCycle": "next_learn_cycle", 
            "relativeStateOfCharge": "relative_state_of_charge", 
            "remainingCapacity": "remaining_capacity", 
            "retentionTime": "retention_time", 
            "serialNumber": "serial_number", 
            "temperature": "temperature", 
            "temperatureHigh": "temperature_high", 
            "voltage": "voltage", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.status = None
        self.absolute_state_of_charge = None
        self.battery_present = None
        self.battery_status = None
        self.battery_type = None
        self.charging_state = None
        self.child_action = None
        self.completed_charge_cycles = None
        self.current = None
        self.date_of_manufacture = None
        self.design_capacity = None
        self.design_voltage = None
        self.expected_margin_of_error = None
        self.firmware_version = None
        self.full_capacity = None
        self.health = None
        self.learn_cycle_requested = None
        self.learn_cycle_status = None
        self.learn_mode = None
        self.manufacturer = None
        self.next_learn_cycle = None
        self.relative_state_of_charge = None
        self.remaining_capacity = None
        self.retention_time = None
        self.serial_number = None
        self.temperature = None
        self.temperature_high = None
        self.voltage = None

        ManagedObject.__init__(self, "StorageRaidBattery", parent_mo_or_dn, **kwargs)

