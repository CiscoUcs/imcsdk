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
This is an auto-generated module.
It contains supporting classes for External Method.

"""

from . import imcgenutils
from . import imccoreutils as coreutils
from .imcmethod import ExternalMethod
from .imccoremeta import WriteXmlOption
from .imcconstants import YesOrNo


def aaa_get_compute_auth_tokens(cookie):
    """ Auto-generated IMC XML API Method. """
    method = ExternalMethod("AaaGetComputeAuthTokens")

    method.cookie = cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_keep_alive(cookie):
    """ Auto-generated IMC XML API Method. """
    method = ExternalMethod("AaaKeepAlive")

    method.cookie = cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_login(in_name, in_password):
    """ Auto-generated IMC XML API Method. """
    method = ExternalMethod("AaaLogin")

    method.in_name = in_name
    method.in_password = in_password

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_logout(in_cookie):
    """ Auto-generated IMC XML API Method. """
    method = ExternalMethod("AaaLogout")

    method.in_cookie = in_cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_refresh(in_cookie, in_name, in_password):
    """ Auto-generated IMC XML API Method. """
    method = ExternalMethod("AaaRefresh")

    method.in_cookie = in_cookie
    method.in_name = in_name
    method.in_password = in_password

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_conf_mo(cookie, dn, in_config, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated IMC XML API Method. """
    method = ExternalMethod("ConfigConfMo")

    method.cookie = cookie
    method.dn = dn
    method.in_config = in_config
    method.in_hierarchical = (("false", "true")[in_hierarchical in imcgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_conf_mos(cookie, in_configs, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated IMC XML API Method. """
    method = ExternalMethod("ConfigConfMos")

    method.cookie = cookie
    method.in_configs = in_configs
    method.in_hierarchical = (("false", "true")[in_hierarchical in imcgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_children(cookie, class_id, in_dn, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated IMC XML API Method. """
    method = ExternalMethod("ConfigResolveChildren")

    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = imcgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_dn = in_dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in imcgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_class(cookie, class_id, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated IMC XML API Method. """
    method = ExternalMethod("ConfigResolveClass")

    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = imcgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_hierarchical = (("false", "true")[in_hierarchical in imcgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_dn(cookie, dn, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated IMC XML API Method. """
    method = ExternalMethod("ConfigResolveDn")

    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in imcgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_parent(cookie, dn, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated IMC XML API Method. """
    method = ExternalMethod("ConfigResolveParent")

    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in imcgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def event_subscribe(cookie):
    """ Auto-generated IMC XML API Method. """
    method = ExternalMethod("EventSubscribe")

    method.cookie = cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def event_unsubscribe(cookie):
    """ Auto-generated IMC XML API Method. """
    method = ExternalMethod("EventUnsubscribe")

    method.cookie = cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request

