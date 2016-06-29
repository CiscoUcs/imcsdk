"""This module contains the general information for PidCatalogDimm ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class PidCatalogDimmConsts:
    pass


class PidCatalogDimm(ManagedObject):
    """This is PidCatalogDimm class."""

    consts = PidCatalogDimmConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("PidCatalogDimm", "pidCatalogDimm", "pid-dimm-[name]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'pidCatalog'], [], ["Get"])

    prop_meta = {
        "capacity": MoPropertyMeta("capacity", "capacity", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "datawidth": MoPropertyMeta("datawidth", "datawidth", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
        "manufacturer": MoPropertyMeta("manufacturer", "manufacturer", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "mfgid": MoPropertyMeta("mfgid", "mfgid", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, 0, 510, None, [], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pid": MoPropertyMeta("pid", "pid", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
        "serialnumber": MoPropertyMeta("serialnumber", "serialnumber", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "speed": MoPropertyMeta("speed", "speed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "capacity": "capacity", 
        "childAction": "child_action", 
        "datawidth": "datawidth", 
        "description": "description", 
        "dn": "dn", 
        "manufacturer": "manufacturer", 
        "mfgid": "mfgid", 
        "model": "model", 
        "name": "name", 
        "operability": "operability", 
        "pid": "pid", 
        "rn": "rn", 
        "serialnumber": "serialnumber", 
        "speed": "speed", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.capacity = None
        self.child_action = None
        self.datawidth = None
        self.description = None
        self.manufacturer = None
        self.mfgid = None
        self.model = None
        self.operability = None
        self.pid = None
        self.serialnumber = None
        self.speed = None
        self.status = None

        ManagedObject.__init__(self, "PidCatalogDimm", parent_mo_or_dn, **kwargs)

