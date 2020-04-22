"""This module contains the general information for AdaptorEthOffloadProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorEthOffloadProfileConsts:
    pass


class AdaptorEthOffloadProfile(ManagedObject):
    """This is AdaptorEthOffloadProfile class."""

    consts = AdaptorEthOffloadProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorEthOffloadProfile", "adaptorEthOffloadProfile", "eth-offload", VersionMeta.Version151f, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorEthOffloadProfile", "adaptorEthOffloadProfile", "eth-offload", VersionMeta.Version2013e, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['adaptorHostEthIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "large_receive": MoPropertyMeta("large_receive", "largeReceive", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "tcp_rx_checksum": MoPropertyMeta("tcp_rx_checksum", "tcpRxChecksum", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "tcp_segment": MoPropertyMeta("tcp_segment", "tcpSegment", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "tcp_tx_checksum": MoPropertyMeta("tcp_tx_checksum", "tcpTxChecksum", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "large_receive": MoPropertyMeta("large_receive", "largeReceive", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "tcp_rx_checksum": MoPropertyMeta("tcp_rx_checksum", "tcpRxChecksum", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "tcp_segment": MoPropertyMeta("tcp_segment", "tcpSegment", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "tcp_tx_checksum": MoPropertyMeta("tcp_tx_checksum", "tcpTxChecksum", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "largeReceive": "large_receive", 
            "rn": "rn", 
            "status": "status", 
            "tcpRxChecksum": "tcp_rx_checksum", 
            "tcpSegment": "tcp_segment", 
            "tcpTxChecksum": "tcp_tx_checksum", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "largeReceive": "large_receive", 
            "rn": "rn", 
            "status": "status", 
            "tcpRxChecksum": "tcp_rx_checksum", 
            "tcpSegment": "tcp_segment", 
            "tcpTxChecksum": "tcp_tx_checksum", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.large_receive = None
        self.status = None
        self.tcp_rx_checksum = None
        self.tcp_segment = None
        self.tcp_tx_checksum = None
        self.child_action = None

        ManagedObject.__init__(self, "AdaptorEthOffloadProfile", parent_mo_or_dn, **kwargs)

