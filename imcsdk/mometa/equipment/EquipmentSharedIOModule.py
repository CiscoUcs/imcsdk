"""This module contains the general information for EquipmentSharedIOModule ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class EquipmentSharedIOModuleConsts:
    pass


class EquipmentSharedIOModule(ManagedObject):
    """This is EquipmentSharedIOModule class."""

    consts = EquipmentSharedIOModuleConsts()
    naming_props = set(['slotId'])

    mo_meta = {
        "modular": MoMeta("EquipmentSharedIOModule", "equipmentSharedIOModule", "shared-io-module-[slot_id]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['equipmentSystemIOController'], ['commEpIpmiLan', 'computeSharedIOMbPowerStats', 'computeSharedIOMbTempStats', 'mgmtController'], ["Get"])
    }


    prop_meta = {

        "modular": {
            "adapter_hw_revision": MoPropertyMeta("adapter_hw_revision", "adapterHWRevision", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_firmware_version": MoPropertyMeta("current_firmware_version", "currentFirmwareVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "fip_mode": MoPropertyMeta("fip_mode", "fipMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "iptype": MoPropertyMeta("iptype", "iptype", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "iscsi_boot_capable": MoPropertyMeta("iscsi_boot_capable", "iscsiBootCapable", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "lldp": MoPropertyMeta("lldp", "lldp", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "mac_address": MoPropertyMeta("mac_address", "macAddress", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "pci_link": MoPropertyMeta("pci_link", "pciLink", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "product_id": MoPropertyMeta("product_id", "productId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "serial_number": MoPropertyMeta("serial_number", "serialNumber", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "slot_id": MoPropertyMeta("slot_id", "slotId", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "usnic_capable": MoPropertyMeta("usnic_capable", "usnicCapable", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vid": MoPropertyMeta("vid", "vid", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vntag_mode": MoPropertyMeta("vntag_mode", "vntagMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "modular": {
            "adapterHWRevision": "adapter_hw_revision", 
            "childAction": "child_action", 
            "currentFirmwareVersion": "current_firmware_version", 
            "description": "description", 
            "dn": "dn", 
            "fipMode": "fip_mode", 
            "iptype": "iptype", 
            "iscsiBootCapable": "iscsi_boot_capable", 
            "lldp": "lldp", 
            "macAddress": "mac_address", 
            "pciLink": "pci_link", 
            "productId": "product_id", 
            "rn": "rn", 
            "serialNumber": "serial_number", 
            "slotId": "slot_id", 
            "status": "status", 
            "usnicCapable": "usnic_capable", 
            "vendor": "vendor", 
            "vid": "vid", 
            "vntagMode": "vntag_mode", 
        },

    }

    def __init__(self, parent_mo_or_dn, slot_id, **kwargs):
        self._dirty_mask = 0
        self.slot_id = slot_id
        self.adapter_hw_revision = None
        self.child_action = None
        self.current_firmware_version = None
        self.description = None
        self.fip_mode = None
        self.iptype = None
        self.iscsi_boot_capable = None
        self.lldp = None
        self.mac_address = None
        self.pci_link = None
        self.product_id = None
        self.serial_number = None
        self.status = None
        self.usnic_capable = None
        self.vendor = None
        self.vid = None
        self.vntag_mode = None

        ManagedObject.__init__(self, "EquipmentSharedIOModule", parent_mo_or_dn, **kwargs)

