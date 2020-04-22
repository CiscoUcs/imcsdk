"""This module contains the general information for PidCatalogPCIAdapter ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PidCatalogPCIAdapterConsts:
    pass


class PidCatalogPCIAdapter(ManagedObject):
    """This is PidCatalogPCIAdapter class."""

    consts = PidCatalogPCIAdapterConsts()
    naming_props = set(['slot'])

    mo_meta = {
        "classic": MoMeta("PidCatalogPCIAdapter", "pidCatalogPCIAdapter", "pid-pciadapter-[slot]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['pidCatalog'], [], ["Get"]),
        "modular": MoMeta("PidCatalogPCIAdapter", "pidCatalogPCIAdapter", "pid-pciadapter-[slot]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['pidCatalog'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "device": MoPropertyMeta("device", "device", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "pid": MoPropertyMeta("pid", "pid", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "subdevice": MoPropertyMeta("subdevice", "subdevice", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "subvendor": MoPropertyMeta("subvendor", "subvendor", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "device": MoPropertyMeta("device", "device", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "pid": MoPropertyMeta("pid", "pid", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "subdevice": MoPropertyMeta("subdevice", "subdevice", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "subvendor": MoPropertyMeta("subvendor", "subvendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "description": "description", 
            "device": "device", 
            "dn": "dn", 
            "pid": "pid", 
            "rn": "rn", 
            "slot": "slot", 
            "status": "status", 
            "subdevice": "subdevice", 
            "subvendor": "subvendor", 
            "vendor": "vendor", 
        },

        "modular": {
            "childAction": "child_action", 
            "description": "description", 
            "device": "device", 
            "dn": "dn", 
            "pid": "pid", 
            "rn": "rn", 
            "slot": "slot", 
            "status": "status", 
            "subdevice": "subdevice", 
            "subvendor": "subvendor", 
            "vendor": "vendor", 
        },

    }

    def __init__(self, parent_mo_or_dn, slot, **kwargs):
        self._dirty_mask = 0
        self.slot = slot
        self.child_action = None
        self.description = None
        self.device = None
        self.pid = None
        self.status = None
        self.subdevice = None
        self.subvendor = None
        self.vendor = None

        ManagedObject.__init__(self, "PidCatalogPCIAdapter", parent_mo_or_dn, **kwargs)

