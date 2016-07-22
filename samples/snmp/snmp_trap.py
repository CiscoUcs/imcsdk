# Copyright 2015 Cisco Systems, Inc.
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
This module performs the operation related to SNMP Traps.
"""


def search_specific_trap(hostname, snmp_mo_list):
    """
    This method to search SNMP Trap for a host in SNMP trap list.
    Args:
        hostname: SNMP Trap Host
        snmp_mo_list : List of MOs of commSnmpTrap class

    Returns:
        MO of SNMP Traps else False if trap does not exist
    """

    for trap in snmp_mo_list:
        if trap.hostname == hostname:
            return trap
    return False


def snmp_trap_get(handle, hostname=None):
    """
    This method fetches SNMP Trap List
    Args:
        handle: ImcHandle
        hostname: SNMP Trap Host

    Returns:
        MO list of SNMP Traps else False if trap does not exist
    """

    snmp_mo_list = handle.query_classid(class_id="commSnmpTrap")
    if hostname:
        return search_specific_trap(snmp_mo_list=snmp_mo_list,
                                    hostname=hostname)
    else:
        return snmp_mo_list


def snmp_trap_set(handle, id,
                  hostname,
                  user="unknown",
                  admin_state="Enabled",
                  notification_type="traps",
                  version="v3"):
    """
    This method fetches SNMP Trap List
    Args:
        handle: ImcHandle
        id : Trap ID
        hostname: SNMP Trap Host
        user : SNMP User
        admin_state: Enabled or Disabled
        notification_type : traps or
        version : v2c,v1,v3

    Returns:
        SNMP Traps MO
    """

    from imcsdk.mometa.comm.CommSnmpTrap import CommSnmpTrap
    snmp_mo = CommSnmpTrap(parent_mo_or_dn="sys/svc-ext/snmp-svc", id=id,
                           user=user,
                           hostname=hostname,
                           admin_state=admin_state,
                           notification_type=notification_type,
                           version=version)

    handle.set_mo(snmp_mo)
    return snmp_mo


def snmp_trap_clear(handle, hostname):
    """
    This method clears SNMP Trap for specific host
    Args:
        handle: ImcHandle
        hostname: SNMP Trap Host

    Returns:
        SNMP Trap Mo or False if trap not found for Host
    """

    snmp_mo = snmp_trap_get(handle, hostname)
    if snmp_mo:
        snmp_mo.admin_action = "clear"
        handle.set_mo(snmp_mo)
    return snmp_mo
