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


import logging
from imcsdk.imcexception import ImcOperationError

log = logging.getLogger('imc')


def _get_mo(handle, dn=None, **kwargs):

    if handle is None:
        raise ImcOperationError("Get Managed Object for dn:%s" % dn,
                                "Handle is None")

    if dn:
        mo = handle.query_dn(dn)
        if mo is None:
            raise ImcOperationError("Get Managed Object for dn:%s" % dn,
                                    "Managed Object doesn't exist")
        return mo

    return None


def _is_invalid_value(value):
    return value in ["", None]


def _is_valid_arg(param, kwargs):
    return kwargs.get(param) is not None
