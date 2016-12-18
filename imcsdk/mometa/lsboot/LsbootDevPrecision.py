"""This module contains the general information for LsbootDevPrecision ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LsbootDevPrecisionConsts:
    CONFIGURED_BOOT_MODE_LEGACY = "Legacy"
    CONFIGURED_BOOT_MODE_NONE = "None"
    CONFIGURED_BOOT_MODE_UEFI = "Uefi"
    LAST_CONFIGURED_BOOT_ORDER_SOURCE_BIOS = "BIOS"
    LAST_CONFIGURED_BOOT_ORDER_SOURCE_CIMC = "CIMC"
    LAST_CONFIGURED_BOOT_ORDER_SOURCE_UNKNOWN = "UNKNOWN"
    PURPOSE_OPERATIONAL = "operational"
    PURPOSE_UTILITY = "utility"
    REAPPLY_FALSE = "false"
    REAPPLY_NO = "no"
    REAPPLY_TRUE = "true"
    REAPPLY_YES = "yes"
    REBOOT_ON_UPDATE_FALSE = "false"
    REBOOT_ON_UPDATE_NO = "no"
    REBOOT_ON_UPDATE_TRUE = "true"
    REBOOT_ON_UPDATE_YES = "yes"


class LsbootDevPrecision(ManagedObject):
    """This is LsbootDevPrecision class."""

    consts = LsbootDevPrecisionConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("LsbootDevPrecision", "lsbootDevPrecision", "boot-precision", VersionMeta.Version201a, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'computeRackUnit'], [u'lsbootHdd', u'lsbootIscsi', u'lsbootNVMe', u'lsbootPchStorage', u'lsbootPxe', u'lsbootSan', u'lsbootSd', u'lsbootUefiShell', u'lsbootUsb', u'lsbootVMedia'], ["Get", "Set"]),
        "modular": MoMeta("LsbootDevPrecision", "lsbootDevPrecision", "boot-precision", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'computeServerNode'], [u'lsbootHdd', u'lsbootIscsi', u'lsbootNVMe', u'lsbootPchStorage', u'lsbootPxe', u'lsbootSan', u'lsbootSd', u'lsbootUefiShell', u'lsbootUsb', u'lsbootVMedia'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "configured_boot_mode": MoPropertyMeta("configured_boot_mode", "configuredBootMode", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Legacy", "None", "Uefi"], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "last_configured_boot_order_source": MoPropertyMeta("last_configured_boot_order_source", "lastConfiguredBootOrderSource", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["BIOS", "CIMC", "UNKNOWN"], []), 
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
            "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["operational", "utility"], []), 
            "reapply": MoPropertyMeta("reapply", "reapply", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []), 
            "reboot_on_update": MoPropertyMeta("reboot_on_update", "rebootOnUpdate", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "configured_boot_mode": MoPropertyMeta("configured_boot_mode", "configuredBootMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Legacy", "None", "Uefi"], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "last_configured_boot_order_source": MoPropertyMeta("last_configured_boot_order_source", "lastConfiguredBootOrderSource", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["BIOS", "CIMC", "UNKNOWN"], []), 
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
            "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["operational", "utility"], []), 
            "reapply": MoPropertyMeta("reapply", "reapply", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["No", "Yes", "no", "yes"], []), 
            "reboot_on_update": MoPropertyMeta("reboot_on_update", "rebootOnUpdate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["No", "Yes", "no", "yes"], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "configuredBootMode": "configured_boot_mode", 
            "dn": "dn", 
            "lastConfiguredBootOrderSource": "last_configured_boot_order_source", 
            "name": "name", 
            "purpose": "purpose", 
            "reapply": "reapply", 
            "rebootOnUpdate": "reboot_on_update", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "configuredBootMode": "configured_boot_mode", 
            "dn": "dn", 
            "lastConfiguredBootOrderSource": "last_configured_boot_order_source", 
            "name": "name", 
            "purpose": "purpose", 
            "reapply": "reapply", 
            "rebootOnUpdate": "reboot_on_update", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.configured_boot_mode = None
        self.last_configured_boot_order_source = None
        self.name = None
        self.purpose = None
        self.reapply = None
        self.reboot_on_update = None
        self.status = None

        ManagedObject.__init__(self, "LsbootDevPrecision", parent_mo_or_dn, **kwargs)

