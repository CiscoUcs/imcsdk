"""This module contains the general information for AdaptorEthSRIOVProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorEthSRIOVProfileConsts:
    pass


class AdaptorEthSRIOVProfile(ManagedObject):
    """This is AdaptorEthSRIOVProfile class."""

    consts = AdaptorEthSRIOVProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorEthSRIOVProfile", "adaptorEthSRIOVProfile", "eth-sriov", VersionMeta.Version423a, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version423a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "no_of_v_fs": MoPropertyMeta("no_of_v_fs", "noOfVFs", "uint", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["0-64"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "sriov_completion_count": MoPropertyMeta("sriov_completion_count", "sriovCompletionCount", "uint", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-16", "1-16"]),
            "sriov_interrupt_count": MoPropertyMeta("sriov_interrupt_count", "sriovInterruptCount", "uint", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-16", "1-16"]),
            "sriov_receive_count": MoPropertyMeta("sriov_receive_count", "sriovReceiveCount", "uint", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-8", "1-8"]),
            "sriov_transmit_count": MoPropertyMeta("sriov_transmit_count", "sriovTransmitCount", "uint", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["0-8", "1-8"]),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "noOfVFs": "no_of_v_fs", 
            "rn": "rn", 
            "sriovCompletionCount": "sriov_completion_count", 
            "sriovInterruptCount": "sriov_interrupt_count", 
            "sriovReceiveCount": "sriov_receive_count", 
            "sriovTransmitCount": "sriov_transmit_count", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.no_of_v_fs = None
        self.sriov_completion_count = None
        self.sriov_interrupt_count = None
        self.sriov_receive_count = None
        self.sriov_transmit_count = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorEthSRIOVProfile", parent_mo_or_dn, **kwargs)

