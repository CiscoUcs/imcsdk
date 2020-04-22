"""This module contains the general information for BiosVfDCPMMFirmwareDowngrade ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfDCPMMFirmwareDowngradeConsts:
    VP_DCPMMFIRMWARE_DOWNGRADE_DISABLED = "Disabled"
    VP_DCPMMFIRMWARE_DOWNGRADE_ENABLED = "Enabled"
    _VP_DCPMMFIRMWARE_DOWNGRADE_DISABLED = "disabled"
    _VP_DCPMMFIRMWARE_DOWNGRADE_ENABLED = "enabled"
    VP_DCPMMFIRMWARE_DOWNGRADE_PLATFORM_DEFAULT = "platform-default"


class BiosVfDCPMMFirmwareDowngrade(ManagedObject):
    """This is BiosVfDCPMMFirmwareDowngrade class."""

    consts = BiosVfDCPMMFirmwareDowngradeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfDCPMMFirmwareDowngrade", "biosVfDCPMMFirmwareDowngrade", "DCPMM-Firmware-Downgrade", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfDCPMMFirmwareDowngrade", "biosVfDCPMMFirmwareDowngrade", "DCPMM-Firmware-Downgrade", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_dcpmm_firmware_downgrade": MoPropertyMeta("vp_dcpmm_firmware_downgrade", "vpDCPMMFirmwareDowngrade", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_dcpmm_firmware_downgrade": MoPropertyMeta("vp_dcpmm_firmware_downgrade", "vpDCPMMFirmwareDowngrade", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpDCPMMFirmwareDowngrade": "vp_dcpmm_firmware_downgrade", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpDCPMMFirmwareDowngrade": "vp_dcpmm_firmware_downgrade", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_dcpmm_firmware_downgrade = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfDCPMMFirmwareDowngrade", parent_mo_or_dn, **kwargs)

