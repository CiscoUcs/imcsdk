Table of Contents
=================

1.  `Overview <#overview>`__
2.  `Management Information Model <#management-information-model>`__

    1. `Managed Objects <#managed-objects>`__
    2. `References To Managed
       Objects <#references-to-managed-objects>`__
    3. `Properties Of Managed
       Objects <#properties-of-managed-objects>`__
    4. `Methods <#methods>`__

3.  `Installation <#installation>`__

    1. `Pre-install Checklist <#pre-install-checklist>`__
    2. `Installation Steps <#installation-steps>`__

4.  `Uninstallation <#uninstallation>`__

    1. `Uninstallation Steps <#uninstallation-steps>`__

5.  `Getting Started <#getting-started>`__

    1. `Connecting Disconnecting <#connecting-disconnecting>`__
    2. `Base APIs <#basic-apis>`__
    3. `Creating Objects <#creating-objects>`__
    4. `Querying Objects <#querying-objects>`__
    5. `Modifying Objects <#modifying-objects>`__
    6. `Deleting Objects <#deleting-objects>`__

6.  `Retrieving Meta Information <#retrieving-meta-information>`__

7.  `Backup And Import <#backup-and-import>`__

    1. `Backup IMC <#backup-imc>`__
    2. `Import IMC <#import-imc>`__

8. `Technical Support <#technical-support>`__

9. `Firmware Installation <#firmware-installation>`__

10. `Inventory <#inventory>`__


Overview
--------

Cisco IMC Python SDK is a python module which helps automate all aspects
of Cisco IMC management servers i.e. both C-Series and E-Series.
With the introduction of the modular C-3260 platforms, the latest version
of Cisco IMC Python SDK supports both the classic C-Series (for e.g. C220, C240, C22 etc)
and the modular C-Series (C3260).

Bulk of the Cisco IMC Python SDK work on the IMC Manager’s Management
Information Tree (MIT), performing create, modify or delete actions on
the Managed Objects (MO) in the tree. The next chapter provides an
overview of the Cisco IMC Management Information Model (MIM).


Management Information Model
----------------------------

All the physical and logical components that comprise Cisco IMC are
represented in a hierarchical Management Information Model, referred to
as the Management Information Tree (MIT). Each node in the tree
represents a Managed Object (MO), uniquely identified by its
Distinguished Name. (DN)

The figure below illustrates a sample (partial) MIT for Rack Unit.

::

    On a Classic C-series Server
    ----------------------------
    Tree (topRoot)              Distinguished Name
    |-sys                       sys
    |-ComputeRackUnit              sys/rack-unit-1
        |-AdaptorUnit                  sys/rack-unit-1/adaptor-1
            |-AdaptorCfgBackup             sys/rack-unit-1/adaptor-1/export-config

    On a Modular C-series Server
    ----------------------------
    Tree (topRoot)              Distinguished Name
    |-sys                       sys
    |-EquipmentChassis             sys/chassis-1
        |-ComputeServerNode             sys/chassis-1/server-1
            |-AdaptorUnit                   sys/chassis-1/server-1/adaptor-1
                |-AdaptorHostEthIf              sys/chassis-1/server-1/adaptor-1/host-eth-eth0


Managed Objects
~~~~~~~~~~~~~~~

Managed Objects (MO) are abstractions of Cisco IMC resources, such as
such as rack-mounted servers, cpu, memory and network adaptors. Managed
Objects represent any physical or logical entity that is configured /
managed in the Cisco IMC MIT. For example, physical entities such as
rack unit, I/O cards, Processors and logical entities such as User
roles are represented as Managed Objects.

Every Managed Object is uniquely identified in the tree with its
Distinguished Name (Dn) and can be uniquely identified within the
context of its parent with its Relative Name (Rn). The Dn identifies the
place of the MO in the MIT. A Dn is a concatenation of all the relative
names starting from the root to the MO itself. Essentially, Dn =
[Rn]/[Rn]/[Rn]/…/[Rn].

In the example below, Dn provides a fully qualified name for adaptor-1
in the model.

::

    < dn = “sys/rack-unit-1/adaptor-1” />

The above written Dn is composed of the following Rn:

::

    topSystem MO: rn=”sys”
    computeRackUnit MO: rn=”rack-unit-<id>”
    adaptorUnit MO: rn =”adaptor-<id>”

A Relative Name (Rn) may have the value of one or more of the MO’s
properties embedded in it. This allows in differentiating multiple MOs
of the same type within the context of the parent. Any properties that
form part of the Rn as described earlier are referred to as Naming
properties.

For instance, multiple blade MOs reside under a chassis MO. The adaptor
MO contains the adaptor identifier as part of its Rn (adaptor-[id]),
thereby uniquely identifying each adaptor MO in the context of a rack unit.

