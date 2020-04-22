"""This module contains the general information for BiosProfileToken ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosProfileTokenConsts:
    pass


class BiosProfileToken(ManagedObject):
    """This is BiosProfileToken class."""

    consts = BiosProfileTokenConsts()
    naming_props = set(['name'])

    mo_meta = {
        "classic": MoMeta("BiosProfileToken", "biosProfileToken", "token-[name]", VersionMeta.Version301c, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosProfile'], [], ["Get"]),
        "modular": MoMeta("BiosProfileToken", "biosProfileToken", "token-[name]", VersionMeta.Version301c, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosProfile'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "actual_value": MoPropertyMeta("actual_value", "actualValue", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "configured_value": MoPropertyMeta("configured_value", "configuredValue", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version301c, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

        "modular": {
            "actual_value": MoPropertyMeta("actual_value", "actualValue", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "configured_value": MoPropertyMeta("configured_value", "configuredValue", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version301c, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "actualValue": "actual_value", 
            "childAction": "child_action", 
            "configuredValue": "configured_value", 
            "dn": "dn", 
            "name": "name", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "actualValue": "actual_value", 
            "childAction": "child_action", 
            "configuredValue": "configured_value", 
            "dn": "dn", 
            "name": "name", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.actual_value = None
        self.child_action = None
        self.configured_value = None
        self.status = None

        ManagedObject.__init__(self, "BiosProfileToken", parent_mo_or_dn, **kwargs)

