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
import time
from threading import Timer

from .imcdriver import ImcDriver
from .imcexception import ImcException, ImcLoginError

log = logging.getLogger('imc')


class ImcSession(object):
    """
    ImcSession class is session interface for any Imc related communication.
    Parent class of ImcHandle, used internally by ImcHandle class.
    """

    def __init__(self, ip, username, password, port=None, secure=None,
                 proxy=None):
        self.__ip = ip
        self.__username = username
        self.__password = password
        self.__proxy = proxy
        self.__uri = self.__create_uri(port, secure)

        self.__imc = ip
        self.__name = None
        self.__cookie = None
        self.__session_id = None
        self.__version = None
        self.__refresh_period = None
        self.__priv = None
        self.__domains = None
        self.__channel = None
        self.__evt_channel = None
        self.__last_update_time = None

        self.__refresh_timer = None
        self.__force = False

        self.__dump_xml = False
        self.__redirect = False
        self.__driver = ImcDriver(proxy=self.__proxy)

    @property
    def ip(self):
        return self.__ip

    @property
    def username(self):
        return self.__username

    @property
    def proxy(self):
        return self.__proxy

    @property
    def uri(self):
        return self.__uri

    @property
    def imc(self):
        return self.__imc

    @property
    def name(self):
        return self.__name

    @property
    def cookie(self):
        return self.__cookie

    @property
    def session_id(self):
        return self.__session_id

    @property
    def version(self):
        return self.__version

    @property
    def refresh_period(self):
        return self.__refresh_period

    @property
    def priv(self):
        return self.__priv

    @property
    def domains(self):
        return self.__domains

    @property
    def channel(self):
        return self.__channel

    @property
    def evt_channel(self):
        return self.__evt_channel

    @property
    def last_update_time(self):
        return self.__last_update_time

    def __create_uri(self, port, secure):
        """
        Generates IMC URI used for connection

        Args:
            port (int): port The port number to be used during connection
            secure (bool or None): True for secure connection otherwise False

        Returns:
            uri (str)

        Example:
            uri = __create_uri(port=443, secure=True)
        """

        if secure is not None and port is not None:
            self.__secure = secure
            self.__port = int(port)
        elif secure is not None and port is None:
            if secure:
                self.__port = 443
                self.__secure = True
            else:
                self.__port = 80
                self.__secure = False
        elif secure is None and port is not None:
            if int(port) == 80:
                self.__secure = False
                self.__port = 80
            elif int(port) == 443:
                self.__secure = True
                self.__port = 443
            else:
                self.__secure = True
                self.__port = int(port)
        else:
            self.__secure = True
            self.__port = 443

        https_or_http = ("http", "https")[self.__secure]
        host = self.__ip
        port = str(self.__port)
        uri = "%s://%s%s%s" % (https_or_http, host, ":", port)
        return uri

    def __clear(self):
        """
        Internal method to clear the session variables
        """

        self.__name = None
        self.__cookie = None
        self.__session_id = None
        self.__version = None
        self.__refresh_period = None
        self.__priv = None
        self.__domains = None
        self.__channel = None
        self.__evt_channel = None
        self.__last_update_time = str(time.asctime())

    def __update(self, response):
        """
        Internal method to update the session variables
        """

        from .imccoremeta import ImcVersion
        self.__cookie = response.out_cookie
        self.__session_id = response.out_session_id
        self.__version = ImcVersion(response.out_version)
        self.__refresh_period = response.out_refresh_period
        self.__priv = response.out_priv
        self.__domains = response.out_domains
        self.__channel = response.out_channel
        self.__evt_channel = response.out_evt_channel
        self.__last_update_time = str(time.asctime())

    def post(self, uri, data=None, read=True):
        """
        sends the request and receives the response from imcm server

        Args:
            uri (str): URI of the  the imc Server
            data (str): request data to send via post request

        Returns:
            response xml string

        Example:
            response = post("http://192.168.1.1:80", data=xml_str)
        """

        response = self.__driver.post(uri=uri, data=data, read=read)
        return response

    def post_xml(self, xml_str, read=True):
        """
        sends the xml request and receives the response from imc server

        Args:
            xml_str (str): xml string

        Returns:
            response xml string

        Example:
            response = post_xml('<aaaLogin inName="user" inPassword="pass">')
        """

        imc_uri = self.__uri + "/nuova"
        response_str = self.post(uri=imc_uri, data=xml_str, read=read)
        if self.__driver.redirect_uri:
            self.__uri = self.__driver.redirect_uri

        return response_str

    def post_elem(self, elem):
        """
        sends the request and receives the response from imc server using xml
        element

        Args:
            elem (xml element)

        Returns:
            response xml string

        Example:
            response = post_elem(elem=xml_element)
        """

        from . import imcxmlcodec as xc
        dump_xml = self.__dump_xml
        if dump_xml:
            if elem.tag == "aaaLogin":
                elem.attrib['inPassword'] = "*********"
                xml_str = xc.to_xml_str(elem)
                log.debug('%s ====> %s' % (self.__uri, xml_str))
                elem.attrib['inPassword'] = self.__password
                xml_str = xc.to_xml_str(elem)
            else:
                xml_str = xc.to_xml_str(elem)
                log.debug('%s ====> %s' % (self.__uri, xml_str))
        else:
            xml_str = xc.to_xml_str(elem)

        response_str = self.post_xml(xml_str)
        if dump_xml:
            log.debug('%s <==== %s' % (self.__uri, response_str))

        if response_str:
            response = xc.from_xml_str(response_str, self)
            return response

        return None

    def file_download(self, url_suffix, file_dir, file_name):
        """
        Downloads the file from imc server

        Args:
            url_suffix (str): suffix url to be appended to
                    http\https://host:port/ to locate the file on the server
            file_dir (str): The directory to download to
            file_name (str): The destination file name for the download

        Returns:
            None

        Example:
            file_download(url_suffix='backupfile/config_backup.xml',
            file_dir='/home/user/backup', file_name='my_config_backup.xml')
        """

        from .imcgenutils import download_file

        file_url = "%s/%s" % (self.__uri, url_suffix)

        self.__driver.add_header('Cookie', 'imc-cookie=%s'
                                 % self.__cookie)

        download_file(driver=self.__driver,
                      file_url=file_url,
                      file_dir=file_dir,
                      file_name=file_name)

        self.__driver.remove_header('Cookie')

    def file_upload(self, url_suffix, file_dir, file_name):
        """
        Uploads the file on IMC server.

        Args:
            url_suffix (str): suffix url to be appended to
                http\https://host:port/ to locate the file on the server
            file_dir (str): The directory to upload from
            file_name (str): The destination file name for the download

        Returns:
            None

        Example:
            file_dir = "/home/user/backup"\n
            file_name = "config_backup.xml"\n
            uri_suffix = "operations/file-%s/importconfig.txt" % file_name\n
            file_upload(url_suffix=uri_suffix, file_dir=file_dir,
            file_name=file_name)
        """

        from .imcgenutils import upload_file

        file_url = "%s/%s" % (self.__uri, url_suffix)

        self.__driver.add_header('Cookie', 'imc-cookie=%s'
                                 % self.__cookie)

        upload_file(self.__driver,
                    uri=file_url,
                    file_dir=file_dir,
                    file_name=file_name)

        self.__driver.remove_header('Cookie')

    def __start_refresh_timer(self):
        """
        Internal method to support auto-refresh functionality.
        """

        if self.__refresh_period > 60:
            interval = int(self.__refresh_period) - 60
        else:
            interval = 60
        self.__refresh_timer = Timer(interval, self._refresh)
        # TODO:handle exit and logout active connections. revert from daemon
        self.__refresh_timer.setDaemon(True)
        self.__refresh_timer.start()

    def __stop_refresh_timer(self):
        """
        Internal method to support auto-refresh functionality.
        """

        if self.__refresh_timer is not None:
            self.__refresh_timer.cancel()
            self.__refresh_timer = None

    def _refresh(self, auto_relogin=False):
        """
        Sends the aaaRefresh query to the imc to refresh the connection
        (to prevent session expiration).
        """

        from .imcmethodfactory import aaa_refresh

        self.__stop_refresh_timer()

        elem = aaa_refresh(self.__cookie, self.__username, self.__password)
        response = self.post_elem(elem)
        if response.error_code != 0:
            self.__cookie = None
            if auto_relogin:
                return self._login()
            return False

        self.__cookie = response.out_cookie
        self.__refresh_period = int(response.out_refresh_period)
        self.__priv = response.out_priv.split(',')
        self.__domains = response.out_domains
        self.__last_update_time = str(time.asctime())

        # re-enable the timer
        self.__start_refresh_timer()
        return True

    def __is_fabric_interconnect(self):
        from .imcmethodfactory import config_resolve_class

        nw_elem = config_resolve_class(cookie=self.__cookie,
                                       class_id="networkElement")
        try:
            nw_elem_response = self.post_elem(nw_elem)
            if nw_elem_response.error_code == 0:
                return True
            else:
                return False
        except:
            return False

    def __validate_connection(self):
        """
        Internal method to validate if needs to reconnect or if exist use the
        existing connection.
        """

        from .mometa.top.TopSystem import TopSystem
        from .imcmethodfactory import config_resolve_dn

        if self.__cookie is not None and self.__cookie != "":
            if not self.__force:
                top_system = TopSystem()
                elem = config_resolve_dn(cookie=self.__cookie,
                                         dn=top_system.dn)
                response = self.post_elem(elem)
                if response.error_code != 0:
                    return False
                return True
            else:
                self._logout()
        return False

    def __validate_imc(self):
        """ ValidateIMC method validates if a given host is valid IMC Server."""

        from .imcmethodfactory import config_resolve_class

        valid_models = ("R460-4640810", "C260-BASE-2646")
        model_validated = False

        rack_elem = config_resolve_class(cookie=self.__cookie,
                                         class_id="computeRackUnit")
        rack_elem_response = self.post_elem(rack_elem)
        if rack_elem_response.error_code == 0:
            for rack in rack_elem_response.out_configs.child:
                model_name = rack.model
                if model_name.startswith("UCSC"):
                    model_validated = True
                elif model_name.startswith("UCS-E"):
                    model_validated = True
                elif model_name in valid_models:
                    model_validated = True
            if not model_validated:
                self._logout()
                return False

        if self.__is_fabric_interconnect():
            self._logout()
            return False
        return True

    def _login(self, auto_refresh=False, force=False):
        """
        Internal method responsible to do a login on imc server.

        Args:
            auto_refresh (bool): if set to True, it refresh the cookie
                                    continuously
            force (bool): if set to True it reconnects even if cookie exists
                                    and is valid for respective connection.

        Returns:
            True on successful connect
        """

        from .mometa.top.TopSystem import TopSystem
        from .mometa.firmware.FirmwareRunning import FirmwareRunning, \
            FirmwareRunningConsts
        from .imccoremeta import ImcVersion
        from .imcmethodfactory import aaa_login
        from .imcmethodfactory import config_resolve_dn

        if self.__validate_connection():
            return True

        elem = aaa_login(in_name=self.__username, in_password=self.__password)
        response = self.post_elem(elem)
        if response.error_code != 0:
            self.__clear()
            raise ImcException(response.error_code, response.error_descr)
        self.__update(response)

        # Verify not to connect to IMC
        if not self.__validate_imc():
            raise ImcLoginError("Not a supported server.")

        top_system = TopSystem()
        if response.out_version is None or response.out_version == "":
            firmware = FirmwareRunning(top_system,
                                       FirmwareRunningConsts.DEPLOYMENT_SYSTEM)
            elem = config_resolve_dn(cookie=self.__cookie, dn=firmware.dn)
            response = self.post_elem(elem)
            if response.error_code != 0:
                raise ImcException(response.error_code,
                                   response.error_descr)
            firmware = response.out_config.child[0]
            self._version = ImcVersion(firmware.version)

        top_system = TopSystem()
        elem = config_resolve_dn(cookie=self.__cookie, dn=top_system.dn)
        response = self.post_elem(elem)
        if response.error_code != 0:
            raise ImcException(response.error_code, response.error_descr)
        top_system = response.out_config.child[0]
        self._imc = top_system.name
        self.__virtual_ipv4_address = top_system.address

        if auto_refresh:
            self.__start_refresh_timer()

        return True

    def _logout(self):
        """
        Internal method to disconnect from imc server.

        Args:
            None

        Returns:
            True on successful disconnect

        """

        from .imcmethodfactory import aaa_logout

        if self.__cookie is None:
            return True

        if self.__refresh_timer:
            self.__refresh_timer.cancel()

        if self.__cookie:
            elem = aaa_logout(self.__cookie)
            response = self.post_elem(elem)

            if response.error_code == "555":
                return True

            if response.error_code != 0:
                raise ImcException(response.error_code,
                                   response.error_descr)

            self.__clear()

            return True

    def _set_dump_xml(self):
        """
        Internal method to set dump_xml to True
        """
        self.__dump_xml = True

    def _unset_dump_xml(self):
        """
        Internal method to set dump_xml to False
        """
        self.__dump_xml = False
