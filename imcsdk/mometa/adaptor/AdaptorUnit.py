"""This module contains the general information for AdaptorUnit ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorUnitConsts:
    ADMIN_STATE_ADAPTOR_RESET = "adaptor-reset"
    ADMIN_STATE_ADAPTOR_RESET_DEFAULT = "adaptor-reset-default"
    ADMIN_STATE_POLICY = "policy"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_MISSING = "missing"
    PRESENCE_NOT_SUPPORTED = "not-supported"
    PRESENCE_UNKNOWN = "unknown"


class AdaptorUnit(ManagedObject):
    """This is AdaptorUnit class."""

    consts = AdaptorUnitConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("AdaptorUnit", "adaptorUnit", "adaptor-[id]", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['computeRackUnit'], ['adaptorCfgBackup', 'adaptorCfgImporter', 'adaptorExtEthIf', 'adaptorHostEthIf', 'adaptorHostFcIf', 'faultInst', 'mgmtController'], ["Get", "Set"]),
        "modular": MoMeta("AdaptorUnit", "adaptorUnit", "adaptor-[id]", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['computeServerNode'], ['adaptorCfgBackup', 'adaptorCfgImporter', 'adaptorExtEthIf', 'adaptorHostEthIf', 'adaptorHostFcIf', 'faultInst', 'mgmtController'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["adaptor-reset", "adaptor-reset-default", "policy"], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 64, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["0-20"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "cimc_management_enabled": MoPropertyMeta("cimc_management_enabled", "cimcManagementEnabled", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pci_addr": MoPropertyMeta("pci_addr", "pciAddr", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "missing", "not-supported", "unknown"], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["adaptor-reset", "adaptor-reset-default", "policy"], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 64, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["0-20"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "cimc_management_enabled": MoPropertyMeta("cimc_management_enabled", "cimcManagementEnabled", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pci_addr": MoPropertyMeta("pci_addr", "pciAddr", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "missing", "not-supported", "unknown"], []),
            "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "description": "description", 
            "dn": "dn", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "cimcManagementEnabled": "cimc_management_enabled", 
            "model": "model", 
            "pciAddr": "pci_addr", 
            "pciSlot": "pci_slot", 
            "presence": "presence", 
            "serial": "serial", 
            "vendor": "vendor", 
        },

        "modular": {
            "adminState": "admin_state", 
            "description": "description", 
            "dn": "dn", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "cimcManagementEnabled": "cimc_management_enabled", 
            "model": "model", 
            "pciAddr": "pci_addr", 
            "pciSlot": "pci_slot", 
            "presence": "presence", 
            "serial": "serial", 
            "vendor": "vendor", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_state = None
        self.description = None
        self.status = None
        self.child_action = None
        self.cimc_management_enabled = None
        self.model = None
        self.pci_addr = None
        self.pci_slot = None
        self.presence = None
        self.serial = None
        self.vendor = None

        ManagedObject.__init__(self, "AdaptorUnit", parent_mo_or_dn, **kwargs)

