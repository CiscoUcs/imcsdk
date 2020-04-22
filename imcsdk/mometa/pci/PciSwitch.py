"""This module contains the general information for PciSwitch ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PciSwitchConsts:
    pass


class PciSwitch(ManagedObject):
    """This is PciSwitch class."""

    consts = PciSwitchConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("PciSwitch", "pciSwitch", "pci-switch-[id]", VersionMeta.Version402c, "OutputOnly", 0xf, [], ["read-only"], ['computeBoard'], ['faultInst', 'pciLink'], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version402c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "device_id": MoPropertyMeta("device_id", "deviceId", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version402c, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "manufacturer": MoPropertyMeta("manufacturer", "manufacturer", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "num_of_adaptors": MoPropertyMeta("num_of_adaptors", "numOfAdaptors", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_revision": MoPropertyMeta("product_revision", "productRevision", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "sub_device_id": MoPropertyMeta("sub_device_id", "subDeviceId", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sub_vendor_id": MoPropertyMeta("sub_vendor_id", "subVendorId", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "temperature": MoPropertyMeta("temperature", "temperature", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor_id": MoPropertyMeta("vendor_id", "vendorId", "string", VersionMeta.Version402c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "deviceId": "device_id", 
            "dn": "dn", 
            "health": "health", 
            "id": "id", 
            "manufacturer": "manufacturer", 
            "numOfAdaptors": "num_of_adaptors", 
            "productName": "product_name", 
            "productRevision": "product_revision", 
            "rn": "rn", 
            "slot": "slot", 
            "status": "status", 
            "subDeviceId": "sub_device_id", 
            "subVendorId": "sub_vendor_id", 
            "temperature": "temperature", 
            "type": "type", 
            "vendorId": "vendor_id", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.device_id = None
        self.health = None
        self.manufacturer = None
        self.num_of_adaptors = None
        self.product_name = None
        self.product_revision = None
        self.slot = None
        self.status = None
        self.sub_device_id = None
        self.sub_vendor_id = None
        self.temperature = None
        self.type = None
        self.vendor_id = None

        ManagedObject.__init__(self, "PciSwitch", parent_mo_or_dn, **kwargs)

