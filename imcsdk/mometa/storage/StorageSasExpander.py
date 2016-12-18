"""This module contains the general information for StorageSasExpander ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageSasExpanderConsts:
    pass


class StorageSasExpander(ManagedObject):
    """This is StorageSasExpander class."""

    consts = StorageSasExpanderConsts()
    naming_props = set([u'id'])

    mo_meta = {
        "classic": MoMeta("StorageSasExpander", "storageSasExpander", "sas-expander-[id]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["read-only"], [u'topSystem'], [u'mgmtController'], ["Get"]),
        "modular": MoMeta("StorageSasExpander", "storageSasExpander", "sas-expander-[id]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["read-only"], [u'equipmentChassis'], [u'faultInst', u'mgmtController', u'storageSasUplink'], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-999"]), 
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "current_fw_version": MoPropertyMeta("current_fw_version", "currentFwVersion", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-999"]), 
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "sas_address": MoPropertyMeta("sas_address", "sasAddress", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "description": "description", 
            "dn": "dn", 
            "id": "id", 
            "name": "name", 
            "rn": "rn", 
            "status": "status", 
            "currentFwVersion": "current_fw_version", 
        },

        "modular": {
            "childAction": "child_action", 
            "description": "description", 
            "dn": "dn", 
            "id": "id", 
            "name": "name", 
            "rn": "rn", 
            "status": "status", 
            "sasAddress": "sas_address", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.description = None
        self.name = None
        self.status = None
        self.current_fw_version = None
        self.sas_address = None

        ManagedObject.__init__(self, "StorageSasExpander", parent_mo_or_dn, **kwargs)

