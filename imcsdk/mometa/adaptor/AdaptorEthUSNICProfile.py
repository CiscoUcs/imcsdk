"""This module contains the general information for AdaptorEthUSNICProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorEthUSNICProfileConsts:
    COALESCING_TYPE_IDLE = "IDLE"
    COALESCING_TYPE_MIN = "MIN"


class AdaptorEthUSNICProfile(ManagedObject):
    """This is AdaptorEthUSNICProfile class."""

    consts = AdaptorEthUSNICProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorEthUSNICProfile", "adaptorEthUSNICProfile", "ethusnic", VersionMeta.Version151x, "InputOutput", 0x3ffff, [], ["admin"], ['adaptorHostEthIf'], [], ["Get", "Remove", "Set"]),
        "modular": MoMeta("AdaptorEthUSNICProfile", "adaptorEthUSNICProfile", "ethusnic", VersionMeta.Version2013e, "InputOutput", 0x3ffff, [], ["admin"], ['adaptorHostEthIf'], [], ["Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "class_of_service": MoPropertyMeta("class_of_service", "classOfService", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[0-6]""", [], []),
            "coalescing_time": MoPropertyMeta("coalescing_time", "coalescingTime", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["0-65535"]),
            "coalescing_type": MoPropertyMeta("coalescing_type", "coalescingType", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["IDLE", "MIN"], []),
            "completion_queue_count": MoPropertyMeta("completion_queue_count", "completionQueueCount", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-512"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "interrupt_count": MoPropertyMeta("interrupt_count", "interruptCount", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-514"]),
            "large_receive": MoPropertyMeta("large_receive", "largeReceive", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "receive_queue_count": MoPropertyMeta("receive_queue_count", "receiveQueueCount", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["1-256"]),
            "receive_queue_ring_size": MoPropertyMeta("receive_queue_ring_size", "receiveQueueRingSize", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], ["64-16384"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x400, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "tcp_rx_checksum": MoPropertyMeta("tcp_rx_checksum", "tcpRxChecksum", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "tcp_segment": MoPropertyMeta("tcp_segment", "tcpSegment", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "tcp_tx_checksum": MoPropertyMeta("tcp_tx_checksum", "tcpTxChecksum", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "transmit_queue_count": MoPropertyMeta("transmit_queue_count", "transmitQueueCount", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], ["1-256"]),
            "transmit_queue_ring_size": MoPropertyMeta("transmit_queue_ring_size", "transmitQueueRingSize", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, [], ["64-16384"]),
            "usnic_count": MoPropertyMeta("usnic_count", "usnicCount", "uint", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, [], ["1-225"]),
        },

        "modular": {
            "class_of_service": MoPropertyMeta("class_of_service", "classOfService", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[0-6]""", [], []),
            "coalescing_time": MoPropertyMeta("coalescing_time", "coalescingTime", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["0-65535"]),
            "coalescing_type": MoPropertyMeta("coalescing_type", "coalescingType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["IDLE", "MIN"], []),
            "completion_queue_count": MoPropertyMeta("completion_queue_count", "completionQueueCount", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-512"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "interrupt_count": MoPropertyMeta("interrupt_count", "interruptCount", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-514"]),
            "large_receive": MoPropertyMeta("large_receive", "largeReceive", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "receive_queue_count": MoPropertyMeta("receive_queue_count", "receiveQueueCount", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["1-256"]),
            "receive_queue_ring_size": MoPropertyMeta("receive_queue_ring_size", "receiveQueueRingSize", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], ["64-4096"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "tcp_rx_checksum": MoPropertyMeta("tcp_rx_checksum", "tcpRxChecksum", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "tcp_segment": MoPropertyMeta("tcp_segment", "tcpSegment", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "tcp_tx_checksum": MoPropertyMeta("tcp_tx_checksum", "tcpTxChecksum", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "transmit_queue_count": MoPropertyMeta("transmit_queue_count", "transmitQueueCount", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], ["1-256"]),
            "transmit_queue_ring_size": MoPropertyMeta("transmit_queue_ring_size", "transmitQueueRingSize", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, [], ["64-4096"]),
            "usnic_count": MoPropertyMeta("usnic_count", "usnicCount", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, [], ["1-225"]),
        },

    }

    prop_map = {

        "classic": {
            "classOfService": "class_of_service", 
            "coalescingTime": "coalescing_time", 
            "coalescingType": "coalescing_type", 
            "completionQueueCount": "completion_queue_count", 
            "dn": "dn", 
            "interruptCount": "interrupt_count", 
            "largeReceive": "large_receive", 
            "receiveQueueCount": "receive_queue_count", 
            "receiveQueueRingSize": "receive_queue_ring_size", 
            "rn": "rn", 
            "status": "status", 
            "tcpRxChecksum": "tcp_rx_checksum", 
            "tcpSegment": "tcp_segment", 
            "tcpTxChecksum": "tcp_tx_checksum", 
            "transmitQueueCount": "transmit_queue_count", 
            "transmitQueueRingSize": "transmit_queue_ring_size", 
            "usnicCount": "usnic_count", 
        },

        "modular": {
            "classOfService": "class_of_service", 
            "coalescingTime": "coalescing_time", 
            "coalescingType": "coalescing_type", 
            "completionQueueCount": "completion_queue_count", 
            "dn": "dn", 
            "interruptCount": "interrupt_count", 
            "largeReceive": "large_receive", 
            "receiveQueueCount": "receive_queue_count", 
            "receiveQueueRingSize": "receive_queue_ring_size", 
            "rn": "rn", 
            "status": "status", 
            "tcpRxChecksum": "tcp_rx_checksum", 
            "tcpSegment": "tcp_segment", 
            "tcpTxChecksum": "tcp_tx_checksum", 
            "transmitQueueCount": "transmit_queue_count", 
            "transmitQueueRingSize": "transmit_queue_ring_size", 
            "usnicCount": "usnic_count", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.class_of_service = None
        self.coalescing_time = None
        self.coalescing_type = None
        self.completion_queue_count = None
        self.interrupt_count = None
        self.large_receive = None
        self.receive_queue_count = None
        self.receive_queue_ring_size = None
        self.status = None
        self.tcp_rx_checksum = None
        self.tcp_segment = None
        self.tcp_tx_checksum = None
        self.transmit_queue_count = None
        self.transmit_queue_ring_size = None
        self.usnic_count = None

        ManagedObject.__init__(self, "AdaptorEthUSNICProfile", parent_mo_or_dn, **kwargs)

