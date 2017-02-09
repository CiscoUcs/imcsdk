=======
History
=======

0.9.2.0 (2017-02-10)
--------------------
* Adds support for IMC version 3.0(1c)
* New APIs for the following features:-

  * Secure Drive Encryption
  * BIOS Profile
  * Native Hardware Inventory Collection
  * Enable Redfish support
  * LDAP
  * NTP
  * IP Filtering
  * IP Blocking
  * Asset Tagging

* Redesigned APIs for the following features:-

  * SNMP Traps and users 
  * Local Users
  * Adaptor operations
  * KVM/Sol/Vmedia operations
  * Power Budgeting and Power Capping
  * Boot Order Precision and Legacy Boot order
  
* Improved local inventory collection API that handles multiple IMC servers and more formats
* Support to filter out Managed Object properties based on the property version and platform version
* Support for handling of interim/spin IMC builds
* Updated verbs for Managed Objects
* Bug fix for monitoring firmware upgrade
* Bug fix for handle.query_children API with class_id and hierarchy as filters
* Improved test Coverage

0.9.1.0 (2016-11-25)
--------------------
* Support for Modular C3260 and Classic platforms
* Supports every Managed Object exposed by IMC upto version 2.0(13e)
* Support to invoke APIs on individual server modules in case of C3260 platform
* Support for TLSv1.1/v1.2 and fallback to TLSv1 for older versions
* Support to filter out non-applicable properties based on the C-series platform
* Validation of Managed Object version with the C-series version for better error-handling

0.9.0.3 (2016-08-25)
--------------------
* Added APIs layer to the sdk

0.9.0.1 (2016-08-25)
--------------------
* Fixed an issue with pip install

0.9.0.0 (2016-08-25)
--------------------
* Python SDK for IMC rack server management and related automation
* Supports every Managed Object exposed by IMC
* APIs for CRUD operations simplified
* Runtime memory usage is reduced
* Nosetests for unit testing
* Samples directory for more real world use cases
* Integrating the sphinx framework for documentation
* PEP8 Compliance
