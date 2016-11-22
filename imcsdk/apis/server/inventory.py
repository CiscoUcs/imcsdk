# Copyright 2016 Cisco Systems, Inc.
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
This module provides apis for inventory of the server
"""

import csv
import re
from imcsdk.imccoreutils import IMC_PLATFORM

INVENTORY_TXT_FILE = "inventory.txt"
INVENTORY_CSV_FILE = "inventory.csv"


def _extract_server_id_from_dn(handle, dn):
    if handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        return "1"

    if handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        match = re.search(r"server-([\d])/([\w]+)", dn)
        if match:
            return match.group(1)

    return "--"


def _get_rack_class_id(handle):
    from imcsdk.imcexception import ImcValidationException

    if handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        return("ComputeRackUnit")
    elif handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        return("ComputeServerNode")
    else:
        raise ImcValidationException("Invalid platform type:%s detected" %
                                     handle.platform)


def _write_to_txt_file(temp_str):
    with open(INVENTORY_TXT_FILE, "a") as file_handle:
        file_handle.write(temp_str)


def _get_rack_info_csv(handle):
    with open(INVENTORY_CSV_FILE, "a") as write_handle:
        fieldnames = ['Rack-Id', 'Vendor', 'Model', 'Serial', 'UUID']
        writer = csv.DictWriter(write_handle, fieldnames=fieldnames)
        writer.writeheader()

        racks = handle.query_classid(_get_rack_class_id(handle))
        for rack in racks:
            if rack.presence == "missing":
                continue
            writer.writerow({
                'Rack-Id': rack.server_id,
                'Vendor': rack.vendor,
                'Model': rack.model,
                'Serial': rack.serial,
                'UUID': rack.uuid
            })
        writer.writerow({})


def _get_rack_info_txt(handle):
    _write_to_txt_file("============= RACK-INFO =============\n")
    _write_to_txt_file(
        "RACK-ID  RACK-VENDOR              RACK-MODEL     RACK-SERIAL    "
        "RACK-UUID\n")

    racks = handle.query_classid(_get_rack_class_id(handle))
    for rack in racks:
        _write_to_txt_file(
            "  %s   %20.20s %20.20s      %10.10s     %30.30s\n" %
            (rack.server_id, rack.vendor, rack.model, rack.serial, rack.uuid))
    _write_to_txt_file("\n")


def _get_rack_info(handle, file_format):
    if file_format == "txt":
        _get_rack_info_txt(handle)
    elif file_format == "csv":
        _get_rack_info_csv(handle)


def _get_cpu_info_csv(handle):
    with open(INVENTORY_CSV_FILE, "a") as write_handle:
        fieldnames = [
            'Server-Id',
            'Cpu-Id',
            'Vendor',
            'Model',
            'Serial',
            'Speed',
            'Architecture',
            'Cores',
        ]
        writer = csv.DictWriter(write_handle, fieldnames=fieldnames)
        writer.writeheader()

        cpus = handle.query_classid("ProcessorUnit")
        for cpu in cpus:
            if cpu.presence == "missing":
                continue
            writer.writerow({
                'Server-Id': _extract_server_id_from_dn(handle, cpu.dn),
                'Cpu-Id': cpu.id,
                'Vendor': cpu.vendor,
                'Model': cpu.model,
                'Serial': 'N/A',
                'Speed': cpu.speed,
                'Architecture': cpu.arch,
                'Cores': cpu.cores
            })
        writer.writerow({})


def _get_cpu_info_txt(handle):
    _write_to_txt_file("============= CPU-INFO =============\n")
    _write_to_txt_file(
        "CPU-ID   CPU-ARCH   CPU-VENDOR                  CPU-MODEL\n")

    cpus = handle.query_classid("ProcessorUnit")
    for cpu in cpus:
        if cpu.presence == "missing":
            continue
        _write_to_txt_file(
            "  %s %10.10s      %20.20s        %30.30s\n" %
            (cpu.id, cpu.arch, cpu.vendor, cpu.model))
    _write_to_txt_file("\n")


def _get_cpu_info(handle, file_format):
    if file_format == "txt":
        _get_cpu_info_txt(handle)
    elif file_format == "csv":
        _get_cpu_info_csv(handle)


def _get_mem_info_csv(handle):
    with open(INVENTORY_CSV_FILE, "a") as write_handle:
        fieldnames = [
            'Server-Id',
            'Dimm-Id',
            'Vendor',
            'Model',
            'Serial',
            'Speed',
            'Capacity']
        writer = csv.DictWriter(write_handle, fieldnames=fieldnames)
        writer.writeheader()

        dimms = handle.query_classid("MemoryUnit")
        for dimm in dimms:
            if dimm.presence == "missing":
                continue
            writer.writerow({
                'Server-Id': _extract_server_id_from_dn(handle, dimm.dn),
                'Dimm-Id': dimm.id,
                'Vendor': dimm.vendor,
                'Model': dimm.model,
                'Serial': dimm.serial,
                'Speed': dimm.clock,
                'Capacity': dimm.capacity
            })
        writer.writerow({})


def _get_mem_info_txt(handle):
    _write_to_txt_file("============= DIMM-INFO =============\n")
    _write_to_txt_file(
        "DIMM-ID Capacity Speed Vendor       Model          Serial")

    dimms = handle.query_classid("MemoryUnit")
    for dimm in dimms:
        if dimm.presence == "missing":
            continue
        _write_to_txt_file(
            "  %s      %.8s    %.5s  %.5s   %.20s %.10s" %
            (dimm.id, dimm.capacity, dimm.clock,
             dimm.vendor, dimm.model, dimm.serial)
        )


def _get_mem_info(handle, file_format):
    if file_format == "txt":
        _get_mem_info_txt(handle)
    elif file_format == "csv":
        _get_mem_info_csv(handle)


def _get_psu_info_csv(handle):
    with open(INVENTORY_CSV_FILE, "a") as write_handle:
        fieldnames = ['Psu-Id', 'Vendor', 'Model', 'Serial', 'FW-version']
        writer = csv.DictWriter(write_handle, fieldnames=fieldnames)
        writer.writeheader()

        psus = handle.query_classid("EquipmentPsu")
        for psu in psus:
            if psu.presence == "missing":
                continue
            writer.writerow({
                'Psu-Id': psu.id,
                'Vendor': psu.vendor,
                'Model': psu.model,
                'Serial': psu.serial,
                'FW-version': psu.fw_version
            })
        writer.writerow({})


def _get_psu_info_txt(handle):
    _write_to_txt_file("============= PSU-INFO =============\n")
    _write_to_txt_file(
        "PSU-ID PSU-PRESENCE    PSU-VENDOR           PSU-MODEL\n")

    psus = handle.query_classid("EquipmentPsu")
    for psu in psus:
        if psu.presence == "missing":
            continue
        _write_to_txt_file(
            "  %s    %.10s        %.20s    %.20ss\n" %
            (psu.id, psu.presence, psu.vendor, psu.model))
    _write_to_txt_file("\n")


def _get_psu_info(handle, file_format):
    if file_format == "txt":
        _get_psu_info_txt(handle)
    elif file_format == "csv":
        _get_psu_info_csv(handle)


def _get_pci_info_csv(handle):
    with open(INVENTORY_CSV_FILE, "a") as write_handle:
        fieldnames = ['Server-Id', 'Pci-Id', 'Vendor', 'Model', 'FW-version']
        writer = csv.DictWriter(write_handle, fieldnames=fieldnames)
        writer.writeheader()

        pci_devices = handle.query_classid("PciEquipSlot")
        for device in pci_devices:
            writer.writerow({
                'Server-Id': _extract_server_id_from_dn(handle, device.dn),
                'Pci-Id': device.id,
                'Vendor': device.vendor,
                'Model': device.model,
                'FW-version': device.version
            })
        writer.writerow({})


def _get_pci_info_txt(handle):

    _write_to_txt_file("============= PCI-INFO =============\n")
    _write_to_txt_file(
        "PCI-ID VENDOR       MODEL                                   "
        "FW-VERSION\n")

    pci_devices = handle.query_classid("PciEquipSlot")
    for device in pci_devices:
        _write_to_txt_file(
            "%.5s      %.20s   %.40s     %.10s\n" %
            (device.id, device.vendor, device.model, device.version))
    _write_to_txt_file("\n")


def _get_pci_info(handle, file_format):
    if file_format == "txt":
        _get_pci_info_txt(handle)
    elif file_format == "csv":
        _get_pci_info_csv(handle)


def _get_vic_info_csv(handle):
    with open(INVENTORY_CSV_FILE, "a") as write_handle:
        fieldnames = ['Server-Id', 'Adaptor-Id', 'Vendor',
                      'Model', 'Serial', 'PCI-Slot']
        writer = csv.DictWriter(write_handle, fieldnames=fieldnames)
        writer.writeheader()

        adaptors = handle.query_classid("AdaptorUnit")
        for adaptor in adaptors:
            writer.writerow({
                'Server-Id': _extract_server_id_from_dn(handle, adaptor.dn),
                'Adaptor-Id': adaptor.id,
                'Vendor': adaptor.vendor,
                'Model': adaptor.model,
                'Serial': adaptor.serial,
                'PCI-Slot': adaptor.pci_slot
            })
        writer.writerow({})


def _get_vic_info_txt(handle):
    _write_to_txt_file("============= VIC-INFO =============\n")
    _write_to_txt_file(
        "ADAPTOR-ID  VENDOR              MODEL               PCI-SLOT\n")

    adaptors = handle.query_classid("AdaptorUnit")
    for adaptor in adaptors:
        _write_to_txt_file(
            "  %s         %.20s   %.20s     %.5s\n" %
            (adaptor.id, adaptor.vendor, adaptor.model, adaptor.pci_slot))
    _write_to_txt_file("\n")


def _get_vic_info(handle, file_format):
    if file_format == "txt":
        _get_vic_info_txt(handle)
    elif file_format == "csv":
        _get_vic_info_csv(handle)


def _get_lom_info_csv(handle):
    with open(INVENTORY_CSV_FILE, "a") as write_handle:
        fieldnames = ['Server-Id', 'LOM-Adaptor-Id',
                      'Model', 'PCI-Slot', 'No. Interfaces']
        writer = csv.DictWriter(write_handle, fieldnames=fieldnames)
        writer.writeheader()

        adaptors = handle.query_classid("NetworkAdapterUnit")
        ctr = 1
        for adaptor in adaptors:
            writer.writerow({
                'Server-Id': _extract_server_id_from_dn(handle, adaptor.dn),
                'LOM-Adaptor-Id': str(ctr),
                'Model': adaptor.model,
                'PCI-Slot': adaptor.slot,
                'No. Interfaces': adaptor.num_intf
            })
            ctr += 1
        writer.writerow({})


def _get_lom_info_txt(handle):
    _write_to_txt_file("============= NETWORK-ADAPTOR-INFO =============\n")
    _write_to_txt_file(
        "LOM-ADAPTOR-ID       MODEL             PCI-SLOT   #INTERFACES\n")

    adaptors = handle.query_classid("NetworkAdapterUnit")
    ctr = 1
    for adaptor in adaptors:
        _write_to_txt_file(
            "  %s          %.20s      %.5s         %.5s\n" %
            (str(ctr), adaptor.model, adaptor.slot, adaptor.num_intf))
        ctr += 1
    _write_to_txt_file("\n")


def _get_lom_info(handle, file_format):
    if file_format == "txt":
        _get_lom_info_txt(handle)
    elif file_format == "csv":
        _get_lom_info_csv(handle)


def _get_storage_info_csv(handle):
    with open(INVENTORY_CSV_FILE, "a") as write_handle:
        fieldnames = [
            'Server-Id',
            'Controller-Id',
            'Type',
            'Vendor',
            'Model',
            'Serial',
            'PCI-Slot',
            'Firmware']
        writer = csv.DictWriter(write_handle, fieldnames=fieldnames)
        writer.writeheader()

        controllers = handle.query_classid("StorageController")
        ctr = 1
        for controller in controllers:
            prop = handle.query_children(in_dn=controller.dn,
                                         class_id="StorageControllerProps")
            writer.writerow({
                'Server-Id': _extract_server_id_from_dn(handle, controller.dn),
                'Controller-Id': str(ctr),
                'Type': controller.type,
                'Vendor': controller.vendor,
                'Model': controller.model,
                'Serial': controller.serial,
                'PCI-Slot': controller.pci_slot,
                'Firmware': prop[0].firmware_package_build
            })
            ctr += 1

        flex_controllers = handle.query_classid("StorageFlexFlashController")
        for controller in flex_controllers:
            writer.writerow({
                'Server-Id': _extract_server_id_from_dn(handle, controller.dn),
                'Controller-Id': str(ctr),
                'Type': controller.product_name,
                'Vendor': controller.vendor,
                'Model': "N/A",
                'Serial': "N/A",
                'PCI-Slot': "N/A",
                'Firmware': controller.fw_version
            })
            ctr += 1
        writer.writerow({})


def _get_storage_info_txt(handle):
    _write_to_txt_file("============= STORAGE-CONTROLLER-INFO =============\n")
    _write_to_txt_file(
        "ID      TYPE            VENDOR        MODEL               "
        "SERIAL     PCI-SLOT   FIRMWARE\n")

    controllers = handle.query_classid("StorageController")
    ctr = 1
    for controller in controllers:
        prop = handle.query_children(
            in_dn=controller.dn,
            class_id="StorageControllerProps")
        _write_to_txt_file(
            " %s      %.10s        %.10s   "
            "%.30s     %.10s   %.5s     %.10s\n" %
            (str(ctr),
             controller.type,
             controller.vendor,
             controller.model,
             controller.serial,
             controller.pci_slot,
             prop[0].firmware_package_build))
        ctr += 1

    flex_controllers = handle.query_classid("StorageFlexFlashController")
    for controller in flex_controllers:
        _write_to_txt_file(
            " %s      %.10s     %.10s   %.30s"
            "     %.10s   %.5s        %.10s\n" %
            (str(ctr),
             controller.product_name,
             controller.vendor,
             "N/A",
             "N/A",
             "N/A",
             controller.fw_version))
        ctr += 1
    _write_to_txt_file("\n")


def _get_storage_info(handle, file_format):
    if file_format == "txt":
        _get_storage_info_txt(handle)
    elif file_format == "csv":
        _get_storage_info_csv(handle)


def _get_tpm_info_csv(handle):
    with open(INVENTORY_CSV_FILE, "a") as write_handle:
        fieldnames = ['Server-Id', 'Tpm-Id', 'Vendor',
                      'Model', 'Serial', 'Revision']
        writer = csv.DictWriter(write_handle, fieldnames=fieldnames)
        writer.writeheader()

        tpms = handle.query_classid("EquipmentTpm")
        ctr = 1
        for tpm in tpms:
            if tpm.presence in ['missing', 'empty']:
                continue
            writer.writerow({
                'Server-Id': _extract_server_id_from_dn(handle, tpm.dn),
                'Tpm-Id': str(ctr),
                'Vendor': tpm.vendor,
                'Model': tpm.model,
                'Serial': tpm.serial,
                'Revision': tpm.tpm_revision,
            })
            ctr += 1
        writer.writerow({})


def _get_tpm_info_txt(handle):
    _write_to_txt_file("============= NETWORK-ADAPTOR-INFO =============\n")
    _write_to_txt_file("TPM-ID \tVENDOR \tMODEL \tSERIAL \tREVISION\n")

    tpms = handle.query_classid("EquipmentTpm")
    ctr = 1
    for tpm in tpms:
        if tpm.presence in ['missing', 'empty']:
            continue
        _write_to_txt_file(
            "  %s \t%s \t%s \t%s \t%s\n" %
            (str(ctr), tpm.vendor, tpm.model, tpm.serial, tpm.tpm_revision))
        ctr += 1
    _write_to_txt_file("\n")


def _get_tpm_info(handle, file_format):
    if file_format == "txt":
        _get_tpm_info_txt(handle)
    elif file_format == "csv":
        _get_tpm_info_csv(handle)


def _delete_inventory_files(file_format):
    import os

    if file_format == "txt" or file_format == "csv":
        file_name = "INVENTORY_" + file_format.upper() + "_FILE"
    else:
        return

    if os.path.exists(file_name):
        os.remove(file_name)


def get_inventory(handle, types="all", file_format="csv"):
    """
    This method fetches the inventory of the server for various
    items like cpus, memory, psu or the entire server

    Args:
        handle (ImcHandle)
        types (string): comma separated values for the parts like
            "cpu, memory, psu, pci, vic, lom, storage, tpm" or "all"
        file_format (string): "txt", "csv"

    Returns:
        Inventory in the format specified via format field
    """

    callback_dict = {
        'rack': _get_rack_info,
        'cpu': _get_cpu_info,
        'memory': _get_mem_info,
        'psu': _get_psu_info,
        'pci': _get_pci_info,
        'vic': _get_vic_info,
        'lom': _get_lom_info,
        'storage': _get_storage_info,
        'tpm': _get_tpm_info
    }

    _delete_inventory_files(file_format)

    if types == "all":
        item_list = [
            "rack",
            "cpu",
            "memory",
            "psu",
            "pci",
            "vic",
            "lom",
            "storage",
            "tpm"]
    else:
        item_list = types.split(",")

    for item in item_list:
        try:
            callback_dict[item](handle, file_format)
        except KeyError:
            print('Unknown type \'%s\' found' % item)
            print('Valid types for inventory are :-')
            print(callback_dict.keys())