References To Managed Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The contents of the Managed Objects are referred to during the operation
of IMC. Some of the MOs are referred to implicitly or as part of
deployment of another MO.

A singleton MO type is found utmost once in the entire MIT and is
typically referred to implicitly.

Non-Singleton MO type may be instantiated one or more times in the MIT.
In many cases, when an MO refers to another, the reference is made by
name. Depending on the type of the referenced MO, the resolution may be
hierarchical.

Properties of Managed Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Properties of Managed Objects can be classified as Configuration or
Operational.

Configuration properties may be classified as:

-  Naming properties: Form part of the Rn. **Needs** to be specified
   only during MO creation and cannot be modified later.
-  Create-Only properties: **May** be specified only during MO creation
   and cannot be modified later. If the property is not specified, a
   default value is assumed.
-  Read / Write properties: **May** be specified during MO creation and
   can also be modified subsequently.

Operational properties indicate the current status of the MO / system
and are hence read-only.

Methods
~~~~~~~

Methods are Cisco IMC XML APIs, used to manage and monitor the system.
There are methods supported for:

-  Authentication

   -  AaaLogin
   -  AaaRefresh
   -  AaaLogout

-  Configuration

   -  ConfigConfMo


-  Query

   -  ConfigResolveDn
   -  ConfigResolveClass
   -  ConfigResolveChildren
   -  ConfigResolveParent

-  Event Monitor

   -  EventSubscribe


Installation
------------

Pre-install Checklist
~~~~~~~~~~~~~~~~~~~~~

Ensure the following are available

::

    python >= 2.7
    pip

Installation Steps
~~~~~~~~~~~~~~~~~~

-  Installing the last released version of the SDK from pypi

::

    pip install imcsdk

-  Installing the latest developer version from github

::

    git clone https://github.com/CiscoUcs/imcsdk/
    cd imcsdk
    sudo make install

Uninstallation
--------------

Uninstallation Steps
~~~~~~~~~~~~~~~~~~~~

Irrespective of the method that was used to install the SDK, it can be
uninstalled using the below command,

::

    pip uninstall imcsdk

Getting Started
---------------

Connecting Disconnecting
~~~~~~~~~~~~~~~~~~~~~~~~

::

    from imcsdk.imchandle import ImcHandle

    # Create a connection handle
    handle = ImcHandle("192.168.1.1", "admin", "password")

    # Login to the server
    handle.login()

    # Logout from the server
    handle.logout()

Refer `ImcHandle API
Reference <https://ciscoucs.github.io/imcsdk_docs/imcsdk.html#module-imcsdk.imchandle>`__
for detailed parameter sets to ``ImcHandle``

The handle maintains a reference to the type of platform (classic or modular) that it is managing.
This can be accessed using the ``handle.platform`` property.

Cisco IMC servers running firmware version 3.0(1c) on which secure login is enabled, support only TLS version 1.2.
This includes servers on which http -> https redirection is enabled and running firmware version 3.0(1c).

For successfully connecting to such servers, the following requirements have to be fulfilled :-

- Python2 version >= 2.7.9 or Python3 version >= 3.2
- Openssl version >= 1.0.1


Base APIs
~~~~~~~~~

The SDK provides APIs to enable CRUD operations.

-  **C**\ reate an object - ``add_mo``
-  **R**\ etrieve an object -
   ``query_dn``,\ ``query_classid``
-  **U**\ pdate an object - ``set_mo``
-  **D**\ elete an object - ``remove_mo``


All these methods are invoked on a ``ImcHandle`` instance. We refer it
by ``handle`` in all the examples here-after. Refer to the `Connecting
Disconnecting <#connecting-disconnecting>`__ to create a new handle.

Creating Objects
~~~~~~~~~~~~~~~~

Creating managed objects is done via ``add_mo`` API.

Example:

The below example creates a vnic(\ ``AdaptorHostEthIf``) Object

::

    from imcsdk.mometa.adaptor.AdaptorHostEthIf import AdaptorHostEthIf

    vnic = AdaptorHostEthIf(parent_mo_or_dn='sys/rack-unit-1/adaptor-1',
                            name='vnic-1', mac='00:11:22:33:44:55',
                            mtu=1500, pxe_boot=True, uplink_port=0)
    handle.add_mo(vnic)


`Add Mo API
reference <https://ciscoucs.github.io/imcsdk_docs/imcsdk.html?highlight=add_mo#imcsdk.imchandle.ImcHandle.add_mo>`__

Querying Objects
~~~~~~~~~~~~~~~~

-  Querying Objects via Distinguished Name (DN)

   ::

       object = handle.query_dn("sys/rack-unit-1")

-  Querying Objects via class Id

   The below returns all objects of type ``computeRackUnit``

   ::

       object_array = handle.query_classid("computeRackUnit")

