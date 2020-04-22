"""This module contains the general information for PidCatalog ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PidCatalogConsts:
    ADMIN_ACTION_DELETE_PID_CATALOG = "delete-pid-catalog"


class PidCatalog(ManagedObject):
    """This is PidCatalog class."""

    consts = PidCatalogConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("PidCatalog", "pidCatalog", "pid", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['computeBoard'], ['activatePIDCatalog', 'pidCatalogCpu', 'pidCatalogDimm', 'pidCatalogHdd', 'pidCatalogPCIAdapter', 'uploadPIDCatalog'], ["Get"]),
        "modular": MoMeta("PidCatalog", "pidCatalog", "pid", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['computeBoard'], ['activatePIDCatalog', 'pidCatalogCpu', 'pidCatalogDimm', 'pidCatalogHdd', 'pidCatalogPCIAdapter'], ["Get"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete-pid-catalog"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["delete-pid-catalog"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "name": "name", 
            "version": "version", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "name": "name", 
            "version": "version", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.status = None
        self.child_action = None
        self.name = None
        self.version = None

        ManagedObject.__init__(self, "PidCatalog", parent_mo_or_dn, **kwargs)

