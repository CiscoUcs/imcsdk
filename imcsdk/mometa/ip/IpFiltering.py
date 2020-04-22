"""This module contains the general information for IpFiltering ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class IpFilteringConsts:
    ADMIN_ACTION_CLEAR_ALL = "clearAll"
    ADMIN_ACTION_CLEAR_FILTER1 = "clearFilter1"
    ADMIN_ACTION_CLEAR_FILTER2 = "clearFilter2"
    ADMIN_ACTION_CLEAR_FILTER3 = "clearFilter3"
    ADMIN_ACTION_CLEAR_FILTER4 = "clearFilter4"


class IpFiltering(ManagedObject):
    """This is IpFiltering class."""

    consts = IpFilteringConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("IpFiltering", "ipFiltering", "ip-filter", VersionMeta.Version301c, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['mgmtIf'], [], ["Get", "Set"]),
        "modular": MoMeta("IpFiltering", "ipFiltering", "ip-filter", VersionMeta.Version301c, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['mgmtIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clearAll", "clearFilter1", "clearFilter2", "clearFilter3", "clearFilter4"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "enable": MoPropertyMeta("enable", "enable", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "filter1": MoPropertyMeta("filter1", "filter1", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
            "filter2": MoPropertyMeta("filter2", "filter2", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
            "filter3": MoPropertyMeta("filter3", "filter3", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []),
            "filter4": MoPropertyMeta("filter4", "filter4", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clearAll", "clearFilter1", "clearFilter2", "clearFilter3", "clearFilter4"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "enable": MoPropertyMeta("enable", "enable", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["No", "Yes", "no", "yes"], []),
            "filter1": MoPropertyMeta("filter1", "filter1", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
            "filter2": MoPropertyMeta("filter2", "filter2", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
            "filter3": MoPropertyMeta("filter3", "filter3", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []),
            "filter4": MoPropertyMeta("filter4", "filter4", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "enable": "enable", 
            "filter1": "filter1", 
            "filter2": "filter2", 
            "filter3": "filter3", 
            "filter4": "filter4", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "enable": "enable", 
            "filter1": "filter1", 
            "filter2": "filter2", 
            "filter3": "filter3", 
            "filter4": "filter4", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.enable = None
        self.filter1 = None
        self.filter2 = None
        self.filter3 = None
        self.filter4 = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "IpFiltering", parent_mo_or_dn, **kwargs)

