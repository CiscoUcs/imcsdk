"""This module contains the general information for AdaptorGenProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorGenProfileConsts:
    pass


class AdaptorGenProfile(ManagedObject):
    """This is AdaptorGenProfile class."""

    consts = AdaptorGenProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorGenProfile", "adaptorGenProfile", "general", VersionMeta.Version151f, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['adaptorUnit'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorGenProfile", "adaptorGenProfile", "general", VersionMeta.Version2013e, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['adaptorUnit'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "fip_mode": MoPropertyMeta("fip_mode", "fipMode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "lldp": MoPropertyMeta("lldp", "lldp", "string", VersionMeta.Version208d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "port_channel_enable": MoPropertyMeta("port_channel_enable", "portChannelEnable", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vntag_mode": MoPropertyMeta("vntag_mode", "vntagMode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "configuration_pending": MoPropertyMeta("configuration_pending", "configurationPending", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "iscsi_boot_supported": MoPropertyMeta("iscsi_boot_supported", "iscsiBootSupported", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "port_channel_capable": MoPropertyMeta("port_channel_capable", "portChannelCapable", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "usnic_supported": MoPropertyMeta("usnic_supported", "usnicSupported", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor_id": MoPropertyMeta("vendor_id", "vendorId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "fip_mode": MoPropertyMeta("fip_mode", "fipMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "lldp": MoPropertyMeta("lldp", "lldp", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "port_channel_enable": MoPropertyMeta("port_channel_enable", "portChannelEnable", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vntag_mode": MoPropertyMeta("vntag_mode", "vntagMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "configuration_pending": MoPropertyMeta("configuration_pending", "configurationPending", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "no", "yes"], []),
            "iscsi_boot_supported": MoPropertyMeta("iscsi_boot_supported", "iscsiBootSupported", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pci_link": MoPropertyMeta("pci_link", "pciLink", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "physical_nic_mode": MoPropertyMeta("physical_nic_mode", "physicalNicMode", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "port_channel_capable": MoPropertyMeta("port_channel_capable", "portChannelCapable", "string", VersionMeta.Version404b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "usnic_supported": MoPropertyMeta("usnic_supported", "usnicSupported", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor_id": MoPropertyMeta("vendor_id", "vendorId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "fipMode": "fip_mode", 
            "lldp": "lldp", 
            "portChannelEnable": "port_channel_enable", 
            "rn": "rn", 
            "status": "status", 
            "vntagMode": "vntag_mode", 
            "childAction": "child_action", 
            "configurationPending": "configuration_pending", 
            "iscsiBootSupported": "iscsi_boot_supported", 
            "model": "model", 
            "pciSlot": "pci_slot", 
            "portChannelCapable": "port_channel_capable", 
            "productName": "product_name", 
            "revision": "revision", 
            "serial": "serial", 
            "usnicSupported": "usnic_supported", 
            "vendor": "vendor", 
            "vendorId": "vendor_id", 
        },

        "modular": {
            "dn": "dn", 
            "fipMode": "fip_mode", 
            "lldp": "lldp", 
            "portChannelEnable": "port_channel_enable", 
            "rn": "rn", 
            "status": "status", 
            "vntagMode": "vntag_mode", 
            "childAction": "child_action", 
            "configurationPending": "configuration_pending", 
            "iscsiBootSupported": "iscsi_boot_supported", 
            "model": "model", 
            "pciLink": "pci_link", 
            "pciSlot": "pci_slot", 
            "physicalNicMode": "physical_nic_mode", 
            "portChannelCapable": "port_channel_capable", 
            "productName": "product_name", 
            "revision": "revision", 
            "serial": "serial", 
            "usnicSupported": "usnic_supported", 
            "vendor": "vendor", 
            "vendorId": "vendor_id", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.fip_mode = None
        self.lldp = None
        self.port_channel_enable = None
        self.status = None
        self.vntag_mode = None
        self.child_action = None
        self.configuration_pending = None
        self.iscsi_boot_supported = None
        self.model = None
        self.pci_slot = None
        self.port_channel_capable = None
        self.product_name = None
        self.revision = None
        self.serial = None
        self.usnic_supported = None
        self.vendor = None
        self.vendor_id = None
        self.pci_link = None
        self.physical_nic_mode = None

        ManagedObject.__init__(self, "AdaptorGenProfile", parent_mo_or_dn, **kwargs)

