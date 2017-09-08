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
        "classic": MoMeta("AdaptorGenProfile", "adaptorGenProfile", "general", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'adaptorUnit'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorGenProfile", "adaptorGenProfile", "general", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'adaptorUnit'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "configuration_pending": MoPropertyMeta("configuration_pending", "configurationPending", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "fip_mode": MoPropertyMeta("fip_mode", "fipMode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "iscsi_boot_supported": MoPropertyMeta("iscsi_boot_supported", "iscsiBootSupported", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "lldp": MoPropertyMeta("lldp", "lldp", "string", VersionMeta.Version208d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "usnic_supported": MoPropertyMeta("usnic_supported", "usnicSupported", "string", VersionMeta.Version151x, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "vendor_id": MoPropertyMeta("vendor_id", "vendorId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "vntag_mode": MoPropertyMeta("vntag_mode", "vntagMode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "configuration_pending": MoPropertyMeta("configuration_pending", "configurationPending", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "no", "yes"], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "fip_mode": MoPropertyMeta("fip_mode", "fipMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "iscsi_boot_supported": MoPropertyMeta("iscsi_boot_supported", "iscsiBootSupported", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "lldp": MoPropertyMeta("lldp", "lldp", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "product_name": MoPropertyMeta("product_name", "productName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []), 
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "usnic_supported": MoPropertyMeta("usnic_supported", "usnicSupported", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "vendor_id": MoPropertyMeta("vendor_id", "vendorId", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "vntag_mode": MoPropertyMeta("vntag_mode", "vntagMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "pci_link": MoPropertyMeta("pci_link", "pciLink", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "configurationPending": "configuration_pending", 
            "dn": "dn", 
            "fipMode": "fip_mode", 
            "iscsiBootSupported": "iscsi_boot_supported", 
            "lldp": "lldp", 
            "model": "model", 
            "pciSlot": "pci_slot", 
            "productName": "product_name", 
            "revision": "revision", 
            "rn": "rn", 
            "serial": "serial", 
            "status": "status", 
            "usnicSupported": "usnic_supported", 
            "vendor": "vendor", 
            "vendorId": "vendor_id", 
            "vntagMode": "vntag_mode", 
        },

        "modular": {
            "childAction": "child_action", 
            "configurationPending": "configuration_pending", 
            "dn": "dn", 
            "fipMode": "fip_mode", 
            "iscsiBootSupported": "iscsi_boot_supported", 
            "lldp": "lldp", 
            "model": "model", 
            "pciSlot": "pci_slot", 
            "productName": "product_name", 
            "revision": "revision", 
            "rn": "rn", 
            "serial": "serial", 
            "status": "status", 
            "usnicSupported": "usnic_supported", 
            "vendor": "vendor", 
            "vendorId": "vendor_id", 
            "vntagMode": "vntag_mode", 
            "pciLink": "pci_link", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.configuration_pending = None
        self.fip_mode = None
        self.iscsi_boot_supported = None
        self.lldp = None
        self.model = None
        self.pci_slot = None
        self.product_name = None
        self.revision = None
        self.serial = None
        self.status = None
        self.usnic_supported = None
        self.vendor = None
        self.vendor_id = None
        self.vntag_mode = None
        self.pci_link = None

        ManagedObject.__init__(self, "AdaptorGenProfile", parent_mo_or_dn, **kwargs)

