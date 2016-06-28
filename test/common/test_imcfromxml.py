# Copyright 2015 Cisco Systems, Inc.
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

from nose.tools import assert_equal


def test_001_mo_from_xml():
    import imcsdk.imcxmlcodec as xc

    response_str = '''
<configResolveClass cookie="0002618494/31e2450c-0262-1262-8802-0d8fd9f6083c" response="yes" classId="computeRackUnit">
<outConfigs>
<computeRackUnit dn="sys/rack-unit-1" adminPower="policy" availableMemory="131072" model="UCSC-C240-M3L" memorySpeed="1600" name="UCS C240 M3L" numOfAdaptors="1" numOfCores="16" numOfCoresEnabled="16" numOfCpus="2" numOfEthHostIfs="2" numOfFcHostIfs="2" numOfThreads="32" operPower="on" originalUuid="4A42480B-345D-4CD0-8824-A399795E279C" presence="equipped" serverId="1" serial="FCH1752V07Z" totalMemory="131072" usrLbl="hffgfg" uuid="4A42480B-345D-4CD0-8824-A399795E279C" vendor="Cisco Systems Inc" cimcResetReason="watchdog-reset">

<networkAdapterUnit slot="L" model="Intel Onboard 1Gbps Ethernet Adapter" numIntf="4" presence="equipped" rn="network-adapter-L" >
<networkAdapterEthIf id="1" mac="3c:08:f6:d9:8f:12" rn="eth-1" ></networkAdapterEthIf>
<networkAdapterEthIf id="2" mac="3c:08:f6:d9:8f:13" rn="eth-2" ></networkAdapterEthIf>
<networkAdapterEthIf id="3" mac="3c:08:f6:d9:8f:14" rn="eth-3" ></networkAdapterEthIf>
</networkAdapterUnit>
</computeRackUnit>
</outConfigs>
</configResolveClass>
    '''

    response = xc.from_xml_str(response_str)
    assert_equal(response.out_configs.child[0].__class__.__name__,
                 'ComputeRackUnit')
    assert_equal(response.out_configs.child[0].child[0].__class__.__name__,
                 'NetworkAdapterUnit')
    assert_equal(response.out_configs.child[0].child[0].child[0].__class__.__name__,
                 'NetworkAdapterEthIf')
