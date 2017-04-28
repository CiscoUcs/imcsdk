Containerized imcsdk for CIMC 3.0 using Docker
==============================================

The new CIMC version 3.0 needs:

-  TLS 1.2
-  Python2 version >= 2.7.9  or  Python3 version >= 3.2
-  OpenSSL version >= 1.0.1

https://github.com/CiscoUcs/imcsdk/blob/master/docs/imcsdk_ug.rst#getting-started

RHEL ships with Python 2.7.5 as the system Python version:

::

        # cat /etc/redhat-release
        Red Hat Enterprise Linux Server release 7.2 (Maipo)

        # python -V
        Python 2.7.5


CentOS also ships with Python 2.7.5 as the system Python version:

::

        # cat /etc/centos-release
        CentOS Linux release 7.3.1611 (Core)

        # python -V
        Python 2.7.5


Upgrading system Python in RHEL from Python 2.7.5 to Python  >= 2.7.9 breaks a lot of packages like pip, yum, ansible, OpenStack packages, etc.

Upgrading system OpenSSL to version >= 1.0.1 may break VPN client and SSL.  Apple MacOS sierra ships with OpenSSL 0.9.8 and will not even allow the user to upgrade OpenSSL.

Hence, the best approach is to containerize imcsdk using Docker with all the required dependencies/packages needed to programmatically interact with CIMC 3.0.

The container must have the following packages needed for CIMC 3.0:

