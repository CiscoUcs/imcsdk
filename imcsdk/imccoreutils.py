# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License prop
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains the ImcSdk Core utilities.
"""

import os
import re
import logging

from . import imcgenutils
from . import mometa
from . import methodmeta
from . imcmeta import MO_CLASS_ID, METHOD_CLASS_ID, OTHER_TYPE_CLASS_ID, \
    MO_CLASS_META
from .imcexception import ImcOperationError, ImcValidationException, \
    ImcOperationErrorDetail
from .imccoremeta import MoPropertyMeta

log = logging.getLogger('imc')


class ConfigConfMosConstants:
    RESPONSE_MO_IS_CONFIGURED = 'is_configured'
    RESPONSE_OBJECT = 'response_object'
    RESPONSE_MOS = 'response_mos'
    RESPONSE_STATUS = 'response_status'
    RESPONSE_STATUS_FAIL = 'failure'
    RESPONSE_STATUS_SUCCESS = 'success'
    RESPONSE_STATUS_PART_SUCCESS = 'paritial success'
    RESPONSE_FAILED_MOS = 'failed'
    RESPONSE_PASSED_MOS = 'passed'


class IMC_PLATFORM:
    TYPE_MODULAR = "modular"
    TYPE_CLASSIC = "classic"

IMC_PLATFORM_LIST = [IMC_PLATFORM.TYPE_CLASSIC,
                     IMC_PLATFORM.TYPE_MODULAR]
global_handles = []


def get_imc_obj(class_id, elem, mo_obj=None):
    """
    This creates object of type ExternalMethod or ManagedObject or GenericMo
    depending on element tag

    Args:
        class_id (str): class id
        elem (xml element): xml element
        mo_obj : parent managed object

    Returns:
        object of type ExternalMethod or ManagedObject or GenericMo
    """

    import inspect

    from . import imcmethod
    from . import imcmo
    from . import imccore

    if class_id in METHOD_CLASS_ID:
        return imcmethod.ExternalMethod(class_id)
    elif class_id in MO_CLASS_ID:
        mo_class = load_class(class_id)
        mo_class_params = inspect.getargspec(mo_class.__init__)[0][2:]
        mo_class_param_dict = {}
        for param in mo_class_params:
            mo_class_param_dict[param] = None

        p_dn = ""
        if "dn" in elem.attrib:
            p_dn = os.path.dirname(elem.attrib["dn"])
        elif "rn" in elem.attrib and mo_obj:
            p_dn = mo_obj.dn

        mo_meta = get_mo_meta(mo_class)
        class_parents = mo_meta.parents
        if 'topRoot' in class_parents:
            mo_obj = mo_class(from_xml_response=True, **mo_class_param_dict)
        else:
            mo_obj = mo_class(parent_mo_or_dn=p_dn,
                              from_xml_response=True, **mo_class_param_dict)
        return mo_obj
    elif class_id in OTHER_TYPE_CLASS_ID:
        module_ = load_module(class_id)
        return getattr(module_, class_id)()
    elif class_id == 'OperationStatus':
        mo_obj = imccore.OperationStatus(operation_status=elem.text)
        return mo_obj

    # This case handles object types that are not known to this version
    # of the SDK. This case can arise when the IMC server has higher
    # version with more objects and the SDK is not at the latest
    # version yet.

    p_dn = ""
    if "dn" in elem.attrib:
        p_dn = os.path.dirname(elem.attrib["dn"])
    elif mo_obj:
        p_dn = mo_obj.dn

    mo_obj = imcmo.GenericMo(class_id=elem.tag, parent_mo_or_dn=p_dn,
                             **elem.attrib)
    return mo_obj


def load_module(module_name):
    """
    This loads the module into the current name space

    Args:
        module_name (str): module_name

    Returns:
        module_import
    """

    module_name = imcgenutils.word_u(module_name)
    if module_name and module_name in MO_CLASS_ID:
        fq_module_name = mometa.__name__ + ".%s" % module_name
        module_import = __import__(fq_module_name, globals(), locals(),
                                   [module_name])
        return module_import
    elif module_name and module_name in METHOD_CLASS_ID:
        fq_module_name = methodmeta.__name__ + ".%sMeta" % module_name
        module_import = __import__(fq_module_name, globals(), locals(),
                                   [module_name])
        return module_import
    elif module_name and module_name in OTHER_TYPE_CLASS_ID:
        fq_module_name = OTHER_TYPE_CLASS_ID[module_name]
        module_import = __import__(fq_module_name, globals(), locals(),
                                   [module_name], level=1)
        return module_import


def load_class(class_id):
    """
    This loads the class into the current name space

    Args:
        class_id (str): class_id

    Returns:
        MangedObject or ExtenalMethod Object or None
    """

    class_id = imcgenutils.word_u(class_id)
    if class_id and class_id in MO_CLASS_ID:
        mod_class_id = imcgenutils.word_l(class_id)
        class_id_sub_pkg = re.match("([a-z])+", mod_class_id).group()
        mo_pkg = mometa.__name__ + ".%s.%s" % (class_id_sub_pkg, class_id)
        mo_module = __import__(mo_pkg, globals(), locals(), [class_id])
        mo_class = getattr(mo_module, class_id)
        return mo_class
    elif class_id and class_id in METHOD_CLASS_ID:
        mo_import = methodmeta.__name__ + ".%sMeta" % (class_id)
        method_meta = __import__(mo_import, globals(), locals(),
                                 [class_id])
        return getattr(method_meta, class_id)
    return None


def load_mo(elem):
    """
    This loads the managed object  into the current name space

    Args:
        elem (str): element

    Returns:
        MangedObject
    """

    import inspect

    mo_class_id = elem.tag
    mo_class = load_class(mo_class_id)
    mo_class_params = inspect.getargspec(mo_class.__init__)[0][2:]
    mo_class_param_dict = {}
    for param in mo_class_params:
        mo_class_param_dict[param] = elem.attrib[
            mo_class.PROPERTY_MAP[param]]

    mo_obj = mo_class(parent_mo_or_dn="", **mo_class_param_dict)
    return mo_obj


def is_valid_class_id(class_id):
    """
    Methods checks whether the provided class_id is valid or not."""

    if class_id in MO_CLASS_ID or class_id in METHOD_CLASS_ID:
        return True
    return False


def find_class_id_in_mo_meta_ignore_case(class_id):
    """
    Methods whether class_id is valid or not . Given class is case insensitive.
    """

    if not class_id:
        return None
    if class_id in MO_CLASS_ID:
        return class_id
    l_class_id = class_id.lower()
    for key in MO_CLASS_ID:
        if key.lower() == l_class_id:
            return key
    return None


def find_class_id_in_method_meta_ignore_case(class_id):
    """
    Methods whether class_id is valid or not . Given class is case insensitive.
    """

    if class_id in METHOD_CLASS_ID:
        return class_id
    l_class_id = class_id.lower()
    for key in METHOD_CLASS_ID:
        if key.lower() == l_class_id:
            return key
    return None


def get_mo_property_meta(class_id, key, platform=None):
    """
    Methods returns the mo property meta of the provided key for the given
    class_id.

    Args:
        class_id (str): class_id of mo
        key (str): prop of class_id

    Returns:
        Object of type MoPropertyMeta

    Example:
        prop_meta = get_mo_property_meta(class_id="aaaUser", key="usr_lbl")
    """

    class_obj = load_class(class_id)

    if platform is None:
        platform = IMC_PLATFORM.TYPE_CLASSIC

    if key == "mo_meta":
        return class_obj.mo_meta[platform]

    prop_meta = class_obj.prop_meta[platform]
    prop_map = class_obj.prop_map[platform]
    if key in prop_map:
        return prop_meta[prop_map[key]]
    elif key in prop_meta:
        return prop_meta[key]
    return None


def write_object(mo_or_list):
    """
    This prints the managed object on the standard output.
    """

    from . import imcmethod
    from . import imcmo
    if isinstance(mo_or_list, imcmethod.ExternalMethod):
        if hasattr(mo_or_list, "out_config"):
            for child in mo_or_list.out_config.child:
                if isinstance(child, imcmo.ManagedObject):
                    write_object(child)
    elif isinstance(mo_or_list, list) and len(mo_or_list) > 0:
        for mo in mo_or_list:
            if (isinstance(mo, imcmo.ManagedObject) or
                    isinstance(mo, imcmo.GenericMo)):
                print(mo)
    elif (isinstance(mo_or_list, imcmo.ManagedObject) or
            isinstance(mo_or_list, imcmo.GenericMo)):
        print(mo_or_list)


def extract_molist_from_method_response(method_response,
                                        in_hierarchical=False):
    """
    Methods extracts mo list from response received from imc server i.e.
    external method object

    Args:
        method_response (ExternalMethod Object): response
        in_hierarchical (bool): if True, return all the hierarchical child of
                                    managed objects

    Returns:
        List of ManagedObjects

    Example:
        response = handle.query_dn("sys/rack-unit-1", need_response=True)\n
        molist = extract_molist_from_method_response(method_response=response,
                in_hierarchical=True)
    """

    mo_list = []
    if hasattr(method_response, "out_config"):
        if len(method_response.out_config.child) == 0:
            return mo_list
    else:
        if len(method_response.out_configs.child) == 0:
            return mo_list
    if in_hierarchical:
        if hasattr(method_response, "out_config"):
            current_mo_list = method_response.out_config.child
        else:
            current_mo_list = method_response.out_configs.child
        while len(current_mo_list) > 0:
            child_mo_list = []
            for mo in current_mo_list:
                mo_list.append(mo)
                while mo.child_count() > 0:
                    for child in mo.child:
                        mo.child_remove(child)
                        child.mark_clean()
                        child_mo_list.append(child)
                        break
            current_mo_list = child_mo_list
    else:
        mo_list = method_response.out_configs.child

    return mo_list


def filter_molist_on_class_id(mo_list, class_id=None):
    if not class_id:
        return mo_list

    out_list = [mo for mo in mo_list if mo._class_id.lower() == class_id.lower()]
    return out_list


def write_mo_tree(mo, level=0, depth=None, show_level=[],
                  print_tree=True, tree_dict={}, dn=None):
    """
    Prints tree structure of any managed object

    Args:
        mo (object): ManagedObject
        level (int): by default zero
        depth (int or None): last level to process
        show_level (int list): levels to display
        print_tree (bool): if True, print mo tree
        tree_dict (dict): by default {}
        dn (str): dn

    Returns:
        dictionary

    Example:
        mo=handle.query_dn("sys/rack-unit-1")\n
        tree_dict = write_mo_tree(mo, depth=3, show_level=[1, 3])\n
    """

    if not mo.dn:
        mo.dn = dn
    indent = "    "

    level_indent = "%s%s)" % (indent * level, level)

    level_key_dn = "level_%s_dn" % (str(level))
    if level_key_dn not in tree_dict:
        tree_dict[level_key_dn] = {mo.dn: mo}
    else:
        tree_dict[level_key_dn][mo.dn] = mo

    level_key_mo = "level_%s_mo" % (str(level))
    if level_key_mo not in tree_dict:
        tree_dict[level_key_mo] = {mo.class_id: [mo]}
    else:
        if mo.class_id not in tree_dict[level_key_mo]:
            tree_dict[level_key_mo][mo.class_id] = [mo]
        else:
            tree_dict[level_key_mo][mo.class_id].append(mo)

    key_all_mo = "all_mo"
    if key_all_mo not in tree_dict:
        tree_dict[key_all_mo] = {mo.class_id: [mo]}
    else:
        if mo.class_id not in tree_dict[key_all_mo]:
            tree_dict[key_all_mo][mo.class_id] = [mo]
        else:
            tree_dict[key_all_mo][mo.class_id].append(mo)

    if print_tree:
        if not show_level:
            print(("%s %s (%s)" % (level_indent, mo.dn, mo.class_id)))
        elif level in show_level:
            print(("%s %s (%s)" % (level_indent, mo.dn, mo.class_id)))

    for child in mo.child:
        child.mark_clean()
        level += 1
        if depth is None:
            tree_dict = write_mo_tree(child, level, depth,
                                      show_level, print_tree,
                                      tree_dict, dn)
        elif level <= depth:
            tree_dict = write_mo_tree(child, level, depth,
                                      show_level, print_tree,
                                      tree_dict, dn)
        level -= 1

    return tree_dict


def extract_mo_tree_from_config_method_response(method_response,
                                                depth=None,
                                                show_level=[],
                                                print_tree=False,
                                                tree_dict={}):
    """
    extracts tree structure of any managed object from config method response

    Args:
        method_response (object): ExternalMethod
        depth (int or None): last level to process
        show_level (int list): levels to display
        print_tree (bool): if True, print mo tree
        tree_dict (dict): by default {}

    Returns:
        dictionary

    Example:
        response=handle.query_dn("sys/rack-unit-1", need_response=True)\n
        tree_dict = write_mo_tree(response, depth=3, show_level=[1, 3])\n
    """

    current_mo_list = method_response.out_config.child
    for current_mo in current_mo_list:
        level = 0
        tree_dict = write_mo_tree(current_mo, level, depth,
                                  show_level, print_tree,
                                  tree_dict)
    return tree_dict


def print_mo_hierarchy(class_id, level=0, depth=None,
                       show_level=[], platform=None):
    """
    print hierarchy of class_id

    Args:
        class_id (str): class id
        platform (str): "classic" or "modular"
        level (int): by default zero
        depth (int or None): last level to process
        show_level (int list): levels to display

    Returns:
        None

    Example:
        print_mo_hierarchy(class_id, level=0, depth=3, show_level=[1,3])\n
    """

    indent = " "
    level_indent = "%s%s)" % (indent * level, level)
    class_id = imcgenutils.word_u(class_id)

    if platform is None:
        platform = "classic"

    if level == 0:
        parents = [imcgenutils.word_u(parent) for parent in
                   MO_CLASS_META[platform][class_id].parents]
        print(("[%s]" % (", ".join(sorted(parents)))))

    if level == 0 or not show_level or level in show_level:
        print(("%s%s" % (level_indent, imcgenutils.word_u(class_id))))

    children = sorted(MO_CLASS_META[platform][class_id].children)

    level += 1
    if depth is None or level <= depth:
        for ch_ in children:
            child = imcgenutils.word_u(ch_)
            if child == class_id:
                continue
            print_mo_hierarchy(child, level, depth,
                               show_level, platform)
    level -= 1


def get_naming_props(rn_str, rn_pattern):
    """
    extract naming property and its value from a given rn and its pattern

    Args:
        rn_str (str): rn value
        rn_pattern (str): rn pattern from mo_meta

    Returns:
        dictionary

    Example:
        naming_props = get_naming_props(rn_str="psu-2",
                    rn_pattern="psu-[id]")
    """

    rn_regex = re.sub(r"\[(.+?)\]", r"(?P<\1>.+)", rn_pattern)
    rn_regex_pat = re.compile(rn_regex)
    match_obj = re.match(rn_regex_pat, rn_str)
    if match_obj is None:
        log.debug("Error getting naming props. rn_str: %s rn_pattern %s" %
                  (rn_str, rn_pattern))
        return {}
    naming_prop_dict = match_obj.groupdict()
    return naming_prop_dict


class ClassIdMeta(object):

    def __init__(
            self,
            class_id,
            include_prop=True,
            show_tree=True,
            depth=None,
            platform=None):
        if platform is None:
            platform = "classic"
        self.__mo_meta = MO_CLASS_META[platform][class_id]
        self.class_id = class_id
        self.xml_attribute = self.__mo_meta.xml_attribute
        self.rn = self.__mo_meta.rn
        self.min_version = self.__mo_meta.version
        self.access = self.__mo_meta.inp_out
        self.access_privilege = self.__mo_meta.access
        self.parents = self.__mo_meta.parents
        self.children = self.__mo_meta.children
        self.props = {}

        self._str_tree = "\n"
        self._str_props = "\n"

        if show_tree:
            self._str_tree = _show_tree(class_id, depth, platform=platform)

        if include_prop:
            class_obj = load_class(self.class_id)
            self.props = class_obj.prop_meta[platform]
            for prop in sorted(self.props):
                self._str_props += str(self.props[prop]) + "\n"

    def __str__(self):
        """
        Method to return string representation.
        """

        ts = 8
        out_str = ""

        out_str += self._str_tree

        out_str += "\n"
        out_str += str("ClassId").ljust(ts * 4) + str(self.class_id) + "\n"
        out_str += ("-" * len("ClassId")).ljust(ts * 4) + "-" * len(
            self.class_id)+"\n"
        out_str += str("xml_attribute").ljust(ts * 4) + ':' + str(
            self.xml_attribute) + "\n"
        out_str += str("rn").ljust(ts * 4) + ':' + str(
            self.rn) + "\n"
        out_str += str("min_version").ljust(ts * 4) + ':' + str(
            self.min_version) + "\n"
        out_str += str("access").ljust(ts * 4) + ':' + str(self.access) + "\n"
        out_str += str("access_privilege").ljust(ts * 4) + ':' + str(
            self.access_privilege) + "\n"
        out_str += str("parents").ljust(ts * 4) + ':' + str(self.parents) + \
            "\n"
        out_str += str("children").ljust(ts * 4) + ':' + str(self.children)

        out_str += self._str_props

        return out_str


def _show_tree(class_id, depth=None, level=0, ancestor_str="",
               ancestor=[], last_child=True, platform=None):

    meta_class_id = imcgenutils.word_u(class_id)

    out_str = ""

    if platform is None:
        platform = "classic"
    if not ancestor:
        for parent in sorted(MO_CLASS_META[platform][meta_class_id].parents):
            out_str += "[" + imcgenutils.word_u(parent) + "]" + "\n"

    index = len(ancestor) + 1

    level += 1

    if meta_class_id in ancestor:
        out_str += ancestor_str + "  |-" + meta_class_id + "\n"
    else:
        ancestor.append(meta_class_id)
        out_str += ancestor_str + "  |-" + meta_class_id + "\n"
        children = sorted(MO_CLASS_META[platform][meta_class_id].children)
        total = len(children)
        count = 0
        if depth is None or level < depth + 1:
            for child in children:
                count += 1

                if last_child:
                    ancestor_str_ = ancestor_str + "   "
                else:
                    ancestor_str_ = ancestor_str + "  |"

                out_str += _show_tree(child, depth, level,
                                      ancestor_str_, ancestor, total == count,
                                      platform=platform)

        ancestor.pop(index - 1)
    return out_str


def search_class_id(class_id):
    """
    case insensitive search for class_id in meta.
    if unable to find exact class_id, this will also suggest matching class_id.

    Args:
        class_id (str): string matching class_id.(case insensitive)

    Returns:
        (str) or None

    Example:
        class_ids = search_class_id(class_id="aaa")
    """

    from . import imcmeta

    meta_class_id = find_class_id_in_mo_meta_ignore_case(class_id=class_id)

    if meta_class_id:
        return meta_class_id

    # if class_id not exists in meta
    l_class_id = class_id.lower()
    class_ids = sorted([cid for cid in imcmeta.MO_CLASS_ID
                        if re.search(l_class_id, cid, re.IGNORECASE)])
    if class_ids:
        log.info('"%s" did not match any available Class Ids.\n'
                 'Related Class Ids are:\n%s\n%s' %
                 (class_id,
                  "-"*len("Related Class Ids are:"),
                  "\n".join(class_ids)))
    else:
        log.info('"%s" did not match any available Class Ids.' % class_id)


def get_meta_info(class_id, include_prop=True,
                  show_tree=True, depth=None,
                  platform=IMC_PLATFORM.TYPE_CLASSIC):
    """
    Gets class id meta information

    Args:
        class_id (str): string matching class_id.(case insensitive)
        include_prop (bool): by default True. If False, excludes property.
        show_tree (bool): by default True. If False will not display mo tree.
        depth (int): depth to which hierarchy is displayed.

    Returns:
        None: If class_id is not present in meta.
        Or
        ClassIdMeta Object: class_id
                            xml_attribute
                            rn
                            min_version
                            access
                            access_privilege
                            parents : parent list
                            children : children list
                            properties : property list
                            props : {property_name : MoPropertyMeta Object}

    Example:
        meta = get_meta_info(class_id="computerackunit")
        meta = get_meta_info(class_id="computerackunit", depth=2)
        meta = get_meta_info(class_id="computerackunit", include_prop=False)
        meta = get_meta_info(class_id="computerackunit", show_tree=False)

        print(meta.xml_attribute)
        print(meta.children)
        print(meta.props["name"])
    """

    meta_class_id = search_class_id(class_id)
    if not meta_class_id:
        return

    return ClassIdMeta(meta_class_id, include_prop, show_tree, depth, platform)


def prop_exists(mo, prop_name, platform=None):

    if platform:
        return(platform in list(mo.prop_meta.keys()) and
               prop_name in list(mo.prop_meta[platform].keys()))

    for platform in IMC_PLATFORM_LIST:
        if platform in list(mo.prop_meta.keys()) and \
                prop_name in list(mo.prop_meta[platform].keys()):
            return True

    return False


def _get_property_from_prop_meta_for_platform(mo, prop, platform):

    if platform in list(mo.prop_meta.keys()) and \
            prop in list(mo.prop_meta[platform].keys()):
        return mo.prop_meta[platform][prop]

    return None


def get_prop_meta(mo, prop, platform=None):
    """
    Internal Method that returns the property meta object
    """

    if platform:
        return _get_property_from_prop_meta_for_platform(mo, prop, platform)

    for platform in IMC_PLATFORM_LIST:
        prop_ = _get_property_from_prop_meta_for_platform(
                mo,
                prop,
                platform)
        if prop_:
            return prop_

    return None


def validate_property_value(mo, prop, value):

    messages = []
    for platform in IMC_PLATFORM_LIST:
        prop_ = _get_property_from_prop_meta_for_platform(
                mo,
                prop,
                platform)
        if prop_:
            match, msg = prop_.validate_property_value(value)
            if match:
                return match, msg
            else:
                messages.append("[" + platform + "]:" + msg)

    msg = ""
    if len(messages) != 0:
        msg = "Validation Errors are: "
        for s in messages:
            msg += s + ", "

    return False, msg


def is_writable_prop(mo, prop, platform=None):

    for platform in IMC_PLATFORM_LIST:
        prop_ = _get_property_from_prop_meta_for_platform(
                mo,
                prop,
                platform)
        if prop_ and prop_.access == MoPropertyMeta.READ_WRITE:
            return True

    return False


def property_exists_in_prop_map(mo, prop_name):

    for platform in IMC_PLATFORM_LIST:
        if platform in list(mo.prop_map.keys()) and \
                prop_name in list(mo.prop_map[platform].keys()):
            return True

    return False


def _get_property_from_prop_map_for_platform(mo, prop, platform):

    if platform in list(mo.prop_map.keys()) and \
            prop in list(mo.prop_map[platform].keys()):
        return mo.prop_map[platform][prop]

    return None


def get_property_from_prop_map(mo, prop, platform=None):

    if platform:
        return _get_property_from_prop_map_for_platform(mo, prop, platform)

    for platform in IMC_PLATFORM_LIST:
        prop_ = _get_property_from_prop_map_for_platform(
                mo,
                prop,
                platform)
        if prop_:
            return prop_

    return None


def get_mo_meta(mo, platform=None):

    if platform:
        try:
            return mo.mo_meta[platform]
        except KeyError:
            raise ImcValidationException("The Managed Object:%s "
                                         "does not exist for this platform"
                                         % (mo.__class__.__name__))

    for platform in IMC_PLATFORM_LIST:
        if platform in list(mo.mo_meta.keys()):
            return mo.mo_meta[platform]

    return None


def validate_mo_version(handle, mo):
    """
    This is called from add_mo/set_mo to verify if the mo is supported on
    the particular server
    """
    return

    try:
        mo_version = mo.get_version(platform=handle.platform)
    except ImcValidationException:
        raise ImcValidationException("This functionality is not supported "
                                     "on the current platform")

    if mo_version > handle.version:
        raise ImcOperationError(
                "Validate Version",
                "Platform(version:%s) does not support "
                "Managed Object:%s(supported since version:%s)"
                % (handle.version, mo.__class__.__name__, mo_version))


def get_server_dn(handle, server_id="1"):
    """
    This method gives the dn for a particular rack server based on
    the type of platform

    For classic: "sys/rack-unit-1"
    For modular: "sys/chassis-1/server-<server_id>"
    """

    if handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        return "sys/rack-unit-1"
    elif handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        return "sys/chassis-1/server-" + str(server_id)
    else:
        raise ImcOperationError("Unknown platform", "type:%s detected" %
                                handle.platform)


def get_dn_prefix_for_platform(handle):
    """
    This method checks the platform property from handle and returns the prefix
    for that specific platform

    Args:
        handle (ImcHandle)

    Returns:
        dn prefix in string format

    Examples:
        get_dn_prefix_for_platform(handle) => "sys/rack-unit-1/" for classic
        get_dn_prefix_for_platform(handle) => "sys/chassis-1/" for modular
    """

    if handle.platform == IMC_PLATFORM.TYPE_CLASSIC:
        return "sys/rack-unit-1"
    elif handle.platform == IMC_PLATFORM.TYPE_MODULAR:
        return "sys/chassis-1"
    else:
        return ""


def is_platform_m4(handle):
    return match_platform_type(handle, "M4")


def is_platform_m5(handle):
    return match_platform_type(handle, "M5") or \
        match_platform_type(handle, "C125")


def match_platform_type(handle, match_string):
    if handle.model:
        return handle.model.find(match_string) != -1
    return False


def _set_server_dn(handle, kwargs):
    server_id = kwargs.get("server_id", "1")
    return get_server_dn(handle, str(server_id))


def get_handle_from_cookie(cookie):

    for handle in global_handles:
        if handle.cookie == cookie:
            return handle

    return None


def add_handle_to_list(handle):
    if handle and handle not in global_handles:
        global_handles.append(handle)


def remove_handle_from_list(handle):
    if handle and handle in global_handles:
        global_handles.remove(handle)


def default_cb(dn, *args):
    return dn


def process_conf_mos_response(response, api='process_conf_mos_response',
                              raise_exception=True,
                              error_msg='Configuration Error',
                              callback=default_cb, *cbargs):
    from imcsdk.imccoreutils import ConfigConfMosConstants as Const
    messages = []
    if response[Const.RESPONSE_STATUS] != Const.RESPONSE_STATUS_SUCCESS:
        for dn, error in sorted(response[Const.RESPONSE_MOS][
                Const.RESPONSE_FAILED_MOS].items()):
            d = {}
            # log.debug("Error(%s) while processing dn(%s)" % (error, dn))
            d["Object"] = callback(dn, *cbargs)
            d["Error"] = error
            messages.append(d)

        if len(messages) != 0 and raise_exception:
            raise ImcOperationErrorDetail(api, error_msg,
                                          messages)

    return messages


def sanitize_message(message):
    message = re.sub("^Operation failed. ", "", message.strip())

    return message


def sanitize_xml_parsing_error(text):
    import re
    text = sanitize_message(text)
    if "XML PARSING ERROR:" not in text:
        return text

    text = text.replace("XML PARSING ERROR:", "")
    text = text.split(".")[0]
    match = re.search(r'\[facet.*\]\s', text)
    if match:
        replace = match.group()
        text = text.replace(replace, "")

    text = text.strip()
    return text
