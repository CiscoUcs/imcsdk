# Copyright 2015 Cisco Systems, Inc.
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

try:
    import xml.etree.cElementTree as ET
    from xml.etree.cElementTree import Element, SubElement
except ImportError:
    import cElementTree as ET
    from cElementTree import Element, SubElement

from . import imcgenutils
from . import imccoreutils
from . import imcexception as ex
from .imccore import ImcErrorResponse


def to_xml_str(elem):
    """
    Converts xml element to xml string.

    Args:
        elem (xml element)

    Returns:
        xml string

    Example:
        xml_str = to_xml_str(elem=xml_element)
    """

    return ET.tostring(elem)


def extract_root_elem(xml_str):
    """
    extracts root xml element from xml string.

    Args:
        xml_str (str): xml string

    Returns:
        xml element

    Example:
        xml_str='''
        <lsClone dn="org-root/ls-testsp" inHierarchical="false"
        inServerName="test" inTargetOrg="">
        </lsClone>
        '''
        root_element = extract_root_elem(xml_str)
    """

    xml_str = xml_str.strip("\x00")
    root_elem = ET.fromstring(xml_str)
    return root_elem


def from_xml_str(xml_str, handle=None):
    """
    Generates response object from the given xml string.

    Args:
        xml_str (str): xml string
        handle : ImcHandle

    Returns:
        object (external method or managed object or generic managed object)

    Example:
        xml_str='''\n
        <lsServer dn="org-root/ls-testsp" dynamicConPolicyName="test"\n
        extIPPoolName="ext-mgmt" name="testsp" />\n
        '''\n
        root_element = extract_root_elem(xml_str)\n
    """

    xml_str = xml_str.strip("\x00")
    root_elem = ET.fromstring(xml_str)
    if root_elem.tag == "error":
        error_code = root_elem.attrib['errorCode']
        error_descr = root_elem.attrib['errorDescr']
        response = ImcErrorResponse(error_code=error_code, error_descr=error_descr)
        # Do not raise an exception, it is upto the top level application to understand what type of object is returned
        return response

    class_id = imcgenutils.word_u(root_elem.tag)
    response = imccoreutils.get_imc_obj(class_id, root_elem)
    response.from_xml(root_elem, handle)
    return response
