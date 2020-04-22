# Copyright 2017 Cisco Systems, Inc.
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
This module performs the firmware version related checks for all and specific
apis.
"""
import logging

log = logging.getLogger('imc')


def fix_bootloader_options(handle, boot_device=None):
    # In HP release: 4.0(1a), bootloader parameters are made mandatory.
    # This causes an issue if these parameters need to be cleared or
    # if a device needs to be created with no bootloader options
    # handle has been kept here to see if any more version checks need to be added.
    # Although, it is expected that CIMC will fix this issue in the future, it is not guaranteed.
    # Hence, this function does the job of skipping bootloader options if nothing has been set today.
    # From intersight we do not have a case of modification of an existing boot device where we need to clear these params
    # Hence the below fix of skipping them will work for now.

    if boot_device is None:
        return

    for key, value in boot_device.items():
        if key in ['boot_loader_name', 'boot_loader_path', 'boot_loader_descr'] and value == "":
            boot_device.pop(key, None)

    return
