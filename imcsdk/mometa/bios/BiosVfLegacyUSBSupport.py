"""This module contains the general information for BiosVfLegacyUSBSupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfLegacyUSBSupportConsts:
    VP_LEGACY_USBSUPPORT_AUTO = "Auto"
    VP_LEGACY_USBSUPPORT_DISABLED = "Disabled"
    VP_LEGACY_USBSUPPORT_ENABLED = "Enabled"
    _VP_LEGACY_USBSUPPORT_AUTO = "auto"
    _VP_LEGACY_USBSUPPORT_DISABLED = "disabled"
    _VP_LEGACY_USBSUPPORT_ENABLED = "enabled"
    VP_LEGACY_USBSUPPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfLegacyUSBSupport(ManagedObject):
    """This is BiosVfLegacyUSBSupport class."""

    consts = BiosVfLegacyUSBSupportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfLegacyUSBSupport", "biosVfLegacyUSBSupport", "LegacyUSB-Support", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfLegacyUSBSupport", "biosVfLegacyUSBSupport", "LegacyUSB-Support", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_legacy_usb_support": MoPropertyMeta("vp_legacy_usb_support", "vpLegacyUSBSupport", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "auto", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_legacy_usb_support": MoPropertyMeta("vp_legacy_usb_support", "vpLegacyUSBSupport", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "auto", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpLegacyUSBSupport": "vp_legacy_usb_support", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpLegacyUSBSupport": "vp_legacy_usb_support", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_legacy_usb_support = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfLegacyUSBSupport", parent_mo_or_dn, **kwargs)

