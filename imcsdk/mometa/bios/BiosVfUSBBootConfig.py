"""This module contains the general information for BiosVfUSBBootConfig ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfUSBBootConfigConsts:
    VP_MAKE_DEVICE_NON_BOOTABLE_DISABLED = "Disabled"
    VP_MAKE_DEVICE_NON_BOOTABLE_ENABLED = "Enabled"
    _VP_MAKE_DEVICE_NON_BOOTABLE_DISABLED = "disabled"
    _VP_MAKE_DEVICE_NON_BOOTABLE_ENABLED = "enabled"
    VP_MAKE_DEVICE_NON_BOOTABLE_PLATFORM_DEFAULT = "platform-default"


class BiosVfUSBBootConfig(ManagedObject):
    """This is BiosVfUSBBootConfig class."""

    consts = BiosVfUSBBootConfigConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfUSBBootConfig", "biosVfUSBBootConfig", "USB-Boot-Config", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfUSBBootConfig", "biosVfUSBBootConfig", "USB-Boot-Config", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_make_device_non_bootable": MoPropertyMeta("vp_make_device_non_bootable", "vpMakeDeviceNonBootable", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_make_device_non_bootable": MoPropertyMeta("vp_make_device_non_bootable", "vpMakeDeviceNonBootable", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpMakeDeviceNonBootable": "vp_make_device_non_bootable", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpMakeDeviceNonBootable": "vp_make_device_non_bootable", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_make_device_non_bootable = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfUSBBootConfig", parent_mo_or_dn, **kwargs)

