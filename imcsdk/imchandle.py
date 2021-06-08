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


import logging
from collections import OrderedDict

from . import imcgenutils
from . import imccoreutils
from .imcexception import ImcException
from .imcconstants import NamingId
from .imcsession import ImcSession

log = logging.getLogger('imc')

CONFIG_CONF_MOS_BUFFER_SIZE = 10


class ImcHandle(ImcSession):
    """
    ImcHandle class is the user interface point for any Imc communication.

    Args:
        ip (str): The IP or Hostname of the IMC Server
        username (str): The username as configured on the Imc Server
        password (str): The password as configured on the Imc Server
        port (int or None): The port number to be used during connection
        secure (bool or None): True for secure connection, otherwise False
        proxy (str): The proxy object to be used to connect
        auto_refresh (bool): if set to True, it'll refresh the cookie continuously
        force (bool): if set to True it'll reconnect even if cookie exists
            and is valid for the respective connection.
        timeout (int): timeout value in secs

    Example:
        handle = ImcHandle("192.168.1.1","admin","password")\n
        handle = ImcHandle("192.168.1.1","admin","password", secure=True)\n
        handle = ImcHandle("192.168.1.1","admin","password", secure=False)\n
        handle = ImcHandle("192.168.1.1","admin","password", port=80)\n
        handle = ImcHandle("192.168.1.1","admin","password", port=443)\n
        handle = ImcHandle("192.168.1.1","admin","password", port=100,
                 secure=True)\n
        handle = ImcHandle("192.168.1.1","admin","password", port=100,
                 secure=False)\n
    """

    def __init__(self, ip, username, password, port=None, secure=None,
                 proxy=None, auto_refresh=False, force=False, timeout=None):

        ImcSession.__init__(self, ip=ip, username=username, password=password,
                            port=port, secure=secure, proxy=proxy,
                            auto_refresh=auto_refresh, force=force,
                            timeout=timeout)
        self.__to_commit = OrderedDict()

    def __enter__(self):
        """
        Initiates a connection to the server referenced by the ImcHandle.
        A cookie is populated in the ImcHandle, if the login is successful.

        The class instance is returned.
        """

        self._login()
        return self

    def __exit__(self, *exc):
        """
        Disconnects from the server referenced by the ImcHandle and exits.
        """

        self._logout()

    def is_starship(self):
        """
        Check if SDK is running in starship mode
        """
        return self._is_starship()

    def set_starship_proxy(self, proxy):
        """
        Connects to the server via the proxy URL
        """
        self._set_starship_proxy(proxy)

    def unset_starship_proxy(self):
        """
        Connects to the server via the proxy URL
        """
        self._set_starship_proxy(None)

    def set_starship_headers(self, headers):
        """
        Set the headers to be used in connection
        """
        self._set_starship_headers(headers)

    def unset_starship_headers(self):
        """
        Set the headers to be used in connection
        """
        self._set_starship_headers(None)

    def set_dump_xml(self):
        """
        Enables the logging of xml requests and responses.
        """

        self._set_dump_xml()

    def unset_dump_xml(self):
        """
        Disables the logging of xml requests and responses.
        """

        self._unset_dump_xml()

    def login(self, auto_refresh=None, force=None, timeout=None):
        """
        Initiates a connection to the server referenced by the ImcHandle.
        A cookie is populated in the ImcHandle, if the login is successful.

        Args:
            auto_refresh (bool): if set to True, it refresh the cookie
                continuously
            force (bool): if set to True it'll reconnect even if cookie exists
                and is valid for the respective connection.
            timeout (int): timeout value in secs

        Returns:
            True on successful connect

        Example:
            handle.login()\n
            handle.login(auto_refresh=True)\n
            handle.login(force=True)\n
            handle.login(auto_refresh=True, force=True)\n

            where handle is ImcHandle()
        """

        return self._login(auto_refresh=auto_refresh, force=force, timeout=timeout)

    def logout(self, timeout=None):
        """
        Disconnects from the server referenced by the ImcHandle.

        Args:
            None
            timeout (int): timeout value in secs

        Returns:
            True on successful disconnect

        Example:
            handle.logout()

            where handle is ImcHandle()
        """

        return self._logout(timeout=timeout)

    def process_xml_elem(self, elem, timeout=None):
        """
        process_xml_elem is a helper method which posts xml elements to the
        server and returns parsed response. It's role is to operate on the
        output of methods from Imcmethodfactory, which return xml element
        node(s).

        Args:
            elem (xml element object)

        Returns:
            mo list or external method object

        Example:
            elem = imcmethodfactory.config_resolve_class(cookie=
                handle.cookie, class_id="computeRackUnit")\n
            objs = handle.process_xml_elem(elem)
        """

        response = self.post_elem(elem, timeout=timeout)
        if response.error_code != 0:
            raise ImcException(response.error_code, response.error_descr)

        if hasattr(response, "out_config"):
            return response.out_config.child
        else:
            return response

    def get_auth_token(self, timeout=None):
        """
        Returns a token that is used for IMC authentication.

        Args:
            None

        Returns:
            auth_token (str)
            timeout (int): timeout value in secs

        Example:
            handle.get_auth_token()

        """

        from .imcmethodfactory import aaa_get_compute_auth_tokens

        auth_token = None
        mo = self.query_classid(class_id=NamingId.COMPUTE_BOARD)
        if not mo:
            mo = self.query_classid(class_id=NamingId.COMPUTE_RACK_UNIT)

        if mo:
            elem = aaa_get_compute_auth_tokens(cookie=self.cookie)
            response = self.post_elem(elem, timeout=timeout)
            if response.error_code != 0:
                raise ImcException(response.error_code,
                                   response.error_descr)

            # cat = self.AaaGetNComputeAuthTokenByDn(mo[0].Dn, 1, None)
            auth_token = response.out_tokens.split(',')[0]

        return auth_token

    def query_dn(self, dn, hierarchy=False, need_response=False, timeout=None):
        """
        Finds an object using it's distinguished name.

        Args:
            dn (str): distinguished name of the object to be queried for.
            hierarchy(bool): True/False,
                                get all objects in hierarchy if True
            need_response(bool): True/False,
                                return the response xml node, instead of parsed
                                objects
            timeout (int): timeout value in secs

        Returns:
            managedobject or None   by default\n
            managedobject list      if hierarchy=True\n
            externalmethod object   if need_response=True\n

        Example:
            obj = handle.query_dn("sys/rack-unit-1")\n
            obj = handle.query_dn("sys/rack-unit-1", hierarchy=True)\n
            obj = handle.query_dn("sys/rack-unit-1", need_response=True\n
            obj = handle.query_dn("sys/rack-unit-1", hierarchy=True,
            need_response=True)\n
        """

        from .imcmethodfactory import config_resolve_dn

        if not dn:
            raise ValueError("Provide dn.")

        elem = config_resolve_dn(cookie=self.cookie, dn=dn,
                                 in_hierarchical=hierarchy)
        response = self.post_elem(elem, timeout=timeout)
        if response.error_code != 0:
            raise ImcException(response.error_code, response.error_descr)

        if need_response:
            return response

        if hierarchy:
            out_mo_list = imccoreutils.extract_molist_from_method_response(
                response,
                hierarchy)
            return out_mo_list

        mo = None
        if len(response.out_config.child) > 0:
            mo = response.out_config.child[0]
        return mo

    def query_classid(self, class_id=None, hierarchy=False,
                      need_response=False, timeout=None):
        """
        Finds an object using it's class id.

        Args:
            class_id (str): class id of the object to be queried for.

            hierarchy(bool): if set to True will return all the child
                             hierarchical objects.
            need_response(bool): if set to True will return only response
                                object.
            timeout (int): timeout value in secs


        Returns:
            managedobjectlist or None   by default\n
            managedobjectlist or None   if hierarchy=True\n
            methodresponse              if need_response=True\n

        Example:
            obj = handle.query_classid(class_id="computeRackUnit")\n
            obj = handle.query_classid(class_id="computeRackUnit",
                hierarchy=True)\n
            obj = handle.query_classid(class_id="computeRackUnit",
                need_response=True)\n

        """

        # ToDo - How to handle unknown class_id

        from .imcmethodfactory import config_resolve_class

        if not class_id:
            raise ValueError("Provide Parameter class_id")

        meta_class_id = imccoreutils.find_class_id_in_mo_meta_ignore_case(
                                                                class_id)
        if not meta_class_id:
            meta_class_id = class_id
        elem = config_resolve_class(cookie=self.cookie,
                                    class_id=meta_class_id,
                                    in_hierarchical=hierarchy)
        response = self.post_elem(elem, timeout=timeout)
        if response.error_code != 0:
            raise ImcException(response.error_code, response.error_descr)

        if need_response:
            return response

        out_mo_list = imccoreutils.extract_molist_from_method_response(
                                                                    response,
                                                                    hierarchy)
        return out_mo_list

    def query_children(self, in_mo=None, in_dn=None, class_id=None,
                       hierarchy=False, timeout=None):
        """
        Finds children of a given managed object or distinguished name.
        Arguments can be specified to query only a specific type(class_id)
        of children.
        Arguments can also be specified to query only direct children or the
        entire hierarchy of children.

        Args:
            in_mo (managed object): query children managed object under this
                                        object.
            in_dn (dn string): query children managed object for a
                                given managed object of the respective dn.
            class_id(str): by default None, if given find only specific
                            children object for a given class_id.
            hierarchy(bool): if set to True will return all the child
                              hierarchical objects.
            timeout (int): timeout value in secs

        Returns:
            managedobjectlist or None   by default\n
            managedobjectlist or None   if hierarchy=True\n

        Example:
            mo_list = handle.query_children(in_mo=mo)\n
            mo_list = handle.query_children(in_mo=mo, class_id="classid")\n
            mo_list = handle.query_children(in_dn=dn)\n
            mo_list = handle.query_children(in_dn=dn, class_id="classid")\n
        """

        from .imcmethodfactory import config_resolve_children

        if not in_mo and not in_dn:
            raise ValueError('[Error]: GetChild: Provide in_mo or in_dn.')

        if in_mo:
            parent_dn = in_mo.dn
        elif in_dn:
            parent_dn = in_dn

        meta_class_id = None
        # Setting the default class-id to None
        # When hierarchy and class-id are passed together to Cisco IMC,
        # an empty response is received.
        # Hence, passing the class-id only when hierarchy is not set
        # When both hierarchy and class-id are set, do local filtering for class-id
        if class_id and not hierarchy:
            meta_class_id = imccoreutils.find_class_id_in_mo_meta_ignore_case(
                class_id)
            if not meta_class_id:
                meta_class_id = class_id

        elem = config_resolve_children(cookie=self.cookie,
                                       class_id=meta_class_id,
                                       in_dn=parent_dn,
                                       in_hierarchical=hierarchy)

        response = self.post_elem(elem, timeout=timeout)
        if response.error_code != 0:
            raise ImcException(response.error_code, response.error_descr)

        out_mo_list = imccoreutils.extract_molist_from_method_response(response,
                                                                       hierarchy
                                                                       )
        if class_id and hierarchy:
            out_mo_list = imccoreutils.filter_molist_on_class_id(
                                out_mo_list,
                                class_id=class_id)
        return out_mo_list

    def add_mo(self, mo, modify_present=True, timeout=None):
        """
        Adds a managed object.

        Args:
            mo (managedobject): ManagedObject to be added.
            modify_present (bool): True/False,
                                    overwrite existing object if True
            timeout (int): timeout value in secs

        Returns:
            None

        Example:
            obj = handle.add_mo(mo)
        """

        from .imccoreutils import validate_mo_version

        validate_mo_version(self, mo)

        if modify_present in imcgenutils.AFFIRMATIVE_LIST:
            if self.query_dn(mo.dn) is None:
                mo.status = "created"
            else:
                mo.status = "modified"
        else:
            mo.status = "created"

        self.__to_commit[mo.dn] = mo
        self._commit(timeout=timeout)

    def set_mo(self, mo, timeout=None):
        """
        Modifies a managed object and adds it to ImcHandle commit buffer (if
         not already in it).

        Args:
            mo (managedobject): Managed object with modified properties.
            timeout (int): timeout value in secs

        Returns:
            None

        Example:
            obj = handle.set_mo(mo)
        """

        from .imccoreutils import validate_mo_version

        validate_mo_version(self, mo)

        mo.status = "modified"
        self.__to_commit[mo.dn] = mo
        self._commit(timeout=timeout)

    def remove_mos(self, mos, timeout=None):
        """
        removes multiple managed objects in a single request

        Args:
            mos (managedobject): List of managed objects
            timeout (int): timeout value in secs

        Returns:
            dict: {'response_status': string,
                    'response_mos': {'dn':
                                        {'is_configured': bool,
                                         'response_object': MO or ImcException
                                        }
                                    }
                  }

        Example:
            obj = handle.remove_mos(mos)
        """
        for mo in mos:
            mo.status = "deleted"
            if mo.parent_mo:
                mo.parent_mo.child_remove(mo)
            self.__to_commit[mo.dn] = mo

        return self._commit_mos(timeout)

    def remove_mo(self, mo, timeout=None):
        """
        Removes a managed object.

        Args:
            mo (managedobject): Managed object to be removed.
            timeout (int): timeout value in secs

        Returns:
            None

        Example:
            obj = handle.remove_mo(mo)
        """

        from .imccoreutils import validate_mo_version

        validate_mo_version(self, mo)

        mo.status = "deleted"
        if mo.parent_mo:
            mo.parent_mo.child_remove(mo)

        self.__to_commit[mo.dn] = mo
        self._commit(timeout=timeout)

    def _commit(self, timeout=None):
        """
        Commit the buffer to the server. Pushes all the configuration changes
        so far to the server.
        Configuration could be added to the commit buffer using add_mo(),
        set_mo(), remove_mo().

        Args:
            timeout (int): timeout value in secs

        Returns:
            None

        Example:
            self._commit()
        """

        from .imcbasetype import ConfigMap
        from .imcmethodfactory import config_conf_mo
        mo_dict = self.__to_commit
        if not mo_dict:
            # log.debug("Commit Buffer is Empty")
            return None

        config_map = ConfigMap()
        for mo_dn in mo_dict:

            config_map.child_add(mo_dict[mo_dn])
            elem = config_conf_mo(self.cookie, dn=mo_dn,
                                  in_config=config_map,
                                  in_hierarchical=False)
            response = self.post_elem(elem, timeout=timeout)
            if response.error_code != 0:
                self.__to_commit.clear()
                raise ImcException(response.error_code, response.error_descr)

            for out_mo in response.out_config.child:
                out_mo.sync_mo(mo_dict[out_mo.dn])

        self.__to_commit.clear()

    def add_mos(self, mos, modify_present=True, timeout=None):
        """
        adds multiple managed objects in a single request

        Args:
            mos (managedobject): List of managed objects
            timeout (int): timeout value in secs

        Returns:
            dict: {'response_status': string,
                    'response_mos': {'dn':
                                        {'is_configured': bool,
                                         'response_object': MO or ImcException
                                        }
                                    }
                  }

        Example:
            obj = handle.set_mos(mos)
        """
        for mo in mos:
            if modify_present in imcgenutils.AFFIRMATIVE_LIST:
                if self.query_dn(mo.dn) is None:
                    mo.status = "created"
                else:
                    mo.status = "modified"
            else:
                mo.status = "created"

            self.__to_commit[mo.dn] = mo

        return self._commit_mos(timeout)

    def set_mos(self, mos, timeout=None):
        """
        Sets multiple managed objects in a single request

        Args:
            mos (managedobject): List of managed objects
            timeout (int): timeout value in secs

        Returns:
            dict: {'response_status': string,
                    'response_mos': {'dn':
                                        {'is_configured': bool,
                                         'response_object': MO or ImcException
                                        }
                                    }
                  }

        Example:
            obj = handle.set_mos(mos)
        """
        for mo in mos:
            self.__to_commit[mo.dn] = mo

        return self._commit_mos(timeout)

    def __process_config_conf_mos(self, mos, timeout=None):
        """
        Internal method to process configconfmos.
        IMC XmlApi method 'configConfMos' support maximum 10 MOs in single
        request.
        """

        from .imcbasetype import ConfigMap, Pair, FailedMos
        from .imccore import OperationStatus, ImcErrorResponse
        from .imcmethodfactory import config_conf_mos
        from .imccoreutils import ConfigConfMosConstants as Const
        from .imcexception import ImcException

        if not mos:
            return None

        response_status = None

        config_map = ConfigMap()
        for mo in mos:
            child_list = mo.child
            while len(child_list) > 0:
                current_child_list = child_list
                child_list = []
                for child_mo in current_child_list:
                    child_list.extend(child_mo.child)

            pair = Pair()
            pair.key = mo.dn
            pair.child_add(mo)
            config_map.child_add(pair)

        elem = config_conf_mos(self.cookie, config_map, False)
        failed = {}
        passed = {}

        response = self.post_elem(elem, timeout)
        if isinstance(response, ImcErrorResponse):
            error_code = response.error_code
            error_descr = response.error_descr
            # clear the commit buffer incase of an exception
            self.__to_commit.clear()
            raise ImcException(error_code, error_descr)
        for ch in response.out_configs.child:
            if isinstance(ch, OperationStatus):
                response_status = ch.operation_status
                continue

            for chd in ch.child:
                if isinstance(ch, Pair):
                    passed[chd.dn] = chd
                elif isinstance(ch, FailedMos):
                    failed[chd.dn] = chd.error_descr
        mos_dict = {
            Const.RESPONSE_PASSED_MOS: passed,
            Const.RESPONSE_FAILED_MOS: failed
        }

        response_dict = {
            Const.RESPONSE_STATUS: response_status,
            Const.RESPONSE_MOS: mos_dict
        }

        return response_dict

    def _commit_mos(self, timeout=None):
        """Method to send multiple mos in a single XML API request"""

        from .imccoreutils import ConfigConfMosConstants as Const
        mo_dict = self.__to_commit
        if not mo_dict:
            # log.debug("Commit Buffer is Empty")
            return None

        status = 0

        # status_dict is used to convert a string value of status to an integer
        status_dict = {
            Const.RESPONSE_STATUS_FAIL: 1,
            Const.RESPONSE_STATUS_SUCCESS: 2,
            Const.RESPONSE_STATUS_PART_SUCCESS: 4
        }

        # this is the final dictionary to be returned
        ret = {
            Const.RESPONSE_STATUS: None,
            Const.RESPONSE_MOS: {}
        }

        mos = list(mo_dict.values())
        for i in range(0, len(mos), CONFIG_CONF_MOS_BUFFER_SIZE):
            # Configure the mo list received in batches of 10 on the endpoint
            mos_ = list(mos)[i: i + CONFIG_CONF_MOS_BUFFER_SIZE]
            response_dict_ = self.__process_config_conf_mos(mos_, timeout)

            # Fetch the status from configuration of a batch and save it in
            # the overall status
            status_str = response_dict_[Const.RESPONSE_STATUS]
            status |= status_dict[status_str]

            # Update the ret dictionary
            response_mos_ = response_dict_[Const.RESPONSE_MOS]
            passed = ret[Const.RESPONSE_MOS].get(Const.RESPONSE_PASSED_MOS, {})
            failed = ret[Const.RESPONSE_MOS].get(Const.RESPONSE_FAILED_MOS, {})
            passed.update(response_mos_[Const.RESPONSE_PASSED_MOS])
            failed.update(response_mos_[Const.RESPONSE_FAILED_MOS])

            ret[Const.RESPONSE_MOS][Const.RESPONSE_PASSED_MOS] = passed
            ret[Const.RESPONSE_MOS][Const.RESPONSE_FAILED_MOS] = failed


        if status == 0:
            ret[Const.RESPONSE_STATUS] = None
        elif status == 1:
            ret[Const.RESPONSE_STATUS] = Const.RESPONSE_STATUS_FAIL
        elif status == 2:
            ret[Const.RESPONSE_STATUS] = Const.RESPONSE_STATUS_SUCCESS
        elif status >= 3:
            ret[Const.RESPONSE_STATUS] = Const.RESPONSE_STATUS_PART_SUCCESS

        # Always cleanup the commit buffer
        self.__to_commit.clear()
        return ret
