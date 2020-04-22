"""This module contains the general information for GenerateRandomPassword ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class GenerateRandomPasswordConsts:
    pass


class GenerateRandomPassword(ManagedObject):
    """This is GenerateRandomPassword class."""

    consts = GenerateRandomPasswordConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("GenerateRandomPassword", "generateRandomPassword", "generate-random-pwd", VersionMeta.Version301c, "OutputOnly", 0xf, [], ["admin", "user"], ['aaaUserEp'], [], ["Get"]),
        "modular": MoMeta("GenerateRandomPassword", "generateRandomPassword", "generate-random-pwd", VersionMeta.Version301c, "OutputOnly", 0xf, [], ["admin", "user"], ['aaaUserEp'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 20, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 20, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "password": "password", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "password": "password", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.password = None
        self.status = None

        ManagedObject.__init__(self, "GenerateRandomPassword", parent_mo_or_dn, **kwargs)

