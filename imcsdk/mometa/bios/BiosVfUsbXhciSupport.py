"""This module contains the general information for BiosVfUsbXhciSupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfUsbXhciSupportConsts:
    VP_USB_XHCI_SUPPORT_DISABLED = "Disabled"
    VP_USB_XHCI_SUPPORT_ENABLED = "Enabled"
    _VP_USB_XHCI_SUPPORT_DISABLED = "disabled"
    _VP_USB_XHCI_SUPPORT_ENABLED = "enabled"
    VP_USB_XHCI_SUPPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfUsbXhciSupport(ManagedObject):
    """This is BiosVfUsbXhciSupport class."""

    consts = BiosVfUsbXhciSupportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfUsbXhciSupport", "biosVfUsbXhciSupport", "UsbXhci-Support", VersionMeta.Version303a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfUsbXhciSupport", "biosVfUsbXhciSupport", "UsbXhci-Support", VersionMeta.Version303a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_usb_xhci_support": MoPropertyMeta("vp_usb_xhci_support", "vpUsbXhciSupport", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_usb_xhci_support": MoPropertyMeta("vp_usb_xhci_support", "vpUsbXhciSupport", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpUsbXhciSupport": "vp_usb_xhci_support", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpUsbXhciSupport": "vp_usb_xhci_support", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_usb_xhci_support = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfUsbXhciSupport", parent_mo_or_dn, **kwargs)

