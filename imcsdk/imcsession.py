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


import time
import logging
import os
from threading import Timer

from .imcexception import ImcException, ImcLoginError
from .imccoremeta import ImcVersion
from .imcdriver import ImcDriver
from .imcgenutils import Progress

log = logging.getLogger('imc')


class ImcSession(object):
    """
    ImcSession class is session interface for any Imc related communication.
    Parent class of ImcHandle, used internally by ImcHandle class.
    """

    def __init__(self, ip, username, password, port=None, secure=None,
                 proxy=None, auto_refresh=False, force=False, timeout=None):
        self.__ip = ip
        self.__username = username
        self.__password = password
        self.__proxy = proxy
        self.__auto_refresh = auto_refresh
        self.__timeout = timeout
        self.__uri = self.__create_uri(port, secure)
        self.__starship_proxy = None
        self.__starship_headers = None
        self.__model = None

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
        self.__force = force

        self.__dump_xml = False
        self.__redirect = False
        self.__driver = ImcDriver(proxy=self.__proxy)

        # In debug mode, log the XMLs to a file
        if os.path.exists('/tmp/imcsdk_debug'):
            self.__dump_xml = True

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

    @property
    def platform(self):
        return self.__platform

    @property
    def model(self):
        return self.__model

    @property
    def version(self):
        return self.__version

    def __create_uri(self, port, secure):
        """
        Generates IMC URI used for connection

        Args:
            port (int or None): The port number to be used during connection
            secure (bool or None): True for secure connection otherwise False

        Returns:
            uri (str)

        Example:
            uri = __create_uri(port=443, secure=True)
        """

        port = _get_port(port, secure)
        protocol = _get_proto(port, secure)

        uri = "%s://%s%s%s" % (protocol, self.__ip, ":", str(port))
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
        self.__refresh_period = int(response.out_refresh_period)
        self.__priv = response.out_priv
        self.__domains = response.out_domains
        self.__channel = response.out_channel
        self.__evt_channel = response.out_evt_channel
        self.__last_update_time = str(time.asctime())

    def post(self, uri, data=None, read=True, timeout=None):
        """
        sends the request and receives the response from the imc server

        Args:
            uri (str): URI of the  the imc Server
            data (str): request data to send via post request

        Returns:
            response xml string

        Example:
            response = post("http://192.168.1.1:80", data=xml_str)
        """

        timeout = timeout if timeout is not None else self.__timeout
        response = self.__driver.post(uri=uri, data=data, read=read, timeout=timeout)
        return response

    def post_xml(self, xml_str, read=True, timeout=None):
        """
        sends the xml request and receives the response from the imc server

        Args:
            xml_str (str): xml string
            read (bool): if True, returns response.read() else returns object.
            timeout (int): if set, this will be used as timeout in secs for urllib2

        Returns:
            response xml string

        Example:
            response = post_xml('<aaaLogin inName="user" inPassword="pass">')
        """

        if self.__starship_proxy is not None:
            self.__uri = self.__starship_proxy
            imc_uri = self.__starship_proxy
        else:
            imc_uri = self.__uri + "/nuova"
        response_str = self.post(uri=imc_uri, data=xml_str, read=read, timeout=timeout)
        if self.__driver.redirect_uri:
            self.__uri = self.__driver.redirect_uri

        return response_str

    def dump_xml_request(self, elem):
        from . import imcxmlcodec as xc
        if not self.__dump_xml:
            return

        if elem.tag == "aaaLogin":
            elem.attrib['inPassword'] = "*********"
            xml_str = xc.to_xml_str(elem)
            log.debug('%s ====> %s' % (self.__uri, xml_str))
            elem.attrib['inPassword'] = self.__password
            xml_str = xc.to_xml_str(elem)
        else:
            xml_str = xc.to_xml_str(elem)
            log.debug('%s ====> %s' % (self.__uri, xml_str))

    def dump_xml_response(self, resp):
        if self.__dump_xml:
            log.debug('%s <==== %s' % (self.__uri, resp))

    def post_elem(self, elem, timeout=None):
        """
        sends the request and receives the response from the imc server using xml
        element

        Args:
            elem (xml element)
            timeout (int): if set, it is used as timeout in secs for urllib2

        Returns:
            response xml string

        Example:
            response = post_elem(elem=xml_element)
        """

        from . import imcxmlcodec as xc

        if self._is_stale_cookie(elem):
            elem.attrib['cookie'] = self.cookie

        self.dump_xml_request(elem)
        xml_str = xc.to_xml_str(elem)

        response_str = self.post_xml(xml_str, timeout=timeout)
        self.dump_xml_response(response_str)

        if response_str:
            response = xc.from_xml_str(response_str, self)

            # Cookie update should happen with-in the lock
            # this ensures that the next packet goes out
            # with the new cookie
            if elem.tag == "aaaRefresh":
                self._update_cookie(response)

            return response

        return None

    def file_download(
            self,
            url_suffix,
            file_dir,
            file_name,
            progress=Progress()):
        """
        Downloads the file from the imc server

        Args:
            url_suffix (str): suffix url to be appended to
                    http\https://host:port/ to locate the file on the server
            file_dir (str): The directory to download to
            file_name (str): The destination file name for the download
            progress (imcgenutils.Progress): Class that has method to display progress

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
                      file_name=file_name,
                      progress=progress)

        self.__driver.remove_header('Cookie')

    def file_upload(
            self,
            url_suffix,
            file_dir,
            file_name,
            progress=Progress()):
        """
        Uploads the file on IMC server.

        Args:
            url_suffix (str): suffix url to be appended to
                http\https://host:port/ to locate the file on the server
            file_dir (str): The directory to upload from
            file_name (str): The destination file name for the download
            progress (imcgenutils.Progress): Class that has method to display progress

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
                    file_name=file_name,
                    progress=progress)

        self.__driver.remove_header('Cookie')

    def _start_refresh_timer(self):
        """
        Internal method to support auto-refresh functionality.
        """

        if self.__refresh_period > 60:
            interval = int(self.__refresh_period) - 60
        else:
            interval = 60
        self.__refresh_timer = Timer(interval, self._refresh)
        self.__refresh_timer.setDaemon(True)
        self.__refresh_timer.start()

    def _stop_refresh_timer(self):
        """
        Internal method to support auto-refresh functionality.
        """

        if self.__refresh_timer:
            self.__refresh_timer.cancel()
            self.__refresh_timer = None

    def _update_cookie(self, response):
        if response.error_code != 0:
            return
        self.__cookie = response.out_cookie

    def _is_stale_cookie(self, elem):
        return 'cookie' in elem.attrib and elem.attrib[
            'cookie'] != "" and elem.attrib['cookie'] != self.cookie

    def _refresh(self, auto_relogin=True):
        """
        Sends the aaaRefresh query to the imc to refresh the connection
        (to prevent session expiration).
        """

        from .imcmethodfactory import aaa_refresh

        self._stop_refresh_timer()

        elem = aaa_refresh(self.__cookie,
                           self.__username,
                           self.__password)
        response = self.post_elem(elem)
        if response.error_code != 0:
            self.__cookie = None
            if auto_relogin:
                return self._login(auto_refresh=True)
            return False

        self.__cookie = response.out_cookie
        self.__refresh_period = int(response.out_refresh_period)
        self.__priv = response.out_priv.split(',')
        self.__domains = response.out_domains
        self.__last_update_time = str(time.asctime())

        # re-enable the timer
        self._start_refresh_timer()
        return True

    def _is_fabric_interconnect(self):
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

    def _validate_connection(self):
        """
        Internal method to validate if needs to reconnect or if exist use the
        existing connection.
        """

        from .mometa.top.TopSystem import TopSystem
        from .imcmethodfactory import config_resolve_dn

        if self.__cookie and self.__cookie != "":
            if not self.__force:
                top_system = TopSystem()
                elem = config_resolve_dn(cookie=self.__cookie,
                                         dn=top_system.dn)
                response = self.post_elem(elem)
                if response.error_code != 0:
                    return False
                return True
            else:
                try:
                    self._logout()
                except Exception as e:
                    # Logout can fail when the cookie is stale.
                    # Cookie can be stale when CIMC has restarted.
                    # Empty the cookie here.
                    self.__cookie = None
                    raise
        return False

    def _validate_model(self, model):
        valid_model_prefixes = ["UCSC", "UCS-E", "UCSS", "HX"]
        valid_models = ["R460-4640810", "C260-BASE-2646"]

        if model in valid_models:
            return True

        for prefix in valid_model_prefixes:
            if model.startswith(prefix):
                return True

        return False

    def _validate_imc(self):
        """
        This method validates if a given host is a supported IMC server
        """
        from .imcmethodfactory import config_resolve_class

        request = config_resolve_class(cookie=self.__cookie,
                                       class_id="biosUnit")
        response = self.post_elem(request)

        if not response or response.error_code != 0 or \
                len(response.out_configs.child) == 0:
            self.logout()
            return False

        for element in response.out_configs.child:
            model = element.model

            if not self._validate_model(model):
                self._logout()
                return False

            self._set_platform(model=model)
            self._set_model(model=model)

        return True

    def _update_version(self, response=None):
        from .imccoremeta import ImcVersion
        from .imcmethodfactory import config_resolve_dn
        from .mometa.top.TopSystem import TopSystem
        from .mometa.firmware.FirmwareRunning import FirmwareRunning, \
            FirmwareRunningConsts

        # If the aaaLogin response has the version populated, we do not
        # need to query for it
        # There are cases where version is missing from aaaLogin response
        # In such cases the later part of this method populates it
        if response.out_version and response.out_version != "":
            return

        top_system = TopSystem()
        firmware = FirmwareRunning(top_system,
                                   FirmwareRunningConsts.DEPLOYMENT_SYSTEM)
        elem = config_resolve_dn(cookie=self.__cookie,
                                 dn=firmware.dn)
        response = self.post_elem(elem)
        if response.error_code != 0:
            raise ImcException(response.error_code,
                               response.error_descr)
        firmware = response.out_config.child[0]
        self._set_version(firmware.version)

    def _update_domain_name_and_ip(self):
        from .imcmethodfactory import config_resolve_dn
        from .mometa.top.TopSystem import TopSystem

        top_system = TopSystem()
        elem = config_resolve_dn(cookie=self.__cookie, dn=top_system.dn)
        response = self.post_elem(elem)
        if response.error_code != 0:
            raise ImcException(response.error_code, response.error_descr)
        top_system = response.out_config.child[0]
        self.__imc = top_system.name
        self.__virtual_ipv4_address = top_system.address

    def _login(self, auto_refresh=None, force=None, timeout=None):
        """
        Internal method responsible to do a login on imc server.

        Args:
            auto_refresh (bool): if set to True, it refresh the cookie
                                    continuously
            force (bool): if set to True it reconnects even if cookie exists
                                    and is valid for respective connection.
            timeout (int): timeout value in secs

        Returns:
            True on successful connect
        """
        from .imcmethodfactory import aaa_login
        from .imccoreutils import add_handle_to_list

        self.__force = force if force is not None else self.__force
        auto_refresh = auto_refresh if auto_refresh is not None else self.__auto_refresh

        if self._validate_connection():
            return True

        elem = aaa_login(in_name=self.__username,
                         in_password=self.__password)
        response = self.post_elem(elem, timeout=timeout)
        if response.error_code != 0:
            self.__clear()
            raise ImcException(response.error_code, response.error_descr)
        self.__update(response)

        # Verify to connect to IMC only
        if not self._validate_imc():
            raise ImcLoginError("Not a supported server.")

        self._update_version(response)
        self._update_domain_name_and_ip()

        if auto_refresh:
            self._start_refresh_timer()

        add_handle_to_list(self)
        return True

    def _logout(self, timeout=None):
        """
        Internal method to disconnect from the imc server.

        Args:
            None

        Returns:
            True on successful disconnect

        """

        from .imcmethodfactory import aaa_logout
        from .imccoreutils import remove_handle_from_list

        if self.__cookie is None:
            return True

        if self.__refresh_timer:
            self.__refresh_timer.cancel()

        elem = aaa_logout(self.__cookie)
        response = self.post_elem(elem, timeout=timeout)

        if response.error_code == "555":
            return True

        if response.error_code != 0:
            raise ImcException(response.error_code,
                               response.error_descr)

        self.__clear()

        remove_handle_from_list(self)
        return True

    def _is_starship(self):
        if self.__starship_proxy:
            return True
        return False

    def _set_starship_proxy(self, proxy):
        """
        Internal method to set proxy URL in starship environment
        """
        self.__starship_proxy = proxy
        self.__driver.__redirect_uri = proxy

    def _set_starship_headers(self, headers):
        """
        Internal method to set proxy URL in starship environment
        """
        self.__starship_headers = headers
        for header in headers:
            self.__driver.add_header(header, headers[header])

        # set cookie for to_xml to work correctly
        if headers["x-barracuda-session"]:
            self.__cookie = headers["x-barracuda-session"]
        else:
            self.__cookie = headers["x-barracuda-apikey"]

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

    def _set_platform(self, model=None, platform=None):
        """
        Internal method to set the platform type
        Not to be exposed at the handle
        """
        from imcsdk.imccoreutils import IMC_PLATFORM
        modular_platform_prefixes = ["UCSC-C3X", "UCSS-S32"]
        if platform:
            self.__platform = platform
        elif model:
            self.__platform = IMC_PLATFORM.TYPE_CLASSIC
            for prefix in modular_platform_prefixes:
                if model.startswith(prefix):
                    self.__platform = IMC_PLATFORM.TYPE_MODULAR

    def _set_version(self, version):
        self.__version = ImcVersion(version)

    def _set_model(self, model, force=False):
        """
        Internal method to set the server model
        Not to be exposed at the handle
        """
        if force and model:
            self.__model = model
            return

        from .imccoreutils import IMC_PLATFORM
        class_ids = {
            IMC_PLATFORM.TYPE_MODULAR: "ComputeServerNode",
            IMC_PLATFORM.TYPE_CLASSIC: "ComputeRackUnit"
            }

        # Check for the right platform
        if self.__platform in class_ids:
            mo_list = self.query_classid(class_ids.get(self.__platform))
            if mo_list:
                self.__model = mo_list[0].model
                return

        # Unknown platform, should not end up here
        # Blindly assign the model passed
        self.__model = model

    def add_header(self, header_prop, header_value):
        self.__driver.add_header(header_prop, header_value)

def _get_port(port, secure):
    if port:
        return int(port)

    if secure is False:
        return 80
    return 443


def _get_proto(port, secure):
    if secure is None:
        if port == "80":
            return "http"
    elif secure is False:
        return "http"
    return "https"
