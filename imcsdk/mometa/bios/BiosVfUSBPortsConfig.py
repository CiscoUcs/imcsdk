"""This module contains the general information for BiosVfUSBPortsConfig ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfUSBPortsConfigConsts:
    VP_ALL_USB_DEVICES_DISABLED = "Disabled"
    VP_ALL_USB_DEVICES_ENABLED = "Enabled"
    _VP_ALL_USB_DEVICES_DISABLED = "disabled"
    _VP_ALL_USB_DEVICES_ENABLED = "enabled"
    VP_ALL_USB_DEVICES_PLATFORM_DEFAULT = "platform-default"
    VP_USB_PORT_FRONT_DISABLED = "Disabled"
    VP_USB_PORT_FRONT_ENABLED = "Enabled"
    _VP_USB_PORT_FRONT_DISABLED = "disabled"
    _VP_USB_PORT_FRONT_ENABLED = "enabled"
    VP_USB_PORT_FRONT_PLATFORM_DEFAULT = "platform-default"
    VP_USB_PORT_INTERNAL_DISABLED = "Disabled"
    VP_USB_PORT_INTERNAL_ENABLED = "Enabled"
    _VP_USB_PORT_INTERNAL_DISABLED = "disabled"
    _VP_USB_PORT_INTERNAL_ENABLED = "enabled"
    VP_USB_PORT_INTERNAL_PLATFORM_DEFAULT = "platform-default"
    VP_USB_PORT_KVM_DISABLED = "Disabled"
    VP_USB_PORT_KVM_ENABLED = "Enabled"
    _VP_USB_PORT_KVM_DISABLED = "disabled"
    _VP_USB_PORT_KVM_ENABLED = "enabled"
    VP_USB_PORT_KVM_PLATFORM_DEFAULT = "platform-default"
    VP_USB_PORT_REAR_DISABLED = "Disabled"
    VP_USB_PORT_REAR_ENABLED = "Enabled"
    _VP_USB_PORT_REAR_DISABLED = "disabled"
    _VP_USB_PORT_REAR_ENABLED = "enabled"
    VP_USB_PORT_REAR_PLATFORM_DEFAULT = "platform-default"
    VP_USB_PORT_SDCARD_DISABLED = "Disabled"
    VP_USB_PORT_SDCARD_ENABLED = "Enabled"
    _VP_USB_PORT_SDCARD_DISABLED = "disabled"
    _VP_USB_PORT_SDCARD_ENABLED = "enabled"
    VP_USB_PORT_SDCARD_PLATFORM_DEFAULT = "platform-default"
    VP_USB_PORT_VMEDIA_DISABLED = "Disabled"
    VP_USB_PORT_VMEDIA_ENABLED = "Enabled"
    _VP_USB_PORT_VMEDIA_DISABLED = "disabled"
    _VP_USB_PORT_VMEDIA_ENABLED = "enabled"
    VP_USB_PORT_VMEDIA_PLATFORM_DEFAULT = "platform-default"


class BiosVfUSBPortsConfig(ManagedObject):
    """This is BiosVfUSBPortsConfig class."""

    consts = BiosVfUSBPortsConfigConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfUSBPortsConfig", "biosVfUSBPortsConfig", "USB-Ports-Config", VersionMeta.Version151f, "InputOutput", 0x7ff, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfUSBPortsConfig", "biosVfUSBPortsConfig", "USB-Ports-Config", VersionMeta.Version2013e, "InputOutput", 0x7ff, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_all_usb_devices": MoPropertyMeta("vp_all_usb_devices", "vpAllUsbDevices", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_usb_port_front": MoPropertyMeta("vp_usb_port_front", "vpUsbPortFront", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_usb_port_internal": MoPropertyMeta("vp_usb_port_internal", "vpUsbPortInternal", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_usb_port_kvm": MoPropertyMeta("vp_usb_port_kvm", "vpUsbPortKVM", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_usb_port_rear": MoPropertyMeta("vp_usb_port_rear", "vpUsbPortRear", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_usb_port_sd_card": MoPropertyMeta("vp_usb_port_sd_card", "vpUsbPortSDCard", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_usb_port_v_media": MoPropertyMeta("vp_usb_port_v_media", "vpUsbPortVMedia", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_all_usb_devices": MoPropertyMeta("vp_all_usb_devices", "vpAllUsbDevices", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_usb_port_front": MoPropertyMeta("vp_usb_port_front", "vpUsbPortFront", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_usb_port_internal": MoPropertyMeta("vp_usb_port_internal", "vpUsbPortInternal", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_usb_port_kvm": MoPropertyMeta("vp_usb_port_kvm", "vpUsbPortKVM", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_usb_port_rear": MoPropertyMeta("vp_usb_port_rear", "vpUsbPortRear", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_usb_port_sd_card": MoPropertyMeta("vp_usb_port_sd_card", "vpUsbPortSDCard", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_usb_port_v_media": MoPropertyMeta("vp_usb_port_v_media", "vpUsbPortVMedia", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpAllUsbDevices": "vp_all_usb_devices", 
            "vpUsbPortFront": "vp_usb_port_front", 
            "vpUsbPortInternal": "vp_usb_port_internal", 
            "vpUsbPortKVM": "vp_usb_port_kvm", 
            "vpUsbPortRear": "vp_usb_port_rear", 
            "vpUsbPortSDCard": "vp_usb_port_sd_card", 
            "vpUsbPortVMedia": "vp_usb_port_v_media", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpAllUsbDevices": "vp_all_usb_devices", 
            "vpUsbPortFront": "vp_usb_port_front", 
            "vpUsbPortInternal": "vp_usb_port_internal", 
            "vpUsbPortKVM": "vp_usb_port_kvm", 
            "vpUsbPortRear": "vp_usb_port_rear", 
            "vpUsbPortSDCard": "vp_usb_port_sd_card", 
            "vpUsbPortVMedia": "vp_usb_port_v_media", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_all_usb_devices = None
        self.vp_usb_port_front = None
        self.vp_usb_port_internal = None
        self.vp_usb_port_kvm = None
        self.vp_usb_port_rear = None
        self.vp_usb_port_sd_card = None
        self.vp_usb_port_v_media = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfUSBPortsConfig", parent_mo_or_dn, **kwargs)