-  Python 2.7.13 (Python >= 2.7.9 is needed for CIMC 3.0)
-  pip with Python 2.7.13
-  OpenSSL 1.0.1
-  Cisco's Python imcsdk library (https://github.com/CiscoUcs/imcsdk)
-  DMTF's Python RedFish library (python-redfish-library in https://github.com/DMTF/python-redfish-library)
-  epel-release and latest Ansible (if the user want to automate anything with CIMC 3.0)
-  Python requests library needed to interact with RedFish URIs /redfish/v1/*

Download the ``Dockerfile`` in this directory to your host.

Install Docker on the RHEL/CentOS/MacOS host.  Ubuntu host has not been tested as the above container is a CentOS images.

**RHEL**   - https://docs.docker.com/engine/installation/linux/rhel/
**CentOS** - https://docs.docker.com/engine/installation/linux/centos/
**MacOS**  - https://docs.docker.com/docker-for-mac/install/

After installing and starting the Docker daemon on the host, go to the directory that contains the downloaded ``Dockerfile`` and build the ``centos-cimc-3.0`` container.  This takes 15-20 minutes.

::

        cd <path to downloaded Dockerfile>
        docker build --rm -t centos-cimc-3.0 .


Remove unwanted intermediate containers:

::

        docker images | grep '<none>' | awk '{print $3}' | xargs docker rmi -f


Check the built image of the container ``centos-cimc-3.0``:

::

        $ docker images
        REPOSITORY                                    TAG                 IMAGE ID            CREATED             SIZE
        centos-cimc-3.0                               latest              2e353ccfbc24        About an hour ago   1.08 GB
        centos                                        latest              a8493f5f50ff        3 weeks ago         192 MB


Run/start the built container:

::

        docker run --hostname cimc-3.0 --name cimc-3.0 -d centos-cimc-3.0


Check the started running container ``cimc-3.0``:

::

        $ docker ps -a
        CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
        9df66e090529        2e353ccfbc24        "sleep infinity"    2 minutes ago      Up 2 minutes                           cimc-3.0


Enter inside the container to start interacting with CIMC 3.0 from inside the container:

::

        $ docker exec -it cimc-3.0 /bin/bash
        [root@cimc-3 /]#


Once inside the container, make sure that all the packages needed for CIMC 3.0 are installed in the container.

::

        [root@cimc-3 /]# python2.7.13 -V
        Python 2.7.13
         
        [root@cimc-3 /]# openssl version
        OpenSSL 1.0.1e-fips 11 Feb 2013
         
        [root@cimc-3 /]# pip list | grep 'imcsdk\|redfish\|requests'
        imcsdk (0.9.2.0)
        redfish (1.0.0)
        requests (2.13.0)
         
        [root@cimc-3 /]# ansible --version
        ansible 2.3.0.0
         
        [root@cimc-3 /]# curl --version
        curl 7.29.0


Test if ``imcsdk`` APIs work with CIMC 3.0 inside the container.  Below, we use imcsdk to get the BIOS settings and the inventory of the UCS server with CIMC 3.0.

::

        [root@cimc-3 /]# python2.7.13
        Python 2.7.13 (default, Apr 19 2017, 20:05:12)
        [GCC 4.8.5 20150623 (Red Hat 4.8.5-11)] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        >>>
        >>> import imcsdk
        >>> from imcsdk.imchandle import ImcHandle
        >>> from imcsdk.apis.server.inventory import inventory_get
        >>> imcsdk.__version__
        '0.9.2.0'
         
        >>> handle = ImcHandle("10.18.253.253", "admin", "SomePassword")
        >>> handle.login()
        True
         
        >>> handle.version._ImcVersion__version
        '3.0(1c)'
         
        >>> bios_settings = handle.query_dn('sys/rack-unit-1/bios/bios-settings')
        >>> bios_settings.__dict__
        {'status': None, 'dn': 'sys/rack-unit-1/bios/bios-settings', '_ManagedObject__xtra_props': {}, '_ManagedObject__parent_dn': 'sys/rack-unit-1/bios', '_dirty_mask': 0, '_handle': <imcsdk.imchandle.ImcHandle object at 0x7f799136ec90>, '_child': [], '_ManagedObject__xtra_props_dirty_mask': 1, '_ManagedObject__status': None, 'rn': 'bios-settings', '_ManagedObject__parent_mo': None, '_class_id': 'BiosSettings', 'child_action': None}
         
        >>> inventory_get(handle=handle)
        {'10.18.253.253': {'vic': [{'dn': 'sys/rack-unit-1/adaptor-MLOM', 'vendor': 'Cisco Systems Inc', 'model': 'UCSC-MLOM-CSC-02', 'pci_slot': 'MLOM', 'id': 'MLOM', 'serial': 'FCH20477D4X'}], 'vHBAs': [], 'tpm': [{'dn': 'sys/rack-unit-1/board/tpm', 'model': 'NA', 'vendor': 'NA', 'serial': 'NA', 'tpm_revision': 'NA'}
         
        >>> (Press CTRL+D to exit)
        [root@cimc-3 /]# exit


Test if Python's ``requests`` library works with **RedFish** URIs CIMC 3.0 inside the container.

Below, we use Python's ``requests`` library with **RedFish** URIs (``/redfish/v1/*``) to get the model number, serial number and BIOS version of the UCS server with CIMC 3.0.

::

        [root@cimc-3 /]# python2.7.13
        Python 2.7.13 (default, Apr 19 2017, 20:05:12)
        [GCC 4.8.5 20150623 (Red Hat 4.8.5-11)] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        >>>
        >>> import json
        >>> import requests
        >>> ro = requests.get("https://10.18.253.253/redfish/v1/Systems", verify=False, auth=("admin", "SomePassword"))
        >>> ro
        <Response [200]>
         
        >>> ro_json = ro.json()
        >>> uri = "https://10.18.253.253" + ro_json['Members'][0]['@odata.id']
        >>> ro = requests.get(uri, verify=False, auth=("admin", "SomePassword"))
        >>> ro
        <Response [200]>
         
        >>> ro_json = ro.json()
        >>> ro_json['Model']
        u'UCS C220 M4S'
         
        >>> ro_json['SerialNumber']
        u'FCH2047V0LJ'
         
        >>> ro_json['BiosVersion']
        u'C220M4.3.0.1b.0.1201161639'
         
        >>> (Press CTRL+D to exit)
        [root@cimc-3 /]# exit


Test if we can use ``curl`` to get objects from RedFish URIs inside the container.

::

        [root@cimc-3 /]# curl --insecure -u admin:SomePassword https://10.18.253.253/redfish/v1
        {
          "Chassis":{
            "@odata.id":"/redfish/v1/Chassis"
          },
          "@odata.id":"/redfish/v1/",
          "JSONSchemas":{
            "@odata.id":"/redfish/v1/JSONSchemas"
          },
          "RedfishVersion":"1.0.0",
          "EventService":{
            "@odata.id":"/redfish/v1/EventService"
          },
          "Systems":{
            "@odata.id":"/redfish/v1/Systems"
          },
          "Description":"Root Service",
          "Name":"Cisco RESTful Root Service",
          "Links":{
            "Sessions":{
              "@odata.id":"/redfish/v1/SessionService/Sessions"
            }
          },
          "TaskService":{
            "@odata.id":"/redfish/v1/TaskService"
          },
          "Managers":{
            "@odata.id":"/redfish/v1/Managers"
          },
          "@odata.type":"#ServiceRoot.1.0.0.ServiceRoot",
          "SessionService":{
            "@odata.id":"/redfish/v1/SessionService"
          },
          "@odata.context":"/redfish/v1/$metadata#ServiceRoot",
          "Id":"RootService",
          "AccountService":{
            "@odata.id":"/redfish/v1/AccountService"
          },
          "MessageRegistry":{
            "@odata.id":"/redfish/v1/MessageRegistry"
          }
        }
         
        [root@cimc-3 /]# curl --insecure -u admin:SomePassword https://10.18.253.253/redfish/v1/Systems
        {
          "Members":[{
              "@odata.id":"/redfish/v1/Systems/FCH2047V0LJ"
            }],
          "Description":"Collection of Computer Systems",
          "@odata.type":"#Cisco_ComputerSystemCollection",
          "@odata.id":"/redfish/v1/Systems",
          "Members@odata.count":1,
          "Name":"Computer System Collection",
          "@odata.context":"/redfish/v1/$metadata#Systems"
        }
         
        [root@cimc-3 /]# curl --insecure -u admin:SomePassword https://10.18.253.253/redfish/v1/Systems/FCH2047V0LJ
        {
          "SerialNumber":"FCH2047V0LJ",
          "Boot":{
            "BootSourceOverrideEnabled":"Disabled",
            "BootSourceOverrideTarget":"None"
          },
          "Id":"FCH2047V0LJ",
          "AssetTag":"Unknown",
          "PowerState":"Off",
          "SystemType":"Physical",
          "ProcessorSummary":{
            "Model":"Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz",
            "Count":2
          },
          "HostName":"C220-FCH2047V0LJ",
          "MemorySummary":{
            "TotalSystemMemoryGiB":256,
            "State":{
              "HealthRollup":"OK",
              "Health":"OK"
            }
          },
          "Processors":{
            "@odata.id":"/redfish/v1/Systems/FCH2047V0LJ/Processors"
          },
          "Description":"",
          "Links":{
            "CooledBy":["/redfish/v1/Chassis/1/Thermal"],
            "Chassis":["/redfish/v1/Chassis/1"],
            "PoweredBy":["/redfish/v1/Chassis/1/Power"],
            "ManagedBy":["/redfish/v1/Managers/CIMC"]
          },
          "SimpleStorage":{
            "@odata.id":"/redfish/v1/Systems/FCH2047V0LJ/SimpleStorage"
          },
          "UUID":"5236D4DC-04B3-4864-8A96-22C481844E0A",
          "Status":{
            "State":"Enabled",
            "Health":"Warning"
          },
          "BiosVersion":"C220M4.3.0.1b.0.1201161639",
          "Name":"UCS C220 M4S",
          "LogServices":{
            "@odata.id":"/redfish/v1/Systems/FCH2047V0LJ/LogServices"
          },
          "Actions":{
            "#System.Reset":{
              "Target":"/redfish/v1/Systems/FCH2047V0LJ/Actions/System.Reset",
              "ResetType@Redfish.AllowableValues":["On","ForceOff","GracefulShutdown","ForceRestart","Nmi"]
            }
          },
          "@odata.context":"/redfish/v1/$metadata#Systems/Members/$entity",
          "@odata.type":"#Cisco_ComputerSystem",
          "@odata.id":"/redfish/v1/Systems/FCH2047V0LJ",
          "Manufacturer":"Cisco Systems",
          "IndicatorLED":"Off",
          "Model":"UCS C220 M4S",
          "EthernetInterfaces":{
            "@odata.id":"/redfish/v1/Systems/FCH2047V0LJ/EthernetInterfaces"
          }
        }
         
        [root@cimc-3 /]# exit


Links about RedFish:

-  https://www.dmtf.org/standards/redfish
-  http://redfish.dmtf.org
-  RedFish API spec - http://redfish.dmtf.org/schemas/DSP0266_1.1.html
-  Redfish Schema Index - http://redfish.dmtf.org/redfish/schema_index

If the container ``cimc-3.0`` is not needed, stop and remote it:

::

        docker stop cimc-3.0 && docker rm cimc-3.0


If the image ``centos-cimc-3.0`` is not needed, remove it:

::

        docker rmi centos-cimc-3.0
        docker rmi centos


After the Docker image ``centos-cimc-3.0`` is built from the downloaded ``Dockerfile``, it can be tagged (``docker tag``), pushed to any registry (``docker push``), pulled from the registry (``docker pull``), run/started (``docker run``), and used to programmatically interact with CIMC 3.0.
