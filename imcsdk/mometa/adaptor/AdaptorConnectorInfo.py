"""This module contains the general information for AdaptorConnectorInfo ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorConnectorInfoConsts:
    pass


class AdaptorConnectorInfo(ManagedObject):
    """This is AdaptorConnectorInfo class."""

    consts = AdaptorConnectorInfoConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorConnectorInfo", "adaptorConnectorInfo", "connector-info", VersionMeta.Version204c, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['adaptorExtEthIf'], [], ["Get"]),
        "modular": MoMeta("AdaptorConnectorInfo", "adaptorConnectorInfo", "connector-info", VersionMeta.Version303a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['adaptorExtEthIf'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version204c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "part_number": MoPropertyMeta("part_number", "partNumber", "string", VersionMeta.Version204c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "part_revision": MoPropertyMeta("part_revision", "partRevision", "string", VersionMeta.Version204c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "present": MoPropertyMeta("present", "present", "string", VersionMeta.Version204c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version204c, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "supported": MoPropertyMeta("supported", "supported", "string", VersionMeta.Version204c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version204c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version204c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "part_number": MoPropertyMeta("part_number", "partNumber", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "part_revision": MoPropertyMeta("part_revision", "partRevision", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "present": MoPropertyMeta("present", "present", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "supported": MoPropertyMeta("supported", "supported", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "partNumber": "part_number", 
            "partRevision": "part_revision", 
            "present": "present", 
            "rn": "rn", 
            "status": "status", 
            "supported": "supported", 
            "type": "type", 
            "vendor": "vendor", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "partNumber": "part_number", 
            "partRevision": "part_revision", 
            "present": "present", 
            "rn": "rn", 
            "status": "status", 
            "supported": "supported", 
            "type": "type", 
            "vendor": "vendor", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.part_number = None
        self.part_revision = None
        self.present = None
        self.status = None
        self.supported = None
        self.type = None
        self.vendor = None

        ManagedObject.__init__(self, "AdaptorConnectorInfo", parent_mo_or_dn, **kwargs)

