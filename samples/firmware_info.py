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
This module gets firmware related information.
"""

from imcsdk.imccoreutils import write_object


def firmware_info(handle, dump=True):
    """
    Gets the current running firmware info.

    Args:
        handle (ImcHandle)
        dump (bool): True or False

    Returns:
        FirmwareRunning: Managed Object

    Example:
        firmware_info(handle, dump=False)

    """

    firmware_list = handle.query_classid(class_id="firmwareRunning")
    if dump:
        write_object(mo_or_list=firmware_list)
    else:
        return firmware_list
