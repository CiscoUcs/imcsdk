# Copyright 2019 Cisco Systems, Inc.
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
This module provides APIs for configuring PXE device under precison boot order
"""

import logging
import re

import imcsdk.imccoreutils as imccoreutils
import imcsdk.imcgenutils as imcgenutils
from imcsdk.imcexception import ImcOperationError, ImcOperationErrorDetail
from imcsdk.mometa.lsboot.LsbootDevPrecision import LsbootDevPrecision

log = logging.getLogger('imc')

PXE_DELIMITER = "~~~"
PXE_API_ERROR = "Cannot configure PXE device."


class PxeBootDevice(object):
    def __init__(self):
        self.boot_device = None
        self.slot = None
        self.vnic_name = None
        self.order = None
        self.pci_link = None
        self.port = None


def _filter_pxe_device(boot_devices):
    # filter pxe devices out of boot devices to be configured
    pxe_devices = [device for device in boot_devices
                   if device['device-type'] == 'pxe']
    return pxe_devices


def _remove_pxe_with_mac_for_m4(handle, pxe_devices):
    from imcsdk.imccoreutils import is_platform_m4

    if not is_platform_m4(handle):
        return pxe_devices
    return [device for device in pxe_devices if device['interface_source'] != 'mac']


def _parse_pxe_devices(devices):
    #  segregate devices on the basis of interface source
    #  slot_interface_map (dict)
    #  key: slot + "~~~" + interface_name
    #  value: boot device
    #
    #  mac_address_map (dict)
    #  key: mac address
    #  value: boot device
    #
    #  slot_port_map (dict)
    #  key: slot/slot + "~~~" + port
    #  value: boot device

    log.debug("Parsing PXE Devices.")
    slot_interface_map = {}
    mac_address_map = {}
    slot_port_map = {}

    for device in devices:
        log.debug(device)
        slot = device.get('slot', None)
        if slot is None or slot == "":
            device.pop('slot', None)

        interface_source = device.get('interface_source', None)
        if interface_source is None:
            raise ImcOperationError(PXE_API_ERROR,
                                    "Interface source is required.")
        if interface_source not in ('name', 'mac', 'port'):
            raise ImcOperationError(
                PXE_API_ERROR,
                "Interface source is incorrect. Correct values are \
                ['name', 'mac', 'port'].")


        if interface_source == "name":
            # find the interface using given slot and interface name
            # enable pxe boot on respective interface
            # derive logical port for the respective interface
            # update respective boot device with port
            # send slot and port to end point
            #
            # if slot or interface does not exist on endpoint throw an error

            # remove port and mac_address from the device
            device.pop('port', None)
            device.pop('mac_address', None)

            # slot is mandatory
            if not slot:
                raise ImcOperationError(PXE_API_ERROR,
                                        "Slot is required")

            interface_name = device.get('interface_name', None)
            if not interface_name:
                raise ImcOperationError(PXE_API_ERROR,
                                        "Interface name is required")

            slot_interface_name = slot + PXE_DELIMITER + interface_name

            # check if duplicate entry of slot + interface combination
            if slot_interface_name in slot_interface_map:
                continue
            slot_interface_map[slot_interface_name] = device
        elif interface_source == "mac":
            # find the interface using mac address
            # enable the pxe boot on the respective interface
            # send only mac_address to the end point
            # mac_address only present in M5 server

            # remove  port and interface_name
            device.pop('port', None)
            device.pop('interface_name', None)

            mac_address = device.get('mac_address', None)
            if not mac_address:
                raise ImcOperationError(PXE_API_ERROR,
                                        "MAC address is required")
            mac_address_map[mac_address] = device
        elif interface_source == "port":
            # if interface source is port then it is considered as non-vic adapter
            # enable the pxe boot on the respective slot/slot+port

            # remove interface_name and mac_address
            device.pop('interface_name', None)
            device.pop('mac_address', None)

            if not slot:
                raise ImcOperationError(PXE_API_ERROR,
                                        "Slot is required")

            port = device.get('port', None)
            if port is None:
                slot_port_name = slot
            else:
                slot_port_name = slot + PXE_DELIMITER + str(port)    
            
            if slot_port_name in slot_port_map:
                continue
            slot_port_map[slot_port_name] = device

    return slot_interface_map, mac_address_map, slot_port_map


def _get_all_ep_vnics(handle):
    # fetches all eth interfaces from end point
    vnics = handle.query_classid(class_id="AdaptorHostEthIf")
    if vnics is None:
        return []
    return vnics


def _parse_all_ep_vnics(ep_vnics):
    ep_slot_vnicname_map = {}
    ep_mac_map = {}
    pattern = re.compile(r'^sys/rack-unit-1/adaptor-(?P<slot>.*)/host-eth-(?P<vnicname>.*)$')
    for ep_vnic in ep_vnics:
        # update ep_slot_vnicname_map
        match = re.search(pattern, ep_vnic.dn)
        if not match:
            raise ImcOperationError(PXE_API_ERROR,
                                    "Invalid Interface.")
        slot = match.groupdict()['slot']
        vnicname = match.groupdict()['vnicname']
        slot_vnicname = slot + PXE_DELIMITER + vnicname
        ep_slot_vnicname_map[slot_vnicname] = ep_vnic

        # update ep_mac_map
        ep_mac_map[ep_vnic.mac] = ep_vnic

    return ep_slot_vnicname_map, ep_mac_map


def _enable_pxe_boot_vnic(handle, slot_vnicname_map, ep_slot_vnicname_map):
    # if pxe device with slot and vnicname matches endpoint vnic
    # then enable pxe boot for resp vnic

    log.debug("enabling pxe boot on vnics using slot and vnicname")

    vnics_to_configure = []

    # iterate through pxe device with source interace_name
    # if available at end point, enable the pxe boot for resp vnic
    # if not available, throw warning not error out

    missing_vnic_str = ""
    for slot_vnicname in slot_vnicname_map:
        if slot_vnicname not in ep_slot_vnicname_map:
            device = slot_vnicname_map[slot_vnicname]
            err_str = "PXE device at order '%s' has interface missing with slot '%s' and name '%s' on server." %(device['order'], device['slot'], device['interface_name'])
            if missing_vnic_str:
                missing_vnic_str += "\n"
            missing_vnic_str += err_str
            continue
        if missing_vnic_str:
            continue
        vnic = ep_slot_vnicname_map[slot_vnicname]
        vnic.pxe_boot = "enabled"
        vnics_to_configure.append(vnic)

    if missing_vnic_str:
        log.debug(missing_vnic_str)
        raise ImcOperationError(PXE_API_ERROR,
                                missing_vnic_str)

    handle.set_mos(vnics_to_configure)
    # to do handle response of set mos
    # ignore exception if vnic is not found at end point
    # or should we skip the pxe device from boot policy?


def _enable_pxe_boot_mac(handle, mac_address_map, ep_mac_map):
    # if pxe device mac address matches endpoint vnic
    # then enable pxe boot for resp vnic

    log.debug("enabling pxe boot on vnics using mac address")
    vnics_to_configure = []

    # iterate through pxe device with source mac address
    # if available at end point, enable the pxe boot for resp vnic
    #
    # skip if resepctive interface does not exist at end point

    # iterate through end point mac to form a end point available slot map
    ep_slot_map = {}
    pattern = re.compile(r'^sys/rack-unit-1/adaptor-(?P<slot>.*)/host-eth-(?P<vnicname>.*)$')
    for mac in ep_mac_map:
        match = re.search(pattern, ep_mac_map[mac].dn)
        if not match:
            raise ImcOperationError(PXE_API_ERROR,
                                        "Invalid Interface.")
        
        slotEp = match.groupdict()['slot']
        if slotEp in ep_slot_map:
            continue
        ep_slot_map[slotEp] = mac

    # if slot is not given in the pxe device enable pxe with respective mac address
    # if slot is given in the pxe device check whether it is present on the end point
    # if slot is present on the end point check whether mac is present on the endpoint if present enable pxe on the respective vnic
    # if slot is present on the end point check whether mac is present on the endpoint if not present return an error
    # 
    # if slot is not present on the end point consider it as non-vic adapter and enable pxe
    missing_mac_str = ""
    for mac in mac_address_map:
        slot = mac_address_map[mac].get('slot', None)
        # if slot is not given in the pxe device and if mac address not present on the end point, then enable pxe with provided mac considering non-vic adapter
        if slot is None or slot =="":
            if mac not in ep_mac_map:
                continue
        else:
            # if slot is given in the pxe device and not present on the end point, then enable pxe with provided mac considering non-vic adapter
            if slot not in ep_slot_map:
                continue
            else:
                # if slot is given in the pxe device and present on the end point but mac is not present on the endpoint then throw an error since it is a vic adpater
                if mac not in ep_mac_map:
                    device = mac_address_map[mac]
                    err_str = "PXE device at order '%s' has interface missing with MAC address '%s' on server." %(device['order'], device['mac_address'])
                    if missing_mac_str:
                        missing_mac_str += "\n"
                    missing_mac_str += err_str
        if missing_mac_str:
            continue
        
        vnic = ep_mac_map[mac]
        vnic.pxe_boot = "enabled"
        vnics_to_configure.append(vnic)

    if missing_mac_str:
        raise ImcOperationError(PXE_API_ERROR,
                                missing_mac_str)

    handle.set_mos(vnics_to_configure)
    # to do handle set_mos response


def _enable_pxe_boot(handle, slot_vnicname_map, mac_address_map):
    # fetch all vnics from end point
    ep_vnics = _get_all_ep_vnics(handle)

    # parse all end point vnics to create slot_vnicname and mac map
    # of end point vnics
    ep_slot_vnicname_map, ep_mac_map = _parse_all_ep_vnics(ep_vnics)

    if len(slot_vnicname_map) > 0:
        log.debug("PXE Devices with source name:\n%s" % slot_vnicname_map)
        _enable_pxe_boot_vnic(handle, slot_vnicname_map, ep_slot_vnicname_map)

    if len(mac_address_map) > 0:
        log.debug("PXE Devices with source MAC address:\n%s" % mac_address_map)
        _enable_pxe_boot_mac(handle, mac_address_map, ep_mac_map)


def _parse_vnic_gen_profiles(handle):
    # slot_vnicname_map (dict)
    # key: slot~~~vnicname
    # value: PxeBootDevice Instance
    slot_vnicname_map = {}

    egps = handle.query_classid(class_id="AdaptorEthGenProfile")
    if egps is None:
        egps = []

    pattern = re.compile(r'^sys/rack-unit-1/adaptor-(?P<slot>.*)/host-eth-(?P<vnicname>.*)/general$')
    for egp in egps:
        match = re.search(pattern, egp.dn)
        if not match:
            raise ImcOperationError(PXE_API_ERROR,
                                    "Invalid Interface.")
        slot = match.groupdict()['slot']
        vnicname = match.groupdict()['vnicname']

        key = slot + PXE_DELIMITER + vnicname
        if key not in slot_vnicname_map:
            slot_vnicname_map[key] = PxeBootDevice()

        pxe_bd = slot_vnicname_map[key]
        pxe_bd.slot = slot
        pxe_bd.interface_name = vnicname
        pxe_bd.pci_link = int(egp.pci_link)

        # adds check to raise error if interface order is 'any'.
        # specific to M4
        # if egp.order.lower() == "any":
        #    raise ImcOperationError(PXE_API_ERROR,
        #                            "Interface '%s' on slot '%s' with order value 'ANY' is not supported. "\
        #                            "Configure order with numberic value." % (vnicname, slot))
        pxe_bd.order = egp.order

    return slot_vnicname_map


def _get_bootable_slot_vnicname(handle):
    # get all the end point vnics
    vnics = handle.query_classid(class_id="AdaptorHostEthIf")
    if vnics is None:
        vnics = []

    # filter bootable vnics
    # bootable_vnics (list of slot~~~vnicname)
    bootable_vnics = []
    pattern = re.compile(r'^sys/rack-unit-1/adaptor-(?P<slot>.*)/host-eth-(?P<vnicname>.*)$')
    for vnic in vnics:
        if vnic.pxe_boot.lower() != "enabled":
            continue
        match = re.search(pattern, vnic.dn)
        if not match:
            raise ImcOperationError(PXE_API_ERROR,
                                    "Invalid Interface.")
        slot_vnicname_dict = match.groupdict()
        slot = match.groupdict()['slot']
        vnicname = match.groupdict()['vnicname']
        bootable_vnics.append(slot + PXE_DELIMITER + vnicname)

    return bootable_vnics

def _derive_logical_port(handle, affected_slots):
    # fetch the pcilink and order of all vnics at end point
    # slot_vnicname_map (dict)
    # key: slot~~~vnicname
    # value: PxeBootDevice Instance
    slot_vnicname_map = _parse_vnic_gen_profiles(handle)

    # get all bootable vnics from endpoint
    # bootable_vnics (list of slot~~~vnicname)
    bootable_slot_vnicname_list = _get_bootable_slot_vnicname(handle)

    # filter slot_vnicname_map for bootable vnic
    # bootable_slot_vnicname_map (dict)
    # key: slot~~~vnicname
    # value: PxeBootDevice Instance
    bootable_slot_vnicname_map = {}
    for bootable_slot_vnicname in bootable_slot_vnicname_list:
        bootable_slot_vnicname_map[bootable_slot_vnicname] = \
            slot_vnicname_map[bootable_slot_vnicname]

    log.debug("Bootable Interfaces on all slots.....")
    for k in bootable_slot_vnicname_map:
        log.debug("%s, %s" %(k, bootable_slot_vnicname_map[k].__dict__))

    # segregate all bootable vnics per slot
    per_slot_map = {}
    for pxe_bd in bootable_slot_vnicname_map.values():
        slot = pxe_bd.slot
        vnicname = pxe_bd.interface_name
        if slot not in affected_slots:
            continue

        if pxe_bd.order.lower() == "any":
           raise ImcOperationError(PXE_API_ERROR,
                                   "Interface '%s' on slot '%s' with order value 'ANY' is not supported. "\
                                   "Configure order with numeric value." % (vnicname, slot))

        if slot not in per_slot_map:
            per_slot_map[slot] = []
        per_slot_map[slot].append(pxe_bd)

    # sort  vnics per slot by pcilink then order
    # slot_vnicname_port_map (dict)
    # key: slot~~~vnicname
    # value: PXEBootDevice Instance with port
    slot_vnicname_port_map = {}
    for slot, pxe_bds in per_slot_map.items():
        sorted_pxe_bds = sorted(pxe_bds, key=lambda i: (i.pci_link, int(i.order)))
        for index, pxe_bd in enumerate(sorted_pxe_bds):
            pxe_bd.port = str(index)
            slot_vnicname = pxe_bd.slot + PXE_DELIMITER + pxe_bd.interface_name
            slot_vnicname_port_map[slot_vnicname] = pxe_bd

    return slot_vnicname_port_map


def prepare_pxe_devices(handle, boot_devices):

    # filter pxe devices
    pxe_devices = _filter_pxe_device(boot_devices)
    if len(pxe_devices) == 0:
        log.debug("No PXE device to configure.")
        return
    log.debug("PXE Devices:\n")
    log.debug(pxe_devices)
    log.debug("\n")

    # remove pxe device with mac address for M4
    pxe_devices = _remove_pxe_with_mac_for_m4(handle, pxe_devices)

    # parse pxe devices
    # on the basis of interface source
    slot_vnicname_map, mac_address_map, slot_port_map = _parse_pxe_devices(pxe_devices)
    if len(slot_vnicname_map) == 0 and len(mac_address_map) == 0 and len(slot_port_map):
        log.debug("No PXE device with source as Interface name or MAC Address or Port.")
        return

    # enable pxe boot on respective vnics
    _enable_pxe_boot(handle, slot_vnicname_map, mac_address_map)

    # derive port for a pxe device which has slot and interface name
    if len(slot_vnicname_map) == 0:
        return

    affected_slots = [ slot_vnicname.split(PXE_DELIMITER)[0] for slot_vnicname in slot_vnicname_map]
    # slot_vnicname_port_map (dict)
    # key: slot~~~vnicname
    # value: PXEBootDevice Instance with port
    slot_vnicname_port_map = _derive_logical_port(handle, affected_slots)

    # update port in actual pxe boot device
    log.debug("Updated PXE device:")
    for slot_vnicname, device in slot_vnicname_map.items():
        device['port'] = slot_vnicname_port_map[slot_vnicname].port
        device.pop('interface_name', None)
        log.debug(device)


def disable_pxeboot_vnics_all(handle):
    ep_vnics = _get_all_ep_vnics(handle)
    disable_vnics = []
    for vnic in ep_vnics:
        if vnic.pxe_boot == "enabled":
            vnic.pxe_boot = "disabled"
            disable_vnics.append(vnic)

    if disable_vnics:
        log.debug("Disabling bootable vnics.")
        handle.set_mos(disable_vnics)


