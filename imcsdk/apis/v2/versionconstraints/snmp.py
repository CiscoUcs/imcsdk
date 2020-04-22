# Copyright 2017 Cisco Systems, Inc.
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
This module performs the firmware version related checks for all and specific
apis.
"""
import logging

log = logging.getLogger('imc')


def snmp_multiple_config_with_configcommit_for_hp_and_above(handle, mos):
    '''
    In any of the cimc version, if any of the snmp configuration is modified,
    by default snmp engine commit for each and every change in config.
    Each commit takes 60-90 seconds approximately.
    Hence in case of sending back to back request to modify snmp config,
    next request always fails as the commit is in progress for first request.
    Second request will go through only after the commit is complete for first
    request.

    This behaviour is very time consuming if you want to configure all 15
    snmpuser and snmptrap.
    To reduce the time and number of request, we chose to use 'configConfMos'.
    However in case of snmpuser and snmptrap, even you send multiple config in
    a single request using configConfMos, at end point they are traversed
    sequentially. Hence no reduction in time.

    To fix this, in HP(4.0) release, a parameter 'config_change' is introduced
    which lets user control when to commit the snmp configuration change.
    If this parameter is not part of request, by default the commit happen with
    every modify request.

    This function will add the functionality to use this new parameter
    'config_change' if the version of cimc is HP and above.
    '''

    # if version is less than HP then return
    log.debug(handle.version)
    handle_major_version = int(handle.version.major)
    log.debug("Major version is <%d>" % handle_major_version)
    if handle_major_version < 4:
        return mos

    log.debug("Optimize using "
              "'snmp_multiple_config_with_configcommit_for_hp_and_above'")

    # for all the mos to be configured, set 'config_change' to
    # "no-commit" for the mos
    for mo in mos:
        mo.config_change = "no-commit"
    return mos


def snmp_commit_explicitly_for_hp_and_above(handle, parent_dn):
    '''
    In HP, an MO 'CommSnmpConfigCommit' is introduced which explicitly sends
    message to trigger commit on SNMP engine.

    This function is used to send explicitly send commit to end point for SNMP,
    if we send multiple user or trap request earlier as no-commit.
    '''

    from imcsdk.mometa.comm.CommSnmpConfigCommit import CommSnmpConfigCommit
    from imcsdk.mometa.comm.CommSnmpConfigCommit import \
        CommSnmpConfigCommitConsts

    # if version is less than HP then return
    log.debug(handle.version)
    handle_major_version = int(handle.version.major)
    log.debug("Major version is <%d>" % handle_major_version)
    if handle_major_version < 4:
        return

    log.debug("Optimize using "
              "'snmp_commit_explicitly_for_hp_and_above'")
    mo = CommSnmpConfigCommit(parent_mo_or_dn=parent_dn,
                              commit=CommSnmpConfigCommitConsts.COMMIT_YES)
    handle.set_mo(mo)
