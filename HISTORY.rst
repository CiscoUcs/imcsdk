History
=======

0.9.14 (2023-12-13)
---------------------
* Added support for ancient IMCs
* Added support for DNAC DN1 - DN3 servers
* Added support for CNR server
* Added support for Python 3.11

0.9.13 (2022-07-21)
---------------------
* Adds support for IMC version 4.2(2a)

0.9.12 (2021-10-28)
---------------------
* Bug fixes

0.9.11 (2021-07-12)
---------------------
* Adds support for IMC version 4.2(1a) for M6 servers
* Adds support for IMC version 4.1(3a) for M5 servers
* Adds APIs for AaaTacacsPlus

0.9.10 (2020-04-23)
---------------------
* More python3 compatibility fixes

0.9.9 (2020-04-22)
---------------------
* Fixes an issue with version meta

0.9.8 (2020-04-22)
---------------------
* Adds support for IMC version 4.1(1c), 4.1(1d)

0.9.7 (2019-07-08)
---------------------
* Adds support for IMC version 4.0(1c), 4.0(2b)

0.9.6 (2018-10-10)
---------------------
* Updated requirements to include setuptools

0.9.5 (2018-08-24)
--------------------
* Fixed an issue with missed requirement files
* Added Python 3.6,3.7 to package meta

0.9.4 (2018-08-24)
--------------------
* Support for Python3

0.9.3.1 (2018-05-27)
--------------------
* Support for more APIs
* Misc bug fixes

0.9.3.0 (2017-09-19)
--------------------
* Adds support for IMC version 3.0(2b), 3.0(3a) and 3.1(1d)
* Adds support for HX platform
* Fixes sync_mo
* Containerizes imcsdk support for CIMC 3.0 using Docker
* Adds context manager support for ImcHandle
* Redesigned APIs for the following,

  * BIOS
  * Boot Order
  * Certificate
  * KVM
  * LDAP
  * NTP
  * SNMP
  * SOL
  * Syslog
  * Storage
  * vMedia

0.9.2.0 (2017-02-10)
--------------------
* Adds support for IMC version 3.0(1c)
* New APIs for the following,

  * Secure Drive Encryption
  * BIOS Profile
  * Native Hardware Inventory Collection
  * Enable Redfish support
  * LDAP
  * NTP
  * IP Filtering
  * IP Blocking
  * Asset Tagging

* Redesigned APIs for the following,

  * SNMP Traps and users
  * Local Users
  * Adaptor operations
  * KVM/Sol/Vmedia operations
  * Power Budgeting and Power Capping
  * Boot Order Precision and Legacy Boot order

* Improved local inventory collection API; handles multiple IMC servers and supports multiple output formats
* Support for skipping attributes of a Managed object not known to a server
  version
* Support for handling of interim/spin builds
* Bug fix in monitoring firmware upgrade API
* Bug fix in handle.query_children API when class_id and hierarchy are
  specified
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
