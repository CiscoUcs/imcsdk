"""This module contains the general information for HuuFirmwareComponent ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class HuuFirmwareComponentConsts:
    pass


class HuuFirmwareComponent(ManagedObject):
    """This is HuuFirmwareComponent class."""

    consts = HuuFirmwareComponentConsts()
    naming_props = set(['component'])

    mo_meta = {
        "classic": MoMeta("HuuFirmwareComponent", "huuFirmwareComponent", "component-[component]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['huuFirmwareRunning'], [], ["Get"]),
        "modular": MoMeta("HuuFirmwareComponent", "huuFirmwareComponent", "component-[component]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['huuFirmwareRunning'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "cntrl_id": MoPropertyMeta("cntrl_id", "cntrlId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "component": MoPropertyMeta("component", "component", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "device_id": MoPropertyMeta("device_id", "deviceId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version154, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "mac_addr": MoPropertyMeta("mac_addr", "macAddr", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "running_version": MoPropertyMeta("running_version", "runningVersion", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "sub_device_id": MoPropertyMeta("sub_device_id", "subDeviceId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sub_vendor_id": MoPropertyMeta("sub_vendor_id", "subVendorId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor_id": MoPropertyMeta("vendor_id", "vendorId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "cntrl_id": MoPropertyMeta("cntrl_id", "cntrlId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "component": MoPropertyMeta("component", "component", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "device_id": MoPropertyMeta("device_id", "deviceId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "mac_addr": MoPropertyMeta("mac_addr", "macAddr", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "running_version": MoPropertyMeta("running_version", "runningVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "sub_device_id": MoPropertyMeta("sub_device_id", "subDeviceId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sub_vendor_id": MoPropertyMeta("sub_vendor_id", "subVendorId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor_id": MoPropertyMeta("vendor_id", "vendorId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "cntrlId": "cntrl_id", 
            "component": "component", 
            "description": "description", 
            "deviceId": "device_id", 
            "dn": "dn", 
            "id": "id", 
            "macAddr": "mac_addr", 
            "rn": "rn", 
            "runningVersion": "running_version", 
            "slot": "slot", 
            "status": "status", 
            "subDeviceId": "sub_device_id", 
            "subVendorId": "sub_vendor_id", 
            "vendorId": "vendor_id", 
        },

        "modular": {
            "childAction": "child_action", 
            "cntrlId": "cntrl_id", 
            "component": "component", 
            "description": "description", 
            "deviceId": "device_id", 
            "dn": "dn", 
            "id": "id", 
            "macAddr": "mac_addr", 
            "rn": "rn", 
            "runningVersion": "running_version", 
            "slot": "slot", 
            "status": "status", 
            "subDeviceId": "sub_device_id", 
            "subVendorId": "sub_vendor_id", 
            "vendorId": "vendor_id", 
        },

    }

    def __init__(self, parent_mo_or_dn, component, **kwargs):
        self._dirty_mask = 0
        self.component = component
        self.child_action = None
        self.cntrl_id = None
        self.description = None
        self.device_id = None
        self.id = None
        self.mac_addr = None
        self.running_version = None
        self.slot = None
        self.status = None
        self.sub_device_id = None
        self.sub_vendor_id = None
        self.vendor_id = None

        ManagedObject.__init__(self, "HuuFirmwareComponent", parent_mo_or_dn, **kwargs)

