"""This module contains the general information for PciAdapterFruInventory ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PciAdapterFruInventoryConsts:
    pass


class PciAdapterFruInventory(ManagedObject):
    """This is PciAdapterFruInventory class."""

    consts = PciAdapterFruInventoryConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("PciAdapterFruInventory", "pciAdapterFruInventory", "pci-adapter-fru-[id]", VersionMeta.Version422a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['computeRackUnit'], ['pciAdapterFruInventoryInfo', 'pciAdapterPortStatus', 'pciAdapterTemperature'], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version422a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "device_id": MoPropertyMeta("device_id", "deviceId", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "fw_version": MoPropertyMeta("fw_version", "fwVersion", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "manufacturer": MoPropertyMeta("manufacturer", "manufacturer", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "part_number": MoPropertyMeta("part_number", "partNumber", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], []),
            "pci_link_speed": MoPropertyMeta("pci_link_speed", "pciLinkSpeed", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "serial_number": MoPropertyMeta("serial_number", "serialNumber", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "sub_device_id": MoPropertyMeta("sub_device_id", "subDeviceId", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sub_vendor_id": MoPropertyMeta("sub_vendor_id", "subVendorId", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor_id": MoPropertyMeta("vendor_id", "vendorId", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "description": "description", 
            "deviceId": "device_id", 
            "dn": "dn", 
            "fwVersion": "fw_version", 
            "id": "id", 
            "manufacturer": "manufacturer", 
            "name": "name", 
            "partNumber": "part_number", 
            "pciLinkSpeed": "pci_link_speed", 
            "rn": "rn", 
            "serialNumber": "serial_number", 
            "status": "status", 
            "subDeviceId": "sub_device_id", 
            "subVendorId": "sub_vendor_id", 
            "vendor": "vendor", 
            "vendorId": "vendor_id", 
            "version": "version", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.description = None
        self.device_id = None
        self.fw_version = None
        self.manufacturer = None
        self.name = None
        self.part_number = None
        self.pci_link_speed = None
        self.serial_number = None
        self.status = None
        self.sub_device_id = None
        self.sub_vendor_id = None
        self.vendor = None
        self.vendor_id = None
        self.version = None

        ManagedObject.__init__(self, "PciAdapterFruInventory", parent_mo_or_dn, **kwargs)

