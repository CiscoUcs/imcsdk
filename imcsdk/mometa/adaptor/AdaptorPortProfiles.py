"""This module contains the general information for AdaptorPortProfiles ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorPortProfilesConsts:
    pass


class AdaptorPortProfiles(ManagedObject):
    """This is AdaptorPortProfiles class."""

    consts = AdaptorPortProfilesConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorPortProfiles", "adaptorPortProfiles", "port-profiles", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['adaptorExtEthIf'], [], ["Get"]),
        "modular": MoMeta("AdaptorPortProfiles", "adaptorPortProfiles", "port-profiles", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['adaptorExtEthIf'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "port_profiles_count": MoPropertyMeta("port_profiles_count", "portProfilesCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "port_profiles_name": MoPropertyMeta("port_profiles_name", "portProfilesName", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "port_profiles_count": MoPropertyMeta("port_profiles_count", "portProfilesCount", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "port_profiles_name": MoPropertyMeta("port_profiles_name", "portProfilesName", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "portProfilesCount": "port_profiles_count", 
            "portProfilesName": "port_profiles_name", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "portProfilesCount": "port_profiles_count", 
            "portProfilesName": "port_profiles_name", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.port_profiles_count = None
        self.port_profiles_name = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorPortProfiles", parent_mo_or_dn, **kwargs)

