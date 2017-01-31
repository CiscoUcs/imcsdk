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


"""
This module demonstrates the use of health and fault related functionality
"""


def faults_get(handle, parent_class_id=None, dump=False):
    """
    Fetch fault related information.
    By default, fetches all the faults in the system.

    Args:
        handle (ImcHandle)
        parent_class_id (string): Class Id for which faults are needed.
        dump (bool): True or False

    Returns:
        FaultInst: List of Managed Objects

    Examples:
        faults_get(handle, parent_class_id="computeRackUnit", dump=False)
        faults_get(handle, dump=True)
    """

    from imcsdk.imccoreutils import write_object

    if parent_class_id:
        fault_list = []
        pmos = handle.query_classid(parent_class_id)
        for mo in pmos:
            fault_list.append(handle.query_children(in_mo=mo,
                                                    class_id="FaultInst"))
    else:
        fault_list = handle.query_classid(class_id="FaultInst")

    if dump:
        write_object(fault_list)

    return fault_list
