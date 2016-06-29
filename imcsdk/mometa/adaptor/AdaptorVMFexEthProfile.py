"""This module contains the general information for AdaptorVMFexEthProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorVMFexEthProfileConsts:
    pass


class AdaptorVMFexEthProfile(ManagedObject):
    """This is AdaptorVMFexEthProfile class."""

    consts = AdaptorVMFexEthProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorVMFexEthProfile", "adaptorVMFexEthProfile", "vmfexprofile", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'adaptorVMFexEthIf'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "coalescing_time": MoPropertyMeta("coalescing_time", "coalescingTime", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "coalescing_type": MoPropertyMeta("coalescing_type", "coalescingType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "completion_queue_count": MoPropertyMeta("completion_queue_count", "completionQueueCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "completion_queue_ring_size": MoPropertyMeta("completion_queue_ring_size", "completionQueueRingSize", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
        "interrupt_count": MoPropertyMeta("interrupt_count", "interruptCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "interrupt_mode": MoPropertyMeta("interrupt_mode", "interruptMode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "large_receive": MoPropertyMeta("large_receive", "largeReceive", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[a-zA-Z0-9\-\._:]{1,32}""", [], []), 
        "pci_order": MoPropertyMeta("pci_order", "pciOrder", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "receive_queue_count": MoPropertyMeta("receive_queue_count", "receiveQueueCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "receive_queue_ring_size": MoPropertyMeta("receive_queue_ring_size", "receiveQueueRingSize", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "receive_side_scaling": MoPropertyMeta("receive_side_scaling", "receiveSideScaling", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "receive_side_scaling_ext_ip_v6_hash": MoPropertyMeta("receive_side_scaling_ext_ip_v6_hash", "receiveSideScalingExtIpV6Hash", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "receive_side_scaling_ext_tcp_ip_v6_hash": MoPropertyMeta("receive_side_scaling_ext_tcp_ip_v6_hash", "receiveSideScalingExtTCPIpV6Hash", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "receive_side_scaling_ip_v4_hash": MoPropertyMeta("receive_side_scaling_ip_v4_hash", "receiveSideScalingIpV4Hash", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "receive_side_scaling_ip_v6_hash": MoPropertyMeta("receive_side_scaling_ip_v6_hash", "receiveSideScalingIpV6Hash", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "receive_side_scaling_tcp_ip_v4_hash": MoPropertyMeta("receive_side_scaling_tcp_ip_v4_hash", "receiveSideScalingTCPIpV4Hash", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "receive_side_scaling_tcp_ip_v6_hash": MoPropertyMeta("receive_side_scaling_tcp_ip_v6_hash", "receiveSideScalingTCPIpV6Hash", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        "tcp_rx_checksum": MoPropertyMeta("tcp_rx_checksum", "tcpRxChecksum", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "tcp_segment": MoPropertyMeta("tcp_segment", "tcpSegment", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "tcp_tx_checksum": MoPropertyMeta("tcp_tx_checksum", "tcpTxChecksum", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        "transmit_queue_count": MoPropertyMeta("transmit_queue_count", "transmitQueueCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "transmit_queue_ring_size": MoPropertyMeta("transmit_queue_ring_size", "transmitQueueRingSize", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "trusted_class_of_service": MoPropertyMeta("trusted_class_of_service", "trustedClassOfService", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "coalescingTime": "coalescing_time", 
        "coalescingType": "coalescing_type", 
        "completionQueueCount": "completion_queue_count", 
        "completionQueueRingSize": "completion_queue_ring_size", 
        "dn": "dn", 
        "interruptCount": "interrupt_count", 
        "interruptMode": "interrupt_mode", 
        "largeReceive": "large_receive", 
        "name": "name", 
        "pciOrder": "pci_order", 
        "receiveQueueCount": "receive_queue_count", 
        "receiveQueueRingSize": "receive_queue_ring_size", 
        "receiveSideScaling": "receive_side_scaling", 
        "receiveSideScalingExtIpV6Hash": "receive_side_scaling_ext_ip_v6_hash", 
        "receiveSideScalingExtTCPIpV6Hash": "receive_side_scaling_ext_tcp_ip_v6_hash", 
        "receiveSideScalingIpV4Hash": "receive_side_scaling_ip_v4_hash", 
        "receiveSideScalingIpV6Hash": "receive_side_scaling_ip_v6_hash", 
        "receiveSideScalingTCPIpV4Hash": "receive_side_scaling_tcp_ip_v4_hash", 
        "receiveSideScalingTCPIpV6Hash": "receive_side_scaling_tcp_ip_v6_hash", 
        "rn": "rn", 
        "status": "status", 
        "tcpRxChecksum": "tcp_rx_checksum", 
        "tcpSegment": "tcp_segment", 
        "tcpTxChecksum": "tcp_tx_checksum", 
        "transmitQueueCount": "transmit_queue_count", 
        "transmitQueueRingSize": "transmit_queue_ring_size", 
        "trustedClassOfService": "trusted_class_of_service", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.coalescing_time = None
        self.coalescing_type = None
        self.completion_queue_count = None
        self.completion_queue_ring_size = None
        self.interrupt_count = None
        self.interrupt_mode = None
        self.large_receive = None
        self.name = None
        self.pci_order = None
        self.receive_queue_count = None
        self.receive_queue_ring_size = None
        self.receive_side_scaling = None
        self.receive_side_scaling_ext_ip_v6_hash = None
        self.receive_side_scaling_ext_tcp_ip_v6_hash = None
        self.receive_side_scaling_ip_v4_hash = None
        self.receive_side_scaling_ip_v6_hash = None
        self.receive_side_scaling_tcp_ip_v4_hash = None
        self.receive_side_scaling_tcp_ip_v6_hash = None
        self.status = None
        self.tcp_rx_checksum = None
        self.tcp_segment = None
        self.tcp_tx_checksum = None
        self.transmit_queue_count = None
        self.transmit_queue_ring_size = None
        self.trusted_class_of_service = None

        ManagedObject.__init__(self, "AdaptorVMFexEthProfile", parent_mo_or_dn, **kwargs)

