# Copyright 2016 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from nose.tools import raises
from ..connection.info import custom_setup, custom_teardown

from imcsdk.imcexception import ImcOperationError, ImcException
from imcsdk.apis.server.vic import vnic_create, vnic_create_all
from imcsdk.apis.server.vic import vnic_delete_all


handle = None

def setup_module():
    global handle
    handle = custom_setup()


def teardown_module():
    custom_teardown(handle)

vnics = [
    {"AdaptorEthCompQueueProfile.Count":5,"AdaptorEthGenProfile.Arfs":"disabled","AdaptorEthGenProfile.Nvgre":"disabled","AdaptorEthGenProfile.Order":2,"AdaptorEthGenProfile.PciLink":0,"AdaptorEthGenProfile.RateLimit":"OFF","AdaptorEthGenProfile.TrustedClassOfService":"disabled","AdaptorEthGenProfile.Vlan":100,"AdaptorEthGenProfile.VlanMode":"ACCESS","AdaptorEthGenProfile.Vmq":"disabled","AdaptorEthGenProfile.Vxlan":"disabled","AdaptorEthInterruptProfile.CoalescingTime":128,"AdaptorEthInterruptProfile.CoalescingType":"MIN","AdaptorEthInterruptProfile.Count":9,"AdaptorEthInterruptProfile.Mode":"MSI","AdaptorEthOffloadProfile.LargeReceive":"enabled","AdaptorEthOffloadProfile.TcpRxChecksum":"enabled","AdaptorEthOffloadProfile.TcpSegment":"enabled","AdaptorEthOffloadProfile.TcpTxChecksum":"enabled","AdaptorEthRecvQueueProfile.Count":5,"AdaptorEthRecvQueueProfile.RingSize":510,"AdaptorEthUSNICProfile.CoalescingType":"MIN","AdaptorEthUSNICProfile.InterruptCount":9,"AdaptorEthUSNICProfile.LargeReceive":"enabled","AdaptorEthUSNICProfile.ReceiveQueueCount":5,"AdaptorEthUSNICProfile.ReceiveQueueRingSize":510,"AdaptorEthUSNICProfile.TcpRxChecksum":"enabled","AdaptorEthUSNICProfile.TcpSegment":"enabled","AdaptorEthUSNICProfile.TcpTxChecksum":"enabled","AdaptorEthUSNICProfile.TransmitQueueCount":2,"AdaptorEthUSNICProfile.TransmitQueueRingSize":100,"AdaptorEthUSNICProfile.coalescingTime":128,"AdaptorEthUSNICProfile.completionQueueCount":5,"AdaptorEthWorkQueueProfile.Count":2,"AdaptorEthWorkQueueProfile.RingSize":100,"AdaptorHostEthIf.AdvancedFilter":"disabled","AdaptorHostEthIf.Cdn":"vnic1","AdaptorHostEthIf.ClassOfService":4,"AdaptorHostEthIf.Mtu":2000,"AdaptorHostEthIf.Name":"vnic2","AdaptorHostEthIf.UplinkPort":1,"AdaptorRssProfile.ReceiveSideScaling":"enabled","AdaptorUnit.Id":"2","adaptorEthUSNICProfile.ClassOfService":5,"adaptorEthUSNICProfile.usnicCount":5},
    {"AdaptorEthCompQueueProfile.Count":5,"AdaptorEthGenProfile.Arfs":"disabled","AdaptorEthGenProfile.Nvgre":"disabled","AdaptorEthGenProfile.Order":3,"AdaptorEthGenProfile.PciLink":0,"AdaptorEthGenProfile.RateLimit":"OFF","AdaptorEthGenProfile.TrustedClassOfService":"disabled","AdaptorEthGenProfile.Vlan":100,"AdaptorEthGenProfile.VlanMode":"ACCESS","AdaptorEthGenProfile.Vmq":"disabled","AdaptorEthGenProfile.Vxlan":"disabled","AdaptorEthInterruptProfile.CoalescingTime":128,"AdaptorEthInterruptProfile.CoalescingType":"MIN","AdaptorEthInterruptProfile.Count":9,"AdaptorEthInterruptProfile.Mode":"MSI","AdaptorEthOffloadProfile.LargeReceive":"enabled","AdaptorEthOffloadProfile.TcpRxChecksum":"enabled","AdaptorEthOffloadProfile.TcpSegment":"enabled","AdaptorEthOffloadProfile.TcpTxChecksum":"enabled","AdaptorEthRecvQueueProfile.Count":5,"AdaptorEthRecvQueueProfile.RingSize":510,"AdaptorEthUSNICProfile.CoalescingType":"MIN","AdaptorEthUSNICProfile.InterruptCount":9,"AdaptorEthUSNICProfile.LargeReceive":"enabled","AdaptorEthUSNICProfile.ReceiveQueueCount":5,"AdaptorEthUSNICProfile.ReceiveQueueRingSize":510,"AdaptorEthUSNICProfile.TcpRxChecksum":"enabled","AdaptorEthUSNICProfile.TcpSegment":"enabled","AdaptorEthUSNICProfile.TcpTxChecksum":"enabled","AdaptorEthUSNICProfile.TransmitQueueCount":2,"AdaptorEthUSNICProfile.TransmitQueueRingSize":100,"AdaptorEthUSNICProfile.coalescingTime":128,"AdaptorEthUSNICProfile.completionQueueCount":5,"AdaptorEthWorkQueueProfile.Count":2,"AdaptorEthWorkQueueProfile.RingSize":100,"AdaptorHostEthIf.AdvancedFilter":"disabled","AdaptorHostEthIf.Cdn":"vnic3","AdaptorHostEthIf.ClassOfService":4,"AdaptorHostEthIf.Mtu":2000,"AdaptorHostEthIf.Name":"vnic3","AdaptorHostEthIf.UplinkPort":1,"AdaptorRssProfile.ReceiveSideScaling":"enabled","AdaptorUnit.Id":"2","adaptorEthUSNICProfile.ClassOfService":5,"adaptorEthUSNICProfile.usnicCount":5},
    {"AdaptorEthCompQueueProfile.Count":5,"AdaptorEthGenProfile.Arfs":"disabled","AdaptorEthGenProfile.Nvgre":"disabled","AdaptorEthGenProfile.Order":1,"AdaptorEthGenProfile.PciLink":0,"AdaptorEthGenProfile.RateLimit":"OFF","AdaptorEthGenProfile.TrustedClassOfService":"disabled","AdaptorEthGenProfile.Vlan":100,"AdaptorEthGenProfile.VlanMode":"ACCESS","AdaptorEthGenProfile.Vmq":"disabled","AdaptorEthGenProfile.Vxlan":"disabled","AdaptorEthInterruptProfile.CoalescingTime":128,"AdaptorEthInterruptProfile.CoalescingType":"MIN","AdaptorEthInterruptProfile.Count":9,"AdaptorEthInterruptProfile.Mode":"MSI","AdaptorEthOffloadProfile.LargeReceive":"enabled","AdaptorEthOffloadProfile.TcpRxChecksum":"enabled","AdaptorEthOffloadProfile.TcpSegment":"enabled","AdaptorEthOffloadProfile.TcpTxChecksum":"enabled","AdaptorEthRecvQueueProfile.Count":5,"AdaptorEthRecvQueueProfile.RingSize":510,"AdaptorEthWorkQueueProfile.Count":2,"AdaptorEthWorkQueueProfile.RingSize":100,"AdaptorHostEthIf.AdvancedFilter":"disabled","AdaptorHostEthIf.Cdn":"","AdaptorHostEthIf.ClassOfService":4,"AdaptorHostEthIf.Mtu":2000,"AdaptorHostEthIf.Name":"eth0","AdaptorHostEthIf.UplinkPort":0,"AdaptorRssProfile.ReceiveSideScaling":"enabled","AdaptorUnit.Id":"2"},
    {"AdaptorEthCompQueueProfile.Count":5,"AdaptorEthGenProfile.Arfs":"disabled","AdaptorEthGenProfile.Nvgre":"disabled","AdaptorEthGenProfile.Order":0,"AdaptorEthGenProfile.PciLink":0,"AdaptorEthGenProfile.RateLimit":"OFF","AdaptorEthGenProfile.TrustedClassOfService":"disabled","AdaptorEthGenProfile.Vlan":100,"AdaptorEthGenProfile.VlanMode":"ACCESS","AdaptorEthGenProfile.Vmq":"disabled","AdaptorEthGenProfile.Vxlan":"disabled","AdaptorEthInterruptProfile.CoalescingTime":128,"AdaptorEthInterruptProfile.CoalescingType":"MIN","AdaptorEthInterruptProfile.Count":9,"AdaptorEthInterruptProfile.Mode":"MSI","AdaptorEthOffloadProfile.LargeReceive":"enabled","AdaptorEthOffloadProfile.TcpRxChecksum":"enabled","AdaptorEthOffloadProfile.TcpSegment":"enabled","AdaptorEthOffloadProfile.TcpTxChecksum":"enabled","AdaptorEthRecvQueueProfile.Count":5,"AdaptorEthRecvQueueProfile.RingSize":510,"AdaptorEthWorkQueueProfile.Count":2,"AdaptorEthWorkQueueProfile.RingSize":100,"AdaptorHostEthIf.AdvancedFilter":"disabled","AdaptorHostEthIf.Cdn":"","AdaptorHostEthIf.ClassOfService":4,"AdaptorHostEthIf.Mtu":2000,"AdaptorHostEthIf.Name":"eth1","AdaptorHostEthIf.UplinkPort":0,"AdaptorRssProfile.ReceiveSideScaling":"enabled","AdaptorUnit.Id":"2"}
]


def test_vnic_delete_all():
    vnic_delete_all(handle)


def test_vnic_create_all():
    vnic_create_all(handle, vnics)


