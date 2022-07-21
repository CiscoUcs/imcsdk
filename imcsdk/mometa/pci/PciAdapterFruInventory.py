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
        "classic": MoMeta("PciAdapterFruInventory", "pciAdapterFruInventory", "pci-adapter-fru-[id]", VersionMeta.Version422a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['computeRackUnit'], ['pciAdapterFruInventoryInfo'], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version422a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "device_id": MoPropertyMeta("device_id", "deviceId", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "sub_device_id": MoPropertyMeta("sub_device_id", "subDeviceId", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "sub_vendor_id": MoPropertyMeta("sub_vendor_id", "subVendorId", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor_id": MoPropertyMeta("vendor_id", "vendorId", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "deviceId": "device_id", 
            "dn": "dn", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
            "subDeviceId": "sub_device_id", 
            "subVendorId": "sub_vendor_id", 
            "vendorId": "vendor_id", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.device_id = None
        self.status = None
        self.sub_device_id = None
        self.sub_vendor_id = None
        self.vendor_id = None

        ManagedObject.__init__(self, "PciAdapterFruInventory", parent_mo_or_dn, **kwargs)

