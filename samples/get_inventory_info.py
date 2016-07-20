# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module fetches inventory information of IMC.
"""


import logging
from connection.info import imc_login, imc_logout

logging.basicConfig()
log = logging.getLogger('imc')
log.setLevel(logging.DEBUG)


class RackUnitInventory:
    def __init__(self, rack_unit):
        self.class_id = "Rack Unit"
        self.number_of_cpus = rack_unit.num_of_cpus
        self.number_of_cores = rack_unit.num_of_cores
        self.available_memory = rack_unit.available_memory
        self.number_of_adaptors = rack_unit.num_of_adaptors
        self.number_of_eth_interfaces = rack_unit.num_of_eth_host_ifs
        self.number_of_fc_interfaces = rack_unit.num_of_fc_host_ifs
        self.uuid = rack_unit.uuid
        self.psu_units = []
        self.boot_definitions = []
        self.network_adaptor_units = []
        self.compute_boards = []

    def get_rack_health_info(self, handle):
        locator_led_info = handle.query_dn(dn="sys/rack-unit-1/indicator-led-5")
        if locator_led_info is not None:
            if locator_led_info.color == "green":
                if locator_led_info.oper_state == "on":
                    self.operation_state = "Good"
                elif locator_led_info.oper_state == "off":
                    self.operation_state = "Good(Memory Test In Progress)"
            if locator_led_info.color == "amber":
                if locator_led_info.oper_state == "on":
                    self.operation_state = "Fault"
                elif locator_led_info.oper_state == "off":
                    self.operation_state = "Severe fault"
                elif locator_led_info.oper_state == "blinking":
                    self.operation_state = "Severe fault"


class NetworkAdaptorUnitInventory:
    def __init__(self, network_adaptor_unit):
        self.class_id = "Network Adaptor Unit"
        self.model = network_adaptor_unit.model
        self.num_int_f = network_adaptor_unit.num_intf
        self.slot = network_adaptor_unit.slot


class ComputeBoardInventory:
    def __init__(self, compute_board):
        self.class_id = "Compute Board"
        self.id = compute_board.id
        self.model = compute_board.model
        self.oper_power = compute_board.oper_power
        self.perf = compute_board.perf
        self.power = compute_board.power
        self.presence = compute_board.presence
        self.serial = compute_board.serial
        self.processor_units = []
        self.memory_arrays = []
        self.storage_controllers = []
        self.pid_catalog_dimms = []
        self.pid_catalog_pci_adapters = []
        self.bios_units = []
        self.temp_stats = []
        self.power_stats = []


class ProcessorUnitInventory:
    def __init__(self, processor_unit):
        self.class_id = "Processor Unit"
        self.id = processor_unit.id
        self.arch = processor_unit.arch
        self.cores = processor_unit.cores
        self.cores_enabled = processor_unit.cores_enabled
        self.model = processor_unit.model
        self.socket_designation = processor_unit.socket_designation
        self.speed = processor_unit.speed
        self.stepping = processor_unit.stepping
        self.threads = processor_unit.threads
        self.vendor = processor_unit.vendor
        self.sensor_description = None
        self.temperature = None


class MemoryArrayInventory:
    def __init__(self, memory_array):
        self.class_id = "Memory Array"
        self.id = memory_array.id
        self.curr_capacity = memory_array.curr_capacity
        self.max_capacity = memory_array.max_devices
        self.populated = memory_array.populated
        self.memory_units = []


class MemoryUnitInventory:
    def __init__(self, memory_unit):
        self.class_id = "Memory Unit"
        self.id = memory_unit.id
        self.capacity = memory_unit.capacity
        self.clock = memory_unit.clock
        self.form_factor = memory_unit.form_factor
        self.location = memory_unit.location
        self.model = memory_unit.model
        self.oper_state = memory_unit.oper_state
        self.operability = memory_unit.operability
        self.presence = memory_unit.presence
        self.serial = memory_unit.serial
        self.type = memory_unit.type
        self.vendor = memory_unit.vendor
        self.visibility = memory_unit.visibility


class StorageControllerInventory:
    def __init__(self, storage_controller):
        self.class_id = "Storage Controller"
        self.id = storage_controller.id
        self.model = storage_controller.model
        self.type = storage_controller.type
        self.vendor = storage_controller.vendor
        self.serial = storage_controller.serial
        self.pci_slot = storage_controller.pci_slot
        self.presence = storage_controller.presence
        self.storage_local_disks = []
        self.storage_virtual_drives = []
        self.firmware_deployment = None
        self.firmware_version = None


class StorageLocalDiskInventory:
    def __init__(self, storage_local_disk):
        self.class_id = "Storage Local Disk"
        self.id = storage_local_disk.id
        self.interface_type = storage_local_disk.interface_type
        self.drive_state = storage_local_disk.drive_state
        self.drive_serial_number = storage_local_disk.drive_serial_number
        self.vendor = storage_local_disk.vendor
        self.product_id = storage_local_disk.product_id
        self.health = storage_local_disk.health
        self.pd_status = storage_local_disk.pd_status
        self.link_speed = storage_local_disk.link_speed


class StorageVirtualDriveInventory:
    def __init__(self, storage_virtual_drive):
        self.class_id = "Storage Virtual Drive"
        self.id = storage_virtual_drive.id
        self.name = storage_virtual_drive.name
        self.raid_level = storage_virtual_drive.raid_level
        self.access_policy = storage_virtual_drive.access_policy
        self.allow_background_init = storage_virtual_drive.allow_background_init
        self.auto_delete_oldest = storage_virtual_drive.auto_delete_oldest
        self.auto_snapshot = storage_virtual_drive.auto_snapshot
        self.cache_policy = storage_virtual_drive.cache_policy
        self.disk_cache_policy = storage_virtual_drive.disk_cache_policy
        self.drive_state = storage_virtual_drive.drive_state
        self.drives_per_span = storage_virtual_drive.drives_per_span
        self.health = storage_virtual_drive.health
        self.size = storage_virtual_drive.size
        self.strip_size = storage_virtual_drive.strip_size
        self.vd_status = storage_virtual_drive.vd_status


class PidCatalogDimmInventory:
    def __init__(self, pid_catalog_dimm):
        self.class_id = "DIMM"
        self.name = pid_catalog_dimm.name
        self.model = pid_catalog_dimm.model
        self.manufacturer = pid_catalog_dimm.manufacturer
        self.operability = pid_catalog_dimm.operablity
        self.capacity = pid_catalog_dimm.capacity
        self.data_width = pid_catalog_dimm.data_width
        self.serial_number = pid_catalog_dimm.serial_number
        self.description = pid_catalog_dimm.description


class PidCatalogPciAdapterInventory:
    def __init__(self, pci_adapter):
        self.class_id = "PCI Adapter"
        self.Pid = pci_adapter.pid
        self.slot = pci_adapter.slot
        self.description = pci_adapter.description
        self.vendor = pci_adapter.vendor


class BiosUnitInventory:
    def __init__(self, bios_unit):
        self.class_id = "Bios Unit"
        self.model = bios_unit.model
        self.vendor = bios_unit.vendor
        self.firmware_deployment = None
        self.firmware_version = None


class BootDefinitionInventory:
    def __init__(self, boot_definition):
        self.class_id = "Boot Definition"
        self.name = boot_definition.name
        self.purpose = boot_definition.purpose
        self.reboot_on_update = boot_definition.reboot_on_update


class PsuUnitInventory:
    def __init__(self, psu_unit):
        self.class_id = "Power Supply Unit"
        self.name = psu_unit.id
        self.model = psu_unit.model
        self.vendor = psu_unit.vendor
        self.serial = psu_unit.serial
        self.power = psu_unit.power
        self.thermal = psu_unit.thermal
        self.operability = psu_unit.operability
        self.presence = psu_unit.presence


class TempStatInventory:
    def __init__(self, temp_stat):
        self.class_id = "Temperature Statistic"
        self.ambient_temp = temp_stat.ambient_temp
        self.front_temp = temp_stat.front_temp
        self.ioh1_temp = temp_stat.ioh1_temp
        self.ioh2_temp = temp_stat.ioh2_temp
        self.rear_temp = temp_stat.rear_temp
        self.time_collected = temp_stat.time_collected


class PowerStatInventory:
    def __init__(self, power_stat):
        self.class_id = "Power Statistic"
        self.ConsumedPower = power_stat.consumed_power
        self.InputCurrent = power_stat.input_current
        self.InputVoltage = power_stat.input_voltage
        self.time_collected = power_stat.time_collected


def get_rack_unit_inventory(handle):
    """
    The method fetches rack unit inventory.

    Args:
        handle: ImcHandle

    Returns:
        Rack Unit Inv Object
    """

    rack_unit = handle.query_classid(class_id="computeRackUnit")
    rack_unit_obj = RackUnitInventory(rack_unit[0])
    rack_unit_obj.get_rack_health_info(handle)
    rack_unit_obj.psu_units = get_psu_unit_inventory(handle,
                                                     rack_unit[0])
    rack_unit_obj.boot_definitions = get_boot_definition_inventory(handle,
                                                                   rack_unit[0])
    rack_unit_obj.network_adaptor_units = get_network_adaptor_unit_inventory(
        handle,
        rack_unit[0])
    rack_unit_obj.compute_boards = get_compute_board_inventory(handle,
                                                               rack_unit[0])

    return rack_unit_obj


def get_psu_unit_inventory(handle, rack_unit):
    """
    The method fetches PSU unit inventory of a Rack Server.

    Args:
        handle: ImcHandle
        rack_unit: Managed Object

    Returns:
        Storage PSU Unit Inv Object
    """

    psu_unit_inventory = []
    psu_units = handle.query_children(in_mo=rack_unit, class_id="equipmentPsu")
    if psu_units:
        for psu_unit in psu_units:
            psu_unit_obj = PsuUnitInventory(psu_unit)
            psu_unit_inventory.append(psu_unit_obj)

    return psu_unit_inventory


def get_boot_definition_inventory(handle, rack_unit):
    """
    The method fetches boot definition inventory of a rack unit.

    Args:
        handle: ImcHandle
        rack_unit: Managed Object

    Returns:
        Boot definition inventory.
    """

    boot_definition_inventory = []
    boot_definitions = handle.query_children(in_mo=rack_unit,
                                             class_id="lsbootDef")
    if boot_definitions:
        for boot_definition in boot_definitions:
            boot_definition_obj = BootDefinitionInventory(boot_definition)
            boot_definition_inventory.append(boot_definition_obj)

    return boot_definition_inventory


def get_network_adaptor_unit_inventory(handle, rack_unit):
    """
    The method fetches network adaptor inventory of a rack unit.

    Args:
        handle: ImcHandle
        rack_unit: Managed Object

    Returns:
        Network adapter unit inventory.
    """

    network_adaptor_unit_inventory = []
    network_adaptor_units = handle.query_children(in_mo=rack_unit,
                                                  class_id="NetworkAdapterUnit")
    if network_adaptor_units:
        for network_adaptor_unit in network_adaptor_units:
            network_adaptor_unit_obj = NetworkAdaptorUnitInventory(
                                                        network_adaptor_unit)

            adaptor_eth_if_info = handle.query_children(
                in_mo=network_adaptor_unit, class_id="NetworkAdapterEthIf")
            if adaptor_eth_if_info:
                for each_adaptor_eth_if in adaptor_eth_if_info:
                    network_adaptor_unit_obj.__dict__["MacAddressOf <%s>" %
                                                      each_adaptor_eth_if.rn]\
                        = each_adaptor_eth_if.mac

            network_adaptor_unit_inventory.append(network_adaptor_unit_obj)

    return network_adaptor_unit_inventory


def get_compute_board_inventory(handle, rack_unit):
    """
    The method fetches compute board inventory of a rack server.

    Args:
        handle: ImcHandle
        rack_unit: Managed Object

    Returns:
        Compute Board inventory.
    """
    compute_board_inventory = []
    compute_boards = handle.query_children(in_mo=rack_unit,
                                           class_id="ComputeBoard")
    if compute_boards:
        for compute_board in compute_boards:
            compute_board_obj = ComputeBoardInventory(compute_board)
            compute_board_obj.processor_units = get_processor_unit_inventory(
                                                       handle, compute_board)
            compute_board_obj.memory_arrays = get_memory_array_inventory(
                                                       handle, compute_board)
            compute_board_obj.storage_controllers = \
                get_storage_controller_inventory(handle, compute_board)
            compute_board_obj.pid_catalog_dimms = \
                get_pid_catalog_dimm_inventory(handle, compute_board)
            compute_board_obj.pid_catalog_pci_adapters = \
                get_pid_catalog_pci_adapter_inventory(handle, compute_board)
            compute_board_obj.bios_units = get_bios_unit_inventory(
                                                         handle, compute_board)
            compute_board_obj.temp_stats = get_temp_stat_inventory(
                                                         handle, compute_board)
            compute_board_obj.power_stats = get_power_stat_inventory(
                                                       handle, compute_board)

            compute_board_inventory.append(compute_board_obj)

    return compute_board_inventory


def get_processor_unit_inventory(handle, compute_board):
    """
    The method fetches processor unit inventory of a compute blade.

    Args:
        handle: ImcHandle
        compute_board: Managed Object

    Returns:
        Processor unit inventory.
    """

    processor_unit_inventory = []
    processor_units = handle.query_children(in_mo=compute_board,
                                            class_id="ProcessorUnit")
    if processor_units:
        for processor_unit in processor_units:
            processor_unit_obj = ProcessorUnitInventory(processor_unit)

            env_stats = handle.query_children(in_mo=processor_unit,
                                              class_id="ProcessorEnvStats")
            if env_stats:
                for env_stat in env_stats:
                    processor_unit_obj.sensor_description = env_stat.description
                    processor_unit_obj.temperature = env_stat.temperature

            processor_unit_inventory.append(processor_unit_obj)

    return processor_unit_inventory


def get_memory_array_inventory(handle, compute_board):
    """
    The method fetches memory array inventory of a compute board.

    Args:
        handle: ImcHandle
        compute_board: Managed Object

    Returns:
        Memory array Inventory.
    """
    memory_array_inventory = []
    memory_arrays = handle.query_children(in_mo=compute_board,
                                          class_id="MemoryArray")
    if memory_arrays:
        for memory_array in memory_arrays:
            memory_array_obj = MemoryArrayInventory(memory_array)
            memory_array_obj.memory_units = get_memory_unit_inventory(
                handle, memory_array)

            memory_array_inventory.append(memory_array_obj)

    return memory_array_inventory


def get_memory_unit_inventory(handle, memory_array):
    """
    The method fetches memory unit inventory.

    Args:
        handle: ImcHandle
        memory_array: Managed Object

    Returns:
        Inventory of Memory Unit.
    """

    memory_unit_inventory = []
    memory_units = handle.query_children(in_mo=memory_array,
                                         class_id="MemoryUnit")
    if memory_units:
        for memory_unit in memory_units:
            memory_unit_obj = MemoryUnitInventory(memory_unit)

            env_stats = handle.query_children(in_mo=memory_unit,
                                              class_id="MemoryUnitEnvStats")
            if env_stats:
                for env_stat in env_stats:
                    memory_unit_obj.sensor_description = env_stat.description
                    memory_unit_obj.temperature = env_stat.temperature

            memory_unit_inventory.append(memory_unit_obj)

    return memory_unit_inventory


def get_storage_controller_inventory(handle, compute_board):
    """
    The method fetches storage controller inventory of a compute blade.

    Args:
        handle: ImcHandle
        compute_board: Managed Object

    Returns:
        Invetory of storage controller.
    """
    storage_controller_inventory = []
    storage_controllers = handle.query_children(in_mo=compute_board,
                                                class_id="StorageController")
    if storage_controllers:
        for storage_controller in storage_controllers:
            storage_controller_obj = StorageControllerInventory(
                                                      storage_controller)

            firmware_running_info = handle.query_children(
                in_mo=storage_controller, class_id="FirmwareRunning")
            if firmware_running_info:
                for each_fr in firmware_running_info:
                    storage_controller_obj.firmware_deployment =\
                        each_fr.deployment
                    storage_controller_obj.firmware_version = each_fr.version

            storage_controller_obj.storage_local_disks = \
                get_storage_local_disk_inventory(handle, storage_controller)
            storage_controller_obj.storage_virtual_drives = \
                get_storage_virtual_drive_inventory(handle, storage_controller)

            storage_controller_inventory.append(storage_controller_obj)

    return storage_controller_inventory


def get_storage_local_disk_inventory(handle, storage_controller):
    """
    The method fetches local disk inventory of a storage controller.

    Args:
        handle: ImcHandle
        storage_controller: Managed Object

    Returns:
        Storage Local disk Inv Object
    """

    storage_local_disk_inventory = []
    storage_local_disks = handle.query_children(in_mo=storage_controller,
                                                class_id="StorageLocalDisk")
    if storage_local_disks:
        for storage_local_disk in storage_local_disks:
            storage_local_disk_obj = StorageLocalDiskInventory(
                                                            storage_local_disk)

            storage_local_disk_inventory.append(storage_local_disk_obj)

    return storage_local_disk_inventory


def get_storage_virtual_drive_inventory(handle, storage_controller):
    """
    The method fetches virtual drive inventory of a storage controller.

    Args:
        handle: ImcHandle
        storage_controller: Managed Object

    Returns:
        Storage Virtual Drive Inv Object
    """

    storage_virtual_drive_inventory = []
    storage_virtual_drives = handle.query_children(
        in_mo=storage_controller, class_id="StorageVirtualDrive")
    if storage_virtual_drives:
        for storage_virtual_drive in storage_virtual_drives:
            storage_virtual_drive_obj = StorageVirtualDriveInventory(
                                                      storage_virtual_drive)

            storage_virtual_drive_inventory.append(storage_virtual_drive_obj)

    return storage_virtual_drive_inventory


def get_pid_catalog_dimm_inventory(handle, compute_board):
    """
    The method fetches DIMM inventory of a compute board.

    Args:
        handle: ImcHandle
        compute_board: Managed Object

    Returns:
        DIMM invetory
    """

    pid_catalog_dimm_inventory = []
    pid_catalog_dimms = handle.query_children(in_mo=compute_board,
                                              class_id="PidCatalogDimm")
    if pid_catalog_dimms:
        for pid_catalog_dimm in pid_catalog_dimms:
            pid_catalog_dimm_obj = PidCatalogDimmInventory(pid_catalog_dimm)

            pid_catalog_dimm_inventory.append(pid_catalog_dimm_obj)

    return pid_catalog_dimm_inventory


def get_pid_catalog_pci_adapter_inventory(handle, compute_board):
    """
    The method fetches adapter inventory of a compute board.

    Args:
        handle: ImcHandle
        compute_board: Managed Object

    Returns:
        PCI adapter inventory
    """
    pid_catalog_pci_adapter_inventory = []
    pid_catalog_pci_adapters = handle.query_children(
        in_mo=compute_board, class_id="PidCatalogPCIAdapter")
    if pid_catalog_pci_adapters:
        for pid_catalog_pci_adapter in pid_catalog_pci_adapters:
            pid_catalog_pci_adapter_obj = PidCatalogPciAdapterInventory(
                                                    pid_catalog_pci_adapter)

            pid_catalog_pci_adapter_inventory.append(
                pid_catalog_pci_adapter_obj)

    return pid_catalog_pci_adapter_inventory


def get_bios_unit_inventory(handle, compute_board):
    """
    The method fetches bios info of a compute board.

    Args:
        handle: ImcHandle
        compute_board: Managed Object

    Returns:
        Object of Bios Inventory
    """
    bios_unit_inventory = []
    bios_units = handle.query_children(in_mo=compute_board,
                                       class_id="BiosUnit")
    if bios_units:
        for bios_unit in bios_units:
            bios_unit_obj = BiosUnitInventory(bios_unit)

            firmware_running_info = handle.query_children(
                in_mo=bios_unit, class_id="FirmwareRunning")
            if firmware_running_info:
                for each_fr in firmware_running_info:
                    bios_unit_obj.firmware_deployment = each_fr.deployment
                    bios_unit_obj.firmware_version = each_fr.version

            bios_unit_inventory.append(bios_unit_obj)

    return bios_unit_inventory


def get_temp_stat_inventory(handle, compute_board):
    """
    The method fetches temperature statistics of a compute board.

    Args:
        handle: ImcHandle
        compute_board: Managed Object

    Returns:
        Object of Temperature Stat
    """

    temp_stat_inventory = []
    temp_stats = handle.query_children(in_mo=compute_board,
                                       class_id="ComputeRackUnitMbTempStats")
    if temp_stats:
        for temp_stat in temp_stats:
            temp_stat_obj = TempStatInventory(temp_stat)

            temp_stat_inventory.append(temp_stat_obj)

    return temp_stat_inventory


def get_power_stat_inventory(handle, compute_board):
    """
    The method fetches power statistics of a compute board.

    Args:
        handle: ImcHandle
        compute_board: Managed Object

    Returns:
        Object of Power Stat
    """

    power_stat_inventory = []
    power_stats = handle.query_children(in_mo=compute_board,
                                        class_id="ComputeMbPowerStats")
    if power_stats:
        for power_stat in power_stats:
            power_stat_obj = PowerStatInventory(power_stat)

            power_stat_inventory.append(power_stat_obj)

    return power_stat_inventory


def obj_to_str(obj):
    """
    The method coverts the input object to printable string.

    Args:
        obj: Object to be converted to string

    Returns:
        string
    """

    tabsize = 8
    out_str = "\n"
    child_list = []

    out_str += "Managed Object\t\t\t: " + str(obj.class_id) + "\n"
    out_str += "-"*len("Managed Object") + "\n"

    for key in obj.__dict__.keys():
        if key == "class_id":
            continue

        val = obj.__dict__[key]
        if isinstance(val, list):
            child_list.append(key)
            continue

        out_str += str(key).ljust(tabsize*4) + ': ' + str(val) + "\n"

    for child in child_list:
        for child_obj in obj.__dict__[child]:
            out_str += obj_to_str(child_obj)

    out_str += "\n"
    return out_str
