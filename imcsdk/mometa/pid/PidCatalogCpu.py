"""This module contains the general information for PidCatalogCpu ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PidCatalogCpuConsts:
    pass


class PidCatalogCpu(ManagedObject):
    """This is PidCatalogCpu class."""

    consts = PidCatalogCpuConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("PidCatalogCpu", "pidCatalogCpu", "pid-cpu-[id]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['pidCatalog'], [], ["Get"]),
        "modular": MoMeta("PidCatalogCpu", "pidCatalogCpu", "pid-cpu-[id]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['pidCatalog'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "currentspeed": MoPropertyMeta("currentspeed", "currentspeed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pid": MoPropertyMeta("pid", "pid", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "signature": MoPropertyMeta("signature", "signature", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "socketdesignation": MoPropertyMeta("socketdesignation", "socketdesignation", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "currentspeed": MoPropertyMeta("currentspeed", "currentspeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "pid": MoPropertyMeta("pid", "pid", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "signature": MoPropertyMeta("signature", "signature", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "socketdesignation": MoPropertyMeta("socketdesignation", "socketdesignation", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "currentspeed": "currentspeed", 
            "description": "description", 
            "dn": "dn", 
            "id": "id", 
            "model": "model", 
            "operState": "oper_state", 
            "pid": "pid", 
            "rn": "rn", 
            "signature": "signature", 
            "socketdesignation": "socketdesignation", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "currentspeed": "currentspeed", 
            "description": "description", 
            "dn": "dn", 
            "id": "id", 
            "model": "model", 
            "operState": "oper_state", 
            "pid": "pid", 
            "rn": "rn", 
            "signature": "signature", 
            "socketdesignation": "socketdesignation", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.currentspeed = None
        self.description = None
        self.model = None
        self.oper_state = None
        self.pid = None
        self.signature = None
        self.socketdesignation = None
        self.status = None

        ManagedObject.__init__(self, "PidCatalogCpu", parent_mo_or_dn, **kwargs)

