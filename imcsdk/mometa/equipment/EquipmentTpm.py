"""This module contains the general information for EquipmentTpm ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class EquipmentTpmConsts:
    ACTIVE_STATUS_NA = "NA"
    ACTIVE_STATUS_ACTIVATED = "activated"
    ACTIVE_STATUS_DEACTIVATED = "deactivated"
    ACTIVE_STATUS_UNKNOWN = "unknown"
    ENABLED_STATUS_NA = "NA"
    ENABLED_STATUS_DISABLED = "disabled"
    ENABLED_STATUS_ENABLED = "enabled"
    ENABLED_STATUS_UNKNOWN = "unknown"
    OWNERSHIP_NA = "NA"
    OWNERSHIP_OWNED = "owned"
    OWNERSHIP_UNKNOWN = "unknown"
    OWNERSHIP_UNOWNED = "unowned"
    PRESENCE_NA = "NA"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    PRESENCE_INACCESSIBLE = "inaccessible"
    PRESENCE_MISMATCH = "mismatch"
    PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    PRESENCE_MISSING = "missing"
    PRESENCE_NOT_SUPPORTED = "not-supported"
    PRESENCE_UNAUTHORIZED = "unauthorized"
    PRESENCE_UNKNOWN = "unknown"


class EquipmentTpm(ManagedObject):
    """This is EquipmentTpm class."""

    consts = EquipmentTpmConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("EquipmentTpm", "equipmentTpm", "tpm", VersionMeta.Version201a, "OutputOnly", 0xf, [], ["read-only"], ['computeBoard'], [], ["Get"]),
        "modular": MoMeta("EquipmentTpm", "equipmentTpm", "tpm", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["read-only"], ['computeBoard'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "active_status": MoPropertyMeta("active_status", "activeStatus", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "activated", "deactivated", "unknown"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "enabled_status": MoPropertyMeta("enabled_status", "enabledStatus", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "disabled", "enabled", "unknown"], []),
            "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "ownership": MoPropertyMeta("ownership", "ownership", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "owned", "unknown", "unowned"], []),
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "tpm_revision": MoPropertyMeta("tpm_revision", "tpmRevision", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "active_status": MoPropertyMeta("active_status", "activeStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "activated", "deactivated", "unknown"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "enabled_status": MoPropertyMeta("enabled_status", "enabledStatus", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "disabled", "enabled", "unknown"], []),
            "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "ownership": MoPropertyMeta("ownership", "ownership", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "owned", "unknown", "unowned"], []),
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "tpm_revision": MoPropertyMeta("tpm_revision", "tpmRevision", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "activeStatus": "active_status", 
            "childAction": "child_action", 
            "dn": "dn", 
            "enabledStatus": "enabled_status", 
            "firmwareVersion": "firmware_version", 
            "model": "model", 
            "ownership": "ownership", 
            "presence": "presence", 
            "rn": "rn", 
            "serial": "serial", 
            "status": "status", 
            "tpmRevision": "tpm_revision", 
            "vendor": "vendor", 
            "version": "version", 
        },

        "modular": {
            "activeStatus": "active_status", 
            "childAction": "child_action", 
            "dn": "dn", 
            "enabledStatus": "enabled_status", 
            "firmwareVersion": "firmware_version", 
            "model": "model", 
            "ownership": "ownership", 
            "presence": "presence", 
            "rn": "rn", 
            "serial": "serial", 
            "status": "status", 
            "tpmRevision": "tpm_revision", 
            "vendor": "vendor", 
            "version": "version", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.active_status = None
        self.child_action = None
        self.enabled_status = None
        self.firmware_version = None
        self.model = None
        self.ownership = None
        self.presence = None
        self.serial = None
        self.status = None
        self.tpm_revision = None
        self.vendor = None
        self.version = None

        ManagedObject.__init__(self, "EquipmentTpm", parent_mo_or_dn, **kwargs)