`Query DN API
reference <https://ciscoucs.github.io/imcsdk_docs/imcsdk.html?highlight=query_dn#imcsdk.imchandle.ImcHandle.query_dn>`__

`Query Class Id API
reference <https://ciscoucs.github.io/imcsdk_docs/imcsdk.html?highlight=query_classid#imcsdk.imchandle.ImcHandle.query_classid>`__


Modifying Objects
~~~~~~~~~~~~~~~~~

``set_mo`` is used for updating an existing object

::

    # Query for an existing Mo
    rack = handle.query_dn('sys/rack-unit-1')

    # Update the usr_lbl field
    rack.usr_lbl = 'RackUnit10'

    # Add it to the on-going transaction
    handle.set_mo(rack)

`Set Mo API
reference <https://ciscoucs.github.io/imcsdk_docs/imcsdk.html?highlight=set_mo#imcsdk.imchandle.ImcHandle.set_mo>`__

Deleting Objects
~~~~~~~~~~~~~~~~

``remove_mo`` is used for removing an object

::

    # Query for an existing Mo
    vnic = handle.query_dn('sys/rack-unit-1/adaptor-2/host-eth-vnic-1')

    # Remove the object
    handle.remove_mo(vnic)


`Remove Mo API
reference <https://ciscoucs.github.io/imcsdk_docs/imcsdk.html?highlight=remove_mo#imcsdk.imchandle.ImcHandle.remove_mo>`__


Retrieving Meta Information
---------------------------

``get_meta_info`` is useful for getting information about a Managed
object. Since this information can vary based on the type of platform i.e. classic or modular,
this api will also take ``platform`` as an optional parameter.

::

    from imcsdk.imccoreutils import get_meta_info, IMC_PLATFORM

    class_meta = get_meta_info("faultInst", platform=IMC_PLATFORM.TYPE_CLASSIC)
    print class_meta

The below sample output starts with a tree view of where faultInst
fits, its parents and childrens, followed by MO information. It then
shows information about properties of the MO.

-  Mo Property information:

   -  ``xml_attribute`` - the name of the property as expected by the
      server.
   -  ``field_type`` - type of the field
   -  ``min_version`` - IMC server release in which the property was
      first introduced
   -  ``access`` - defines if a property is
      interal/user-readable/user-writable
   -  property restrictions:

      -  ``min_length`` - minimum length for string property type
      -  ``max_length`` - maximum length for string property type
      -  ``pattern`` - allowed patterns, regexs
      -  ``value_set`` - set of allowed values for this property
      -  ``range_val`` - range for int/uint values

sample output: (truncated)

::

	[AdaptorUnit]
	[ComputeBoard]
	[ComputeRackUnit]
	[EquipmentFan]
	[EquipmentPsu]
	[MemoryArray]
	[MemoryUnit]
	[PciEquipSlot]
	[PowerBudget]
	[ProcessorUnit]
	[StorageController]
	[StorageFlexFlashController]
	[StorageFlexFlashPhysicalDrive]
	[StorageFlexFlashVirtualDrive]
	[StorageLocalDisk]
	[StorageRaidBattery]
	[StorageVirtualDrive]
	[SysdebugMEpLog]
	  |-FaultInst


	ClassId                         FaultInst
	-------                         ---------
	xml_attribute                   :faultInst
	rn                              :fault-[code]
	min_version                     :1.5(1f)
	access                          :OutputOnly
	access_privilege                :['admin', 'read-only', 'user']
	parents                         :[u'adaptorUnit', u'computeBoard', u'computeRackUnit', u'equipmentFan', u'equipmentPsu', u'memoryArray', u'memoryUnit', u'pciEquipSlot', u'powerBudget', u'processorUnit', u'storageController', u'storageFlexFlashController', u'storageFlexFlashPhysicalDrive', u'storageFlexFlashVirtualDrive', u'storageLocalDisk', u'storageRaidBattery', u'storageVirtualDrive', u'sysdebugMEpLog']
	children                        :[]

	Property                        ack
	--------                        ---
	xml_attribute                   :ack
	field_type                      :string
	min_version                     :1.5(1f)
	access                          :READ_ONLY
	min_length                      :None
	max_length                      :None
	pattern                         :None
	value_set                       :['false', 'no', 'true', 'yes']
	range_val                       :[]

	Property                        affected_dn
	--------                        -----------
	xml_attribute                   :affectedDN
	field_type                      :string
	min_version                     :1.5(1f)
	access                          :READ_ONLY
	min_length                      :0
	max_length                      :255
	pattern                         :None
	value_set                       :[]
	range_val                       :[]


Backup And Import
-----------------

Backup IMC
~~~~~~~~~~

``backup_create`` is used to take backup of a Cisco IMC server


