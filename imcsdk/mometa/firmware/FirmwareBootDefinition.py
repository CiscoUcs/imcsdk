"""This module contains the general information for FirmwareBootDefinition ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class FirmwareBootDefinitionConsts:
    TYPE_ADAPTOR = "adaptor"
    TYPE_BLADE_BIOS = "blade-bios"
    TYPE_BLADE_CONTROLLER = "blade-controller"
    TYPE_FEX = "fex"
    TYPE_SAS_EXPANDER = "sas-expander"
    TYPE_SIOC = "sioc"
    TYPE_STORAGE_CONTROLLER = "storage-controller"
    TYPE_SYSTEM = "system"


class FirmwareBootDefinition(ManagedObject):
    """This is FirmwareBootDefinition class."""

    consts = FirmwareBootDefinitionConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("FirmwareBootDefinition", "firmwareBootDefinition", "fw-boot-def", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosUnit', 'mgmtController', 'storageController', 'systemIOController'], ['firmwareBootUnit'], ["Get"]),
        "modular": MoMeta("FirmwareBootDefinition", "firmwareBootDefinition", "fw-boot-def", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosUnit', 'mgmtController', 'storageController'], ['firmwareBootUnit'], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["adaptor", "blade-bios", "blade-controller", "fex", "sas-expander", "sioc", "storage-controller", "system"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["adaptor", "blade-bios", "blade-controller", "fex", "sas-expander", "sioc", "storage-controller", "system"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "type": "type", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "type": "type", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "FirmwareBootDefinition", parent_mo_or_dn, **kwargs)

