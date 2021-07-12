# Copyright 2016 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import logging
import logging.handlers

log = logging.getLogger('imc')
console = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)


def enable_file_logging(filename="imcsdk.log"):
    file_handler = logging.handlers.RotatingFileHandler(
              filename, maxBytes=10*1024*1024, backupCount=5)
    log.addHandler(file_handler)


def set_log_level(level=logging.DEBUG):
    """
    Allows setting log level

    Args:
        level: logging level - import logging and pass enums from it(INFO/DEBUG/ERROR/etc..)

    Returns:
        None

    Example:
        from imcsdk import set_log_level
        import logging

        set_log_level(logging.INFO)
    """
    log.setLevel(level)
    console.setLevel(level)

set_log_level(logging.DEBUG)

log.addHandler(console)

if os.path.exists('/tmp/imcsdk_debug'):
    enable_file_logging()

__author__ = 'Cisco Systems'
__email__ = 'ucs-python@cisco.com'
__version__ = '0.9.11'
