"""This module contains the general information for StorageSasExpander ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageSasExpanderConsts:
    MIXED6_G12_GDRIVE_SUPPORT_DISABLED = "Disabled"
    MIXED6_G12_GDRIVE_SUPPORT_ENABLED = "Enabled"
    MIXED6_G12_GDRIVE_SUPPORT_N_A = "N/A"
    MIXED6_G12_GDRIVE_SUPPORT_PENDING = "Pending"


class StorageSasExpander(ManagedObject):
    """This is StorageSasExpander class."""

    consts = StorageSasExpanderConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("StorageSasExpander", "storageSasExpander", "sas-expander-[id]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["read-only"], ['topSystem'], ['mgmtController'], ["Get"]),
        "modular": MoMeta("StorageSasExpander", "storageSasExpander", "sas-expander-[id]", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["read-only"], ['equipmentChassis'], ['faultInst', 'mgmtController', 'storageSasUplink'], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_fw_version": MoPropertyMeta("current_fw_version", "currentFwVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-999"]),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "sas_address": MoPropertyMeta("sas_address", "sasAddress", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "current_fw_version": MoPropertyMeta("current_fw_version", "currentFwVersion", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "enclosure_id": MoPropertyMeta("enclosure_id", "enclosureId", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-999"]),
            "mixed6_g12_g_drive_support": MoPropertyMeta("mixed6_g12_g_drive_support", "mixed6G12GDriveSupport", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "sas_address": MoPropertyMeta("sas_address", "sasAddress", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "currentFwVersion": "current_fw_version", 
            "description": "description", 
            "dn": "dn", 
            "id": "id", 
            "name": "name", 
            "rn": "rn", 
            "sasAddress": "sas_address", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "currentFwVersion": "current_fw_version", 
            "description": "description", 
            "dn": "dn", 
            "enclosureId": "enclosure_id", 
            "id": "id", 
            "mixed6G12GDriveSupport": "mixed6_g12_g_drive_support", 
            "name": "name", 
            "rn": "rn", 
            "sasAddress": "sas_address", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.current_fw_version = None
        self.description = None
        self.name = None
        self.sas_address = None
        self.status = None
        self.enclosure_id = None
        self.mixed6_g12_g_drive_support = None

        ManagedObject.__init__(self, "StorageSasExpander", parent_mo_or_dn, **kwargs)

