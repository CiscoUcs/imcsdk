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
This module provides apis to setup cisco vic adaptor properties \
and create vnics and vhbas
"""

import logging
import time

from imcsdk.imccoreutils import get_server_dn
from imcsdk.apis.v2.utils import _get_mo
from imcsdk.imcexception import ImcOperationError, ImcOperationErrorDetail
from imcsdk.imccoreutils import process_conf_mos_response, sanitize_message
from imcsdk.mometa.adaptor.AdaptorUnit import AdaptorUnitConsts
from imcsdk.mometa.adaptor.AdaptorExtEthIf import AdaptorExtEthIfConsts
from imcsdk.apis.v2.server.serveractions import _wait_for_power_state, \
     server_power_cycle, server_power_state_get
from imcsdk.apis.v2.server.adaptor import adaptor_properties_get

log = logging.getLogger('imc')

class VicConst(object):
    ADAPTOR_ERROR_MSG = "Configure Adapter Failed."
    VNIC_ERROR_MSG = "Create Virtual Ethernet Interface Failed."
    VHBA_ERROR_MSG = "Create Virtual Fibre-Channel Interface Failed."
    DCE_IF_ERROR_MSG = "Configuration of DCE Interface Failed."
    CL74_UNSUPPORTED_ADAPTOR = ["UCSC-PCIE-C100-04", "UCSC-MLOM-C100-04"]


vic_map = {
    "vnic": "AdaptorHostEthIf",
    "vhba": "AdaptorHostFcIf"
}


# Adaptor APIs
def _get_adaptor_dn(handle, adaptor_slot, server_id=1):
    server_dn = get_server_dn(handle, server_id)
    return(server_dn + "/adaptor-" + str(adaptor_slot))


def _get_adaptor_profile_dn(handle, adaptor_slot, server_id=1):
    adaptor_dn = _get_adaptor_dn(handle, adaptor_slot, server_id)
    return(adaptor_dn + "/general")


def _get_adaptor_profile(handle, adaptor_slot, server_id=1):
    dn = _get_adaptor_profile_dn(handle, adaptor_slot, server_id)
    return handle.query_dn(dn)


def _prepare_ep_adaptor_dict(handle, api_error_msg):
    adaptors = adaptor_get_all(handle)
    if not adaptors:
        raise ImcOperationError(api_error_msg,
                                "No adapters present.")

    adaptor_ep_dict = {}
    for adaptor in adaptors:
        adaptor_ep_dict[adaptor.id] = adaptor

    return adaptor_ep_dict


def adaptor_unit_get(handle, adaptor_slot, server_id=1, **kwargs):
    """
    This method fetches the adaptorUnit Managed Object for the specified
    adaptor Slot on a server.

    Args:
        handle (ImcHandle)
        adaptor_slot (string): PCI slot number of the adaptor
        server_id (int): Server Id for C3260 platforms
        kwargs: key=value paired arguments

    Returns:
        AdaptorUnit object

    Examples:
        adaptor_unit_get(handle, adaptor_slot=1, server_id=1)
    """
    return _get_mo(handle, dn=_get_adaptor_dn(handle, adaptor_slot, server_id))

def adaptor_get_all(handle):
    from imcsdk.imcconstants import NamingId
    return handle.query_classid(class_id=NamingId.ADAPTOR_UNIT)


def adaptor_set_all(handle, adaptors=None, server_id=1, **kwargs):
    """
    Example:
        adaptor_set_all(handle,
                        adaptors=[
                            {id: 1,
                            lldp: "enabled",
                            fip_mode: "enabled",
                            port_channel_enable: "enabled",
                            vntag_mode: "enabled",
                            admin_action:None}
                            ]
                        )
    """
    from imcsdk.mometa.adaptor.AdaptorGenProfile import AdaptorGenProfile

    api = 'adaptor_set_all'
    api_error_msg = VicConst.ADAPTOR_ERROR_MSG

    if not adaptors:
        log.debug("No adapters present for configuration")
        return

    # fetch adaptors from end point, adaptor_ep_dict is dict {id, adaptor_mo}
    adaptor_ep_dict = _prepare_ep_adaptor_dict(handle, api_error_msg)

    # validate input and checks if adaptor exists at end point
    for adaptor in adaptors:
        id = adaptor.get('id', None)
        if id is None:
            raise ImcOperationError(
                api_error_msg,
                'Provide adapter slot to configure')

        if id not in adaptor_ep_dict:
            raise ImcOperationError(
                api_error_msg,
                "Adaptor %s is not present at end point." % id)

    # configure adapter
    mos = []

    restart_server = None
    adaptor_list = []

    #adaptors are the configured adaptors in intersight AdaptorConfiguration Policy
    for adaptor in adaptors:
        id = adaptor['id']
        lldp = adaptor.pop('lldp', None)
        fip_mode = adaptor.pop('fip_mode', None)
        port_channel_enable = adaptor.pop('port_channel_enable', None)
        log.debug("Adapter Config Policy - configured Values")
        log.debug("Port Channel: %s, LLDP Mode: %s, Fip Mode: %s", port_channel_enable, lldp, fip_mode)

        # vntag_mode = adaptor.pop('vntag_mode', None)
        # admin_state = adaptor.pop('admin_state', None)

        mo = adaptor_ep_dict[id]
        adaptor_properties = adaptor_properties_get(handle, id, server_id=1)
        adaptor_list.append(adaptor_properties)
        #port_channel_capable  returns None for < Gen4 adapters and False for Gen4+ unsupported portchannel adapters.
        #Hence a check has to be done for both None and False
        #for backward compatibility in deploying Adapter Configuration Policy.
        if adaptor_properties.port_channel_capable == None or adaptor_properties.port_channel_capable == "False":
            log.debug("Port Channel is not supported for the adapter at slot: %s", adaptor_properties.pci_slot)
            port_channel_enable = None

        if adaptor_properties.port_channel_capable == "True" and port_channel_enable == "disabled":
            log.debug("Port Channel is disabled by user for adapter at slot %s. Server restart initiated", adaptor_properties.pci_slot)
            restart_server=True

        mo.admin_state = AdaptorUnitConsts.ADMIN_STATE_ADAPTOR_RESET_DEFAULT

        if port_channel_enable == "disabled":
            AdaptorGenProfile(parent_mo_or_dn=mo,
                              lldp=lldp,
                              fip_mode=fip_mode,
                              port_channel_enable="disabled",
                              vntag_mode="disabled")
        else:
            #port_channel_enable value is set to enabled by default.
            # Hence, its not required to send the default value.
            AdaptorGenProfile(parent_mo_or_dn=mo,
                          lldp=lldp,
                          fip_mode=fip_mode,
                          vntag_mode="disabled")

        mos.append(mo)

    response = handle.set_mos(mos)
    ret = []
    if response:
        ret.append(_process_response(response, api, api_error_msg))

    ext_ethif_adaptor_mos = []
    for adaptor in adaptors:
        id = adaptor['id']
        ext_ethifs = adaptor.pop('ext_ethifs', None)
        if ext_ethifs:
            mo = adaptor_ep_dict[id]
            ext_ethif_mos = _ext_ethif_set_all(handle, ext_ethifs, mo)
            ext_ethif_adaptor_mos.extend(ext_ethif_mos)

    if len(ext_ethif_adaptor_mos) > 0:
        response = handle.set_mos(ext_ethif_adaptor_mos)
        if response:
            error_msg = VicConst.DCE_IF_ERROR_MSG
            ret.append(_process_response(response, api, error_msg))

    results = {}
    results["changed"] = True
    results["msg"] = ""
    results["msg_params"] = ret

    #Power Cycle Host for the changes to take effect.
    if restart_server:
        log.debug("Restarting server...")
        server_power_cycle(handle, timeout=180)
        _wait_for_power_state(handle, state="on", timeout=60, interval=5, server_id=1)
        log.debug("Server restarted successfully. Adaptor initialisation check in progress.")
        for adaptor in adaptor_list:
            adaptor_initialization_in_progress = True
            wait_count = 0
            while adaptor_initialization_in_progress and wait_count < 5:
                try:
                    adaptor = _get_mo(handle, dn=adaptor.dn)
                    adaptor_initialization_in_progress = False
                    log.debug("Adaptor at slot %s initialisation complete.", adaptor.pci_slot)
                except ImcOperationError:
                    log.debug("Adaptor at slot %s initialisation in progress. Sleep for 5s.", adaptor.pci_slot)
                    wait_count += 1
                    time.sleep(5)
            if adaptor_initialization_in_progress:
                log.debug("Adaptor initialisation failure for adaptor at slot %s", adaptor.pci_slot)
                raise ImcOperationError(
                    api_error_msg,
                    "Adaptor %s is not initialised at end point." % adaptor.pci_slot)
        log.debug("Sleeping for 1 minute")
        time.sleep(60)
        log.debug("Returning results")
    return results

def _ext_ethif_set_all(handle, ext_ethifs, adaptor_mo):
    """
    Example:
        _ext_ethif_set_all(handle,
                           ext_ethifs=[
                           {port_id: 1,
                           fec_mode: "Auto"},
                           {port_id: 2,
                           fec_mode: "Off"}],
                           adaptor_mo=<adaptor obj>)
    """
    from imcsdk.mometa.adaptor.AdaptorExtEthIf import AdaptorExtEthIf

    # configure ext_ethifs on adaptor
    mos = []
    cl74_unsupported = False
    ext_ethif_mos_dict = _ext_ethif_get_all(handle, adaptor_mo)
    # FEC mode 'cl74' is not supported for Cisco VIC 1495/1497 adaptors
    # Ignore setting 'cl74' for those adaptors
    if adaptor_mo.model in VicConst.CL74_UNSUPPORTED_ADAPTOR:
       cl74_unsupported = True
    for ext_ethif in ext_ethifs:
        if ext_ethif["port_id"] in ext_ethif_mos_dict:
            # FEC mode configuration is supported only for Bodega adapters
            fec_mode_supported = \
                    ext_ethif_mos_dict[ext_ethif["port_id"]].admin_fec_mode
            if fec_mode_supported:
                if (cl74_unsupported and ext_ethif["fec_mode"] == \
                       AdaptorExtEthIfConsts.ADMIN_FEC_MODE_CL74):
                    continue
                ext_ethif_mos_dict[ext_ethif["port_id"]].admin_fec_mode = \
                        ext_ethif["fec_mode"]
                mos.append(ext_ethif_mos_dict[ext_ethif["port_id"]])
            else:
                log.debug("FEC mode configuration is not supported on adaptor")
                break

    return mos

# VNIC & VHBA APIs
def _process_mo_prop_str(prop_str, api_error_msg):
    '''
    prop_str = "AdaptorFcGenProfile.PciLink"
    validates property string
    separates mo and prop name
    Return mo - AdaptorFcGenProfile, prop - PciLink
    '''
    from imcsdk.imcgenutils import to_python_propname
    props = prop_str.split(".")
    if len(props) != 2:
        raise ImcOperationError(
            api_error_msg,
            "Invalid Key.Either MO or Property name missing")

    mo = props[0]
    prop = to_python_propname(props[1])
    return mo, prop


def _create_child_mo(parent_mo_or_dn, mo_name):
    '''
    creates child object of vnic and vhba
    '''
    from imcsdk.imccoreutils import load_class
    from imcsdk.imccoreutils import find_class_id_in_mo_meta_ignore_case

    class_id = find_class_id_in_mo_meta_ignore_case(mo_name)
    if class_id is None:
        return None

    class_struct = load_class(class_id)
    class_obj = class_struct(parent_mo_or_dn)

    return class_obj


def _vic_get(handle, adaptor_slot, name, vic_type, server_id=1):
    """
    Internal method to get vnic and vhba
    """
    from imcsdk.imccoreutils import load_class

    parent_mo = adaptor_unit_get(handle, adaptor_slot, server_id)
    if parent_mo is None:
        raise ImcOperationError("Cannot create %s." % vic_type,
                                "Adaptor unit %s is missing" % adaptor_slot)

    vic_mo_name = vic_map[vic_type]
    vic_mo_class = load_class(vic_mo_name)
    vic_mo = vic_mo_class(parent_mo_or_dn=parent_mo, name=name)
    return handle.query_dn(vic_mo.dn)

def _vic_get_all(handle, vic_adaptor_slot, vic_type):
    """
    Method to fetch all the  vic's (vnics/vhbas) from the adaptor slot at the end point.
    :param handle:
    :param vic_adaptor_slot: adaptor slot at endpoint
    :param vic_type: vnic or vhba
    :return: Returns the list of vic objects.
    """

    adaptor_mo = adaptor_unit_get(handle, vic_adaptor_slot)
    mos = handle.query_children(adaptor_mo)
    if vic_type == "vnic":
        dn_filter = "host-eth"
    else:
        dn_filter = "host-fc"
    vic_mo = []
    for mo in mos:
        dn = mo.dn
        if dn_filter in dn:
            vic_mo.append(mo)

    return vic_mo

def _ext_ethif_get_all(handle, adaptor_mo):
    """
    Method to fetch all the  external ethernet interfaces from the adaptor slot at the end point.
    :param handle:
    :param adaptor_mo: adaptor mo object
    :return: Returns the list of ext_ethif objects.
    """

    ext_ethifs = {}
    mos = handle.query_children(adaptor_mo, class_id="AdaptorExtEthIf")
    for mo in mos:
        ext_ethifs[mo.port_id] = mo

    return ext_ethifs

def _validate_vic(vic_type, api_error_msg, vic):
    '''
    validates if vic name and adaptor slot present in input
    Validates if mentioned adaptor exists at end point
    Identifies list of adaptor to be configured
    '''

    # check if vic name is present in vic configuration
    vic_mo_name = vic_map[vic_type]
    vic_mo_name_prop = vic_mo_name + ".Name"
    vic_name = vic.pop(vic_mo_name_prop, None)
    if vic_name is None:
        raise ImcOperationError(api_error_msg, "Provide interface name")
    vic['name'] = vic_name

    # check if adaptor slot is present in vic configuration
    vic_adaptor_slot = vic.pop('AdaptorUnit.Id', None)
    if vic_adaptor_slot is None:
        raise ImcOperationError(
            api_error_msg,
            "Provide adaptor slot for interface %s" % vic_name)
    vic['adaptor_slot'] = vic_adaptor_slot


def _validate_vics(vic_type, api_error_msg, vics, adaptor_ep_dict):
    '''
    validates if vic name and adaptor slot present in input
    Validates if mentioned adaptor exists at end point
    Identifies list of adaptor to be configured
    '''
    adaptor_to_configure = []

    for vic in vics:
        _validate_vic(vic_type, api_error_msg, vic)
        vic_name = vic['name']
        vic_adaptor_slot = vic['adaptor_slot']

        # check if adaptor to configure is present at end point
        if vic_adaptor_slot not in adaptor_ep_dict:
            raise ImcOperationError(
                api_error_msg,
                "Adaptor %s is not present at end point for interface %s" %
                (vic_adaptor_slot, vic_name))

        # identify which all adaptor to configure
        if vic_adaptor_slot not in adaptor_to_configure:
            adaptor_to_configure.append(vic_adaptor_slot)

    return adaptor_to_configure


def _create_vic_object(adaptor_mo, vic_name, vic_type, api_error_msg,
                       **kwargs):
    from imcsdk.imccoreutils import load_class
    from imcsdk.imccoreutils import find_class_id_in_mo_meta_ignore_case

    vic_mo_name = vic_map[vic_type]
    vic_mo_class = load_class(vic_mo_name)
    vic_mo = vic_mo_class(parent_mo_or_dn=adaptor_mo, name=vic_name)

    # process vnic/vhba children
    vic_children = {}
    for key, value in kwargs.items():
        mo_name, prop_name = _process_mo_prop_str(key, api_error_msg)
        if not mo_name:
            raise ImcOperationError(api_error_msg,
                                    "MO name is missing.")
        if not prop_name:
            raise ImcOperationError(api_error_msg,
                                    "Property name is missing.")
        prop_value = None if value is None else str(value)

        # VIC 1385 adapter is a multi-pci link adapter and hence just use the pci-link what we have received
        # For all other adapters, hard-code it to 0
        if adaptor_mo.model != "UCSC-PCIE-C40Q-03":
            if mo_name == "AdaptorEthGenProfile" or mo_name == "AdaptorFcGenProfile":
                if prop_name == "pci_link":
                    prop_value = "0"

        # Allow vHBA Type Configuration for Generation4+ adaptor only. Else, set the vhbaType to None as they are not supported.
        adaptorModel = adaptor_mo.model.split("-")
        genVersion = adaptorModel[len(adaptorModel)-1]
        if genVersion < "04" and mo_name == "AdaptorFcGenProfile" and prop_name == "vhba_type":
            prop_value = None

        nmo_name = find_class_id_in_mo_meta_ignore_case(mo_name)
        if nmo_name is None:
            log.debug(
                "Ignoring '%s'. MO '%s' does not exist in meta."
                % (key, mo_name)
            )
            continue
        else:
            mo_name = nmo_name

        if mo_name == vic_mo_name:
            mo = vic_mo
        elif mo_name not in vic_children:
            mo = _create_child_mo(vic_mo, mo_name)
            vic_children[mo_name] = mo
        else:
            mo = vic_children[mo_name]

        setattr(mo, prop_name, prop_value)

    return vic_mo

def _vic_delete_all_under_adaptors(handle, vic_type, adaptor_slots):
    import re

    if vic_type == "vnic":
        api_error_msg = VicConst.VNIC_ERROR_MSG
        ignore_vics = ['eth0', 'eth1']
    elif vic_type == "vhba":
        api_error_msg = VicConst.VHBA_ERROR_MSG
        ignore_vics = ['fc0', 'fc1']

    # create a regex pattern of dn for the input adaptor_slots to be matched
    # against the dn of the mo coming from the end point.
    adaptor_slots = [adaptor_slot.strip() for adaptor_slot in adaptor_slots]
    adaptor_slots_str = "|".join(adaptor_slots)
    pattern_str = "sys/rack-unit-1/adaptor-(%s)" % adaptor_slots_str
    pattern = re.compile(pattern_str)

    # query all the vnics/vhbas from the end point
    vic_mo_name = vic_map[vic_type]
    vics = handle.query_classid(class_id=vic_mo_name)
    if vics is None:
        return

    vics_to_delete = []
    for vic in vics:
        if vic.name in ignore_vics:
            continue

        # ignore vnic or vhba which is not inside the specified adaptors
        vic_dn = vic.dn
        if not pattern.match(vic_dn):
            continue
        vics_to_delete.append(vic)

    response = handle.remove_mos(vics_to_delete)
    ret = []
    if response:
        api = "Configure Interface"
        ret = _process_response(response, api, api_error_msg)
    return ret


def _adaptor_reset_default(handle, adaptor_to_configure, adaptor_ep_dict,
                           api_error_msg):
    api = "adaptor_reset_default"
    mos = []
    for adaptor_slot in adaptor_to_configure:
        mo = adaptor_ep_dict[adaptor_slot]
        mo.admin_state = AdaptorUnitConsts.ADMIN_STATE_ADAPTOR_RESET_DEFAULT
        mos.append(mo)
    response = handle.set_mos(mos)
    if response:
        _process_response(response, api, api_error_msg)


def _create_vics_with_children(handle, vic_type, api_error_msg, vics,
                               adaptors_to_reset=None):
    """
    Internal method to create all vnics or vhbas objects which can be sent to
    end point for configuration
    """
    if adaptors_to_reset is None:
        adaptors_to_reset = []

    # fetch adaptors from end point {id, adaptor_mo}
    adaptor_ep_dict = _prepare_ep_adaptor_dict(handle, api_error_msg)

    # validate vics
    adaptor_to_configure = _validate_vics(vic_type, api_error_msg,
                                          vics, adaptor_ep_dict)

    # delete vics under adaptor to configure
    # _vic_delete_all_under_adaptors(handle, vic_type, adaptor_to_configure)

    if adaptors_to_reset:
        for vic_adaptor_slot in adaptors_to_reset[:]:
            if vic_adaptor_slot not in adaptor_ep_dict or \
                    vic_adaptor_slot not in adaptor_to_configure:
                log.debug("Skipping reset of adapter %s" % vic_adaptor_slot)
                adaptors_to_reset.remove(vic_adaptor_slot)
                continue
        _adaptor_reset_default(handle, adaptors_to_reset, adaptor_ep_dict,
                               api_error_msg)

    # create a list of vnic/vhba objects with its children
    mos = []
    for vic in vics:
        vic_name = vic.pop('name')
        vic_adaptor_slot = vic.pop('adaptor_slot')
        adaptor_mo = adaptor_ep_dict[vic_adaptor_slot]
        mo = _create_vic_object(adaptor_mo, vic_name, vic_type, api_error_msg,
                                **vic)
        mos.append(mo)

    return mos


def _vic_delete_all(handle, vic_type, adaptor_slots=None):
    """
    Internal method to delete all vnics or vhbas
    """

    if adaptor_slots:
        ret = _vic_delete_all_under_adaptors(handle, vic_type, adaptor_slots)
        results = {}
        results["changed"] = True
        results["msg"] = ""
        results["msg_params"] = ret

        return results

    if vic_type == "vnic":
        api_error_msg = VicConst.VNIC_ERROR_MSG
        ignore_vics = ['eth0', 'eth1']
    elif vic_type == "vhba":
        api_error_msg = VicConst.VHBA_ERROR_MSG
        ignore_vics = ['fc0', 'fc1']

    vic_mo_name = vic_map[vic_type]
    vics = handle.query_classid(class_id=vic_mo_name)
    if vics is None:
        return

    vics = [vic for vic in vics if vic.name not in ignore_vics]

    api = '%s_delete_all' % vic_type
    response = handle.remove_mos(vics)
    ret = []
    if response:
        ret = _process_response(response, api, api_error_msg)

    results = {}
    results["changed"] = True
    results["msg"] = ""
    results["msg_params"] = ret

    return results


def vnic_get(handle, adaptor_slot, name, server_id=1):
    """
    This method is used to get a vnic
    Args:
        handle (ImcHandle)
        adaptor_slot (string): PCI slot number of the adaptor
        name (string): Name for the vnic to be deleted
        server_id (int): Server Id for C3260 platforms

    Returns:
        AdaptorHostEthIf object
    """
    vic_type = "vnic"
    return _vic_get(handle, adaptor_slot, name, vic_type, server_id)


def vnic_create(handle, server_id=1, **kwargs):
    """
    This method is used to create a new vnic
    Args:
        handle (ImcHandle)
        server_id (int): Server Id for C3260 platforms
        kwargs: key=value paired arguments for vnic/vhba

    Examples:

    Returns:
        AdaptorHostEthIf object
    """
    vic_type = "vnic"
    api_error_msg = VicConst.VNIC_ERROR_MSG

    _validate_vic(vic_type, api_error_msg, kwargs)
    vic_name = kwargs.pop('name')
    vic_adaptor_slot = kwargs.pop('adaptor_slot')

    # Checks if the required adaptor exists at end point
    adaptor_mo = adaptor_unit_get(handle, vic_adaptor_slot)
    if adaptor_mo is None:
        raise ImcOperationError(api_error_msg,
                                "Adaptor is missing at end point.")

    vic_mo = _create_vic_object(adaptor_mo, vic_name, vic_type,
                                api_error_msg, **kwargs)
    return handle.add_mo(vic_mo)


def _process_response(response, api, error_msg, callback=None, *cbargs):
    callback_params = []
    if callback is not None:
        callback_params = [callback]
        callback_params.extend(cbargs)

    ret = process_conf_mos_response(response, api, False, error_msg,
                                    *callback_params)
    error_msg += "\n"
    if len(ret) != 0:
        for item in ret:
            obj = item["Object"]
            error_msg += "%s: " % obj
            error = item["Error"]
            error = sanitize_message(error)
            error_msg += error + "\n"

        raise ImcOperationErrorDetail(api, error_msg, ret)

    return ret


def _get_vnic_order(vnic):
    api_error_msg = VicConst.VNIC_ERROR_MSG
    children = vnic._child
    for ch in children:
        if ch.get_class_id() == "AdaptorEthGenProfile":
            return int(ch.order)
    raise ImcOperationError(api_error_msg,
                            "Order is missing.")


def _sort_vnic_by_order(vnics):
    nvnics = sorted(vnics, key=_get_vnic_order)
    return nvnics


def vnic_create_all(handle, vnics=None, adaptors_to_reset=None,
                    server_id=1):
    """
    This method is used to create a new vnic
    Args:
        handle (ImcHandle)
        vnics (list): list of dict
        server_id (int): Server Id for C3260 platforms

    Examples:
        vnics = [
            {
                "AdaptorUnit.Id": ADAPTOR_ID,
                "AdaptorHostEthIf.Name": "vnic_usnic",
                "AdaptorHostEthIf.Cdn": "testcdnusnic",
                "AdaptorEthUSNICProfile.usnicCount": "1",
                "AdaptorEthUSNICProfile.TransmitQueueCount": "10"
            },
        ]
        vnic_create_all(handle, vnics)

    Returns:
        dict
    """
    if not vnics:
        log.debug("No vnics are present to be added.")
        return

    api = "vnic_create_all"
    vic_type = "vnic"
    api_error_msg = VicConst.VNIC_ERROR_MSG
    vnic_count_per_request = 3
    ret = []

    vnic_children_classid_to_send_later = ["AdaptorEthUSNICProfile"]

    # create vnics mo with children
    vnics = _create_vics_with_children(handle, vic_type, api_error_msg, vnics,
                                       adaptors_to_reset)

    # sort vnics by order
    vnics = _sort_vnic_by_order(vnics)

    # removing usNic from vnic children to be sent in separate request
    vnic_children_to_send_separately = []
    for vnic in vnics:
        for ch in vnic._child[:]:
            if ch.get_class_id() in vnic_children_classid_to_send_later:
                vnic_children_to_send_separately.append(ch)
                vnic._child.remove(ch)
            # if ch.get_class_id() == "AdaptorEthGenProfile":
            #     object.__setattr__(ch, 'order', None)

    # sending request to add/modify vnic with its children
    for i in range(0, len(vnics), vnic_count_per_request):
        vnics_ = vnics[i: i+vnic_count_per_request]
        response = handle.set_mos(vnics_)
        if response:
            ret.append(_process_response(response, api, api_error_msg))

    # send request for children to be sent separately
    response = handle.set_mos(vnic_children_to_send_separately)
    if response:
        error_msg = 'Setting properties failed for Virtual Ethernet Interface:\
        \n'
        ret.append(_process_response(response, api, error_msg))

    results = {}
    results["changed"] = True
    results["msg"] = ""
    results["msg_params"] = ret

    return results


def vnic_delete_all(handle, adaptor_slots=None):

    """
    delete all vnics.

    Args:
        handle (ImcHandle)

    Returns:
        None

    Raises:
        ImcOperationError: If user is not present

    Example:
        vnic_delete_all(handle)

    """
    vic_type = "vnic"
    _vic_delete_all(handle, vic_type, adaptor_slots)


def vhba_get(handle, adaptor_slot, name, server_id=1):
    """
    This method is used to get a vhba
    Args:
        handle (ImcHandle)
        adaptor_slot (string): PCI slot number of the adaptor
        name (string): Name for the vnic to be deleted
        server_id (int): Server Id for C3260 platforms
        kwargs: key=value paired arguments

    Returns:
        AdaptorHostEthIf object
    """
    vic_type = "vhba"
    return _vic_get(handle, adaptor_slot, name, vic_type, server_id)


def vhba_create(handle, server_id=1, send_request=True, **kwargs):
    """
    This method is used to create a new vhba
    Args:
        handle (ImcHandle)
        name (string): Name for the vhba
        adaptor_slot (string): PCI slot number of the adaptor
        server_id (int): Server Id for C3260 platforms
        kwargs: key=value paired arguments

    Examples:
        For non-C3260 platforms:-
        vhba_create(handle, adaptor_slot="1", name="test-vhba",
                    channel_number=10, mac="00:11:22:33:44:55",
                    mtu=1500, pxe_boot=True, uplink_port=0)

        For C3260 platforms:
        vhba_create(handle, adaptor_slot="1", name="test-vhba",
                    channel_number=10, mac="00:11:22:33:44:55",
                    mtu=1500, pxe_boot=True, uplink_port=0, server_id=1)

    Returns:
        AdaptorHostFcIf object
    """
    vic_type = "vhba"
    api_error_msg = VicConst.VHBA_ERROR_MSG

    _validate_vic(vic_type, api_error_msg, kwargs)
    vic_name = kwargs.pop('name')
    vic_adaptor_slot = kwargs.pop('adaptor_slot')

    # Checks if the required adaptor exists at end point
    adaptor_mo = adaptor_unit_get(handle, vic_adaptor_slot)
    if adaptor_mo is None:
        raise ImcOperationError(api_error_msg,
                                "Adaptor is missing at end point.")

    vic_mo = _create_vic_object(adaptor_mo, vic_name, vic_type,
                                api_error_msg, **kwargs)
    return handle.add_mo(vic_mo)


def vhba_create_all(handle, vhbas=None, adaptors_to_reset=None,
                    server_id=1):
    """
    This method is used to create a new vhba
    Args:
        handle (ImcHandle)
        name (string): Name for the vhba
        adaptor_slot (string): PCI slot number of the adaptor
        server_id (int): Server Id for C3260 platforms
        kwargs: key=value paired arguments

    Examples:
        vhbas = [
            {
                'name': 'vhba1',
                'adaptor_slot': ADAPTOR_ID,
                "adaptorHostEthIf_uplink_port": "11",
                "adaptorEthGenProfile_order": "1",
                "adaptorEthGenProfile_vlan_mode": "ACCESS",
            },
            {
                'name': 'vhba2',
                'adaptor_slot': ADAPTOR_ID,
                "adaptorHostEthIf_uplink_port": "22",
                "adaptorEthGenProfile_order": "1",
                "adaptorEthGenProfile_vlan_mode": "ACCESS",
            },
        ]
        vhba_create_all(handle, vhbas)

    Returns:
        dict
    """
    if not vhbas:
        log.debug("No vhbas are present to be added.")
        return

    api = "vhba_create_all"
    vic_type = "vhba"
    api_error_msg = VicConst.VHBA_ERROR_MSG

    # create vnics with children
    vhbas = _create_vics_with_children(handle, vic_type, api_error_msg, vhbas,
                                       adaptors_to_reset)
    response = handle.set_mos(vhbas)
    ret = []
    if response:
        ret = _process_response(response, api, api_error_msg)

    results = {}
    results["changed"] = True
    results["msg"] = ""
    results["msg_params"] = ret

    return results


def vhba_delete_all(handle, adaptor_slots=None):
    """
    delete all vhbas.

    Args:
        handle (ImcHandle)

    Returns:
        None

    Raises:
        ImcOperationError: If user is not present

    Example:
        vhba_delete_all(handle)

    """
    vic_type = "vhba"
    _vic_delete_all(handle, vic_type, adaptor_slots)
