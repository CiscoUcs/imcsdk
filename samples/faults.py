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

"""
This module gets faults related information.
"""


def get_faults(handle, parent_class_id=None, dump=True):
    """
    Fetch fault related information

    Args:
        handle (ImcHandle)
        parent_class_id (string): Class Id for which faults are needed. If \n
                                None then get all faults.
        dump (bool): True or False
    Returns:
        FaultInst: Managed Object

    Example:
        get_faults(handle, parent_class_id="computeRackUnit", dump=False)
        get_faults(handle,dump=True)
    """

    from imcsdk.imccoreutils import write_object

    if parent_class_id is not None:
        fault_list = []

        pmo = handle.query_classid(parent_class_id)
        for mo in pmo:
            fault_list.append(handle.query_children(in_mo=mo,
                                                    class_id="FaultInst"))
    else:
        fault_list = handle.query_classid(class_id="FaultInst")
    if dump:
        write_object(fault_list)
    else:
        return fault_list
