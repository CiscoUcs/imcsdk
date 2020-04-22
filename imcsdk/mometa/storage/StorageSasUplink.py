"""This module contains the general information for StorageSasUplink ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageSasUplinkConsts:
    pass


class StorageSasUplink(ManagedObject):
    """This is StorageSasUplink class."""

    consts = StorageSasUplinkConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("StorageSasUplink", "storageSasUplink", "uplink", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["read-only"], ['storageSasExpander'], [], ["Get"])
    }


    prop_meta = {

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "server1_uplink1_speed": MoPropertyMeta("server1_uplink1_speed", "server1Uplink1Speed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "server1_uplink2_speed": MoPropertyMeta("server1_uplink2_speed", "server1Uplink2Speed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "server1_uplink3_speed": MoPropertyMeta("server1_uplink3_speed", "server1Uplink3Speed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "server1_uplink4_speed": MoPropertyMeta("server1_uplink4_speed", "server1Uplink4Speed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "server1_uplink5_speed": MoPropertyMeta("server1_uplink5_speed", "server1Uplink5Speed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "server1_uplink6_speed": MoPropertyMeta("server1_uplink6_speed", "server1Uplink6Speed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "server2_uplink1_speed": MoPropertyMeta("server2_uplink1_speed", "server2Uplink1Speed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "server2_uplink2_speed": MoPropertyMeta("server2_uplink2_speed", "server2Uplink2Speed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "server2_uplink3_speed": MoPropertyMeta("server2_uplink3_speed", "server2Uplink3Speed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "server2_uplink4_speed": MoPropertyMeta("server2_uplink4_speed", "server2Uplink4Speed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "server2_uplink5_speed": MoPropertyMeta("server2_uplink5_speed", "server2Uplink5Speed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "server2_uplink6_speed": MoPropertyMeta("server2_uplink6_speed", "server2Uplink6Speed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "server1Uplink1Speed": "server1_uplink1_speed", 
            "server1Uplink2Speed": "server1_uplink2_speed", 
            "server1Uplink3Speed": "server1_uplink3_speed", 
            "server1Uplink4Speed": "server1_uplink4_speed", 
            "server1Uplink5Speed": "server1_uplink5_speed", 
            "server1Uplink6Speed": "server1_uplink6_speed", 
            "server2Uplink1Speed": "server2_uplink1_speed", 
            "server2Uplink2Speed": "server2_uplink2_speed", 
            "server2Uplink3Speed": "server2_uplink3_speed", 
            "server2Uplink4Speed": "server2_uplink4_speed", 
            "server2Uplink5Speed": "server2_uplink5_speed", 
            "server2Uplink6Speed": "server2_uplink6_speed", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.server1_uplink1_speed = None
        self.server1_uplink2_speed = None
        self.server1_uplink3_speed = None
        self.server1_uplink4_speed = None
        self.server1_uplink5_speed = None
        self.server1_uplink6_speed = None
        self.server2_uplink1_speed = None
        self.server2_uplink2_speed = None
        self.server2_uplink3_speed = None
        self.server2_uplink4_speed = None
        self.server2_uplink5_speed = None
        self.server2_uplink6_speed = None
        self.status = None

        ManagedObject.__init__(self, "StorageSasUplink", parent_mo_or_dn, **kwargs)