::

    from imcsdk.utils.imcbackup import backup_create

    backup_file = “/home/user/backup/config_backup.xml”

    For classic platforms :-
    ------------------------
    backup_create(handle,
                  remote_file=backup_file,
                  protocol="ftp", username="user", password="pass",
                  remote_host="10.10.10.10", passphrase="xxxxxx")

    For modular platforms :-
    ------------------------
    backup_create(handle,
                  remote_host=remote_host, remote_file='/path/to/filename.xml',
                  protocol='scp', username="user", password="pass",
                  passphrase='abc', entity = 'CMC')


`Backup IMC API
Reference <https://ciscoucs.github.io/imcsdk_docs/imcsdk.utils.html?highlight=backup_create#imcsdk.utils.imcbackup.backup_create>`__

Import IMC
~~~~~~~~~~

``backup_import`` is used to import an existing backup to a Cisco IMC server

::

    from imcsdk.utils.imcbackup import backup_import

    import_file = “/home/user/backup/config_backup.xml”

    For classic platforms :-
    ------------------------
    backup_import(handle, remote_file=import_file,
                  protocol="ftp", username="user", password="pass",
                  remote_host="10.10.10.10", passphrase="xxxxxx")

    For modular platforms :-
    ------------------------
    backup_import(handle, remote_host=remote_host,
                  remote_file='/path/to/filename.xml', protocol='scp',
                  username=username, password=password,
                  passphrase='abc', entity = 'CMC')


`Import IMC API
Reference <https://ciscoucs.github.io/imcsdk_docs/imcsdk.utils.html?highlight=backup_import#imcsdk.utils.imcbackup.backup_import>`__


Technical Support
-----------------

``tech_support_get`` is used to collect tech-support for a Cisco IMC server

::

    from imcsdk.utils.imctechsupport import tech_support_get

    For classic platforms :-
    ------------------------
    tech_support_get(handle=handle,
                     remote_host=remote_host,
                     remote_file='/path/to/filename.tar.gz',
                     protocol='scp',
                     username=username,
                     password=password)

    For modular platforms :-
    ------------------------
    tech_support_get(handle=handle,
                     remote_host=remote_host,
                     remote_file='/path/to/filename.tar.gz',
                     protocol='scp',
                     username=username,
                     password=password,
                     component='all')


`Tech-support IMC API
Reference <https://ciscoucs.github.io/imcsdk_docs/imcsdk.utils.html?highlight=tech_support_get#imcsdk.utils.imctechsupport.tech_support_get>`__


Firmware Installation
---------------------

``firmware_huu_update`` is used to upgrade firmware of a Cisco IMC server

::

    from imcsdk.utils.imcfirmwareinstall import firmware_huu_update

    For classic platforms :-
    ------------------------
    firmware_huu_update(handle=handle,
                        remote_ip=remote_ip,
                        remote_share='/path/image_name.iso',
                        share_type='nfs',
                        username=username,
                        password=password,
                        update_component='all',
                        stop_on_error='yes',
                        verify_update='no',
                        cimc_secure_boot='no')

    For modular platforms :-
    ------------------------
    firmware_huu_update(handle=handle,
                        remote_ip=remote_ip,
                        remote_share='/path/image_name.iso',
                        share_type='nfs',
                        username=username,
                        password=password,
                        update_component='all',
                        stop_on_error='yes',
                        verify_update='no',
                        cimc_secure_boot='no',
                        server_id=1)

`Firmware Installation IMC API
Reference <https://ciscoucs.github.io/imcsdk_docs/imcsdk.utils.html?highlight=firmware_huu_update#imcsdk.utils.imcfirmwareinstall.firmware_huu_update>`__


Inventory
---------
The ``inventory_get`` API is used to fetch server inventory

::

    from imcsdk.apis.server.inventory import inventory_get

    # Fetch inventory for a single server
    inventory_get(handle=handle)

    # Fetch inventory for a multiple servers
    inventory_get(handle=[handle1, handle2, handle3])

    # Fetch inventory for a single server
    inventory_get(handle=handle, component="all")

    # Fetch disks inventory for a single server
    inventory_get(handle=handle, component="disks")

    # Fetch cpu and disks inventory for a single server
    inventory_get(handle=handle, component=["cpu", "disks"])

    # Fetch cpu and disks inventory for a single server and
    # write it to a file in json format
    inventory_get(handle=handle, component=["cpu", "disks"],
                  file_format="json", file_name="inventory.json")

    # Fetch cpu and disks inventory for a single server and
    # write it to a file in csv format
    inventory_get(handle=handle, component=["cpu", "disks"], file_format="csv",
                  file_name="inventory.csv")

    # Fetch cpu and disks inventory for a single server and
    # write it to a file in html format
    inventory_get(handle=handle, component=["cpu", "disks"],
    file_format="html", file_name="inventory.html")
