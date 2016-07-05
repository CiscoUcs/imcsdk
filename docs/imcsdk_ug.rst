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

    1. `Backup Imc <#backup-imc>`__
    2. `Import Imc <#import-imc>`__


Overview
--------

Cisco IMC Python SDK is a python module which helps automate all aspects
of Cisco IMC management servers i.e. both C-Series and E-Series.

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

    Tree (topRoot)              Distinguished Name	
    |-sys                       sys
    |-ComputeRackUnit              sys/rack-unit-1
        |-AdaptorUnit                  sys/rack-unit-1/adaptor-1
            |-AdaptorCfgBackup             sys/rack-unit-1/adaptor-1/export-config


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

    topSystem MO: rn=”	s” 
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

Base APIs
~~~~~~~~~

The SDK provides APIs to enable CRUD operations.

-  **C**\ reate an object - ``add_mo``
-  **R**\ etrieve an object -
   ``query_dn``,\ ``query_classid``
-  **U**\ pdate an object - ``set_mo``
-  **D**\ elete an object - ``delete_mo``


All these methods are invoked on a ``ImcHandle`` instance. We refer it
by ``handle`` in all the examples here-after. Refer to the `Connecting
Disconnecting <#connecting-disconnecting>`__ to create a new handle.

Creating Objects
~~~~~~~~~~~~~~~~

Creating managed objects is done via ``add_mo`` API.

Example:

The below example creates a new Service Profile(\ ``LsServer``) Object
under the parent ``org-root``

::

    from imcsdk.mometa.adaptor.AdaptorEthISCSIProfile import AdaptorEthISCSIProfile
	
    adapter_profile = AdaptorEthISCSIProfile(parent_mo_or_dn="sys/rack-unit-1/adaptor-2/host-eth-eth1",
                                   initiator_name="abc.def.storage",
                                   initiator_ip_address="10.10.10.10",
                                   initiator_gateway="10.10.10.11",
                                   initiator_subnet_mask="255.255.255.0",
                                   dhcp_iscsi="enabled")
    handle.add_mo(adapter_profile)


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
    adapter_profile = handle.query_dn("sys/rack-unit-1/adaptor-2/host-eth-eth1/ethiscsi")

    # Update description of the service profile
    adapter_profile.initiator_gateway = "10.10.10.12"

    # Add it to the on-going transaction
    handle.set_mo(adapter_profile)

`Set Mo API
reference <https://ciscoucs.github.io/imcsdk_docs/imcsdk.html?highlight=set_mo#imcsdk.imchandle.ImcHandle.set_mo>`__

Deleting Objects
~~~~~~~~~~~~~~~~

``remove_mo`` is used for removing an object

::

    # Query for an existing Mo
    adapter_profile = handle.query_dn("sys/rack-unit-1/adaptor-2/host-eth-eth1/ethiscsi")

    # Remove the object
    handle.remove_mo(adapter_profile)


`Remove Mo API
reference <https://ciscoucs.github.io/imcsdk_docs/imcsdk.html?highlight=remove_mo#imcsdk.imchandle.ImcHandle.remove_mo>`__


Retrieving Meta Information
---------------------------

``get_meta_info`` is useful for getting information about a Managed
object.

::

    from imcsdk.imccoreutils import get_meta_info  

    class_meta = get_meta_info("faultInst")
    print class_meta

The below sample output starts with a tree view of where faultInst
fits, its parents and childrens, followed by MO information. It then
shows information about properties of the MO.

-  Mo Property information:

   -  ``xml_attribute`` - the name of the property as expected by the
      server.
   -  ``field_type`` - type of the field
   -  ``min_version`` - Imc server release in which the property was
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

Backup Imc
~~~~~~~~~~

``backup_imc`` is used to take backup of a Imc server


::

    from imcsdk.utils.imcbackup import backup_imc

    backup_file = “/home/user/backup/config_backup.xml”

    backup_imc(handle, 
               remote_file=backup_file, 
               protocol="ftp", username="user", password="pass",
               remote_host="10.10.10.10", passphrase="xxxxxx")

`Backup Imc API
Reference <https://ciscoucs.github.io/imcsdk_docs/imcsdk.utils.html?highlight=backup_imc#imcsdk.utils.imcbackup.backup_imc>`__

Import Imc
~~~~~~~~~~

``import_imc_backup`` is used to import an existing backup to a Imc server

::

    from imcsdk.utils.imcbackup import import_imc_backup

    import_file = “/home/user/backup/config_backup.xml”

    import_imc_backup(h,remote_file=import_file,
                      protocol="ftp",username="user",password="pass",
                      remote_host="10.10.10.10",passphrase="xxxxxx")

`Import Imc API
Reference <https://ciscoucs.github.io/imcsdk_docs/imcsdk.utils.html?highlight=import_imc_backup#imcsdk.utils.imcbackup.import_imc_backup>`__